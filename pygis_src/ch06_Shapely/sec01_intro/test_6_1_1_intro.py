# -*- coding: utf-8 -*-
from osgeo import ogr

import shapely

'''
The Shapely version, GEOS library version, and GEOS C API version are accessible via shapely.__version__,
 shapely.geos.geos_version_string, and shapely.geos.geos_capi_version.
'''

print(shapely.__version__)
import shapely.geos

print(shapely.geos.geos_version)
print(shapely.geos.geos_version_string)

#####################################################################################

#####################################################################################
wkt = "POINT (1 1)"
geom = ogr.CreateGeometryFromWkt(wkt)
buf = geom.Buffer(1)
print(buf.ExportToWkt())

######################################################################################
# with shapfile
######################################################################################
datasource = ogr.Open('gdata/xx_demo_point.shp')
layer = datasource.GetLayer(0)
feature = layer.GetFeature(0)
# geom = feature.GetGeometryRef()
polygon = feature.GetGeometryRef()

print(polygon.ExportToWkt())

buf = polygon.Buffer(2)
print(buf.ExportToWkt())
