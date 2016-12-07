#!/usr/bin/env python

import os
import sys
print(sys.path[0])

curpath = os.path.split(os.path.realpath(__file__))[0]

import mapnik

stylesheet =  os.path.join(curpath, 'world_population.xml')
image = os.path.join(curpath, 'xworld_style.png')
m = mapnik.Map(600, 300)
mapnik.load_map(m, stylesheet)
m.zoom_all()
mapnik.render_to_file(m, image)
print("rendered image to '{0}'.".format(image))
