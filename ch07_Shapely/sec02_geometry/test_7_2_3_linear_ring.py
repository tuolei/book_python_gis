# -*- coding: utf-8 -*-

from shapely.geometry.polygon import LinearRing

ring = LinearRing([(0, 0), (1, 1), (1, 0)])
print(ring.area)
print(ring.length)
print(ring.bounds)
print(len(ring.coords))
print(list(ring.coords))
print(LinearRing(ring))
