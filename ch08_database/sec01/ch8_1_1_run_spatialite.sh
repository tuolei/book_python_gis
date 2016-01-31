

spatialite test-2.3.sqlite

sqlite3 test-2.3.sqlite 

.nullvalue NULL
.headers on
.mode list

.help

.load 'libspatialite.so.5'

SELECT load_extension('libspatialite.so.5');