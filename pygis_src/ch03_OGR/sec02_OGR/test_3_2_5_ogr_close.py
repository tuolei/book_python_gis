# -*- coding: utf-8 -*-
import os

import os

from osgeo import ogr

inshp = 'gdata/world_borders.shp'
datasource = ogr.Open(inshp)
layer = datasource.GetLayer(0)
feature = layer.GetFeature(0)

feature.Destroy()

datasource.Destroy()


def Test():
    assert True
