# -*- coding: utf-8 -*-
import os
from osgeo import gdal
import config

os.chdir(config.gisws)

import numpy
dataset = gdal.Open("foo.tif")
width = dataset.RasterXSize
height = dataset.RasterYSize
datas = dataset.ReadAsArray(0,0,width,height)

driver = gdal.GetDriverByName("GTiff")
tods = driver.Create("xx_foo3.tif",width,height,3,options=["INTERLEAVE=PIXEL"])
tods.WriteRaster(0,0,width,height,datas.tostring(),width,height,band_list=[1,2,3])

dataset = gdal.Open("foo.tif")
datas = dataset.ReadRaster(0,0,width,height)

datas = []
for i in range(3):
    band = dataset.GetRasterBand(i+1)
    data = band.ReadAsArray(0,0,width,height)
    # datas.append(numpy.reshape(data,(1,-1)))
    # atas = numpy.concatenate(datas)
    datas = numpy.concatenate(data)


def Test():
    assert True
