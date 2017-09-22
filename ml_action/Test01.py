import numpy as np

import operator


def create_data_set():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(x, data_set, labels, k):
    # 获取数据集（二维数组）的行数，这里是4（数据集是4行2列）
    data_set_size = data_set.shape[0]
    # tile：把x数据在x纵向复制成4份，横向复制成1份（也即不变）
    diff_mat = np.tile(x, (data_set_size, 1)) - data_set
    print(diff_mat)
    # 求矩阵各元素的平方
    sq_diff_mat = diff_mat ** 2
    print(sq_diff_mat)
    # 矩阵行求和
    sq_distances = sq_diff_mat.sum(axis=1)
    print(sq_distances)
    # 和的0.5次方，也即针对和开根号
    distances = sq_distances ** 0.5
    print(distances)
    # 返回数组值从小到大的索引值
    sorted_dist_indices = distances.argsort()
    print(sorted_dist_indices)
    # 定义字典
    class_count = {}
    for i in range(k):
        vote_label = labels[sorted_dist_indices[i]]
        print(vote_label)
        class_count[vote_label] = class_count.get(vote_label, 0) + 1
        print(class_count[vote_label])
        sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
        print(sorted_class_count)
    print(sorted_class_count)
    return sorted_class_count[0][0]


def main():
    group, labels = create_data_set()
    a = classify0([1, 1.2], group, labels, 3)
    print(a)


if __name__ == '__main__':
    main()
