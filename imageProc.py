import cv2
import numpy as np
import colorDetection

image = cv2.imread("cubefaces/7b.jpg")
cv2.imshow("something", image)
print(colorDetection.get_dominant_rgb_color(image))
cv2.waitKey(0)
cv2.destroyAllWindows()
