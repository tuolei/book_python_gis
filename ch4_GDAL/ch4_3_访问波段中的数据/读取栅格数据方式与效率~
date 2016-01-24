from osgeo import gdal
import time
dataset = gdal.Open("M51C004002.tif")
band = dataset.GetRasterBand(1)
width = dataset.RasterXSize
height = dataset.RasterYSize
bw = 128
bh = 128
bxsize = width/128
bysize = width/128
start = time.time()
band.ReadAsArray(0,0,width,height)
Out[88]: 
array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=uint8)

print time.time()-start
37.7681210041
start2 = time.time()
for i in range(bysize):
    for j in range(bxsize):
        band.ReadAsArray(bw*j,bh*i,bw,bh)
print time.time()-start2
