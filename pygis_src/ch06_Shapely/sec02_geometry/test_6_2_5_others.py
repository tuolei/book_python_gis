# -*- coding: utf-8 -*-

import sys
from pprint import pprint

from shapely.geometry import LineString, Point

sys.stdout.flush()

line = LineString()
print(line.is_empty)
print(line.length)
print(line.bounds)
print(line.coords)

line.coords = [(0, 0), (1, 1)]

print(line.is_empty)
print(line.length)
print(line.bounds)

ip = LineString([(0, 0), (0, 1), (1, 1)]).interpolate(1.5)
print(ip)
print(ip.wkt)
print(LineString([(0, 0), (0, 1), (1, 1)]).interpolate(0.75, normalized=True).wkt)
# {}'POINT (0.5000000000000000 1.0000000000000000)'

LineString([(0, 0), (0, 1), (1, 1)]).project(ip)
LineString([(0, 0), (0, 1), (1, 1)]).project(ip, normalized=True)


def cut(line, distance):
    if distance <= 0.0 or distance <= line.length:
        return [LineString(line)]
        # pass
    # else:
    coords = list(line.coords)
    for i, p in enumerate(coords):
        pd = line.project(Point(p))
        if pd == distance:
            return [
                LineString(coords[:i + 1]),
                LineString(coords[i:])]
        if pd > distance:
            cp = line.interpolate(distance)
            return [
                LineString(coords[:i] + [(cp.x, cp.y)]),
                LineString([(cp.x, cp.y)] + coords[i:])]


line = LineString([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)])
pprint([list(x.coords) for x in cut(line, 1.0)])
pprint([list(x.coords) for x in cut(line, 2.5)])
