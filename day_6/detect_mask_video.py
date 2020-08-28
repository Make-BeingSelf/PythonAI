# USAGE
# python detect_mask_video.py

# 필요한 라이브러리 import
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2
import os


def detect_and_predict_mask(frame, faceNet, maskNet):
    # 프레임 차원 설정 및 blob 추출
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300),
                                 (104.0, 177.0, 123.0))

    # blob을 전달하고 얼굴 감지값 얻기
    faceNet.setInput(blob)
    detections = faceNet.forward()

    # 예측목록 초기화
    faces = []
    locs = []
    preds = []

    # 감지
    for i in range(0, detections.shape[2]):

        # 탐지의 신뢰도 추출
        confidence = detections[0, 0, i, 2]

        # 신뢰도가 낮은 탐지 필터링
        if confidence > args["confidence"]:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            (startX, startY) = (max(0, startX), max(0, startY))
            (endX, endY) = (min(w - 1, endX), min(h - 1, endY))

            face = frame[startY:endY, startX:endX]
            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            face = cv2.resize(face, (224, 224))
            face = img_to_array(face)
            face = preprocess_input(face)

            faces.append(face)
            locs.append((startX, startY, endX, endY))

    # 얼굴이 감지될 경우에만 예측
    if len(faces) > 0:

        faces = np.array(faces, dtype="float32")
        preds = maskNet.predict(faces, batch_size=32)

    return (locs, preds)


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", type=str,
                default="face_detector",
                help="path to face detector model directory")
ap.add_argument("-m", "--model", type=str,
                default="mask_detector.model",
                help="path to trained face mask detector model")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
                help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

# load our serialized face detector model from disk
print("[INFO] loading face detector model...")
prototxtPath = os.path.sep.join([args["face"], "deploy.prototxt"])
weightsPath = os.path.sep.join([args["face"],
                                "res10_300x300_ssd_iter_140000.caffemodel"])
faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

# load the face mask detector model from disk
print("[INFO] loading face mask detector model...")
maskNet = load_model(args["model"])

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(1.0)

# 5초 후 영상 촬영 시작, 사용자가 거리를 좁혀온다고 가정함
a = 3
while a != 0:
    a -= 1
    time.sleep(1)
    print(f'대상과의 거리는 {a}m 입니다.')

# 거리가 충분히 좁혀졌을 때 촬영시작
if a == 0:
    print('마스크 착용 여부 탐지를 시작합니다......')
    time.sleep(1)

    record_time = time.time() + 20
    mask_on = 0

    # 지속적인 영상 촬영

    while True:
        if time.time() > record_time:
            break

        frame = vs.read()
        frame = imutils.resize(frame, width=1000)

        # 얼굴을 감지하고 마스크 착용 여부를 확인
        (locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet)

        for (box, pred) in zip(locs, preds):

            (startX, startY, endX, endY) = box
            (mask, withoutMask) = pred

            label = "Mask" if mask > withoutMask else "No Mask"
            # 대상이 마스크를 착용하였을 경우 통과
            if label == "Mask":
                color = (0, 255, 0)

                if mask_on == 0:
                    print("대상은 마스크를 착용하였습니다. 즐거운 하루 되십시오.")
                    mask_time = time.time() + 5
                    mask_on = 1
                if mask_time < time.time():
                    exit()
            # 대상이 마스크를 착용하지 않았다면 착용하지 않았다고 경고하며 버저와 개찰구를 봉쇄
            else:
                print("대상은 마스크를 착용하지 않았습니다. 통과하실 수 없습니다.")
                color = (0, 0, 255)

            # include the probability in the label
            label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

            cv2.putText(frame, label, (startX, startY - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
            cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)

        cv2.imshow("마스크 착용감지", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break


cv2.destroyAllWindows()
vs.stop()
