# -*- coding: utf-8 -*-
"""
------------------------
  File Name:      stddev_from_average
  Descripton: 
  Author:         pineapple
  Date:           2020/5/4
------------------------
"""
import pandas as pd
from common_tools import ReadCSV2List

def stddev_from_average(timeseries, datapoint):
    series = pd.Series([float(x[1]) for x in timeseries])
    mean = series.mean()
    stdDev = series.std()
    return abs(datapoint - mean) > 3 * stdDev

if __name__ == "__main__":
    data_path = "/Users/pineapple/TimeSeriesDataMining/Data/AirPassengers.csv"
    data = ReadCSV2List(data_path, head=True, sep=",")
    for line in data[1:]:
        line[1] = float(line[1])
    print(stddev_from_average(data[1:-1], data[-1][1]))
