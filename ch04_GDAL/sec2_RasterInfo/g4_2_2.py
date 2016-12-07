# -*- coding: utf-8 -*-
import os
import config

# tifname = os.path.join(config.gisws, 'm510101.tif')
os.chdir(config.gisws)
from osgeo import gdal

dataset = gdal.Open("foo.tif")


def Test():

    assert os.path.exists( os.path.join(config.gisws, "foo.tif" ))
    assert dataset