import cv2
import numpy as np
import colorDetectionlab
import colorDetectionbgr
import colorDetectionhsv


image = cv2.imread("cubefaces/1w.jpg")
blurredFrame = cv2.blur(image, (3, 3))
cv2.imshow("something", blurredFrame)
# lab = colorDetectionlab.get_dominant_rgb_color(blurredFrame)
# rgb = colorDetectionbgr.get_dominant_rgb_color(blurredFrame)
hsv = colorDetectionhsv.get_dominant_rgb_color(blurredFrame)
print(hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
