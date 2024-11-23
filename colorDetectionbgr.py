import cv2
import numpy as np
import math
def euclidean_distance_3d(bgr1, bgr2):
    return math.sqrt((bgr1[0] - bgr2[0])**2 + (bgr1[1] - bgr2[1])**2 + (bgr1[2] - bgr2[2])**2)

def get_closest_color(bgr):
    prominent_color_palette = {
            'red'   : (0, 0, 255),
            'orange': (0, 160, 255),
            'blue'  : (255, 0, 0),
            'green' : (0, 255, 0),
            'white' : (200, 200, 200),
            'yellow': (0, 200, 200)
        }
    distances = []
    print(bgr)
    for color_name, color_bgr in prominent_color_palette.items():
        distance=euclidean_distance_3d(bgr,color_bgr)
        distances.append({
            'color_name': color_name,
            'color_bgr': color_bgr,
            'distance': distance
        })
        print(f"Color BGR: {color_bgr}, Distance: {distance}")
    closest = min(distances, key=lambda item: item['distance'])
    return closest
def convert_bgr_to_notation(bgr):
    """
    Convert BGR tuple to rubik's cube notation.
    The BGR color must be normalized first by the get_closest_color method.

    :param bgr tuple: The BGR values to convert.
    :returns: str
    """
    color_name = get_closest_color(bgr)['color_name']
    return color_name

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
    color=convert_bgr_to_notation(dominant)
    return color