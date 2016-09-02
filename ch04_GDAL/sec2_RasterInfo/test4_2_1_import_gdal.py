# -*- coding: utf-8 -*-
import os
import gdal
from osgeo import gdal

try:
    import gdal
except:
    from osgeo import gdal

from osgeo.gdalconst import *

gdal.AllRegister()
driver = gdal.GetDriverByName('HFA')
driver.Register()

driver = gdal.GetDriverByName('GTiff')

driver == None

from osgeo import gdal
drv_count = gdal.GetDriverCount()
for idx in range(drv_count):
    driver2 = gdal.GetDriver(idx)
    print("%10s:%s" % (driver2.ShortName,driver2.LongName))


def Test():
    assert driver.ShortName == 'GTiff'

