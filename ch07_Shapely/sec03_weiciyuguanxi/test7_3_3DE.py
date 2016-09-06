# -*- coding: utf-8 -*-
import os


from shapely.geometry import Point, LineString, LinearRing, Polygon

Point(0,0).relate(Point(1,1))
Point(0,0).relate(LineString([(0,0),(1,1)]))

