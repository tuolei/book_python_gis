# -*- coding: utf-8 -*-
import os
import config

os.chdir(config.gisws)

from osgeo import gdal
dataset = gdal.Open('lu75c.tif')
dataset.RasterCount
band = dataset.GetRasterBand(1)
dir(band)

band.XSize
band.YSize
band.DataType

band.GetNoDataValue()
band.GetMaximum()
band.GetMinimum()
band.ComputeRasterMinMax()

band.DataType


def Test():
    assert dataset

