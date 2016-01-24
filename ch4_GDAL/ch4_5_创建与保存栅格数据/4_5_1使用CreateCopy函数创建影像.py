# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

import gdal
src_filename = "m510101.tif"
dst_filename = "m510101_copy.tif"
src_ds = gdal.Open(src_filename)
dst_ds = driver.CreateCopy(dst_filename,src_ds,0)

dst_filename2 = "m510101_copy2.tif"
dst_ds = driver.CreateCopy(dst_filename2,src_ds,0,['TILED = YES','COMPRESS=PACKBITS'])

dst_filename3 = "m510121_copy3.tif"
dst_ds = driver.CreateCopy(dst_filename3,src_ds,0,['TILED = YES','COMPRESS=PACKBITS'])

dataset = gdal.Open("m510101.tif")
width = dataset.RasterXSize
height = dataset.RasterYSize
data = dataset.ReadAsArray(0,0,width,height)
driver = gdal.GetDriverByName("Gtiff")
driver.CreateCopy("m510101.tif")



