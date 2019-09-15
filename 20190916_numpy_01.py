# numpy test
import numpy as np

a = np.arange(5)

print(a)

# 保存
# np.save('/Users/katasugirupan/Desktop/test2/np_save', a)

# 読み込み
b = np.load('/Users/katasugirupan/Desktop/test2/np_save.npy')
print(type(b))
print(b)