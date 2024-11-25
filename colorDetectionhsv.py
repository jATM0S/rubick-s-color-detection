import cv2
import numpy as np
def get_color_name(h, s, v):
    print(h,s,v)
    if s < 65 and v > 50:
        return "white"
    if v < 50:
        return "black"
    if  1 < h < 27:
        return "orange"
    if 27 <= h < 45:
        return "yellow"
    if 45 <= h < 85:
        return "green"
    if 85 <= h < 160:
        return "blue"
    if h<=1 or h > 160:
        return "red"
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
