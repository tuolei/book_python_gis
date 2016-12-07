# -*- coding: utf-8 -*-
import os
from osgeo import gdal
import config

os.chdir(config.gisws)

dataset = gdal.Open("foo.tif")
width = dataset.RasterXSize
height = dataset.RasterYSize
data = dataset.ReadAsArray(0,0,width,height)
driver = gdal.GetDriverByName("GTiff")
driver.CreateCopy("xx_foo1.tif",dataset,0)


dataset = gdal.Open("foo.tif")
width = dataset.RasterXSize
height = dataset.RasterYSize
data = dataset.ReadAsArray(0,0,width,height)
driver = gdal.GetDriverByName("GTiff")
driver.CreateCopy("xx_foo2.tif",dataset,0,["INTERLEAVE=PIXEL"])

# Out[184]: <osgeo.gdal.Dataset; proxy of <Swig Object of type 'GDALDatasetShadow *' at 0x2ed3b70> >

def Test():
    assert True