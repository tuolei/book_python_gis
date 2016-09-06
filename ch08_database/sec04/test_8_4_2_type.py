# -*- coding: utf-8 -*-
import os
import sqlite3 as sqlite

import config

os.chdir(config.gisws)

conn = sqlite.connect("test-2.3.sqlite")
conn.enable_load_extension(True)
conn.execute('SELECT load_extension("libspatialite.so.5")')
cur = conn.cursor()

sql  = "SELECT PK_UID, AsText(Geometry) FROM HighWays WHERE PK_UID = 2"
res = cur.execute(sql)
for rec in res:
    print(rec)

sql = '''SELECT PK_UID, NumPoints(Geometry), GLength(Geometry) ,Dimension(Geometry),
  GeometryType(Geometry) FROM HighWays ORDER BY NumPoints(Geometry) DESC LIMIT 5'''
res = cur.execute(sql)
[print(x) for x in res]

sql = '''SELECT PK_UID, NumPoints(Geometry),
        AsText(StartPoint(Geometry)), Y(PointN(Geometry, 2))
        FROM HighWays ORDER BY NumPoints(Geometry) DESC LIMIT 5'''
res = cur.execute(sql)
[print(x) for x in res]

sql = 'SELECT name, AsText(Geometry) FROM Regions WHERE PK_UID = 52'
res = cur.execute(sql)
[print(x) for x in res]

sql = '''SELECT PK_UID, Area(Geometry), AsText(Centroid(Geometry)),
             Dimension(Geometry), GeometryType(Geometry) FROM Regions
             ORDER BY Area(Geometry) DESC LIMIT 5'''
res = cur.execute(sql)
[print(x) for x in res]

sql = '''SELECT PK_UID, NumInteriorRings(Geometry),
        NumPoints(ExteriorRing(Geometry)),
        NumPoints(InteriorRingN(Geometry, 1))
        FROM regions ORDER BY NumInteriorRings(Geometry) DESC LIMIT 5'''
res = cur.execute(sql)
[print(x) for x in res]

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[row[2] for row in M]
[print(x) for x in M]

