rm -f x_new_db.sqlite
spatialite x_new_db.sqlite
.nullvalue NULL
.headers on
.mode list
.tables


.loadshp xx_atowns  new_town utf-8

.tables

PRAGMA table_info(new_town);

SELECT count(*), GeometryType(Geometry) FROM new_town GROUP BY GeometryType(Geometry);

.loadshp xx_atowns new_town2 utf-8 32632 geom

SELECT * FROM geometry_columns;
SELECT * FROM spatial_ref_sys WHERE Srid = 32632;

SELECT * FROM geom_cols_ref_sys;
SELECT * FROM sqlite_master WHERE name = 'geom_cols_ref_sys';

SELECT * FROM sqlite_master WHERE type = 'trigger' AND tbl_name = 'new_town';