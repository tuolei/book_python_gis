# -*- coding: utf-8 -*-
import os


from shapely.geometry import Point
from shapely.prepared import prep
points = [(1,2),(2,3),(4,3),(5,6), (8,2), (9,1),(34,223)]
polygon = Point(0.0,0.0).buffer(1,0)
prepared_polygon = prep(polygon)
prepared_polygon
hits = filter(prepared_polygon.contains,points)

