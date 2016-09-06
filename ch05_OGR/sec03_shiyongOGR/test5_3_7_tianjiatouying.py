# -*- coding: utf-8 -*-
import os
import os
import config

os.chdir(config.gisws)


from osgeo import ogr
ds = ogr.Open('world_borders.shp')
layer = ds.GetLayer(0)
spatialRef= layer.GetSpatialRef()
print(spatialRef)

#genjuyiyoudetouyingchuangjiantouying
import osr
wkt = spatialRef.ExportToWkt()
spatial = osr.SpatialReference()
spatial.ImportFromWkt(wkt)
# spatial.ImportFromEPSG(3857)

#duishiliangshuju
targetSR = osr.SpatialReference()
targetSR.ImportFromEPSG(4326)
coordTrans = osr.CoordinateTransformation(spatial,targetSR)
feature = layer.GetFeature(0)
geom = feature.GetGeometryRef()
geom.ExportToWkt()
geom.Transform(coordTrans)
geom.ExportToWkt()

#xiedoawenjianzhong
targetSR.MorphToESRI()
file = open('xx_test.prj','w')
file.write(targetSR.ExportToWkt())
file.close()