# -*- coding: utf-8 -*-
import os

#yibande
from shapely.geometry import Point, LineString, LinearRing, MultiPolygon
Point(0,0).has_z
Point(0,0,0).has_z

LinearRing([(1,0),(1,1),(0,0)]).is_ccw

ring= LinearRing([(0,0),(1,1),(1,0)])
ring.is_ccw
ring.coords = list(ring.coords)[::-1]
ring.is_ccw

Point().is_empty
Point(0,0).is_empty

from operator import attrgetter
empties = filter(attrgetter('is_empty'),[Point(),Point(0,0), Point(1,2,3)])
# len(empties)

LineString([(0,0),(1,1),(1,-1)]).is_ring
LinearRing([(0,0),(1,1),(1,-1)]).is_ring

LineString([(0,0),(1,1),(1,-1),(0,1)]).is_simple

MultiPolygon([Point(0,0).buffer(2.0),Point(1,1).buffer(2.0)]).is_valid

from functools import wraps
def validata(func):
    wraps(func)
    def wrapper(*args,**kwargs):
        ob = func(*args,**kwargs)
        if not ob.is_valid:
            pass
            # Todo:
            # raise TopologicalError(Given aruments do not determine a valid geometic object)
        return ob
    return wrapper

# validate
def ring(coordinates):
    return LinearRing(coordinates)

coords = [(0,0),(1,1),(1,-1),(0,1)]
ring(coords)


def Test():
    assert True