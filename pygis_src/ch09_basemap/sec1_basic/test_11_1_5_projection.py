# -*- coding: utf-8 -*-

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

map = Basemap(projection='aeqd', lon_0=10, lat_0=50)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral', lake_color='aqua')
map.drawcoastlines()

# plt.show()

plt.savefig('xx_basemap_proj_1.png')
plt.clf()

map = Basemap(projection='cyl')

# map.drawmapboundary(fill_color='aqua')
# map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))

plt.savefig('xx_basemap_proj_2.png')
plt.clf()

map = Basemap(projection='mbtfpq', lon_0=105)

# map.drawmapboundary(fill_color='aqua')
# map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))
plt.savefig('xx_basemap_proj_3.png')
plt.clf()

map = Basemap(projection='aeqd', lon_0=105, lat_0=39)

# map.drawmapboundary(fill_color='aqua')
# map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))

plt.savefig('xx_basemap_proj_4.png')
plt.clf()

map = Basemap(projection='sinu', lon_0=105, lat_0=39)

# map.drawmapboundary(fill_color='aqua')
# map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))
plt.savefig('xx_basemap_proj_5.png')
plt.clf()
plt.close()