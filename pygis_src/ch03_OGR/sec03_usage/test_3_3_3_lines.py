# -*- coding: utf-8 -*-
import os
# import config
#
# os.chdir(config.gisws)




# 创建线状数据集
from osgeo import ogr
import os

extfile = 'xx_2world_borders.shp'
point_coors = [300,450,750,700,1200,450,750,200]
print(point_coors)
driver = ogr.GetDriverByName("ESRI Shapefile")
if os.access(extfile,os.F_OK):
    driver.DeleteDataSource(extfile)

newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('point',None,ogr.wkbLineString)

wkt = 'LINESTRING (%f %f, %f %f, %f %f, %f %f, %f %f)'  % (point_coors[0],point_coors[1],point_coors[2],point_coors[3],point_coors[4],point_coors[5],point_coors[6],point_coors[7],point_coors[0],point_coors[1])
# wkt = 'LINESTRING(3 4,10 50,20 25)'
print(wkt)
geom = ogr.CreateGeometryFromWkt(wkt)
feat = ogr.Feature(layernew.GetLayerDefn())
feat.SetGeometry(geom)
layernew.CreateFeature(feat)
newds.Destroy()


