# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

from shapely.geometry import asShape
d = {"type":"Point","coordinates": (0.0,0.0)}
shape =asShape(d)
shape.geom_type
list(shape.coords)

class GeoThing(object):
    def __init__(self,d):
        self.__geo_interface__ = d
thing = GeoThing({"typr":"Point","coordinates": (0.0,0.0)})
shape = asShape(thing)
shape.geom_type
list(shape.coords)

from shapely.geometry import mapping
thing = GeoThing({"typr":"Point","coordinates":(0.0,0.0)})
m = mapping(thing)
m['type']
m['coordinates']
