# -*- coding: utf-8 -*-
"""
------------------------
  File Name:      stddev_from_moving_average
  Descripton: 
  Author:         pineapple
  Date:           2020/5/4
------------------------
"""
import pandas as pd
from common_tools import ReadCSV2List

def stddev_from_moving_average(timeseries):
    series = pd.Series([x[1] for x in timeseries])
    expAverage = series.ewm(com=50).mean()
    stdDev = series.ewm(com=50).std()
    length = len(stdDev)
    return abs(series[length-1] - expAverage[length-1]) > 3 * stdDev[length-1]

if __name__ == "__main__":
    data_path = "/Users/pineapple/TimeSeriesDataMining/Data/AirPassengers.csv"
    data = ReadCSV2List(data_path, head=True, sep=",")
    for line in data[1:]:
        line[1] = float(line[1])
    print(stddev_from_moving_average(data[1:]))