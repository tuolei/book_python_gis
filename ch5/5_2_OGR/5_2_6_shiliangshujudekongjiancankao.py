# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

from osgeo import ogr
inshp='world_borders.shp'
datasource = ogr.Open(inshp)
layer = datasource.GetLayer(0)
layer.GetSpatialRef()
layer.GetExtent()

frature = layer.GetFeature(0)
geom =feature.GetGeometryRef()
geom.GetEnvelope()
geom.GetSpatialReference()

geom.GetArea()
