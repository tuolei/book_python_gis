# -*- coding: utf-8 -*-
import os
import config

os.chdir(config.gisws)

from osgeo import gdal
dataset = gdal.Open("K52E015007.tif")
help(dataset.ReadRaster)
help(dataset.ReadAsArray)

dataset.ReadAsArray(50,50,3,3)
dataset.ReadRaster(50,50,3,3)


def Test():
    assert dataset




