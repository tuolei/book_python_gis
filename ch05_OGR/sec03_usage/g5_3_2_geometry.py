# -*- coding: utf-8 -*-


import os


# 创建点要素
from osgeo import ogr
point = ogr.Geometry(ogr.wkbPoint)
point.AddPoint(10,20)
print(type(point))
print(point)

# 创建线要素
line = ogr.Geometry(ogr.wkbLineString)
line.AddPoint(10,20)
line.AddPoint(20,30)
line.AddPoint(10,30)
print(line)

line.SetPoint(1,50,50)
print(line)

print(line.GetPointCount())

print(line.GetX(0))
print(line.GetY(0))

ring = ogr.Geometry(ogr.wkbLinearRing)
ring.AddPoint(0,0)
ring.AddPoint(100,0)
ring.AddPoint(100,100)
ring.AddPoint(0,100)

ring.CloseRings()
print(ring)

# 创建多边形要素
outring = ogr.Geometry(ogr.wkbLinearRing)
outring.AddPoint(0,0)
outring.AddPoint(100,0)
outring.AddPoint(100,100)
outring.AddPoint(0,100)

inring = ogr.Geometry(ogr.wkbLinearRing)
inring.AddPoint(25,25)
inring.AddPoint(75,25)
inring.AddPoint(75,75)
inring.AddPoint(25,75)

polygon = ogr.Geometry(ogr.wkbPolygon)
polygon.AddGeometry(outring)
polygon.AddGeometry(inring)

print(polygon.GetGeometryRef)

outring = polygon.GetGeometryRef(0)
inring = polygon.GetGeometryRef(0)
print(outring)
print(inring)

#fuhejihexingzhuang
multipoint = ogr.Geometry(ogr.wkbMultiPoint)
point = ogr.Geometry(ogr.wkbPoint)
point.AddPoint(10,10)
multipoint.AddGeometry(point)
point.AddPoint(20,20)
multipoint.AddGeometry(point)