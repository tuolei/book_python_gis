# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

# 删除矢量数据
import os
from osgeo import ogr
driver=ogr.GetDriverByName('ESRI Shapefile')
out_shp = 'xx_world_borders.shp'
if os.path.exists(out_shp):
    driver.DeleteDataSource(out_shp)

############
ds =driver.CreateDataSource(out_shp)
layer=ds.CreateLayer('test',geom_type=ogr.wkbPoint)
############
fieldDefn = ogr.FieldDefn('id',ogr.OFTString)
fieldDefn.SetWidth(4)
layer.CreateField(fieldDefn)

featureDefn =layer.GetLayerDefn()
feature=ogr.Feature(featureDefn)

point=ogr.Geometry(ogr.wkbPoint)
point.SetPoint(0,123,123)
feature.SetGeometry(point)

feature.SetField('id',23)

layer.CreateFeature(feature)
ds.Destroy()