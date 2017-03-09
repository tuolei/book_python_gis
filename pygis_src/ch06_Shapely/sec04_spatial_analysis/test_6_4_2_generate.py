# -*- coding: utf-8 -*-
import os

from shapely.geometry import Point, LineString, LinearRing, Polygon, MultiLineString, MultiPoint

line = LineString([(0, 0), (1, 1), (0, 2), (2, 2), (3, 1), (1, 0)])
dilated = line.buffer(0.5)
eroded = dilated.buffer(-0.3)

p = Point(0, 0).buffer(10.0)
print(len(p.exterior.coords))
print(p.area)

q = Point(0, 0).buffer(10.0, 1)
len(q.exterior.coords)
print(q.area)

coords = [(0, 0), (0, 2), (1, 1), (2, 2), (2, 0), (1, 1), (0, 0)]
bowtie = Polygon(coords)
print(bowtie.is_valid)
clean = bowtie.buffer(0)
print(clean.is_valid)
print(clean)
len(clean)
list(clean[0].exterior.coords)

print(Point(0, 0).convex_hull)
print(MultiPoint([(0, 0), (1, 1)]).convex_hull)
print(MultiPoint([(0, 0), (1, 1), (1, -1)]).convex_hull)

print(Point(0, 0).envelope)
print(MultiPoint([(0, 0), (1, 1)]).envelope)

p = Point(0.0, 0.0)
x = p.buffer(1.0)
print(x.area)
len(x.exterior.coords)
s = x.simplify(0.05, preserve_topology=False)
print(s.area)
len(s.exterior.coords)
