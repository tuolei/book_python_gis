# -*- coding: utf-8 -*-
import os
import shutil
import sqlite3 as sqlite

import config

os.chdir(config.gisws)
shutil.copy("test-2.3.sqlite", 'xx_new_db.sqlite')

conn = sqlite.connect('xx_new_db.sqlite')

conn.enable_load_extension(True)
conn.execute('SELECT load_extension("libspatialite.so.5")')
cur = conn.cursor()

recs = cur.execute("SELECT count (*) FROM Towns;")

for rec in recs:
    print(rec)

sql = '''SELECT count(*) FROM Towns WHERE MBRContains(
GeomFromText('POLYGON((554000 4692000, 770000 4692000, 770000 4925000,
554000 4925000, 554000 4692000))'), geometry)'''
res = cur.execute(sql)

for rec in recs:
    print(rec)

sql = '''SELECT count(*) FROM Towns WHERE MBRContains( BuildMBR(554000, 4692000, 770000, 4925000), geometry);'''
res = cur.execute(sql)

for rec in recs:
    print(rec)

sql = '''SELECT count (*) FROM Towns WHERE MBRContains(BuildMBR (654000,4692000, 770000, 4924000), geometry);'''
res = cur.execute(sql)

for rec in recs:
    print(rec)



sql = '''SELECT count (*) FROM Towns WHERE MBRWithin( geometry , BuildMBR (754000, 4692000, 770000, 4924000));'''
res = cur.execute(sql)

for rec in recs:
    print(rec)

sql = '''SELECT count (*) FROM HighWays WHERE MBRIntersects( BuildMBR (754000, 4692000, 770000, 4924000), geometry);'''
res = cur.execute(sql)

for rec in recs:
    print(rec)