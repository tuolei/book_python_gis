# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

a = LineString([(0,0),(1,1),(1,2),(2,2)])
b = LineString([(0,0),(1,1),(2,1),(2,2)])
x = a.intersection(b)
from pprint import pprint
pprint(list(x))

pprint(list(x.geoms))
pprint(list(x))
from shpely.geometry import MultiPoint
m = MultiPoint([(0,0),(1,1),(1,2),(2,2)])
m[:1].wkt
m[3:].wkt
m[4:].wkt

#Collections of Points
from shapely.geometry import MultiPoint
points = MultiPoint([(0.0,0.0),(1.0,1.0)])
points.area
points.length
points.bounds

import pprint
pprint.pprint(list(points.geoms))
pprint.pprint(list(points))

#Collections of Lines
from shapyly.geometry import MultiLineString
coords = [((0,0),(1,1)),((-1,0),(1,0))]
lines = MultiLineString(coords)
lines.area
lines.lebgth
lines.bounds
len(lines.geoms)

#Collections of Polygon
polygons = MultiPolygon([polygon,s,t])
len(polygon.geoms)
len(polygons)
polygons.bounds