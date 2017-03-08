# -*- coding: utf-8 -*-
'''
command:
    python3 ch06_fiona / sec02_intro / g6_2_3_design.py

'''
import fiona

c = fiona.open('gdata/world_borders.shp')
print(c.driver)
print(c.crs)

from fiona.crs import to_string
print(to_string(c.crs))

from fiona.crs import from_string
print(from_string("+datum=WGS84 +ellps=WGS84 +no_defs +proj=longlat"))

from fiona.crs import from_epsg
print(from_epsg(3857))

print(len(c))

print(c.bounds)

from pprint import pprint
pprint(c.schema)