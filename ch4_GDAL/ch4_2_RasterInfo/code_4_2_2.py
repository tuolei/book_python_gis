# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

from osgeo import gdal

dataset = gdal.Open("m510101.tif")

dir(dataset)
