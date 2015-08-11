# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

from shapely.geometry import
from shapely.prepared import
points = [...]
polygon = Point(0.0,0.0).buffer(1,0)
prepared_polygon = prep(polygon)
prepared_polygon
hits = filter(prepared\_polygon.contains,points)

