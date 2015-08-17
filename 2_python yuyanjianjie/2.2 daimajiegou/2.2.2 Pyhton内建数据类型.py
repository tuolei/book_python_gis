# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

import math
int_a = 3
int_b = 4
int_c = 5

long_a = 3
print(type(int_a))
print(type(long_a))

print(int_b /  int_a)
print(int_b * 1.0 / int_a)

print(divmod(int_a,int_b))
print(divmod(int_a*1.0,int_b))

com_i = int_a + int_b * 1j

print(abs(com_i))
print(math.sqrt(int_a ** 2 + int_b ** 2))

print(math.pow(math.e math.pi * (0+1j)) + 1)

print('abcd')
print("abcd")
print('''abcd''')

print('ab''cd')
print("ab'cd")
print('''a'b"c'd''')
print('abcdefgh')

print('abcdnefgh')
print('abcdnefgh')

print('''abcdfdsf''')
