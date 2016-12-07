# -*- coding: utf-8 -*-
from osgeo import gdal

dataset = gdal.Open("gdata/foo.tif")

band = dataset.GetRasterBand(1)
band.ReadAsArray(100, 100, 5, 5, 10, 10)

help(band.ReadAsArray)

band.ReadAsArray(100, 100, 10, 10)

band.XSize
band.YSize
band.ReadAsArray(95, 100, 5, 5)

print(band.XSize)
print(band.YSize)