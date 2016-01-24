spatialite test-2.3.sqlite

.nullvalue NULL
.headers on
.mode list

SELECT * FROM towns LIMIT 5;

select name AS Town, peoples as Population from towns ORDER BY name LIMIT 5;

select name, peoples from towns WHERE peoples > 350000 order by peoples DESC;

select COUNT(*) as '# Towns',
MIN(peoples) as Smaller,
MAX(peoples) as Bigger,
SUM(peoples) as 'Total peoples',
SUM(peoples) / COUNT(*) as 'mean peoples for town'
from towns;

select (10 - 11) * 2 as Number, ABS((10 - 11) * 2) as AbsoluteValue;

select name, peoples, HEX(Geometry)
from Towns where peoples > 350000 order by peoples DESC;

.quit