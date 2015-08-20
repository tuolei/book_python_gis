# -*- coding: utf-8 -*-
import os
#os.chdir('/home/liujx/gdata')

def func(x):
    print('x i',x)
    x = 2
    print('Changed local x to',x)
x =50
func(x)
print('x is still',x)

