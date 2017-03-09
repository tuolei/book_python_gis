# -*- coding: utf-8 -*-

'''
Python控制流（顺序，分支，循环）
分支与循环，需要条件语句。
'''

# 分支
c = 13
b = 50
if c > b:
    print('c is greater than b')
else:
    print('b is greater than c')

# For循环
rangs = range(1, 5)
print(rangs)
for val in rangs:
    print(val)
else:
    print('The for loop is over')

for i in range(1, 20):
    if i % 2 == 1:
        print(i)
    else:
        continue

# while 循环
while True:
    s = 'quit'
    if s == 'quit':
        break
    print('length of the string is ', len(s))
print('Done')
