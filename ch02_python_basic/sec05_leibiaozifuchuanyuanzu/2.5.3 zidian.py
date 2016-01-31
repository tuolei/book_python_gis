# -*- coding: utf-8 -*-
import os
#os.chdir('/home/liujx/gdata')

dict_demo = {'GIS':'Geographic Information System',
    'RS':'Remote Sencing',
    'GPS':'Global Postioning System',
    'DEM':'Dynamic Effect Model'}
print(dict_demo['GPS'])
print(dict_demo['DEM'])
print(dict_demo.items())
dict_demo['DEM '] = 'Digital Elevation Model'
print(dict_demo['DEM'])

print(dict.has_key('RS'))
print(dict.has_key('rs'))
dict_demo['rs'] = 'Remote Sencing'
print(dict_demo.keys())
def(dict_demo['rs']):
dict_demo.key()
for short_name,long_name in dict_demo.items():
    print(('short Name:%4s -> Long Name:%s') % (short_name,long_name))

