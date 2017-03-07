# -*- coding: utf-8 -*-

'''
command: python3 ch06_fiona/sec01_intro/g6_1_3_write.py
写入多层数据
'''
import fiona

with fiona.drivers():
    with fiona.open('gdata/world_borders.shp') as source:
        # print(dir(src))
        meta = source.meta
        f = next(source)
    with fiona.open('/tmp/foo', 'w', layer='bar', **meta) as dst:
        dst.write(f)
    print(fiona.listlayers('/tmp/foo'))
    with fiona.open('/tmp/foo', layer='bar') as src:
        print(len(src))
        f = next(src)
        print(f['geometry']['type'])
        print(f['properties'])
