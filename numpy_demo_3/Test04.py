import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# (4, 3)
print(a.shape)

a.shape = (6, 2)
# (6, 2)
print(a.shape)
'''
[[ 1  2]
 [ 3  4]
 [ 5  6]
 [ 7  8]
 [ 9 10]
 [11 12]]
'''
print(a)
