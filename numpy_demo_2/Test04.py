import numpy as np

a = np.array(([3, 2, 1], [2, 5, 7], [4, 7, 8]))
# 查找到值为2 的元素，并将所有符合条件的元素值置为0
a[a == 2] = 0
'''
[[3 0 1]
 [0 5 7]
 [4 7 8]]
'''
print(a)
