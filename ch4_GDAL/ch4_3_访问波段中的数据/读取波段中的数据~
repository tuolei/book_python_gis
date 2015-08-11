ReadRaster()的函数细节
from osgeo import gdalconst
from osgeo import gdal
from gdalconst import *
dataset = gdal.Open("M51C004002.tif")
band = dataset.GetRasterBand(1)
band.ReadAsArray(100,100,5,5,100,100)


ReadAsArray的原型
help(band.ReadAsArray)
Help on method ReadAsArray in module osgeo.gdal:

ReadAsArray(self, xoff=0, yoff=0, win_xsize=None, win_ysize=None, buf_xsize=None, buf_ysize=None, buf_obj=None) method of osgeo.gdal.Band instance



栅格数据范围的处理
In [69]: band.XSize
Out[69]: 10
In [70]: band.YSize
Out[70]: 10
In [71]: band.ReadAsArray(95,100,5,5)


