# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')


inshp='world_borders.shp'
from osgeo import ogr
datasource=ogr.Open(inshp)
driver = datasource.GetDriver()
driver.name

dir(datasource)

driver = ogr.GetDriverByName('ESRI Shapefile')

import sys
from osgeo import ogr
inshp = 'world_borders.shp'
driver = ogr.GetDriverByName('ESRI Shapefile')
dataSource = driver.Open(inshp,0)
if dataSource is None:
    print('could not open')

print('done')