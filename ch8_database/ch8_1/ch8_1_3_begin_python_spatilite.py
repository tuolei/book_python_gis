from pysqlite2 import dbapi2 as sqlite
db = sqlite.connect("myDatabase.db")
db.enable_load_extension(True)
db.execute('SELECT load_extension("libspatialite.so.5")')

cursor = db.cursor()
cursor.execute('SELECT InitSpatialMetaData();')


cursor.execute("DROP TABLE IF EXISTS cities")
cursor.execute("CREATE TABLE cities (" +
    "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
    "name CHAR(255))")

cursor.execute("SELECT AddGeometryColumn('cities', 'geom', 4326, 'POLYGON', 2)")    
cursor.execute("SELECT CreateSpatialIndex('cities', 'geom')")

cursor.execute("INSERT INTO cities (name, geom)" + \
       " VALUES ({0}, GeomFromText({1}, 4326))".format('"city"', '"wkt"'))

cursor.execute("select name,AsText(geom) FROM cities")
for name,wkt in cursor:
    print(name,wkt)