import cv2
import numpy as np
    

def get_ela(filename):
    im = cv2.imread(filename, cv2.IMREAD_COLOR)
    return apply_ela(im)
    

def apply_ela(img):
    unused, resaved_data = cv2.imencode('.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
    resaved_img = cv2.imdecode(resaved_data, cv2.IMREAD_COLOR)

    ela_im = cv2.absdiff(img, resaved_img)

    channels = cv2.split(ela_im)
    max_diff = 0.0
    for channel in channels:
        unused, max_val, unused, unused = cv2.minMaxLoc(channel)
        max_diff = max(max_diff, max_val)
    scale = 255.0/max_diff

    ela_im = np.multiply(ela_im, scale)
    return ela_im
