# -*- coding: utf-8 -*-
import os
import config

os.chdir(config.gisws)


from shapely.geometry import Point, LineString, LinearRing, Polygon,  MultiLineString, MultiPoint
from shapely.geometry import MultiPolygon

from shapely.ops import cascaded_union
polygons = [Point(i,0).buffer(0.7) for i in range(5)]
cascaded_union(polygons)

m = MultiPolygon(polygons)
m.area
cascaded_union(m).area

#jilainhe
import os
from osgeo import ogr
import shapely
import shapely.geometry

from shapely.ops import cascaded_union

driver = ogr.GetDriverByName('ESRI Shapefile')
out_shp= 'x_world_borders.shp'
if os.path.exists(out_shp):
    driver.DeleteDataSource(out_shp)

newds = driver.CreateDataSource(out_shp)
layernew = newds.CreateLayer('rect',None,ogr.wkbPolygon)

ds = ogr.Open('world_borders.shp')

layer = ds.GetLayer(0)
feat = layer.GetNextFeature()
while feat:
    geom = feat.GetGeometryRef()
    pts = geom.GetGeometryCount()

    new_feat = ogr.Feature(layernew.GetLayerDefn())

    out_poly = []

    for ii in range(pts):
        poly = geom.GetGeometryRef(ii)
        points_num = poly.GetPointCount()
        print(points_num)
        zc_points = poly.GetPoints()
        print(type(zc_points))
        tmp_pt_arr = []
        for x in zc_points:
            tmp_pt_arr.append(x)

        pt = shapely.geometry.LineString(tmp_pt_arr)
        vv = pt.buffer(3000,0)
        out_poly.append(vv)

    tmp_wkt = cascaded_union(out_poly).to_wkb()
    new_geom = ogr.CreateGeometryFromWkb(tmp_wkt)
    new_feat.SetGeometry(new_geom)
    layernew.CreateFeature(new_feat)
    feat = layer.GetNextFeature()

newds.Destroy()


def Test():
    assert True