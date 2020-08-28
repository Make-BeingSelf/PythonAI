import cv2

img = cv2.imread('woman.jpg')

cv2.imshow('woman', img)

# 속성 분석
print(f"width:{img.shape[1]} pixels")
print(f"heigh:{img.shape[0]} pixels")
print(f"channels:{img.shape[2]}")

(b, g, r) = img[0, 0]
print(f"Pixel as (0,0) - Red: {r}, Green:{g}, Blue:{b}")


# image 추출
dot = img[50:100, 50:100]
img[50:100, 50:100] = (0, 0, 255)

cv2.rectangle(img, (150, 50), (200, 100), (0, 255, 0), 5)  # 시작, 끝, 색깔, 두께
# 시작, 반지름, 색깔,두께(-1: Full, +: 두께)
cv2.circle(img, (275, 75), 25, (0, 255, 255), -1)
cv2.line(img, (350, 100), (400, 100), (255, 0, 0), 5)  # 시작, 끝, 색깔, 두께
cv2.putText(img, 'woman', (450, 100), cv2.FONT_HERSHEY_SIMPLEX,
            1, (255, 255, 255), 4)  # 단어, 폰트, 색깔, 두께
cv2.imshow('put', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
