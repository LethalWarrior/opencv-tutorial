import cv2
import random

img = cv2.imread('assets/lena.jpg', -1)

#== Loop through to change pixel values ==#

# for i in range(100):
#     for j in range(1200):
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cropped = img[300:380, 600:650]
img[0:80, 1150:1200] = cropped

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
