# -*- coding: utf-8 -*-
import os

import sqlite3 as sqlite
conn = sqlite.connect("gdata/test-2.3.sqlite")
conn.enable_load_extension(True)
conn.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = conn.cursor()

sql = "SELECT PK_UID, AsText(Geometry) FROM HighWays WHERE PK_UID = 2"
cursor.execute(sql)
[print(rec) for rec in cursor]

sql = '''SELECT PK_UID, NumPoints(Geometry), GLength(Geometry) ,Dimension(Geometry),
  GeometryType(Geometry) FROM HighWays ORDER BY NumPoints(Geometry) DESC LIMIT 5'''
cursor.execute(sql)
[print(x) for x in cursor]

# 更多函数
sql = '''SELECT PK_UID, NumPoints(Geometry),
        AsText(StartPoint(Geometry)), Y(PointN(Geometry, 2))
        FROM HighWays ORDER BY NumPoints(Geometry) DESC LIMIT 5'''
cursor.execute(sql)
[print(x) for x in cursor]

# 多边形类型
sql = 'SELECT name, AsText(Geometry) FROM Regions WHERE PK_UID = 52'
cursor.execute(sql)
[print(x) for x in cursor]

#
sql = '''SELECT PK_UID, Area(Geometry), AsText(Centroid(Geometry)),
             Dimension(Geometry), GeometryType(Geometry) FROM Regions
             ORDER BY Area(Geometry) DESC LIMIT 5'''
cursor.execute(sql)
[print(x) for x in cursor]

#
sql = '''SELECT PK_UID, NumInteriorRings(Geometry),
        NumPoints(ExteriorRing(Geometry)),
        NumPoints(InteriorRingN(Geometry, 1))
        FROM regions ORDER BY NumInteriorRings(Geometry) DESC LIMIT 5'''
cursor.execute(sql)
[print(x) for x in cursor]

# 查看多边形坐标

sql = '''SELECT AsText(InteriorRingN(Geometry, 1)),
    AsText(PointN(InteriorRingN(Geometry, 1), 4)),
    X(PointN(InteriorRingN(Geometry, 1), 5))
    FROM Regions WHERE PK_UID = 55'''
cursor.execute(sql)
[print(x) for x in cursor]


