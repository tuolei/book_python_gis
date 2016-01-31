# -*- coding: utf-8 -*-

from osgeo import gdal
dataset = gdal.Open("/gdata/K52E015007.tif")
dataset.GetMetadata()
ds = gdal.Open('/gdata/lu75c.tif')
ds.GetMetadata()

dataset.GetDescription()

dataset.RasterCount

driver = gdal.GetDriverByName('HDF5')
driver.Register()
mds = gdal.Open("/gdata/MOD09A1.A2009193.h28v06.005.2009203125525.hdf")
mds.RasterCount

img_width,img_height = dataset.RasterXSize,dataset.RasterYSize
img_width,img_height

dataset.GetGeoTransform()

dataset.GetProjection()
