# coding : utf-8
# Author : yuxiang Zeng

import numpy as np
import pandas as pd

def load_data(filename):
    address = './datasets/' + filename + '.xlsx'
    datasets = pd.read_excel(address)
    return datasets
