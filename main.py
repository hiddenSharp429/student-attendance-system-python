# coding : utf-8
# Author : yuxiang Zeng

import numpy as np
import pandas as pd

from ds_tools.data_structure import create_array, append_element, update_element, sort_element, search_element

if __name__ == '__main__':
    arr = create_array(10)
    print(arr)

    arr = append_element(arr, 1)
    print(arr)

    arr = append_element(arr, 3)
    print(arr)

    arr = update_element(arr, 2, 2)
    print(arr)

    arr = sort_element(arr)
    print(arr)

    print(search_element(arr, 3))


