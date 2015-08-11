# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

from osgeo import ogr
wkt = "POINT (1, 1)"
geom = ogr.CreateGeometryFromWkt(wkt)
buf = geom.Buffer(1)
buf.ExportToWkt()

print()