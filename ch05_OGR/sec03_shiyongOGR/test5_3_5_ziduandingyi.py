# -*- coding: utf-8 -*-
import os
import config

os.chdir(config.gisws)


# 在OGR中定义属性字段与赋值
from osgeo import ogr
import os,math
driver =ogr.GetDriverByName("ESRI Shapefile")

extfile = 'xx_3world_borders.shp'
if os.access(extfile,os.F_OK):
    driver.DeleteDataSource(extfile)

extent= [400,1100,300,600]

newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('rect',None,ogr.wkbPolygon)

fieldcnstr = ogr.FieldDefn("fd",ogr.OFTString)
fieldcnstr.SetWidth(32)
layernew.CreateField(fieldcnstr)
fieldf = ogr.FieldDefn("f",ogr.OFTReal)
layernew.CreateField(fieldf)

wkt = 'POLYGON ((%f %f, %f %f, %f %f, %f %f, %f %f ))' % (extent[0],extent[3],extent[1],extent[3],extent[1],extent[2],extent[0],extent[2],extent[0],extent[3])

geom = ogr.CreateGeometryFromWkt(wkt)
feat = ogr.Feature(layernew.GetLayerDefn())
feat.SetField('fd',"2")
feat.SetGeometry(geom)
layernew.CreateFeature(feat)
newds.Destroy()

# 定义字段的位置
extfile = 'xx_8world_borders.shp'
if os.access(extfile,os.F_OK):
    driver.DeleteDataSource(extfile)

newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('rect3',None,ogr.wkbPolygon)
fieldcnstr = ogr.FieldDefn('fd',ogr.OFTString)
fieldcnstr.SetWidth(36)
fieldf = ogr.FieldDefn("f",ogr.OFTReal)
laydef = layernew.GetLayerDefn()
laydef.AddFieldDefn(fieldcnstr)
laydef.AddFieldDefn(fieldf)

newds.Destroy()