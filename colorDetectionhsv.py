import cv2
import numpy as np
def get_color_name(h, s, v):
    if s < 20 and v > 200:
        return "White"
    if v < 50:
        return "Black"
    if h < 10 or h > 160:
        return "Red"
    if 10 <= h < 25:
        return "Orange"
    if 25 <= h < 35:
        return "Yellow"
    if 35 <= h < 85:
        return "Green"
    if 85 <= h < 125:
        return "Blue"
    if 125 <= h < 160:
        return "Purple"
    return "Unknown"
def get_dominant_rgb_color(roi):
    """ Get dominant RGB from a certain region of interest.

    :param roi: the image array
    :returns: tuple
    """
    average = roi.mean(axis=0).mean(axis=0)
    pixels = np.float32(roi.reshape(-1, 3))

    n_colors = 5
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS
    _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
    _, counts = np.unique(labels, return_counts=True)
    dominant = palette[np.argmax(counts)]
    hsv_frame = cv2.cvtColor(np.uint8([[dominant]]), cv2.COLOR_BGR2HSV)[0][0]
    [h,s,v]=hsv_frame
    color=get_color_name(h,s,v)
    return color
    # print(h,s,v)
    # return 
