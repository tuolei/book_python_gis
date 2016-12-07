# -*- coding:utf-8 -*-

'''以GDT开头的就是数值数据类型
要想查看图像中某一波段的数据类型，只需要打印这一波段的DataType属性即可
band.DataType
'''
from osgeo import gdalconst
print(dir(gdalconst))

def Test():
    assert True