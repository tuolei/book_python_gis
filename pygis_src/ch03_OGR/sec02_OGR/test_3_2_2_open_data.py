# -*- coding: utf-8 -*-
import os

from osgeo import ogr

inshp = 'gdata/world_borders.shp'
datasource = ogr.Open(inshp)
driver = datasource.GetDriver()
print(driver.name)
#######################
dir(datasource)
#######################
driver = ogr.GetDriverByName('ESRI Shapefile')

#######################


dataSource = driver.Open(inshp, 0)
if dataSource is None:
    print('could not open')
else:
    print('done')

#

datasource = ogr.Open(inshp)
driver = datasource.GetDriver()

dir(datasource)

# 使用driver打开数据
import sys

dataSource = driver.Open(inshp, 0)
if dataSource is None:
    print('could not open')

print('done')
