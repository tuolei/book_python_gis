import sqlite3 as sqlite
db = sqlite.connect(":memory:")
db.enable_load_extension(True)
db.execute('SELECT load_extension("libspatialite.so.5")')
cursor = db.cursor()
cursor.execute('SELECT InitSpatialMetaData();')

import shapely.wkt
LONDON = 'POINT(-0.1263 51.4980)'
pt = shapely.wkt.loads(LONDON)
cursor.execute("SELECT id,level,AsText(geom) " +
     "FROM gshhs WHERE id IN " +
     "(SELECT pkid FROM idx_gshhs_geom" +
     " WHERE xmin <= ? AND ? <= xmax" +
     " AND ymin <= ? and ? <= ymax) " +
     "AND Contains(geom, GeomFromText(?, 4326))",
     (pt.x, pt.x, pt.y, pt.y, LONDON))

shoreline = None
for id,level,wkt in cursor:
    if level == 1:
        shoreline = wkt

shoreline