# -*- coding: utf-8 -*-
import os


from shapely.geometry import Point, LineString, LinearRing, Polygon,  MultiLineString, MultiPoint


from shapely.ops import polygonize
lines = [
    ((0,0),(1,1)),
    ((0,0),(0,1)),
    ((0,1),(1,1)),
    ((1,1),(1,0)),
    ((1,0),(0,0))
    ]
print(list(polygonize(lines)))

from shapely.ops import linemerge
linemerge(lines)
