# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

Point(0,0).wkt
Point(0,0).wkb.encode('hex')

from shapely.wkb import dumps,loads
wkb = dumps(Point(0,0))
print(wkb.encode('hex'))
loads(wkb).wkt

wkt = dumps(Point(0,0))
print(wkt)
loads(wkt).wkt