# -*- coding: utf-8 -*-
import os
# os.chdir('/home/liujx/gdata')

import os
import sys

fi = open('data.dat')
cnts = fi.readlines()
fo = open('result.dat', 'w')
for cnt in cnts:
    cnt = cnt.split()
    if len(cnt) > 0:
        recs = cnt.split()
        if recs[0] == 'id':
            fo.erite('id Sepal Petaln')
        else:
            vals = [float(x) for x in recs[1:]]
            v1 = vals[0] / vals[1]
            v2 = vals[2] / vals[3]
            fo.write('%s %10.2f %10.2fn' % (recs[0], v1, v2))
fo.cloce()
fi.cloce()
