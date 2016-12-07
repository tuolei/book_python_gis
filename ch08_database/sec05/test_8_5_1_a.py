# -*- coding: utf-8 -*-

import shutil
import sqlite3 as sqlite

shutil.copy("./gdata/test-2.3.sqlite", './gdata/xx_new_db.sqlite')
conn = sqlite.connect('./gdata/xx_new_db.sqlite')

conn.enable_load_extension(True)
conn.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = conn.cursor()

recs = cursor.execute("SELECT count (*) FROM Towns;")
[print(rec) for rec in cursor]

sql = '''SELECT count(*) FROM Towns WHERE MBRContains(
    GeomFromText('POLYGON((554000 4692000, 770000 4692000, 770000 4925000,
    554000 4925000, 554000 4692000))'), geometry)'''
cursor.execute(sql)
[print(rec) for rec in cursor]

sql = '''SELECT count(*) FROM Towns WHERE MBRContains( BuildMBR(554000, 4692000, 770000, 4925000), geometry);'''
cursor.execute(sql)
[print(rec) for rec in cursor]

sql = '''SELECT count (*) FROM Towns WHERE MBRContains(BuildMBR (654000,4692000, 770000, 4924000), geometry);'''
cursor.execute(sql)
[print(rec) for rec in cursor]


sql = '''SELECT count (*) FROM Towns WHERE MBRWithin( geometry , BuildMBR (754000, 4692000, 770000, 4924000))'''
cursor.execute(sql)
[print(rec) for rec in cursor]


sql = '''SELECT count (*) FROM HighWays WHERE MBRIntersects(BuildMBR(754000, 4692000, 770000, 4924000), geometry)'''
cursor.execute(sql)
[print(rec) for rec in cursor]

