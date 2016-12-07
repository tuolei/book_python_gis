# -*- coding: utf-8 -*-
import os
from shapely.geometry import Point

Point(0,0).wkt

# 下面这个，在Python 3中执行有问题。
# Point(0,0).wkb.encode('hex')

from shapely.wkb import dumps,loads
wkb = dumps(Point(0,0))
# print(wkb.encode('hex'))
loads(wkb).wkt

wkt = dumps(Point(0,0))
print(wkt)
loads(wkt).wkt

def Test():
    assert True
