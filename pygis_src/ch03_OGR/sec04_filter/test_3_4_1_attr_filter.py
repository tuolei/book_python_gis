# -*- coding: utf-8 -*-

'''
根据属性条件选择要素
'''

from osgeo import ogr
import os

shpfile = 'gdata/world_borders.shp'
ds = ogr.Open(shpfile)
layer = ds.GetLayer(0)
lyr_count = layer.GetFeatureCount()
print(lyr_count)
layer.SetAttributeFilter("AREA > 800000")
lyr_count = layer.GetFeatureCount()
print(lyr_count)

# 根据属性条件生成要素
driver = ogr.GetDriverByName("ESRI Shapefile")
extfile = 'xx_world_borders.shp'
if os.access(extfile, os.F_OK):
    driver.DeleteDataSource(extfile)
newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('rect', None, ogr.wkbPolygon)
feat = layer.GetNextFeature()
while feat is not None:
    layernew.CreateFeature(feat)
    feat = layer.GetNextFeature()
newds.Destroy()
