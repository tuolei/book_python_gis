# -*- coding: utf-8 -*-

import shutil
import sqlite3 as sqlite

shutil.copy("gdata/test-2.3.sqlite", 'gdata/xx_new_db.sqlite')
conn = sqlite.connect('gdata/xx_new_db.sqlite')

conn.enable_load_extension(True)
conn.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = conn.cursor()

sql = '''SELECT Regions.Name, COUNT(*) FROM Towns, Regions
 WHERE Regions.Name IN (
 'VALLED','AOSTA', 'PIEMONTE', 'UMBRIA', 'LOMBARDIA',
 'CALABRIA', 'MOLISE', 'MARCHE', 'BASILICATA') AND
 Within(Towns.geometry, Regions.Geometry)
 GROUP BY Regions.Name;'''
cursor.execute(sql)
[print(rec) for rec in cursor]

sql = '''SELECT t2.Name, t2.Peoples,
Distance(t1.geometry, t2.geometry) AS Distance
FROM Towns AS t1, Towns AS t2
WHERE t1.Name = 'Firenze' AND
Distance(t1.geometry, t2.geometry) < 10000'''
cursor.execute(sql)
[print(rec) for rec in cursor]
