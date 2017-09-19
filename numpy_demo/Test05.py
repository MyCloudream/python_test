import numpy as np

# 创建等差数组，类似于range
a = np.arange(3)
# [0 1 2]
print(a)
# e的对应元素次幂
# 自然对数的底数e是由一个重要极限给出的.我们定义：当x趋于无限时,lim(1+1/x)^x=e.e是一个无限不循环小数,其值约等于2.718281828…,
print(np.exp(a))
