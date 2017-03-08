# -*- coding: utf-8 -*-
import os
from osgeo import gdal


dataset = gdal.Open("gdata/foo.tif")
width = dataset.RasterXSize
height = dataset.RasterYSize
data = dataset.ReadAsArray(0,0,width,height)
driver = gdal.GetDriverByName("GTiff")
driver.CreateCopy("gdata/xx_foo1.tif",dataset,0)


dataset = gdal.Open("gdata/foo.tif")
width = dataset.RasterXSize
height = dataset.RasterYSize
data = dataset.ReadAsArray(0,0,width,height)
driver = gdal.GetDriverByName("GTiff")
driver.CreateCopy("gdata/xx_foo2.tif",dataset,0,["INTERLEAVE=PIXEL"])

