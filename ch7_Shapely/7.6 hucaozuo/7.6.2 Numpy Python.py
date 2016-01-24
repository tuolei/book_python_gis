# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

from numpy import array
array(Point(0,0))
array(LineString([(0,0),(1,1)]))

Point(0,0).xy
LineString([(0,0),(1,1)]).xy

from shapely.geometry import asPoint
pa = asPoint(array([(0.0,0.0)]))
pa.wkt
