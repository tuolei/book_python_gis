# -*- coding: utf-8 -*-
import os
from osgeo import ogr
import config

os.chdir(config.gisws)

inshp = 'world_borders.shp'
datasource = ogr.Open(inshp)
layer = datasource.GetLayer(0)
dir(layer)

layer.GetFeatureCount()
layer.GetExtent()

layerdef = layer.GetLayerDefn()
for i in range(layerdef.GetFieldCount()):
    defn = layerdef.GetFieldDefn(i)
    print(defn.GetName(), defn.GetWidth(), defn.GetType(), defn.GetPrecision())


def Test():
    assert datasource
    assert layer
