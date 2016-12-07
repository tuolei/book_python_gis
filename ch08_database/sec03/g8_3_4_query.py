# -*- coding: utf-8 -*-
import os
import sqlite3 as sqlite


db = sqlite.connect("gdata/xx_myDatabase2.sqlite")
db.enable_load_extension(True)
db.execute('SELECT load_extension("libspatialite.so.5")')
cursor = db.cursor()

import shapely.wkt

LONDON = 'POINT(-0.1263 51.4980)'
pt = shapely.wkt.loads(LONDON)
sql_cmd = '''SELECT id,level,AsText(geom) FROM gshhs WHERE id IN (SELECT pkid FROM idx_gshhs_geom WHERE xmin <= {0}
    AND {0} <= xmax AND ymin <= {1} and {1} <= ymax) AND Contains(geom, GeomFromText('{2}', 4326))'''.format(
    pt.x, pt.y, LONDON)
# cursor.execute(
#     "SELECT id,level,AsText(geom) " + "FROM gshhs WHERE id IN " + "(SELECT pkid FROM idx_gshhs_geom" + " WHERE xmin <= ? AND ? <= xmax" + " AND ymin <= ? and ? <= ymax) " + "AND Contains(geom, GeomFromText(?, 4326))",
#     (pt.x, pt.x, pt.y, pt.y, "'" + LONDON + "'"))

cursor.execute(sql_cmd)


print('+' * 40)
print(sql_cmd)
print('+' * 40)
shoreline = None
for id, level, wkt in cursor:
    # Todo: 原始数据是1
    if level == 2:
        shoreline = wkt

with open("xx_uk-shoreline.wkt", "w") as fo:
    fo.write(shoreline)


def Test():
    assert db
    assert cursor


def tearDown():
    if cursor:
        cursor.close()
    if db:
        db.close()
