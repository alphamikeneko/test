# numpy test キャストしたデータ
import numpy as np

a = np.arange(5, dtype=np.float32)

print(a)
print(type(a))
print(a.dtype)
print(a.shape)


# 保存
np.save('/Users/katasugirupan/Desktop/test2/np_save2', a)

# 読み込み
b = np.load('/Users/katasugirupan/Desktop/test2/np_save2.npy')
print(a)
print(type(b))
print(b.shape)
