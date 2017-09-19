import numpy as np

a = np.array([
    [1, 2],
    [3, 4]
])
b = np.array([
    [5, 6],
    [7, 8]
])

'''
对应位置元素相乘，结果为：
[[ 5 12]
 [21 32]]
'''
print(a * b)

'''
矩阵相乘，结果为：
[[19 22]
 [43 50]]
'''
print(a.dot(b))
# 矩阵相乘，同上
print(np.dot(a, b))
