# -*- coding: utf-8 -*-
import os
import config

os.chdir(config.gisws)

import os
from osgeo import ogr
def create_shp_by_layer(shp,layer):
    outputfile = shp
    if os.access(outputfile,os.F_OK):
        driver.DeleteDataSource(outputfile)
    newds = driver.CreateDataSource(outputfile)
    pt_layer = newds.CopyLayer(layer,'')
    newds.Destroy()

driver = ogr.GetDriverByName("ESRI Shapefile")
world_shp ='world_borders.shp'
cover_shp= 'world_borders.shp'
world_ds = ogr.Open(world_shp)
cover_ds = ogr.Open(cover_shp)
world_layer =world_ds.GetLayer(0)
cover_layer = cover_ds.GetLayer(0)
print(world_layer.GetFeatureCount())
cover_feats = cover_layer.GetNextFeature()

world_layer.SetSpatialFilterRect(50,60,25,35)
print(world_layer.GetFeatureCount())

out_shp = 'sel_res.shp'
create_shp_by_layer(out_shp,world_layer)

def Test():
    assert True