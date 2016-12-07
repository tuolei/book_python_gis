# -*- coding: utf-8 -*-
import os


from shapely.geometry.polygon import LinearRing
ring = LinearRing([(0,0),(1,1),(1,0)])
ring.area
ring.length
ring.bounds
len(ring.coords)
list(ring.coords)
LinearRing(ring)