# -*- coding: utf-8 -*-

import os
# tifname = os.path.join(config.gisws, 'm510101.tif')
from osgeo import gdal
dataset = gdal.Open("gdata/foo.tif")


