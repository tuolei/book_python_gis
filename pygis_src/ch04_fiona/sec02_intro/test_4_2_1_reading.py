# -*- coding: utf-8 -*-

'''
command:
    python3 ch06_fiona/sec01_intro/g6_1_4_zipfile.py
读取
'''

import fiona

c = fiona.open('gdata/world_borders.shp', 'r')
print(c)
# c.closed
next(c)
len(list(c))

# print(c.next())
len(list(c))

c = fiona.open('gdata/world_borders.shp')
len(list(c))

import pprint

with fiona.open('gdata/world_borders.shp') as src:
    pprint.pprint(src[1])

with fiona.open('gdata/world_borders.shp') as src:
    pprint.pprint(src[0])

####################################################
# 根据索引读取数据
import pprint

with fiona.open('gdata/world_borders.shp') as src:
    pprint.pprint(src[1])

####################################################
# 关闭文件
