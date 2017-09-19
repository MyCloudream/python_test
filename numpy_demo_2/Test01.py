import numpy as np

a = np.floor(10 * np.random.random((2, 2)))
'''
[[ 1.  1.]
 [ 6.  3.]]
'''
print(a)

b = np.floor(10 * np.random.random((2, 2)))
'''
[[ 3.  7.]
 [ 7.  0.]]
'''
print(b)

# 按行拼接，也即竖着拼接,把b放在a的下面
'''
[[ 1.  1.]
 [ 6.  3.]
 [ 3.  7.]
 [ 7.  0.]]
'''
print(np.vstack((a, b)))

# 按列拼接，也即横着拼接，把b放在a的后面
'''
[[ 1.  1.  3.  7.]
 [ 6.  3.  7.  0.]]
'''
print(np.hstack((a, b)))
