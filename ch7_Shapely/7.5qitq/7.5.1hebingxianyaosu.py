# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

from shapely.ops. import polygonize
lines = [
    ((0,0),(1,1)),
    ((0,0),(0,1)),
    ((0,1),(1,1)),
    ((1,1),(1,0)),
    ((1,0),(0,0))
    ]
pprint(list(polygonize(lines)))

from shapely.ops import linemerge
linemerge(lines)
