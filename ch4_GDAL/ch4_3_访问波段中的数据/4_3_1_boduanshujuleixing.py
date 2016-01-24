# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

from osgeo import gdalconst
dir(gdalconst)
band.DataType

from osgeo import gdal
dataset = gdal.Open("m510121.tif")
dataset.ReadAsArray(30,70,5,5).tostring()
dataset.ReadRaster(30,70,5,5)


import Image
im = Image.open("m510121.tif")
region = im.crop((30,70,35,75))
region.tostring()


data = dataset.ReadAsArray(1,1,1,1)
datas = [i for i in data]
from numpy import reshape
datas = [reshape(i,(-1,1)) for i in data]
import numpy
datas = numpy.concatenate(datas,1)


r,g,b = region.split()
r.tostring()
band = dataset.GetRasterBand(1)
band.ReadRaster(30,70,5,5)

help(dataset.WriteRaster)
help(band.WriteRaster)
help(band.WriteArray)

help(im.paste)

help(Image.fromstring)
  

 


