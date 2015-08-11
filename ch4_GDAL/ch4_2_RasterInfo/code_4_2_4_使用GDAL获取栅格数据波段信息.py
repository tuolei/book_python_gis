# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

from osgeo import gdal
dataset = gdal.Open("m510121.tif")
dataset.RasterCount
band = dataset.GetRasterBand(3)

band = dataset.GetRasterBand(1)
dir(band)

band.XSize
band.YSize
band.DataType

band.GetNoDataValue()
band.GetMaximum()
band.GetMinimum()
band.ComputeRasterMinMax()



