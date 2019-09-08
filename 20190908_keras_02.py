import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np

# Sequential : モデルの型
# Dense : 線形変換
# Activation : 活性化関数


NN = Sequential() # ニューラルネット初期化
NN.add(Dense(3, input_dim=3))
NN.add(Activation('sigmoid'))
NN.add(Dense(3))
NN.add(Activation('softmax'))

NN.summary() # サマリー表示

# optimaizer : 勾配法
# loss : 誤差関数
NN.compile(optimizer='adam',loss='categorical_crossentropy')

x = np.array(
[[1,0,0],
[1,1,0],
[0,0,1],
[0,1,0],
[0,0,0]])
y = np.array(
[[0,0,1],
[0,1,0],
[1,0,0],
[1,1,0,],
[0,1,1]])

# 入力データ,正解データ,epochs
NN.fit(x,y,epochs=500)

print(NN.predict(x))
print(y)
