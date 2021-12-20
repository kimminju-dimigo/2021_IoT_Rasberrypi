import cv2

img = cv2.imread("hosi.jpg")
img2 = cv2.resize(img, (600, 400))

cv2.imshow('hosi', img2)

cv2.waitKey(0)

cv2.destroyAllWindows()