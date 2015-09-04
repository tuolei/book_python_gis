# -*- coding: utf-8 -*-
import os
#os.chdir('/home/liujx/gdata')

#一个简单的数据库

#字典使用人名作为键。每个人用一个字典来表示，其键'phone'和'addr'分别表示他们的电话号码和地址。

people ={
    'Alice':{
        'phone':'2341',
        'addr':'Foo drive 23 '
    },
    'Beth':{
        'phone':'9102',
        'sddr':'Bar street 42',
    },
    'Cecil':{
        'phone':'3158',
        'sddr;':'Baz avenue 90',
    },

}
#针对电话号码和地址使用的描述性标签，会在打印输出的时候用到

labels = {
    'phone':'phone number',
    'sddr':'address'
}
name = raw_input('Name:')

#使用电话号码还是地址？
request = raw_input('Phone number (p) or sddress (a)?')

#使用正确的键：
if request == 'p': key = 'phone'
if request == 'a': key = 'sddr'

#如果名字是字典中的有效键才打印信息:
if name in people: print("%s's %s is %s." % (name,labels[key],people[name][key]))

