import numpy as np

a = np.arange(12)

b = a.view()
# [ 0  1  2  3  4  5  6  7  8  9 10 11]
print(b)

a.shape = (3, 4)
# (12,)
print(b.shape)

a[a == 5] = 100
# [  0   1   2   3   4 100   6   7   8   9  10  11]
print(b)
