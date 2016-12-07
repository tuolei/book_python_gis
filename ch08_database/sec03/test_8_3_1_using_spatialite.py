# -*- coding: utf-8 -*-
import sqlite3 as sqlite

db = sqlite.connect(':memory:')
db.enable_load_extension(True)
# db.execute('SELECT load_extension("libspatialite.so.5")')

# Only need to install
# libspatialite7
# libsqlite3-mod-spatialite
db.execute('SELECT load_extension("mod_spatialite.so.7")')

cursor = db.cursor()
cursor.execute('BEGIN')
cursor.execute('SELECT InitSpatialMetaData();')

cursor.execute("DROP TABLE IF EXISTS cities")
cursor.execute("CREATE TABLE cities (" +
               "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
               "name CHAR(255))")

# cursor.execute("CREATE INDEX gshhs_level on gshhs(level)")
cursor.execute("SELECT AddGeometryColumn('cities', 'geom', 4326, 'POLYGON', 2)")
cursor.execute("SELECT CreateSpatialIndex('cities', 'geom')")

cursor.execute("INSERT INTO cities (name, geom)" + \
               " VALUES ({0}, GeomFromText({1}, 4326))".format('"city"',
                                                               '"POLYGON((1 1,5 1,5 5,1 5,1 1),(2 2, 3 2, 3 3, 2 3,2 2))"'))

cursor.execute("SELECT name,AsText(geom) FROM cities")
for name, wkt in cursor:
    print(name, wkt)


def Test():
    assert cursor
    assert db


def TearDown():
    if cursor:
        cursor.close()
    if db:
        db.close()
