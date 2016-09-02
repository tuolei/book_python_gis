# -*- coding: utf-8 -*-
import os
import config
from osgeo import gdal

os.chdir(config.gisws)
dataset = gdal.Open("K52E015007.tif")
dataset.GetMetadata()

ds = gdal.Open('lu75c.tif')
ds.GetMetadata()

dataset.GetDescription()

dataset.RasterCount
img_width, img_height = dataset.RasterXSize, dataset.RasterYSize
img_width, img_height

dataset.GetGeoTransform()

dataset.GetProjection()

driver = gdal.GetDriverByName('HDF5')
driver.Register()
mds = gdal.Open("MOD09A1.A2009193.h28v06.005.2009203125525.hdf")
mds.RasterCount


def Test():
    assert dataset
    assert ds
    assert mds
