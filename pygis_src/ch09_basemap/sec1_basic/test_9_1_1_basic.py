
import os
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# make sure the value of resolution is a lowercase L,
#  for 'low', not a numeral 1
my_map = Basemap(projection='ortho', lat_0=50, lon_0=-100,
                 resolution='l', area_thresh=1000.0)

my_map.drawcoastlines()

# plt.show()
plt.savefig(os.path.join(os.path.split(os.path.realpath(__file__))[0], 'xx_' + os.path.split(os.path.realpath(__file__))[1][5:-3] + '1.png'))

plt.clf()

my_map = Basemap(projection='ortho', lat_0=50, lon_0=-100,
                 resolution='l', area_thresh=1000.0)

my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color='coral')

plt.savefig(os.path.join(os.path.split(os.path.realpath(__file__))[0], 'xx_' + os.path.split(os.path.realpath(__file__))[1][5:-3] + '2.png'))
plt.clf()

my_map = Basemap(projection='ortho', lat_0=50, lon_0=-100,
                 resolution='l', area_thresh=1000.0)

my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color='coral')
my_map.drawmapboundary()

plt.savefig(os.path.join(os.path.split(os.path.realpath(__file__))[0], 'xx_' + os.path.split(os.path.realpath(__file__))[1][5:-3] + '3.png'))
plt.clf()

my_map = Basemap(projection='ortho', lat_0=50, lon_0=-100,
                 resolution='l', area_thresh=1000.0)

my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color='coral')
my_map.drawmapboundary()

my_map.drawmeridians(np.arange(0, 360, 30))
my_map.drawparallels(np.arange(-90, 90, 30))

plt.savefig(os.path.join(os.path.split(os.path.realpath(__file__))[0], 'xx_' + os.path.split(os.path.realpath(__file__))[1][5:-3] + '4.png'))
plt.clf()

my_map = Basemap(projection='ortho', lat_0=0, lon_0=-100,
                 resolution='l', area_thresh=1000.0)

my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color='coral')
my_map.drawmapboundary()

my_map.drawmeridians(np.arange(0, 360, 30))
my_map.drawparallels(np.arange(-90, 90, 30))

plt.savefig(os.path.join(os.path.split(os.path.realpath(__file__))[0], 'xx_' + os.path.split(os.path.realpath(__file__))[1][5:-3] + '5.png'))
plt.clf()

plt.close()
