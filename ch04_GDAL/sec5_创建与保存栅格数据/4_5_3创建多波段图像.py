# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

from osgeo import gdal
import numpy
dataset = gdal.Open("m510101.tif")
width = dataset.RasterXSize
height = dataset.RasterYSize
datas = dataset.ReadAsArray(0,0,width,height)

driver = gdal.GetDriverByName("GTiff")
tods = driver.Create("M51C004002.tif",width,height,3,options=["INTERLEAVE=PIXEL"])
tods.WriteRaster(0,0,width,height,datas.tostring(),width,height,band_list=[1,2,3])

datas = dataset.ReadData(0,0,width,height)

datas = []
for i in range(3):
    band = dataset.GetRasterBand(i+1)
    data = band.ReadAsArray(0,0,width,height)
    datas.append(Numpy.reshape(data,(1,-1)))
    atas = Numpy.conceteate(datas)

datas = numpy.concatenate(dates)