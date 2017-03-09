# -*- coding: utf-8 -*-


from shapely.geometry import Point, LineString, LinearRing, Polygon, MultiLineString

coords = [((0, 0), (1, 1)), ((-1, 0), (1, 0))]
lines = MultiLineString(coords)
print(lines.boundary)
print(list(lines.boundary))
print(lines.boundary.boundary.is_empty)

print(LineString([(0, 0), (1, 1)]).centroid)
print(LineString([(0, 0), (1, 1)]).centroid.wkt)

a = Point(1, 1).buffer(1.5)
b = Point(2, 1).buffer(1.5)
a.difference(b)

a.intersection(b)

a.symmetric_difference(b)

a.union(b)

print(a.union(b).boundary)
a.boundary.union(b.boundary)


