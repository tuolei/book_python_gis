# -*- coding: utf-8 -*-
import os
import config

os.chdir(config.gisws)

# 在datasource层次创建数据
from osgeo import ogr
import os, math

inshp = 'world_borders.shp'
ds = ogr.Open(inshp)
driver = ogr.GetDriverByName("ESRI Shapefile")
outputfile = 'x_world_borders_copy.shp'
if os.access(outputfile, os.F_OK):
    driver.DeleteDataSource(outputfile)

pt_cp = driver.CopyDataSource(ds, outputfile)
pt_cp.Release()

# 在layer层次拷贝数据
from osgeo import ogr
import os, math

inshp = 'world_borders.shp'
ds = ogr.Open(inshp)
driver = ogr.GetDriverByName("ESRI Shapefile")
outputfile = 'world_borders_copy2.shp'
if os.access(outputfile, os.F_OK):
    driver.DeleteDataSource(outputfile)

layer = ds.GetLayer()
newds = driver.CreateDataSource(outputfile)
pt_layer = newds.CopyLayer(layer, 'abcd')
newds.Destroy()

# 在feature层次拷贝数据
ds = ogr.Open(inshp)
driver = ogr.GetDriverByName("ESRI Shapefile")
outputfile = 'world_borders_copy3.shp'
if os.access(outputfile, os.F_OK):
    driver.DeleteDataSource(outputfile)

newds = driver.CreateDataSource(outputfile)
layernew = newds.CreateLayer('worldcopy', None, ogr.wkbLineString)
layer = ds.GetLayer()
extent = layer.GetExtent()
print(extent)
feature = layer.GetNextFeature()
while feature is not None:
    layernew.CreateFeature(feature)
    feature = layer.GetNextFeature()

newds.Destroy()


def Test():
    assert True
