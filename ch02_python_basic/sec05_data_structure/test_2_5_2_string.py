# -*- coding: utf-8 -*-
import os
#os.chdir('/home/liujx/gdata')

path = r'e:book'
print(path)
print('**n\t'"r**")
print(len(path))
str_val ='s'+'pam'
print(str_val)

print('=' * 10)

print('abc'+str(9))

val = int('42')
print(val)
val = str(42)
print(val)
val = float('42.0')
print(val)

print(ord('s'))
print(type(ord('s')))
print(chr(115))
print(type(chr(115)))

s = 'spam'
k = '|'.join(s)
print(k)
s='spam'
l = list(s)
print(l)
k = '|'.join(l)
print(k)

s = s +'a'
s = s[3:]+ 'b'
s = s.replace('pl','pa')

s = 'abcdefg'
print(s[1:])
print(s[1:1])

str_val = 'abcd'
str_val = str_val.capitalize()
print(str_val)

str_val= str_val.lower()
print(str_val)

print(str_val.isalpha())
print(str_val.isdigit())

str_val = 'abcdfgxabcdyzcdba'
str_val = str_val.strip()
print(str_val)
str_val=str_val.strip('a')
print(str_val)

tepstr =str_val
str_val = str_val.strip('bc')
print(str_val)
str_val = tepstr.strip('cd')
print(str_val)

str_val = list(str_val)
str_val.sort()
str_val=''.join(str_val)
print(str_val)

str_val = str_val.upper()
print (str_val)

ind_list =range(5,15)
ind_list = [str(x) for x in ind_list]
print(ind_list)
str_list = [ind.zfill(3) for ind in ind_list]
print(str_list)

str_val ='the are %d %s in the team.'% (2,'girls')
print(str_val)

str_val ='Hello,Python!'
print(len(str_val))
print(str_val.index('y'))
for x in str_val:
    print(x)

