# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

#huanchongyigedian
from shapely.geommetry import Point
point = Point(10,10)
pt_buf = point.buffer(5)
print(pt_buf.wkt)

#Numpy
from numpy import asarray
a = asarray(point)
a.size
a.shape

from shapely.geometry import asLineString
a = array([[1.0,2.0],[3.0,4.0]])
line = asLinrString(a)
print(line.wkt)

#Geo jiekou
d= {"type":"point","coordinates":(0.0,0.0)}
from shapely.geometry import asShape
shape = asShape(d)
print(shape.geom_type)
tuple(shape.coords)

class GeoThing(object):
    def __init__(self,d):
        self.__geo_interface__ = d
thing = GeoThing({"type":"Point","coordinate":(0.0,0.0)})
shape = asShape(thing)
print(shape.geom_type)
tuple(shape.coords)

