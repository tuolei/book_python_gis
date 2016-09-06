# -*- coding: utf-8 -*-
import os


from shapely.geometry import LineString
a = LineString([(0,0),(1,1),(1,2),(2,2)])
b = LineString([(0,0),(1,1),(2,1),(2,2)])
x = a.intersection(b)
from pprint import pprint
pprint(list(x))

pprint(list(x.geoms))
pprint(list(x))
from shapely.geometry import MultiPoint
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
from shapely.geometry import MultiLineString
coords = [((0,0),(1,1)),((-1,0),(1,0))]
lines = MultiLineString(coords)
lines.area
lines.length
lines.bounds
len(lines.geoms)

#Collections of Polygon
from shapely.geometry import MultiPolygon
# polygons = MultiPolygon([polygon,s,t])
# len(polygon.geoms)
# len(polygons)
# polygons.bounds