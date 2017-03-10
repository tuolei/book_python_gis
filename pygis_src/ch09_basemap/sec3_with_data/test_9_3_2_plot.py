
import os
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

my_map = Basemap(projection='merc', lat_0=57, lon_0=-135,
                 resolution='h', area_thresh=0.1,
                 llcrnrlon=-136.25, llcrnrlat=56.0,
                 urcrnrlon=-134.25, urcrnrlat=57.75)

my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color='coral')
my_map.drawmapboundary()

lon = -135.3318
lat = 57.0799
x, y = my_map(lon, lat)
my_map.plot(x, y, 'bo', markersize=12)

plt.savefig(os.path.join(os.path.split(os.path.realpath(__file__))[0], 'xx_' + os.path.split(os.path.realpath(__file__))[1][5:-3] + '1.png'))
plt.clf()

my_map = Basemap(projection='merc', lat_0=57, lon_0=-135,
                 resolution='h', area_thresh=0.1,
                 llcrnrlon=-136.25, llcrnrlat=56.0,
                 urcrnrlon=-134.25, urcrnrlat=57.75)

my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color='coral')
my_map.drawmapboundary()

lons = [-135.3318, -134.8331, -134.6572]
lats = [57.0799, 57.0894, 56.2399]
x, y = my_map(lons, lats)
my_map.plot(x, y, 'bo', markersize=10)

plt.savefig(os.path.join(os.path.split(os.path.realpath(__file__))[0], 'xx_' + os.path.split(os.path.realpath(__file__))[1][5:-3] + '2.png'))
plt.clf()

my_map = Basemap(projection='merc', lat_0=57, lon_0=-135,
                 resolution='h', area_thresh=0.1,
                 llcrnrlon=-136.25, llcrnrlat=56.0,
                 urcrnrlon=-134.25, urcrnrlat=57.75)

my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color='coral')
my_map.drawmapboundary()

lons = [-135.3318, -134.8331, -134.6572]
lats = [57.0799, 57.0894, 56.2399]
x, y = my_map(lons, lats)
my_map.plot(x, y, 'bo', markersize=10)

labels = ['Sitka', 'Baranof Warm Springs', 'Port Alexander']
for label, xpt, ypt in zip(labels, x, y):
    plt.text(xpt, ypt, label)

plt.savefig(os.path.join(os.path.split(os.path.realpath(__file__))[0], 'xx_' + os.path.split(os.path.realpath(__file__))[1][5:-3] + '3.png'))
plt.clf()

my_map = Basemap(projection='merc', lat_0=57, lon_0=-135,
                 resolution='h', area_thresh=0.1,
                 llcrnrlon=-136.25, llcrnrlat=56.0,
                 urcrnrlon=-134.25, urcrnrlat=57.75)

my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color='coral')
my_map.drawmapboundary()

lons = [-135.3318, -134.8331, -134.6572]
lats = [57.0799, 57.0894, 56.2399]
x, y = my_map(lons, lats)
my_map.plot(x, y, 'bo', markersize=10)

labels = ['Sitka', 'Baranof Warm Springs', 'Port Alexander']
for label, xpt, ypt in zip(labels, x, y):
    plt.text(xpt + 10000, ypt + 5000, label)

plt.savefig(os.path.join(os.path.split(os.path.realpath(__file__))[0], 'xx_' + os.path.split(os.path.realpath(__file__))[1][5:-3] + '5.png'))
plt.clf()

my_map = Basemap(projection='merc', lat_0=57, lon_0=-135,
                 resolution='h', area_thresh=0.1,
                 llcrnrlon=-136.25, llcrnrlat=56.0,
                 urcrnrlon=-134.25, urcrnrlat=57.75)

my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color='coral')
my_map.drawmapboundary()

lons = [-135.3318, -134.8331, -134.6572]
lats = [57.0799, 57.0894, 56.2399]
x, y = my_map(lons, lats)
my_map.plot(x, y, 'bo', markersize=10)

labels = ['Sitka', 'Baranof\n  Warm Springs', 'Port Alexander']
x_offsets = [10000, -20000, -25000]
y_offsets = [5000, -50000, -35000]

for label, xpt, ypt, x_offset, y_offset in zip(labels, x, y, x_offsets, y_offsets):
    plt.text(xpt + x_offset, ypt + y_offset, label)

plt.savefig(os.path.join(os.path.split(os.path.realpath(__file__))[0], 'xx_' + os.path.split(os.path.realpath(__file__))[1][5:-3] + '6.png'))
plt.clf()

plt.close()