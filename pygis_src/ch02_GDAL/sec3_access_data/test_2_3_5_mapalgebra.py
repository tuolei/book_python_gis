# -*- coding: utf-8 -*-


from osgeo import gdal
import numpy

dataset = gdal.Open("gdata/foo.tif")
band2 = dataset.GetRasterBand(2)
band3 = dataset.GetRasterBand(3)
cols = 100
rows = 100
# 有没有 astype ， 会产生两种结果
# 使用 pylint3  --extension-pkg-whitelist=numpy
# numpy.float,  无错误输出
# numpy.float16,  有错误输出
# numpy.float64,  有错误输出
data2 = band2.ReadAsArray(0, 0, cols, rows).astype(numpy.float64)
data3 = band3.ReadAsArray(0, 0, cols, rows).astype(numpy.float64)
print(data2)
print(data3)
mask = numpy.greater(data3 + data3, 0)
ndvi = numpy.choose(mask, (-99, (data3 - data2) / (data2 + data2)))

print(ndvi)
