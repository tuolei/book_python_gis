# -*- coding: utf-8 -*-
import os


from shapely.geometry import Polygon
coords =[(0,0),(0,2),(1,1),(2,2),(2,0),(1,1),(0,0)]
p = Polygon(coords)
from shapely.validation import explain_validity
explain_validity(p)

def Test():
    assert True