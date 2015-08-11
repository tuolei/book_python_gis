# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

from osgeo import ogr
inshp='world_borders.shp'
datasource = ogr.Open(inshp)
layer = datasource.GetLayer(0)
feature = layer.GetFeature(0)
print(feature.GetField('Name'))

feat = layer.GetNextFeature()
while feat:
    feat = layer.GetNextFeature()

layer.ResetReading()

feat=layer.GetFeature(0)
feat.keys()
fid=feat.GetField('AREA')
print(fid)

for i in range(feature.GetFieldCount()):
    print(feature.GetField(i))

geom = feature.GetGeometryRef()
geom.GetGeometryName()
geom .GetGeometryCount()
geom.GetPointCount()
geom.GetX()
geom.GetY()
print(geom)
print(geom.ExportToWkt())
polygon=geom.GetGeometryRef(0)
polygon.GetGeometryName()
polygon.GetGeometryCount()
polygon.GetPointCount()
polygon.GetX(0)
polygon.GetY(0)
polygon.GetZ(0)
print(polygon.ExportToWkt())