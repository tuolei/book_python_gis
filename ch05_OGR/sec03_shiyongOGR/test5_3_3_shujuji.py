# -*- coding: utf-8 -*-
import os
import config

os.chdir(config.gisws)



# 创建点状数据集
from osgeo import ogr
import os ,math
driver = ogr.GetDriverByName("ESRI Shapefile")

extfile='xx_1world_borders.shp'
point_coors = [[300,450],[750,700],[1200,450],[750,200],[750,450]]
print(point_coors)
driver = ogr.GetDriverByName("ESRI Shapefile")
if os.access(extfile,os.F_OK):
    driver.DeleteDataSource(extfile)
newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('point',None,ogr.wkbPoint)
for aa in point_coors:
    wkt = 'POINT (' + str(aa[0]) + ' ' + str(aa[1]) + ')'
    geom = ogr.CreateGeometryFromWkt(wkt)
    feat = ogr.Feature(layernew.GetLayerDefn())
    feat.SetGeometry(geom)
    layernew.CreateFeature(feat)

newds.Destroy()

# 创建线状数据集
from osgeo import ogr
import os, math
driver =ogr.GetDriverByName("ESRI Shapefile")

extfile = 'xx_2world_borders.shp'
point_coors = [300,450,750,700,1200,450,750,200]
print(point_coors)
driver = ogr.GetDriverByName("ESRI Shapefile")
if os.access(extfile,os.F_OK):
    driver.DeleteDataSource(extfile)

newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('point',None,ogr.wkbLineString)

wkt = 'LINESTRING (%f %f %f %f %f %f %f %f %f %f)'  % (point_coors[0],point_coors[1],point_coors[2],point_coors[3],point_coors[4],point_coors[5],point_coors[6],point_coors[7],point_coors[0],point_coors[1])
print(wkt)
geom = ogr.CreateGeometryFromWkt(wkt)
feat = ogr.Feature(layernew.GetLayerDefn())
feat.SetGeometry(geom)
layernew.CreateFeature(feat)
newds.Destroy()

# 创建多边形数据集
from osgeo import ogr
import os,math
driver = ogr.GetDriverByName("ESRI Shapefile")

extfile = 'xx_3woeld_borders.shp'
if os.access(extfile,os.F_OK):
    driver.DeleteDataSource(extfile)

extent=[400,1100,300,600]

newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('rect',None,ogr.wkbPolygon)
width = math.fabs(extent[1]-extent[0])
height = math.fabs(extent[3]-extent[3])
tw = width/2
th = width/2
extnew = extent[0]+tw
wkt = 'POLYGON ((%f %f %f %f %f %f %f %f %f %f ))' % (extent[0],extent[3],extent[1],extent[3],extent[1],extent[2],extent[0],extent[2],extent[0],extent[3])

geom = ogr.CreateGeometryFromWkt(wkt)
feat = ogr.Feature(layernew.GetLayerDefn())
feat.SetGeometry(geom)
layernew.CreateFeature(feat)
newds.Destroy()

