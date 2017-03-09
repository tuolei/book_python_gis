# -*- coding: utf-8 -*-
'''
command:
    python3 ch06_fiona/sec02_intro/g6_2_4_records.py
'''
import fiona
from pprint import pprint

c = fiona.open('gdata/world_borders.shp')

rec = next(c)

pprint(rec)
print(rec['id'])
c.close()
print(rec['id'])

pprint(rec['properties'])

pprint(rec['geometry'])
