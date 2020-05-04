# -*- coding: utf-8 -*-
"""
------------------------
  File Name:      3-sigma
  Descripton: 
  Author:         pineapple
  Date:           2020/5/4
------------------------
"""

'''
一个很直接的异常判定思路是，拿最新3个datapoint的平均值（tail_avg方法）和整个序列比较，看是否偏离总体平均水平太多。
怎样算“太多”呢，因为standard deviation表示集合中元素到mean的平均偏移距离，因此最简单就是和它进行比较。这里涉及到3-sigma理论：

简单来说就是：在normal distribution（正态分布）中，99.73%的数据都在偏离mean 3个σ (standard deviation 标准差) 的范围内。
如果某些datapoint到mean的距离超过这个范围，则认为是异常的。
'''