# -*- coding: utf-8 -*-

import os
from osgeo import ogr


def create_shp_by_layer(shp, layer):
    outputfile = shp
    if os.access(outputfile, os.F_OK):
        driver.DeleteDataSource(outputfile)
    newds = driver.CreateDataSource(outputfile)
    pt_layer = newds.CopyLayer(layer, '')
    newds.Destroy()


driver = ogr.GetDriverByName("ESRI Shapefile")
world_shp = './gdata/world_borders.shp'
world_ds = ogr.Open(world_shp)
world_layer = world_ds.GetLayer()
world_layer_name = world_layer.GetName()
print(world_layer.GetFeatureCount())
result = world_ds.ExecuteSQL("select * from %s" % (world_layer_name))

resultFeat = result.GetNextFeature()
while resultFeat:
    # print(resultFeat.GetField('BNDRY_ID'))
    resultFeat = result.GetNextFeature()

out_shp = 'xx_world_borders.shp'
create_shp_by_layer(out_shp, result)
world_ds.ReleaseResultSet(result)
world_ds.Destroy()


def Test():
    assert True
