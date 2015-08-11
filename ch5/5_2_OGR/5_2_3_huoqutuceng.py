# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

inshp='world_borders.shp'
from osgeo import ogr
datasource = ogr.Open(inshp)
layer = datasource.GetLayer(0)
dir(layer)

n = layer.GetFeatureCount()
print('feature count:',n)

extent = layer.GetExtent()
print('extent:',extent)
print('ul:',extent[0],extent[3])
print('lr:',extent[1],extent[2])

layerdef = layer.GetLayerDefn()
for i in range(layerdef.GetFieldCount()):
    defn = layerdef.GetFieldDefn(i)
    print(defn.GetName(),defn.GetWidth(),defn.GetType(),defn.GetPrecision())