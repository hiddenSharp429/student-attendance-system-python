import numpy as np

# 创建数组
def create_array(size):
    array = np.zeros(size)
    for i in range(len(array)):
        array[i] = np.inf
    return array

# 插入值
def append_element(array, value):
    position = search_element(array, np.inf)[0]
    array[position] = value
    array = sort_element(array)
    return array

# 删除某值，输入下标索引
def delete_element(array, index):
    array = np.delete(array, index)
    array = sort_element(array)
    return array

# 修改具体的值
def update_element(array, index, new_value):
    array[index] = new_value
    array = sort_element(array)
    return array

# 查找具体的值索引
def search_element(array, value):
    indices = np.where(array == value)[0]
    return indices if indices.size > 0 else None

# 排序算法
def sort_element(array):
    return np.sort(array)
