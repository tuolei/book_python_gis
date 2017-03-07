# -*- coding: utf-8 -*-

'''
command： python3 ch06_fiona/sec01_intro/s2.py
读取数据集中要素的数目。
'''

import fiona

with fiona.drivers():
    for layername in fiona.listlayers('gdata'):
        with fiona.open('gdata', layer=layername) as src:
            print(layername, len(src))

# 指定索引
with fiona.drivers():
    for i, layername in enumerate(fiona.listlayers('gdata')):
        with fiona.open('gdata', layer=i) as src:
            print(i, layername, len(src))
