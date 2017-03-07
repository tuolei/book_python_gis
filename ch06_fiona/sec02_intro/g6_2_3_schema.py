# -*- coding: utf-8 -*-
'''
command:
    python3 ch06_fiona/sec02_intro/g6_2_3_schema.py
'''
import fiona

c = fiona.open('gdata/world_borders.shp')

from pprint import pprint

pprint(c.schema)

rec = next(c)
print(set(rec.keys()) - set(c.schema.keys()))

print(set(rec['properties'].keys()) == set(c.schema['properties'].keys()))

pprint(fiona.FIELD_TYPES_MAP)

print(type(rec['properties']['CNTRY_NAME']))

print(c.schema['properties']['CNTRY_NAME'])

print(fiona.FIELD_TYPES_MAP[c.schema['properties']['CNTRY_NAME'].split(':')[0]])

from fiona import prop_width
print(prop_width('str:25'))
print(prop_width('str'))

from fiona import prop_type
print(prop_type('int'))
print(prop_type('float'))
print(prop_type('str:25'))

pprint(rec)