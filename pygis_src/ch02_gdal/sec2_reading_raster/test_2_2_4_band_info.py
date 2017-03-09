# -*- coding: utf-8 -*-
import os

from osgeo import gdal

dataset = gdal.Open('gdata/lu75c.tif')
print(dataset.RasterCount)
band = dataset.GetRasterBand(1)
dir(band)

print(band.XSize)
print(band.YSize)
print(band.DataType)

band.GetNoDataValue()
band.GetMaximum()
band.GetMinimum()
band.ComputeRasterMinMax()

print(band.DataType)
