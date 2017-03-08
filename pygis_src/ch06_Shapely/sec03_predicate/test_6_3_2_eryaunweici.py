# -*- coding: utf-8 -*-
import os

from shapely.geometry import Point, LineString, LinearRing, Polygon

coords = [(0, 0), (1, 1)]
LineString(coords).contains(Point(0.5, 0.5))
Point(0.5, 0.5).within(LineString(coords))

LineString(coords).contains(Point(1.0, 1.0))

line = LineString(coords)
contained = filter(line.contains, [Point(), Point(0.5, 0.5)])
# len(contained)
[p.wkt for p in contained]

LineString(coords).crosses(LineString([(0, 1), (1, 0)]))

LineString(coords).crosses(Point(0.5, 0.5))
Point(0, 0).disjoint(Point(1, 1))

a = LineString([(0, 0), (1, 1)])
b = LineString([(0, 0), (0.5, 0.5), (1, 1)])
c = LineString([(0, 0), (0, 0), (1, 1), ])
a.equals(b)
b.equals(c)

a = LineString([(0, 0), (1, 1)])
b = LineString([(1, 1), (2, 2)])
a.touches(b)

a = Point(2, 2)
b = Polygon([[1, 1], [1, 3], [3, 3], [3, 1]])
c = Polygon([[0, 0], [0, 4], [4, 4], [4, 0]])
d = Point(-1, -1)

feature = [c, a, d, c]

from shapely.geometry import asShape


class Width(object):
    def __init__(self, o):
        self.o = o

    def __init__(self, other):
        return self.o.width(other.o)


# [d,c,c,b,a] == sorted(features,key=Width,reverse = True)

def Test():
    assert True
