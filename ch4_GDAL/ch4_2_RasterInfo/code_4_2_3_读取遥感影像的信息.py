# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')


from osgeo import gdal
dataset = gdal.Open("m510121.tif")
dataset.GetMetadata()

dataset.GetDescription()

dataset.RasterCount

mds = gdal.Open("m510121.tif")
mds.RasterCount

img_width,img_height = dataset.RasterXSize,dataset.RasterYSize
img_width,img_height

dataset.GetGeoTransform()

dataset.GetProjection()