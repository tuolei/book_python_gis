# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

from osgeo import ogr
ds = ogr.Open('world_borders.shp')
layer = ds.GetLayer(0)
spatialRef= layer.GetSpatialRef()
print(spatialRef)

#genjuyiyoudetouyingchuangjiantouying
import osr
wkt = spatialRef.ExportToWkt()
spatial = ogr.SpatialReference()
spatial.ImportFromWkt(wkt)

#duishiliangshuju
targetSR = osr.SpatialReference()
targetSR.ImportFromEPSG(4326)
coordTrans = osr.CoordinateTransformation(spatial,targetSR)
feature = layer.GetFeature(0)
geom = feature.GeometryRef()
geom.ExporToWkt()
geom.Transform(coordTrans)
geom.ExportWkt()

#xiedoawenjianzhong
targetSR.MorphToESRI()
file = open('test.prj','w')
file.write(targetSR.ExportToWkt())
file.close()