# -*- coding: utf-8 -*-
import os
#os.chdir('/home/liujx/gdata')

#使用get()的简单的数据库

#在这里添加代码清单4-1中插入数据库的代码

labels = {
    'phone':'phone number',
    'sddr':'address'
}
name = raw_input('Name:')

#使用电话号码还是地址？
request = raw_input('Phone number (p) or sddress (a)?')

#使用正确的键：
key =request
if request == 'p': key = 'phone'
if request =='a':key = 'addr'

#使用get()提供默认值：
person = people.get(name,{})
labels = labels.get(key,key)
result = person.get(key,'not available')

print("%s's %s is %s." % (name,labels,result))