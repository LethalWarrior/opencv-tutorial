import cv2

# Display image in grayscale
img = cv2.imread('assets/lena.jpg', cv2.IMREAD_GRAYSCALE)
# Resize the image to half the size
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
# Rotate the image
img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite('assets/rotated_lena_grayscale_resize_50.jpg', img)

cv2.imshow('Lena Grayscale', img)
# Wait indefinitely
cv2.waitKey(0)
cv2.destroyAllWindows()
