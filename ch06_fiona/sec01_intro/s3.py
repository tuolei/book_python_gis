import fiona
with fiona.drivers():
    for i, layername in enumerate(fiona.listlayers('gdata')):
        with fiona.open('gdata', layer=i) as src:
            print(i, layername, len(src))