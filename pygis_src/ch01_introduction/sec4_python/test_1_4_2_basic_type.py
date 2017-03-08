# -*- coding: utf-8 -*-

import math

n, x, y = 2, 8, 9
a = math.cos(3 * (x - n)) + math.sin(3 * (y - n))

c = 13
b = 50
if c > b:
    print('c is greater than b')
else:
    print('b is greater than c')


'''
布尔型
'''
print(4 > 30)
print(True | False)

# 数值类型
import math

int_a = 3
int_b = 4
int_c = 5
'''
v3.0后，确切的讲， int 型（依赖运行环境C编译器中long型的精度）消失了，long型替代 int 型，
成为新的、不依赖运行环境的、无精度限制的（只要内存装得下）int型。
'''

print(type(int_a))

print(int_b / int_a)

print(int_b * 1.0 / int_a)

print(divmod(int_a, int_b))
print(divmod(int_a * 1.0, int_b))

com_i = int_a + int_b * 1j

print(abs(com_i))
print(math.sqrt(int_a ** 2 + int_b ** 2))

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


def Test():
    assert type(int_a) == type(5)
    assert type(com_i) == type(1.3 + 5.4 * 1j)
