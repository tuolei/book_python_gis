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



recs = cur.execute("select name from sqlite_master where type='table' order by name;")

for rec in recs:
    print(rec)

print('=' * 20)
print('PRAGMA')
cursor = cur
recs = cursor.execute("PRAGMA table_info( Towns)")
for rec in recs:
    print(rec)

# 创建新表

# cursor.execute("DROP TABLE IF EXISTS NewTows")
# cursor.execute("CREATE TABLE cities (" +
#     "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
#     "name CHAR(255))")
#
# # cursor.execute("CREATE INDEX gshhs_level on gshhs(level)")
# cursor.execute("SELECT AddGeometryColumn('cities', 'geom', 4326, 'POLYGON', 2)")
# cursor.execute("SELECT CreateSpatialIndex('cities', 'geom')")


# "insert into tagTable select * from sourceTable;"


print('=' * 20)
print('spatial_ref_sys')
recs = cur.execute('SELECT * FROM spatial_ref_sys LIMIT 5;')

for rec in recs:
    print(rec)




recs = cur.execute('SELECT DISTINCT Srid(geometry) FROM Towns;')

for rec in recs:
    print(rec)
