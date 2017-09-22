import numpy as np

a = np.tile([[3, 2], [1, 2]], (2,2))
# [1 2 1 2 1 2 1 2 1 2]
print(a)

b = np.tile([1, 2], (3, 2))
'''
[[1 2 1 2]
 [1 2 1 2]
 [1 2 1 2]]
'''
print(b)

c = np.tile([1, 2], (1, 1))
'''
[[1 2 1 2 1 2 1 2]
 [1 2 1 2 1 2 1 2]]
'''
print(c)
