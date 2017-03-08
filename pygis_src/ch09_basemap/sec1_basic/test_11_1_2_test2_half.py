# -*- coding: utf-8 -*-

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# make sure the value of resolution is a lowercase L,
#  for 'low', not a numeral 1

'''
画个图就可以了，分界线是西经20和东经160，这样的两条经线（也就是两条经线所组成的经线圈）把地球分为东西两个半球，
记住中国在东半球，美国大部分在西半球就可以了。实在不行就在世界地图上用红笔把这两条经线描红，这样总不会错了。
'''

p1 = plt.subplot(121)
my_map = Basemap(projection='ortho', lat_0=0, lon_0=70, resolution='l', area_thresh=1000.0)
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color='coral')
my_map.drawmapboundary()
my_map.drawmeridians(np.arange(0, 360, 30))
my_map.drawparallels(np.arange(-90, 90, 30))

p2 = plt.subplot(122)
my_map2 = Basemap(projection='ortho', lat_0=0, lon_0=-110, resolution='l', area_thresh=1000.0)
my_map2.drawcoastlines()
my_map2.drawcountries()
my_map2.fillcontinents(color='coral')
my_map2.drawmapboundary()
my_map2.drawmeridians(np.arange(0, 360, 30))
my_map2.drawparallels(np.arange(-90, 90, 30))

# plt.show()
plt.savefig('xx_basemap_2_half.png')
plt.clf()
plt.close()