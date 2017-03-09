# -*- coding: utf-8 -*-
import os

import mapnik

# mapnik.Color('y')
m = mapnik.Map(6000, 3000, "+proj=latlong +datum=WGS84")
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
# polygon_symbolizer = mapnik.PolygonSymbolizer(mapnik.Color('#f2eff9'))
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')

# polygon_symbolizer = mapnik.PolygonSymbolizer(mapnik.Color('blue'))
r.symbols.append(polygon_symbolizer)
# line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('rgb(50%,50%,50%)'),0.1)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('rgb(50%,50%,50%)')
line_symbolizer.stroke_width = 0.1

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style', s)
lyr = mapnik.Layer('world', "+proj=latlong +datum=WGS84")
lyr.datasource = mapnik.Shapefile(file='gdata/world_borders.shp')
lyr.styles.append('My Style')
m.layers.append(lyr)
m.zoom_to_box(lyr.envelope())
mapnik.render_to_file(m, 'xx_world_fk.png', 'png')

