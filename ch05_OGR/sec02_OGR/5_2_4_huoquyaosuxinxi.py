# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

from osgeo import ogr
inshp='world_borders.shp'
datasource = ogr.Open(inshp)
layer = datasource.GetLayer(0)
feature = layer.GetFeature(0)

##############

layer.ResetReading()
feat = layer.GetNextFeature()
while feat:
    feat = layer.GetNextFeature()
##############
layer.ResetReading()
feat=layer.GetFeature(0)
feat.keys()
feat.GetField('CNTRY_NAME')

##################
for i in range(feat.GetFieldCount()):
    print(feat.GetField(i))

##############################
geom = feat.GetGeometryRef()
geom.GetGeometryName()
geom.GetGeometryCount()
geom.GetPointCount()
geom.ExportToWkt()

###############################
polygon=geom.GetGeometryRef(0)
polygon.GetGeometryName()
polygon.GetGeometryCount()
polygon.GetPointCount()
polygon.GetX(0)
polygon.GetY(0)
polygon.GetZ(0)
polygon.ExportToWkt()