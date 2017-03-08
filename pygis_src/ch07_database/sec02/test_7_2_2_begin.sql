ogr2ogr  -f SQLite -dsco SPATIALITE=YES x_china.db stats_county.shp -nlt multipolygon

spatialite x_china.db
.head on

SQL中

select * from STATS_COUNTY limit 5;

select name, popu from stats_county WHERE popu > 500 order by popu DESC;



select COUNT(*) as '# 城镇',
MIN(popu) as '最少',
MAX(popu) as '最多',
SUM(popu) as '人口总数',
SUM(popu) / COUNT(*) as '城镇平均人口'
from stats_county;

select (10 - 11) * 2 as Number, ABS((10 - 11) * 2) as AbsoluteValue;

select name, popu, HEX(GEOMETRY) from stats_county WHERE popu > 500 order by popu DESC;
.quit
