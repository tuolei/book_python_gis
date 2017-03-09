# -*- coding: utf-8 -*-
import os


from shapely.geometry import Point

print(Point(0, 0).geom_type)

Point(0, 0).distance(Point(1, 1))

donut = Point(0, 0).buffer(2, 0).difference(Point(0, 0).buffer(1.0))
print(donut.centroid.wkt)
print(donut.representative_point().wkt)

# Copy feature.
import os
from osgeo import ogr
import shapely.geometry

driver = ogr.GetDriverByName('ESRI Shapefile')
out_shp = 'xx_world_borders.shp'
if os.path.exists(out_shp):
    driver.DeleteDataSource(out_shp)

newds = driver.CreateDataSource(out_shp)
layernew = newds.CreateLayer('rect', None, ogr.wkbPolygon)

ds = ogr.Open('gdata/world_borders.shp')

layer = ds.GetLayer(0)
feat = layer.GetNextFeature()
# 逐个 Copy 到新 shapefile 中
while feat:
    fid = feat.GetField('FIPS_CNTRY')
    # print(fid)
    geom = feat.GetGeometryRef()
    # print(geom)
    pt = shapely.geometry.Point(geom.GetX(),geom.GetY())
    vv = pt.buffer(3.0)

    tmp_wkb = vv.to_wkb()
    # tmp_wkb = vv.ExportToWkb()

    new_geom = ogr.CreateGeometryFromWkb(tmp_wkb)
    new_feat = ogr.Feature(layernew.GetLayerDefn())
    new_feat.SetGeometry(new_geom)
    layernew.CreateFeature(new_feat)

    feat = layer.GetNextFeature()

newds.Destroy()
