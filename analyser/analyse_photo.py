from keras.preprocessing.image import ImageDataGenerator
from PIL import Image
import keras.utils as image
import numpy as np
import cv2
import io
from analyser.model_provider import get_model
from analyser.ela import apply_ela
from math import floor

model_name = 'model-1'
img_width, img_height = 500, 500
class_map = {0:'modified', 1:'original'}

datagen = ImageDataGenerator(rescale=1./255)

def f(x):
    return x * 1./255

def is_fake(img):
#     model = get_model(model_name)
#
#     img = apply_ela(img)
#     img = cv2.resize(img, (img_width, img_height))
#
#     unused, img_data = cv2.imencode('.bmp', img)
#     img = Image.open(io.BytesIO(img_data))
#
#     prediction_data = datagen.standardize(image.img_to_array(img))
#     prediction_data = np.expand_dims(prediction_data, axis=0)
#
#     predictions = model.predict(prediction_data, batch_size=20, verbose=1)
#
#     result = class_map[0 if predictions[0][0] < 0.98 else 1]
#
#     return result == 'modified'
      return true
