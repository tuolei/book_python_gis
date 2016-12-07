# -*- coding: utf-8 -*-
import os
import config

os.chdir(config.gisws)

from osgeo import ogr

inshp = 'world_borders.shp'
datasource = ogr.Open(inshp)
driver = datasource.GetDriver()
driver.name
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
inshp='world_borders.shp'
from osgeo import ogr
datasource=ogr.Open(inshp)
driver = datasource.GetDriver()
driver.name

dir(datasource)

driver = ogr.GetDriverByName('ESRI Shapefile')

# 使用driver打开数据
import sys
from osgeo import ogr
inshp = 'world_borders.shp'
driver = ogr.GetDriverByName('ESRI Shapefile')
dataSource = driver.Open(inshp,0)
if dataSource is None:
    print('could not open')

print('done')



def Test():
    assert datasource
    assert dataSource