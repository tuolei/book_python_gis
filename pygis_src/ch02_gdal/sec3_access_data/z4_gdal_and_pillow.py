from osgeo import gdal

dataset = gdal.Open("gdata/lu75c.tif")
dataset.ReadAsArray(30, 70, 5, 5).tostring()
dataset.ReadRaster(30, 70, 5, 5)

# 使用PIL读取数据
from PIL import Image

im = Image.open("gdata/lu75c.tif")
region = im.crop((30,  35,  70, 75)) # (left, uppper, right, lower)
region.tostring()

data = dataset.ReadAsArray(1, 1, 1, 1)
datas = [i for i in data]
import numpy
from numpy import reshape

datas = [reshape(i, (-1, 1)) for i in data]
datas = numpy.concatenate(datas, 1)  # -------numpy没有定义

# 从波段看
r, g, b = region.split()
r.tostring()
band = dataset.getRasterBand(1)
band.ReadRaster(30, 70, 5, 5)

# 从写数据来看
help(dataset.WriteRaster)
help(band.WriteRaster)
help(band.WriteArray)

# PIL中对数据的写入用的是paste
help(im.paste)
# PIL 还有个好东西----fromstring
help(Image.fromstring)
