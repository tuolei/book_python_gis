# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

def sayHello():
    print('Hello World!')
sayHello()

import math
def get_circle_area(r):
    area = math.pi * r * r
    return(area)
val_r = 3
the_area = get_circle_area(val_r)
print(the_area)