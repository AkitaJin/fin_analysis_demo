#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Descripttion: 
version: 
Author: Jin
Date: 2021-06-17 16:59:08
LastEditors: Jin
LastEditTime: 2021-06-21 14:22:18
'''

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

class Demo():


    '''
    @name: 
    @msg: 
    @param {*} self
    @param {*} filepath
    @return {*}
    '''
    def explore(self, filepath):
        df = pd.read_excel(filepath)
        return 1

if __name__ == '__main__':
    dc = Demo()
    #一步一步生成excel表，最后的函数方法通过图表展示出结果
    # dc.tansuo('HW_data/bank-all.csv')
    # dc.qingxi('HW_data/bank_data.xls')
    # dc.xuanze('HW_data/bank_clean.xls')
    # dc.zhuanhuan('HW_data/bank_choose.xls')
    # dc.biaozhun('HW_data/bank_zhuanhuan.xls')
    # dc.kmeans('HW_data/bank_biaozhun.xls',k=5)
    dc.explore()
    pass