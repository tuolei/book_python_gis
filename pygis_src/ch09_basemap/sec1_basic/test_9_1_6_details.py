# -*- coding: utf-8 -*-


import os
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# make sure the value of resolution is a lowercase L,
#  for 'low', not a numeral 1

# make sure the value of resolution is a lowercase L,
#  for 'low', not a numeral 1
my_map = Basemap(projection='merc', lat_0=57, lon_0=-135,
                 resolution='l', area_thresh=1000.0,
                 llcrnrlon=-136.25, llcrnrlat=56,
                 urcrnrlon=-134.25, urcrnrlat=57.75)

my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color='coral')
my_map.drawmapboundary()

my_map.drawmeridians(np.arange(0, 360, 30))
my_map.drawparallels(np.arange(-90, 90, 30))



# plt.show()
plt.savefig(os.path.join(os.path.split(os.path.realpath(__file__))[0], 'xx_' + os.path.split(os.path.realpath(__file__))[1][5:-3] + '1.png'))

plt.clf()

my_map = Basemap(projection='merc', lat_0=57, lon_0=-135,
                 resolution='h', area_thresh=1000.0,
                 llcrnrlon=-136.25, llcrnrlat=56,
                 urcrnrlon=-134.25, urcrnrlat=57.75)

my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color='coral')
my_map.drawmapboundary()

my_map.drawmeridians(np.arange(0, 360, 30))
my_map.drawparallels(np.arange(-90, 90, 30))


plt.savefig(os.path.join(os.path.split(os.path.realpath(__file__))[0], 'xx_' + os.path.split(os.path.realpath(__file__))[1][5:-3] + '2.png'))
plt.clf()

my_map = Basemap(projection='merc', lat_0=57, lon_0=-135,
                 resolution='h', area_thresh=0.1,
                 llcrnrlon=-136.25, llcrnrlat=56,
                 urcrnrlon=-134.25, urcrnrlat=57.75)

my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color='coral')
my_map.drawmapboundary()

my_map.drawmeridians(np.arange(0, 360, 30))
my_map.drawparallels(np.arange(-90, 90, 30))



plt.savefig(os.path.join(os.path.split(os.path.realpath(__file__))[0], 'xx_' + os.path.split(os.path.realpath(__file__))[1][5:-3] + '3.png'))
plt.clf()


plt.close()


