#!/usr/bin/env python

import os
import mapnik

curpath = os.path.split(os.path.realpath(__file__))[0]

stylesheet = os.path.join(curpath, 'world_population.xml')
image = 'x_world_style.png'
m = mapnik.Map(600, 300)
mapnik.load_map(m, stylesheet)
m.zoom_all()
mapnik.render_to_file(m, image)
print("rendered image to '{0}'.".format(image))
