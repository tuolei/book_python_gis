# -*- coding: utf-8 -*-
import os
import sqlite3 as sqlite

sqlitefile = 'xx_mbra.sqlite'
if os.path.exists(sqlitefile):
    os.remove(sqlitefile)
db = sqlite.connect(sqlitefile)
db.enable_load_extension(True)
db.execute('SELECT load_extension("mod_spatialite.so.7")')

cursor = db.cursor()
cursor.execute('BEGIN')
cursor.execute('SELECT InitSpatialMetaData();')


def create_table(cursor, tab_name):
    cursor.execute("DROP TABLE IF EXISTS {0}".format(tab_name))
    cursor.execute("CREATE TABLE {0} (id INTEGER PRIMARY KEY AUTOINCREMENT, x INTEGER, y INTEGER )".format(tab_name))
    cursor.execute("SELECT AddGeometryColumn('{0}', 'geom', 4326, 'POINT', 2)".format(tab_name))
    cursor.execute("SELECT CreateSpatialIndex('{0}', 'geom')".format(tab_name))


create_table(cursor, 'grid_points')
create_table(cursor, 'mbr_points')
create_table(cursor, 'circle_points')

for ii in range(10):
    for jj in range(10):
        cursor.execute("INSERT INTO grid_points (x,y,geom)" + \
                       ' VALUES ({0}, {1}, GeomFromText("POINT({0} {1})", 4326))'.format(ii, jj))

db.commit()

sql = '''SELECT AsText(geom) FROM grid_points WHERE MBRContains(BuildMBR (4,4,7,6), geom);'''
cursor.execute(sql)

bb = []
for x in cursor:
    bb.append(x)

for x in bb:
    sql_in = 'INSERT INTO  mbr_points (geom) VALUES (GeomFromText("{0}", 4326))'.format(x[0])
    cursor.execute(sql_in)

db.commit()

#######################################
sql = '''SELECT AsText(geom) FROM grid_points WHERE MBRContains(BuildCircleMBR (5,5,1), geom);'''
cursor.execute(sql)

bb = []
for x in cursor:
    bb.append(x)

for x in bb:
    sql_in = 'INSERT INTO  circle_points (geom) VALUES (GeomFromText("{0}", 4326))'.format(x[0])
    cursor.execute(sql_in)

db.commit()
#
# sql = '''SELECT count(*) FROM Towns WHERE MBRContains(
# GeomFromText('POLYGON((554000 4692000, 770000 4692000, 770000 4925000,
# 554000 4925000, 554000 4692000))'), geometry)'''
# res = cur.execute(sql)
#
# for rec in recs:
#     print(rec)
#
# sql = '''SELECT count(*) FROM Towns WHERE MBRContains( BuildMBR(554000, 4692000, 770000, 4925000), geometry);'''
# res = cur.execute(sql)
#
# for rec in recs:
#     print(rec)
#
# sql = '''SELECT count (*) FROM Towns WHERE MBRContains(BuildMBR (654000,4692000, 770000, 4924000), geometry);'''
# res = cur.execute(sql)
#
# for rec in recs:
#     print(rec)
#
#
#
# sql = '''SELECT count (*) FROM Towns WHERE MBRWithin( geometry , BuildMBR (754000, 4692000, 770000, 4924000));'''
# res = cur.execute(sql)
#
# for rec in recs:
#     print(rec)
#
# sql = '''SELECT count (*) FROM HighWays WHERE MBRIntersects( BuildMBR (754000, 4692000, 770000, 4924000), geometry);'''
# res = cur.execute(sql)
#
# for rec in recs:
#     print(rec)
