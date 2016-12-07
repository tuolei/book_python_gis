# -*- coding: utf-8 -*-

from osgeo import gdal

dataset = gdal.Open("gdata/foo.tif")
help(dataset.ReadRaster)
help(dataset.ReadAsArray)

dataset.ReadAsArray(50, 50, 3, 3)
dataset.ReadRaster(50, 50, 3, 3)
dataset.ReadAsArray(30,70,5,5).tostring()

print(dataset.ReadAsArray(50, 50, 3, 3))
print(dataset.ReadRaster(50, 50, 3, 3))
