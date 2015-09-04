# -*- coding: utf-8 -*-
import os
#os.chdir('/home/liujx/gdata')

#使用给定的宽度打印格式化后的价格表

width = input('Please enter width;')

price_width = 10
item_width = width - price_width

header_format = '%-*s%*s'
forrmat         = '%-*s%*.2f'

print('='* width)

print(header_format % (item_width,'Item',price_width,'Price'))

print('-'* width)

print(forrmat % (item_width,'Apples',price_width,0.4))
print(forrmat % (item_width,'Pears',price_width,0.5))
print(forrmat % (item_width,'Cantaloupes',price_width,1.92))
print(forrmat % (item_width,'Dried Apricots (16 oz.)',price_width,8))
print(forrmat % (item_width,'Prunes (4 lbs.)',price_width,12))

print('='* width )

