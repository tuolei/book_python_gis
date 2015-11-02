spatialite my_new_db.sqlite
.nullvalue NULL
.headers on
.mode list
.tables


.loadshp 全国县级统计数据  New cp936

.tables

PRAGMA table_info(NEW);

SELECT count(*), GeometryType(Geometry) FROM New GROUP BY GeometryType(Geometry);

.loadshp shape_towns NewTowns CP1252 32632 geom

SELECT * FROM geometry_columns;
SELECT * FROM spatial_ref_sys WHERE Srid = 32632;

SELECT * FROM geom_cols_ref_sys;
SELECT * FROM sqlite_master WHERE name = 'geom_cols_ref_sys';

 SELECT * FROM sqlite_master WHERE type = 'trigger' AND tbl_name = 'NewTowns';