# -*- coding: utf-8 -*-
"""
------------------------
  File Name:      common_tools
  Descripton: 
  Author:         pineapple
  Date:           2020/5/4
------------------------
"""

def ReadCSV2List(filepath, head=True, sep=","):
    result = []
    with open(filepath, "r") as f:
        if head:
            header = f.readline().strip().split(sep)
            result.append(header)
        line = f.readline()
        while line:
            result.append(line.strip().split(sep))
            line = f.readline()
    return result

if __name__ == "__main__":
    filepath = "/Users/pineapple/TimeSeriesDataMining/Data/AirPassengers.csv"
    print(ReadCSV2List(filepath))