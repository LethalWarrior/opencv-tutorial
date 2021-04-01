import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    #-- 3 is property of width
    width = int(cap.get(3))
    #-- 4 is property of height
    height = int(cap.get(4))

    #-- Provide a black canvas
    image = np.zeros(frame.shape, np.uint8)

    #-- Create smaller images
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    #-- Top left
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    #-- Bottom Left
    image[height//2:, :width//2] =  smaller_frame
    #-- Top Right
    image[:height//2, width//2:] = smaller_frame
    #-- Bottom Right
    image[height//2:, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)

    cv2.imshow('frame', image)

    #-- Check if the key that is being pressed is 'q'
    if cv2.waitKey(1) == ord('q'):
        break;

cap.release()
cv2.destroyAllWindows()
