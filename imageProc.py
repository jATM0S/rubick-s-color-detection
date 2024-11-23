import cv2
import numpy as np
import colorDetectionlab
import colorDetectionbgr
import colorDetectionhsv


image = cv2.imread("cubefaces/5w.jpg")
blurredFrame = cv2.blur(image, (3, 3))
cv2.imshow("something", blurredFrame)
# print(colorDetectionlab.get_dominant_rgb_color(blurredFrame))
# print(colorDetectionbgr.get_dominant_rgb_color(blurredFrame))
print(colorDetectionlab.get_dominant_rgb_color(blurredFrame))
cv2.waitKey(0)
cv2.destroyAllWindows()
