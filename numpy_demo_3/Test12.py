import numpy as np
# 获得0-2π之间的10各数组成的数组，注意不是随机，而是平均分
a = np.linspace(0, 2 * np.pi, 10)
# [ 0. 0.6981317   1.3962634   2.0943951   2.7925268   3.4906585  4.1887902   4.88692191  5.58505361  6.28318531]
print(a)