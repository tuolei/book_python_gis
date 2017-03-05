import fiona

with fiona.drivers():
    for i, layername in enumerate(
            fiona.listlayers('/', vfs='zip://gdata/world_borders.zip')):
        with fiona.open('/', vfs='zip://gdata/world_borders.zip', layer=i) as src:
            print(i, layername, len(src))
