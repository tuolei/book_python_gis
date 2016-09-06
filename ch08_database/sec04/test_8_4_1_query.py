# -*- coding: utf-8 -*-
import os
import sqlite3 as sqlite

import config

os.chdir(config.gisws)

conn = sqlite.connect("test-2.3.sqlite")
conn.enable_load_extension(True)
conn.execute('SELECT load_extension("libspatialite.so.5")')
cur = conn.cursor()

sql = 'SELECT name , peoples , AsText(Geometry) from Towns where peoples > 350000 order by peoples DESC'
res = cur.execute(sql)
for x in res:
    print(x)


sql = 'SELECT name , X(Geometry), Y(Geometry) FROM Towns WHERE peoples > 350000 ORDER BY peoples DESC;'
res = cur.execute(sql)
for x in res:
    print(x)

sql = "SELECT HEX(GeomFromText('POINT(10 20) '));"
res = cur.execute(sql)
for rec in res:
    print (rec)

sql = "SELECT HEX(AsBinary(GeomFromText('POINT(10 20) ')));"
res = cur.execute(sql)
for rec in res:
    print (rec)

sql = "SELECT AsText(GeomFromWKB(X'010100000000000000000024400000000000003440'));"
res = cur.execute(sql)
for rec in res:
    print (rec)