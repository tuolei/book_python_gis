# -*- coding: utf-8 -*-
import os

'''
创建3波段GTiff的例子，多波段影像的创建方式与之类似
'''

from osgeo import gdal

import numpy

dataset = gdal.Open("gdata/foo.tif")

width = dataset.RasterXSize

height = dataset.RasterYSize

datas = dataset.ReadAsArray(0, 0, width, height)

driver = gdal.GetDriverByName("GTiff")

tods = driver.Create("xx_foo3.tif", width, height, 3, options=["INTERLEAVE=PIXEL"])
tods.WriteRaster(0, 0, width, height, datas.tostring(), width, height, band_list=[1, 2, 3])

# tods.Destroy()
del (tods)




# # 向tods写入数据时，需要转换数据类型datas.tostringa().如果需要读取数据，使用下面的数据：
# datas2 = dataset.ReadData(0,0,width,height)
#
#
# # 分波段处理
# datas3 = []
# for i in range(3):
#     band = dataset.GetRasterBand(i+1)
#     data = band.ReadAsArray(0,0,width,height)
#     datas3.append(numpy.reshape(data,(1,-1)))
#     atas = numpy.conceteate(datas)
