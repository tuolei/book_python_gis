# -*- coding: utf-8 -*-
import os

from shapely.geometry import Point, LineString
from numpy import array

print(array(Point(0, 0)))
print(array(LineString([(0, 0), (1, 1)])))

print(Point(0, 0).xy)
print(LineString([(0, 0), (1, 1)]).xy)

from shapely.geometry import asPoint

pa = asPoint(array([(0.0, 0.0)]))


# pa.wkt

