# -*- coding: utf-8 -*-
import os


from shapely.geometry import Point, LineString, LinearRing, Polygon,  MultiLineString, MultiPoint


line = LineString([(0,0),(1,1),(0,2),(2,2),(3,1),(1,0)])
dilated = line.buffer(0.5)
eroded = dilated.buffer(-0.3)

p = Point(0,0).buffer(10.0)
len(p.exterior.coords)
p.area

q = Point(0,0).buffer(10.0,1)
len(q.exterior.coords)
q.area

coords = [(0,0),(0,2),(1,1),(2,2),(2,0),(1,1),(0,0)]
bowtie = Polygon(coords)
bowtie.is_valid
clean = bowtie.buffer(0)
clean.is_valid
clean
len(clean)
list(clean[0].exterior.coords)

Point(0,0).convex_hull
MultiPoint([(0,0),(1,1)]).convex_hull
MultiPoint([(0,0),(1,1),(1,-1)]).convex_hull

Point(0,0).envelope
MultiPoint([(0,0),(1,1)]).envelope

p = Point(0.0,0.0)
x = p.buffer(1.0)
x.area
len(x.exterior.coords)
s = x.simplify(0.05,preserve_topology=False)
s.area
len(s.exterior.coords)

def Test():
    assert True