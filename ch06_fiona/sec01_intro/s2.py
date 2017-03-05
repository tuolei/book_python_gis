
import fiona
with fiona.drivers():
    for layername in fiona.listlayers('gdata'):
        with fiona.open('gdata', layer=layername) as src:
            print(layername, len(src))