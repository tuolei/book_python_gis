# -*- coding: utf-8 -*-

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(projection='cyl')

# map.drawmapboundary(fill_color='aqua')
# map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

# plt.show()

plt.savefig('xx_basemap_6.png')
plt.clf()
plt.close()