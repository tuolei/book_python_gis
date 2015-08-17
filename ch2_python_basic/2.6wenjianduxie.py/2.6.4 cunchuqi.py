# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

import cPickle as p
shoplistfile = 'shoplist.dsts'
shoplist = ['apple','mango','carrot',10,22,35]
f = file(shoplistfile,'w')
p.dump(shoplist,f)
f.close()
del shoplist
f = file(shoplistfile)
stroedlist = p.load(f)
print(stroedlist)