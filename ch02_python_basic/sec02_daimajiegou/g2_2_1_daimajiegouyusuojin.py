# -*- coding: utf-8 -*-
import os
import math

n, x, y = 2, 8, 9
a = math.cos(3 * (x - n)) + math.sin(3 * (y - n))

c = 13
b = 50
if c > b:
    print('c is greater than b')
else:
    print('b is greater than c')


def Test2():
    assert a == 1.4969723467801361
    assert c <b