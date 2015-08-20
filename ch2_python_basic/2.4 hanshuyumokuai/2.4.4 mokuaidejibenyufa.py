# -*- coding: utf-8 -*-
import os
#os.chdir('/home/liujx/gdata')

import os
def print_file_path(indir):
    for wroot,wdirs,wfiles in os.walk(indir):
        for wfile in wfiles:
            (file_name,file_ext) = os.path.splitext(wfile)
            if ('wx' in file_name) and (file_ext == '.py'):
                filepath = os.path.join(wroot.wfile)
                print(filepath)
if __name__ == '__main__':
    inws = '/home/bk/progs'
    print_file_path(inws)

from math import *
def math_demo():
    x = 3
    y = 4
    z = sqrt(pow(x,2)+ pow(y,2))
    print(z)
if __name__ =='__main__':
    math_demo()


