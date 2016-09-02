# -*- coding: utf-8 -*-
import os
import config

# tifname = os.path.join(config.gisws, 'm510101.tif')
os.chdir(config.gisws)
from osgeo import gdal

dataset = gdal.Open("K52E015007.tif")


def Test():

    assert os.path.exists( os.path.join(config.gisws, "K52E015007.tif" ))
    assert dataset