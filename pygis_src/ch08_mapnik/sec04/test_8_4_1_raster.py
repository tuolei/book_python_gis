# -*- coding: utf-8 -*-

import mapnik

datasource = mapnik.Gdal(file='gdata/lu75c.tif')
layer = mapnik.Layer("myLayer")
layer.datasource = datasource
layer.styles.append("myLayerStyle")
symbol = mapnik.RasterSymbolizer()

s = mapnik.Style()
r = mapnik.Rule()
r.symbols.append(mapnik.RasterSymbolizer())
s.rules.append(r)

m = mapnik.Map(600, 300)
m.background = mapnik.Color('steelblue')

rule = mapnik.Rule()
rule.symbols.append(symbol)
style = mapnik.Style()
style.rules.append(rule)

m.append_style('My Style', s)

# lyr = mapnik.Layer('world',"+proj=latlong +datum=WGS84")
# lyr.datasource = mapnik.Shapefile(file='gdata/world_borders.shp')
layer.styles.append('My Style')

m.layers.append(layer)

m.zoom_to_box(layer.envelope())
mapnik.render_to_file(m, 'xx_world_ras.png', 'png')
