# -*- coding: utf-8 -*-
import os


from osgeo import gdal
# Todo: 这儿需要找索引的影像
dataset = gdal.Open("gdata/foo.tif")

band = dataset.GetRasterBand(1)
colormap = band.GetRasterColorTable()
# colormap.GetPaletteInterPretation()
# colormap.Getcount()

