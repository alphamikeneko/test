# numpy test 複数のndarray (npz)
import numpy as np

a1 = np.arange(5, dtype=np.float32)
a2 = np.arange(5,10 ,dtype=np.float32)
print(a1)
print(a2)


# 保存
np.savez('/Users/katasugirupan/Desktop/test2/np_save3', a1, a2)

# 読み込み
b = np.load('/Users/katasugirupan/Desktop/test2/np_save3.npz')
print(b)
print(b.files) # 配列の名前を返す
print(b['arr_0'])
print(b['arr_1'])