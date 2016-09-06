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


print('=' * 60)

cur.execute('CREATE TABLE MyTable (name TEXT NOT NULL, geom BLOB NOT NULL)')
cur.execute("INSERT INTO MyTable (name, geom) VALUES ('one', GeomFromText('POINT(1 1)'))")
cur.execute("INSERT INTO MyTable (name, geom) VALUES ('two', GeomFromText('POINT(2 2)'))")
cur.execute("INSERT INTO MyTable (name, geom) VALUES ('three', GeomFromText('POINT(3 3)'))")
recs = cur.execute("SELECT name, AsText(geom) FROM MyTable;")
for rec in recs:
    print(rec)

cur.close()
conn.close()


conn = sqlite.connect('xx_new_db.sqlite')
conn.enable_load_extension(True)
conn.execute('SELECT load_extension("libspatialite.so.5")')

cur = conn.cursor()
recs = cur.execute("SELECT name, AsText(geom) FROM MyTable;")
for rec in recs:
    print(rec)


# res.next()