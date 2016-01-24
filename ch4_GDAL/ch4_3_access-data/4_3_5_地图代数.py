# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

from osgeo import gdal
import numpy
dataset = gdal.Open("m510121.tif")
band2= dataset.GetRasterBand(2)
band3= dataset.GetRasterBand(3)
cols = 100
rows = 100
data2 = band2.ReadAsArray(0,0,cols,rows).astype(numpy.float16)
data3 = band3.ReadAsArray(0,0,cols,rows).astype(numpy.float16)
mask =numpy.greater(data3 + data3,0)
ndvi = numpy.choose(mask,(-99,(data3 - data2) / (data2 + data2)))



