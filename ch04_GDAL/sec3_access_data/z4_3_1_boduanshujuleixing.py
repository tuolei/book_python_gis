# -*- coding: utf-8 -*-
import os
import sys

from osgeo import gdalconst

dir(gdalconst)

from osgeo import gdal

dataset = gdal.Open("gdata/foo.tif")

print('=' * 20)
band = dataset.GetRasterBand(1)

from PIL import Image

# Todo: will echo warning if the image is big.
im = Image.open("gdata/foo.tif")
# region = im.crop((30,70,35,75))
# region.tostring()


data = dataset.ReadAsArray(1, 1, 1, 1)
datas = [i for i in data]
from numpy import reshape

datas = [reshape(i, (-1, 1)) for i in data]
import numpy

datas = numpy.concatenate(datas, 1)
