from osgeo import gdal
import time

dataset = gdal.Open("gdata/lu75c.tif")
band = dataset.GetRasterBand(1)
width, height = dataset.RasterXSize, dataset.RasterYSize
bw, bh = 128, 128
bxsize = int(width / bw)
bysize = int(height / bh)
band.ReadAsArray(0, 0, width, height)
start = time.time()
band.ReadAsArray(0, 0, width, height)
print(time.time() - start)
start2 = time.time()
for i in range(bysize):
    for j in range(bxsize):
        band.ReadAsArray(bw * j, bh * i, bw, bh)
print(time.time() - start2)
start3 = time.time()
for j in range(bxsize):
    for i in range(bysize):
        band.ReadAsArray(bw * j, bh * i, bw, bh)
print(time.time() - start3)
