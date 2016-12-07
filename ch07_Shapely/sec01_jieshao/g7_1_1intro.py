# -*- coding: utf-8 -*-
import os

from osgeo import ogr

wkt = "POINT (1 1)"
geom = ogr.CreateGeometryFromWkt(wkt)
buf = geom.Buffer(1)
buf.ExportToWkt()


def Test():
    assert buf


def Test2():
    assert geom


def Test3():
    assert geom.ExportToWkt() == wkt
