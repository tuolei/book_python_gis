# -*- coding: utf-8 -*-
import os
#os.chdir('/home/liujx/gdata')

import gdal
from osgeo import gdal

try:
    import gdal
except:
    from osgeo import gdal


gdal.AllRegister()
driver = gdal.GetDriverByName('HFA')
driver.Register()

driver = gdal.GetDriverByName('GTiff')
driver == None

from osgeo import gdal
drv_count = gdal.GetDriverCount()
for idx in range(drv_count):
    driver = gdal.GetDriver(idx)
    print("%10s:%s" % (driver.ShortName,driver.LongName))


 

