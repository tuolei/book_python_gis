# -*- coding: utf-8 -*-
import os
from osgeo import ogr

inshp = 'gdata/world_borders.shp'
datasource = ogr.Open(inshp)
layer = datasource.GetLayer(0)
layer.GetSpatialRef()
layer.GetExtent()

feature = layer.GetFeature(0)
geom = feature.GetGeometryRef()
geom.GetEnvelope()
geom.GetSpatialReference()

geom.GetArea()


def Test():
    assert datasource
    assert layer
