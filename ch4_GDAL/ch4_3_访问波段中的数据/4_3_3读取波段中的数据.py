# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')


from osgeo import gdal
from gdalconst import *
dataset = gdal.Open("m510121.tif")
band = dataset.GetRasterBand(1)
band.ReadAsArray(100,100,5,5,10,10)

help(band.ReadAsArray)

band.ReadAsArray(100,100,10,10)

band.XSize
band.YSize
band.ReadAsArray(95,100,5,5)


