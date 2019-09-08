import keras
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation, Convolution2D, MaxPooling2D, Flatten

from keras.utils import np_utils
#from keras.callbacks import EarlyStopping

(x_tr, y_tr), (x_te, y_te) = mnist.load_data()
print(x_tr.shape, x_te.shape, y_tr.shape, y_te.shape)

CNN = Sequential()
CNN.add(Convolution2D(10, (5,5), input_shape=(28,28,1),padding='same'))
CNN.add(MaxPooling2D(2, 2))
CNN.add(Convolution2D(10, (5,5), padding='same'))
CNN.add(MaxPooling2D(2, 2))
CNN.add(Convolution2D(10, (5, 5), padding='same'))
CNN.add(MaxPooling2D(2, 2))
CNN.add(Flatten())
CNN.add(Dense(10, activation='softmax'))

CNN.summary()


X_tr = x_tr.reshape(60000, 28, 28, 1)/255
X_te = x_te.reshape(10000, 28, 28, 1)/255
Y_tr = np_utils.to_categorical(y_tr, 10)
Y_te = np_utils.to_categorical(y_te, 10)

print(X_te.shape, X_te.shape, Y_tr.shape, Y_te.shape)

CNN.compile(optimizer='adam', loss='categorical_crossentropy', metrics=["accuracy"])

CNN.fit(X_tr, Y_tr, epochs=1, batch_size=100,validation_data=(X_te, Y_te))

