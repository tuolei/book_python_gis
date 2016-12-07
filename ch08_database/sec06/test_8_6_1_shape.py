# -*- coding: utf-8 -*-

import shutil
import sqlite3 as sqlite

shutil.copy("./gdata/test-2.3.sqlite", './gdata/xx_new_db.sqlite')
conn = sqlite.connect('./gdata/xx_new_db.sqlite')

conn.enable_load_extension(True)
conn.execute('SELECT load_extension("mod_spatialite.so.7")')
cur = conn.cursor()

sql = 'create virtual table uu using virtualshape("./gdata/shape_towns", cp1252, 32632)'
cur.execute(sql)

cur.execute('PRAGMA table_info(uu)')
[print(rec) for rec in cur]

cur.execute('SELECT PK_UID, Name, Peoples, AsText(Geometry) FROM uu LIMIT 5')
[print(rec) for rec in cur]

sql2 = '''SELECT PK_UID, Name, Peoples, AsText(Geometry)
    FROM uu WHERE Peoples > 350000 ORDER BY Name;'''
cur.execute(sql2)
[print(rec) for rec in cur]

cur.execute('DROP TABLE uu')