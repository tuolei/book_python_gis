import fiona

c = fiona.open('gdata/world_borders.shp', 'r')
c
c.closed
next(c)
len(list(c))

next(c)
len(list(c))

c = fiona.open('gdata/world_borders.shp')
len(list(c))

import pprint

with fiona.open('gdata/world_borders.shp') as src:
    pprint.pprint(src[1])

with fiona.open('gdata/world_borders.shp') as src:
    pprint.pprint(src[0])

import pprint
with fiona.open('gdata/world_borders.shp') as src:
    pprint.pprint(src[1])

try:
    with fiona.open('gdata/world_borders.shp') as c:
        print(len(list(c)))
        assert True is False
except:
    print(c.closed)
    raise