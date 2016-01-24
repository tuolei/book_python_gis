# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

from osgeo import gdal
dataset = gdal.Open("m510121.tif")
help(dataset.ReadRaster)
help(dataset.ReadAsArray)

dataset.ReadAsArray(50,50,3,3)
dataset.ReadRaster(50,50,3,3)





