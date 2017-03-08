# -*- coding: utf-8 -*-

import math


def sayHello():
    print('Hello World!')


sayHello()


def get_circle_area(r):
    area = math.pi * r * r
    return (area)


val_r = 3
the_area = get_circle_area(val_r)
print(the_area)


def func(x):
    print('x i', x)
    x = 2
    print('Changed local x to', x)


x = 50
func(x)
print('x is still', x)


def say(message, times=1):
    print(message * times)


say('Hello')
say('World', 5)


def func2(a, b=5, c=10):
    print('a is ', a, 'and b is ', b, 'and c is', c)


func2(3, 7)
func2(25, c=24)
func2(c=50, a=100)

import os


def print_file_path(indir):
    for wroot, wdirs, wfiles in os.walk(indir):
        for wfile in wfiles:
            (file_name, file_ext) = os.path.splitext(wfile)
            if ('wx' in file_name) and (file_ext == '.py'):
                filepath = os.path.join(wroot.wfile)
                print(filepath)


from math import *


def math_demo():
    x = 3
    y = 4
    z = sqrt(pow(x, 2) + pow(y, 2))
    print(z)


def sayhi():
    print('Hi ,this is mymodule apeaking.')


version = '0.1'
