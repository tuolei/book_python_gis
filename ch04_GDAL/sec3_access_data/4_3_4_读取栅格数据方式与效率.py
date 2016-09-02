# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

from osgeo import gdal
import time
dataset = gdal.Open("m510121.tif")
band = dataset.GetRasterBand(1)
width = dataset.RasterXSize
height = dataset.RasterYSize
bw = 128
bh = 128
bxsize = width/bw
bysize = width/bh
start = time.time()
band.ReadAsArray(0,0,width,height)
print (time.time()-start)
start2 = time.time()
for i in range(bysize):
    for j in range(bxsize):
        band.ReadAsArray(bw*j,bh*i,bw,bh)

print (time.time()-start2)
start3 = time.time()
for j in range(bxsize):
    for i in range(bysize):
        band.ReadAsArray(bw*j,bh*i,bw,bh)

print (time.time()-start3)
