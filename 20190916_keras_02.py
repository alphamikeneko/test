# データセット作成　テスト検証
import keras
from keras.utils import np_utils
from keras.preprocessing.image import array_to_img, img_to_array, load_img
import numpy as np

from PIL import Image


temp_img = load_img('./faces4/0.jpg', target_size=(64,64))
temp_img_array = img_to_array(temp_img)

print(temp_img_array.shape) # (64,64,3) - 64,64,(RGB)


# 画像表示
def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


# img_show(temp_img_array.reshape(64, 64))
img_show(temp_img_array)


