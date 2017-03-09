# -*- coding: utf-8 -*-
from osgeo import gdal

'''
band = gdal.Open('gdata/foo.tif').GetRasterBand(1)
band.ReadAsArray(100, 100, 5, 5, 10, 10)
# 这个有问题，segmentation fault python
'''

dataset = gdal.Open("gdata/foo.tif")

band = dataset.GetRasterBand(1)
print(band.DataType)

band.ReadAsArray(100, 100, 5, 5, 10, 10)

# help(band.ReadAsArray)

band.ReadAsArray(100, 100, 10, 10)

print(band.XSize)
print(band.YSize)
band.ReadAsArray(95, 100, 5, 5)

print(band.XSize)
print(band.YSize)

'''
以GDT开头的就是数值数据类型
要想查看图像中某一波段的数据类型，只需要打印这一波段的DataType属性即可
band.DataType
'''
from osgeo import gdalconst

print(dir(gdalconst))
