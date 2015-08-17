# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

import ogr

from osgeo import ogr

try:
    from osgeo import ogr
except:
    import ogr
