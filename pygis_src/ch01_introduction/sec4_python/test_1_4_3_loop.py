# -*- coding: utf-8 -*-

rangs = range(1, 5)
print(rangs)
for val in rangs:
    print(val)
else:
    print('The for loop is over')

while True:
    s = 'quit'
    if s == 'quit':
        break
    print('length of the string is ', len(s))
print('Done')

for i in range(1, 20):
    if i % 2 == 1:
        print(i)
    else:
        continue

number = 23
