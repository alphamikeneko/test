import keras
from keras.datasets import mnist
import numpy as np
from PIL import Image

# 文字画像表示
def ConvertToImg(img):
    return Image.fromarray(np.uint8(img))

# Kerasの関数でデータの読み込み。データをシャッフルして学習データと訓練データに分割
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# MNIST一文字の幅
chr_w = 28
# MNIST一文字の高さ
chr_h = 28
# 表示する文字数
num = 128

# MNISTの文字をPILで１枚の画像に描画する
canvas = Image.new('RGB', (int(chr_w * num/2), int(chr_h * num/2)), (255, 255, 255))

# MNISTの文字を読み込んで描画
i = 0
for y in range( int(num/2) ):
    for x in range( int(num/2) ):
        chrImg = ConvertToImg(x_train[i].reshape(chr_w, chr_h))
        canvas.paste(chrImg, (chr_w*x, chr_h*y))
        i = i + 1

canvas.show()
# 表示した画像をJPEGとして保存
canvas.save('mnist.jpg', 'JPEG', quality=100, optimize=True)