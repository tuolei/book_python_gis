# -*- coding: utf-8 -*-


from osgeo import osr
from pprint import pprint

sr = osr.SpatialReference()
sr.SetWellKnownGeogCS('WGS84')
wkt = sr.ExportToWkt()
print(wkt)
pprint(wkt)
