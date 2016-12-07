# -*- coding: utf-8 -*-

import shutil
import sqlite3 as sqlite

shutil.copy("./gdata/test-2.3.sqlite", './gdata/xx_new_db.sqlite')
conn = sqlite.connect('./gdata/xx_new_db.sqlite')
conn.enable_load_extension(True)
conn.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = conn.cursor()

cursor.execute('CREATE TABLE MyTable (name TEXT NOT NULL, geom BLOB NOT NULL)')
cursor.execute("INSERT INTO MyTable (name, geom) VALUES ('one', GeomFromText('POINT(1 1)'))")
cursor.execute("INSERT INTO MyTable (name, geom) VALUES ('two', GeomFromText('POINT(2 2)'))")
cursor.execute("INSERT INTO MyTable (name, geom) VALUES ('three', GeomFromText('POINT(3 3)'))")
cursor.execute("SELECT name, AsText(geom) FROM MyTable;")
[print(rec) for rec in cursor]

cursor.execute("SELECT pk_uid, name, peoples, AsText(geometry) FROM Towns WHERE pk_uid = 8006")
[print(rec) for rec in cursor]

cursor.execute('''UPDATE Towns SET peoples = 150000, name = 'MONZA',
    geometry = GeomFromText('POINT(10 10)', 32632)  WHERE pk_uid = 8006''')
cursor.execute("SELECT pk_uid, name, peoples, AsText(geometry) FROM Towns WHERE pk_uid = 8006")
[print(rec) for rec in cursor]

# 根据选择生成新表
cursor.execute('BEGIN')
cursor.execute('CREATE TABLE Villages AS SELECT * FROM Towns WHERE peoples < 500')
conn.commit()
cursor.execute('SELECT count(*) FROM Villages')
[print(rec) for rec in cursor]

# 根据选择生成新表2

cursor.execute('BEGIN')
cursor.execute('CREATE TABLE Metropolis ( Name TEXT NOT NULL, Population INTEGER NOT NULL, Geometry BLOB NOT NULL);')
cursor.execute('''INSERT INTO Metropolis (Name, Population, Geometry)
        SELECT name, peoples, geometry FROM Towns
        WHERE peoples > 1000000;''')
conn.commit()
cursor.execute('SELECT name, population, AsText(geometry) FROM Metropolis')
[print(rec) for rec in cursor]

# 删除
cursor.execute('DROP TABLE Villages')
cursor.execute('DROP TABLE Metropolis')
cursor.execute('VACUUM')

#

cursor.execute('CREATE TABLE some_table ( N1 SMALLINT, N2 INTEGER NOT NULL, N3 DOUBLE, STR VARCHAR(4) NOT NULL);')
cursor.execute("INSERT INTO some_table VALUES (10, 11, 111.1111, 'first');")
cursor.execute("INSERT INTO some_table VALUES (NULL, 12, NULL, 'second');")
cursor.execute("INSERT INTO some_table VALUES (30, NULL, 222.2222, NULL);")

cursor.execute("INSERT INTO some_table VALUES ('aaaa', 'bbbb', 'cccc', 1234)")
cursor.execute("INSERT INTO some_table VALUES ('A', 'B', 'C', 1234.6789)")

cursor.execute("SELECT * FROM some_table")
[print(rec) for rec in cursor]