import numpy as np

a = np.arange(12)
# [ 0  1  2  3  4  5  6  7  8  9 10 11]
print(a)

b = a
# [ 0  1  2  3  4  5  6  7  8  9 10 11]
print(b)

a.shape = (3, 4)
# (3, 4)
print(b.shape)

a[a == 5] = 100
'''
[[  0   1   2   3]
 [  4 100   6   7]
 [  8   9  10  11]]
'''
print(b)
