# -*- coding: utf-8 -*-
import os
import config

os.chdir(config.gisws)


from osgeo import gdal
# Todo: 这儿需要找索引的影像
dataset = gdal.Open("foo.tif")

band = dataset.GetRasterBand(1)
colormap = band.GetRasterColorTable()
# colormap.GetPaletteInterPretation()
# colormap.Getcount()

def Test():
    assert dataset
    assert band
