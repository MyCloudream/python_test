import numpy as np

# 创建等差数组，类似于range
a = np.arange(4)
# [0 1 2 3]
print(a)
# 求矩阵各元素的平方 [0 1 4 9]
print(a ** 2)
# 求各元素的三次方
print(a ** 3)
# 各元素开根号 [ 0. 1. 1.41421356 1.73205081]
print(np.sqrt(a))
