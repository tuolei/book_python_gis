# -*- coding: utf-8 -*-

from shapely.geometry import LineString

a = LineString([(0, 0), (1, 1), (1, 2), (2, 2)])
b = LineString([(0, 0), (1, 1), (2, 1), (2, 2)])
x = a.intersection(b)
from pprint import pprint

pprint(list(x))

pprint(list(x.geoms))
pprint(list(x))
from shapely.geometry import MultiPoint

m = MultiPoint([(0, 0), (1, 1), (1, 2), (2, 2)])
print(m[:1].wkt)
print(m[3:].wkt)
print(m[4:].wkt)

# Collections of Points
from shapely.geometry import MultiPoint

points = MultiPoint([(0.0, 0.0), (1.0, 1.0)])
print(points.area)
print(points.length)
print(points.bounds)

import pprint

pprint.pprint(list(points.geoms))
pprint.pprint(list(points))

# Collections of Lines
from shapely.geometry import MultiLineString

coords = [((0, 0), (1, 1)), ((-1, 0), (1, 0))]
lines = MultiLineString(coords)
print(lines.area)
print(lines.length)
print(lines.bounds)
print(len(lines.geoms))

# Collections of Polygon
from shapely.geometry import MultiPolygon
# polygons = MultiPolygon([polygon,s,t])
# len(polygon.geoms)
# len(polygons)
# polygons.bounds
