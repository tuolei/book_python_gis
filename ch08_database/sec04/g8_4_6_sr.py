# -*- coding: utf-8 -*-

import sqlite3 as sqlite

db = sqlite.connect(':memory:')
db.enable_load_extension(True)
db.execute('SELECT load_extension("mod_spatialite.so.7")')

cursor = db.cursor()
cursor.execute('BEGIN')
cursor.execute('SELECT InitSpatialMetaData();')
cursor = cursor.execute('SELECT * FROM spatial_ref_sys LIMIT 5;')
[print(rec) for rec in cursor]
cursor.close()
db.close()

################
import shutil
shutil.copy("./gdata/test-2.3.sqlite", './gdata/xx_new_db.sqlite')
conn = sqlite.connect('./gdata/xx_new_db.sqlite')

conn.enable_load_extension(True)
conn.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = conn.cursor()

cursor.execute("select name from sqlite_master where type='table' order by name;")
[print(rec) for rec in cursor]


cursor.execute("PRAGMA table_info( Towns)")
[print(rec) for rec in cursor]

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


# spatial_ref_sys
cursor = cursor.execute('SELECT * FROM spatial_ref_sys LIMIT 5;')
[print(rec) for rec in cursor]



# 空间参考信息
cursor = cursor.execute('SELECT DISTINCT Srid(geometry) FROM Towns;')
[print(rec) for rec in cursor]

cursor = cursor.execute('''SELECT DISTINCT SRID(Towns.geometry), spatial_ref_sys.ref_sys_name FROM Towns,
        spatial_ref_sys WHERE SRID(Towns.geometry) = spatial_ref_sys.srid;''')
[print(rec) for rec in cursor]

# 创建

cursor.execute('BEGIN')
cursor.execute("SELECT AddGeometryColumn('Towns', 'wgs84', 4326, 'POINT', 2)")
cursor.execute("UPDATE Towns SET wgs84 = Transform(geometry, 4326);")
conn.commit()
cursor.execute('SELECT AsText(geometry), Srid(geometry),AsText(wgs84), Srid(wgs84) FROM Towns LIMIT 5;')
[print(rec) for rec in cursor]