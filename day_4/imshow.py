import cv2

img = cv2.imread('woman.jpg')
cv2.imshow('woman', img)
# gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray-woman',gray)

## 속성 분석
print(f"width:{img.shape[1]} pixels" )
print(f"heigh:{img.shape[0]} pixels" )
print(f"channels:{img.shape[2]}")

(b,g,r)=img[0,0]
print(f"Pixel as (0,0) - Red: {r}, Green:{g}, Blue:{b}")


## image 추출
dot = img[50:100,50:100]
cv2.imshow("dot-woman", dot)

img[50:100,50:100] = (0,0,255)
cv2.imshow("dot", img)

cv2.waitKey(0)
cv2.destroyAllWindows()