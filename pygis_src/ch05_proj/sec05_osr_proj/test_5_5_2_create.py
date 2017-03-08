# -*- coding: utf-8 -*-

from osgeo import gdal
import osr

# create from file
dataset = gdal.Open("gdata/lu75c.tif")
# 从数据集中获取空间参考并且建立一个SpatialReference对象
sr = dataset.GetProjectionRef()
osrobj = osr.SpatialReference()
print(osrobj.ImportFromWkt(sr))
print(osrobj.ExportToWkt())
print(osrobj.IsGeographic())
print(osrobj.IsProjected())

# another from file, and compare.
dataset2 = gdal.Open("gdata/foo.tif")
sr2 = dataset2.GetProjectionRef()
osrobj2 = osr.SpatialReference()
osrobj2.ImportFromWkt(sr2)
print(osrobj2.IsSame(osrobj))

# compare.
osrobj3 = osr.SpatialReference()
osrobj3.SetWellKnownGeogCS("WGS84")
print(osrobj3.IsSame(osrobj2))
print(osrobj3.IsSame(osrobj))
print(osrobj3.ExportToWkt())
print(osrobj3.IsGeographic())

ct = osr.CoordinateTransformation(osrobj, osrobj3)
print(ct.TransformPoint(590000, 4928000))
print(ct.TransformPoint(609000, 4928000))
print(ct.TransformPoint(609000, 4914000))
print(ct.TransformPoint(590000, 4914000))
