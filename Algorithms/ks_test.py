# -*- coding: utf-8 -*-
"""
------------------------
  File Name:      ks_test
  Descripton: 
  Author:         pineapple
  Date:           2020/5/4
------------------------
"""
'''
将timeseries分成两段：最近10min（probe），1 hour前 -> 10 min前这50分钟内（reference），
两个样本通过Kolmogorov-Smirnov测试后判断差异是否较大。
如果相差较大，则对refercence这段样本进行 Augmented Dickey-Fuller 检验（ADF检验），
查看其平稳性，如果是平稳的，
说明存在从平稳状态（50分钟）到另一个差异较大状态（10分钟）的突变，序列认为是异常的。
'''

import scipy
import statsmodels.api as sm
from common_tools import ReadCSV2List

def ks_test(timeseries_reference, timeseries_probe):
    reference = scipy.array([x[1] for x in timeseries_reference])
    probe = scipy.array([x[1] for x in timeseries_probe])
    ks_d, ks_p_value = scipy.stats.ks_2samp(reference, probe)
    if ks_p_value < 0.05 and ks_d > 0.5:
        adf = sm.tsa.stattools.adfuller(reference, 10)
        if adf[1] < 0.05:
            return True
    return False

if __name__ == "__main__":
    data_path = "/Users/pineapple/TimeSeriesDataMining/Data/AirPassengers.csv"
    data = ReadCSV2List(data_path, head=True, sep=",")
    for line in data[1:]:
        line[1] = float(line[1])
    split_num = int(len(data)*0.8)
    data1 = data[1: split_num]
    data2 = data[split_num : ]
    print(ks_test(data1, data2))

