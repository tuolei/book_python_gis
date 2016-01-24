# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

from osgeo import ogr
inshp='world_borders.shp'
datasource = ogr.Open(inshp)
layer = datasource.GetLayer(0)
dir(layer)

layer.GetFeatureCount()
layer.GetExtent()

layerdef = layer.GetLayerDefn()
for i in range(layerdef.GetFieldCount()):
    defn = layerdef.GetFieldDefn(i)
    print(defn.GetName(),defn.GetWidth(),defn.GetType(),defn.GetPrecision())