# -*- coding: utf-8 -*-


import mapnik
m = mapnik.Map(600, 400)
m.srs
style1, style2, style3 = [mapnik.Style()] * 3
m.append_style("s1", style1)
m.append_style("s2", style2)
m.append_style("s3", style1)
m.append_style("s1", style3)

layer = mapnik.Layer('lyrname')
layer.srs
ds = mapnik.Shapefile(file='./gdata/world_borders.shp')
layer.datasource = ds
layer.styles.append("s1")
layer.styles.append("s2")
m.layers.append(layer)

m.zoom_to_box(layer.envelope())
mapnik.render_to_file(m,'xworld2.png', 'png')
