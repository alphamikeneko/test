import keras
import numpy as np
from keras.datasets import mnist

import matplotlib.pyplot as plt


(x_tr, y_tr), (x_te, y_te) = mnist.load_data()
print(x_tr.shape, x_te.shape, y_tr.shape, y_te.shape)

data_index = np.random.randint(60000)
print('label=', y_tr[data_index])
plt.imshow(x_tr[data_index], cmap = plt.cm.gray_r)
plt.show()