import numpy as np

mat = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
# 元素总和 45
print(mat.sum())
# 元素行求和 [ 6 15 24]
print(mat.sum(axis=1))
# 元素列求和 [12 15 18]
print(mat.sum(axis=0))
