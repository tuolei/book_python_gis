# -*- coding: utf-8 -*-


from pyproj import Proj
import pyproj

albers = Proj('+proj=aea +lon_0=105 +lat_1=25 +lat_2=47 +ellps=krass')
utm = Proj(proj='utm', zone=48, ellps='krass')
albers_x, albers_y = albers(105, 36)
print(albers_x, albers_y)
utm_x, utm_y = utm(105, 36)
print(utm_x, utm_y)
# 下边直接从 albers转为 utm坐标
to_utm_x, to_utm_y = pyproj.transform(albers, utm, albers_x, albers_y)
print(to_utm_x, to_utm_y)
