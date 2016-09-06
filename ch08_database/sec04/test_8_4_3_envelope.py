# -*- coding: utf-8 -*-
import os
import sqlite3 as sqlite

import config

os.chdir(config.gisws)

conn = sqlite.connect("test-2.3.sqlite")
conn.enable_load_extension(True)
conn.execute('SELECT load_extension("libspatialite.so.5")')
cur = conn.cursor()

sql = '''SELECT Name, AsText(Envelope(Geometry)) FROM Regions LIMIT 5'''
res = cur.execute(sql)
[print(x) for x in res]
