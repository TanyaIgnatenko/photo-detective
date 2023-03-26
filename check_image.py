import numpy as np
import cv2
from analyser.analyse_photo import is_fake


def is_modified(img_buf):
    image = np.asarray(bytearray(img_buf), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return is_fake(image)

