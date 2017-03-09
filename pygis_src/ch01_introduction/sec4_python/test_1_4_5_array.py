# -*- coding: utf-8 -*-


list_val = [1, '3', 5, '4']

print(list_val)
list_val = [x for x in range(5, 0, -1)]
print(list_val)

list_val.append(6)
print(list_val)

list_val = list_val + [7, 8]
print(list_val)

list_val.extend([9, 10])
print(list_val)

list_val.insert(5, 5)
print(list_val)

tep_a = list_val.pop()
print(list_val)
print(tep_a)

tep_a = list_val.pop(5)
print(list_val)
print(tep_a)

val_index = list_val.index(3)
print(list_val)
print(val_index)

list_val.remove(3)
print(list_val)
print(val_index)

for val in list_val:
    print(val)

print(len(list_val))

list_val.sort()
print(list_val)

list_val.reverse()
print(list_val)

a = range(8)
print(a)
b = tuple(a)
print(b)
c = list(b)
print(c)

list_val = range(8, 0, -1)
print(list_val)
index_list = range(8)
for index in index_list:
    print('Tndex: %d' % (index))
    print(list_val[index])
print(list_val[-1])
print(list_val[-2])
print(list_val[2:])
print(list_val[:-2])
print(list_val[2:-2])
print(list_val[:])

dict_demo = {'GIS': 'Geographic Information System',
             'RS': 'Remote Sencing',
             'GPS': 'Global Postioning System',
             'DEM': 'Dynamic Effect Model'}
print(dict_demo['GPS'])
print(dict_demo['DEM'])
print(dict_demo.items())
dict_demo['DEM '] = 'Digital Elevation Model'
print(dict_demo['DEM'])

print('RS' in dict_demo)
print('rs' in dict_demo)
dict_demo['rs'] = 'Remote Sencing'
print(dict_demo.keys())

for short_name, long_name in dict_demo.items():
    print(('short Name:%4s -> Long Name:%s') % (short_name, long_name))


str_val = 's' + 'pam'
print(str_val)

print('=' * 10)

print('abc' + str(9))

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
s = 'spam'
l = list(s)
print(l)
k = '|'.join(l)
print(k)

s = s + 'a'
s = s[3:] + 'b'
s = s.replace('pl', 'pa')
print(s)
s = 'abcdefg'
print(s[1:])
print(s[1:1])

str_val = 'abcd'
str_val = str_val.capitalize()
print(str_val)

str_val = str_val.lower()
print(str_val)

print(str_val.isalpha())
print(str_val.isdigit())

str_val = 'abcdfgxabcdyzcdba'
str_val = str_val.strip()
print(str_val)
str_val = str_val.strip('a')
print(str_val)

tepstr = str_val
str_val = str_val.strip('bc')
print(str_val)
str_val = tepstr.strip('cd')
print(str_val)

str_val = list(str_val)
str_val.sort()
str_val = ''.join(str_val)
print(str_val)

str_val = str_val.upper()
print(str_val)

ind_list = range(5, 15)
ind_list = [str(x) for x in ind_list]
print(ind_list)
str_list = [ind.zfill(3) for ind in ind_list]
print(str_list)

str_val = 'the are %d %s in the team.' % (2, 'girls')
print(str_val)

str_val = 'Hello,Python!'
print(len(str_val))
print(str_val.index('y'))
for x in str_val:
    print(x)
