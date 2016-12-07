# -*- coding: utf-8 -*-

from osgeo import gdal

dataset = gdal.Open("gdata/foo.tif")

import time

band = dataset.GetRasterBand(1)
width = dataset.RasterXSize
height = dataset.RasterYSize
bw = 128
bh = 128
# Todo: 下面两个值大的话可能溢出
bxsize = int(width / bw) - 10
bysize = int(width / bh) - 10
start = time.time()
band.ReadAsArray(0, 0, width, height)
print(time.time() - start)
start2 = time.time()
for tt in range(1000):
    for i in range(bysize):
        for j in range(bxsize):
            band.ReadAsArray(bw * j, bh * i, bw, bh)

print(time.time() - start2)

start3 = time.time()

for tt in range(1000):
    for j in range(bxsize):
        for i in range(bysize):
            band.ReadAsArray(bw * j, bh * i, bw, bh)

print(time.time() - start3)

