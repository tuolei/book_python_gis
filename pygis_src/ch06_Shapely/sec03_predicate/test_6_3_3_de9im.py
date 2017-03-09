# -*- coding: utf-8 -*-

from shapely.geometry import Point, LineString

Point(0, 0).relate(Point(1, 1))
Point(0, 0).relate(LineString([(0, 0), (1, 1)]))
