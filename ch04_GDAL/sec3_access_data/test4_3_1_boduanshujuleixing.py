# -*- coding: utf-8 -*-
import os

import config

os.chdir(config.gisws)

from osgeo import gdalconst
dir(gdalconst)


from osgeo import gdal
dataset = gdal.Open("foo.tif")
dataset.ReadAsArray(30,70,5,5).tostring()
dataset.ReadRaster(30,70,5,5)
print('=' * 20)
band = dataset.GetRasterBand(1)
print(band.DataType)

from PIL import Image
# Todo: will echo waring if the image is big.
im = Image.open("foo.tif")
# region = im.crop((30,70,35,75))
# region.tostring()


data = dataset.ReadAsArray(1,1,1,1)
datas = [i for i in data]
from numpy import reshape
datas = [reshape(i,(-1,1)) for i in data]
import numpy
datas = numpy.concatenate(datas,1)


# r,g,b = region.split()
# r.tostring()
band = dataset.GetRasterBand(1)
band.ReadRaster(30,70,5,5)

# help(dataset.WriteRaster)
# help(band.WriteRaster)
# help(band.WriteArray)
# help(im.paste)
# help(Image.fromstring)
#






