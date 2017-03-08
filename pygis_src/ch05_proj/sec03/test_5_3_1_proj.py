# -*- coding: utf-8 -*-

import pyproj

pyproj.test()

from pyproj import Proj

from pyproj import Proj

p = Proj('+proj=aea +lon_0=105 +lat_1=25 +lat_2=47 +ellps=krass')
x, y = p(105, 36)
print('%.3f,%.3f' % (x, y))

p1 = Proj(proj='utm', zone=10, ellps='WGS84')
print(p)

p2 = Proj('+proj=utm +zone=10 +ellps=WGS84')

p3 = Proj(init="epsg:32667")

p4 = Proj("+init=epsg:32667", preserve_units=True)

lon, lat = p(x, y, inverse=True)
print('%.3f,%.3f' % (lon, lat))

import math  # 验证关键字 radians

x, y = p(math.radians(105), math.radians(36), radians=True)
print('%.3f,%.3f' % (x, y))

# Array

lons = (105, 106, 104)
lats = (36, 35, 34)
x, y = p(lons, lats)  # 将经纬度放入元组中
print('%.3f,%.3f,%.3f' % x)  # 普通打印
print('%.3f,%.3f,%.3f' % y)
type(x)  # 输出的类型为元组
zip(x, y)  # 用 zip函数包装

# Define projction with keywords.

utm = Proj(proj='utm', zone=48, ellps='WGS84')
x, y = utm(105, 36)  # 用关键字定义一个投影。
print(x, y)


utm.is_geocent()
utm.is_latlong() 
latlong=Proj('+proj=latlong') 
print(latlong.is_latlong())
print(latlong.is_geocent())
