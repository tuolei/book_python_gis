
import fiona
with fiona.drivers():
    with open('gdata/world_borders.shp') as src:
        print(dir(src))

        meta = src.meta
        f = next(src)
    with fiona.open('/tmp/foo', 'w', layer='bar', **meta) as dst:
        dst.write(f)
    print(fiona.listlayers('/tmp/foo'))
    with fiona.open('/tmp/foo', layer='bar') as src:
        print(len(src))
        f = next(src)
        print(f['geometry']['type'])
        print(f['properties'])
