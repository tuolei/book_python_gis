# -*- coding: utf-8 -*-

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# map = Basemap(llcrnrlon=-0.5,llcrnrlat=39.8,urcrnrlon=4.,urcrnrlat=43.,
#              resolution='i', projection='tmerc', lat_0 = 39.5, lon_0 = 1)

map = Basemap(projection='robin', lat_0=0, lon_0=-100,
                 resolution='l', area_thresh=1000.0)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='#ddaa66',lake_color='aqua')
map.drawcoastlines()

map.readshapefile('gdata/world_borders', 'comarques')

# plt.show()

import os
plt.savefig(os.path.join(os.path.split(os.path.realpath(__file__))[0], 'xx_' + os.path.split(os.path.realpath(__file__))[1][5:-2] + 'png'))
plt.clf()
plt.close()