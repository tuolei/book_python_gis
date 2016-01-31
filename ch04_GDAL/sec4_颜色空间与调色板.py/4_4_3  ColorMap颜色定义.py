# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

from osgeo import gdal
dataset = gdal.Open("m510101.tif")
band = dataset.GetRasterBand(1)
colormap = band.GetRasterColorTable()
colormap.GetPaletteInterPretation()--------------
colormap.Getcount()
