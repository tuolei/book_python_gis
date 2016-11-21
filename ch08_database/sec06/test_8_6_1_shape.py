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


sql  = 'create virtual table uu using virtualshape(shape_towns, cp1252, 32632)'
res = cur.execute(sql)
sql2 = 'select * from uu'
res2 = cur.execute(sql2)
for rec in res2:
    # print(rec)
    pass

sql2  = '''SELECT PK_UID, Name, Peoples, AsText(Geometry)
    FROM uu WHERE Peoples > 350000 ORDER BY Name;'''
res3 = cur.execute(sql2)

for rec in res3:
    print(rec)

