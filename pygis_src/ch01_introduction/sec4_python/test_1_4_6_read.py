# -*- coding: utf-8 -*-

'''
第一列为序号，后面是测量的数据。分别是萼片的长、宽，花瓣的长、宽。 把上面数据存储为data.dat，放到程序的同一目录下。
程序的目的是计算萼片与花瓣的长宽比。注意读写文件的用法。
'''

'''
id    Sepal.Length Sepal.Width Petal.Length Petal.Width
1            5.1         3.5          1.4         0.2
2            4.9         3.0          1.4         0.2
3            4.7         3.2          1.3         0.2
4            4.6         3.1          1.5         0.2
5            5.0         3.6          1.4         0.2
6            5.4         3.9          1.7         0.4
7            4.6         3.4          1.4         0.3
8            5.0         3.4          1.5         0.2
9            4.4         2.9          1.4         0.2
10           4.9         3.1          1.5         0.1
11           5.4         3.7          1.5         0.2
12           4.8         3.4          1.6         0.2
13           4.8         3.0          1.4         0.1
14           4.3         3.0          1.1         0.1
15           5.8         4.0          1.2         0.2
16           5.7         4.4          1.5         0.4
'''

fi = open('gdata/data_io.dat')
cnts = fi.readlines()
fo = open('gdata/xx_result.dat', 'w')
for cnt in cnts:
    cnt = cnt.strip()
    if len(cnt) > 0:
        recs = cnt.split()
        if recs[0] == 'id':
            fo.write('id Sepal Petal\n')
        else:
            vals = [float(x) for x in recs[1:]]
            v1 = vals[0] / vals[1]
            v2 = vals[2] / vals[3]
            fo.write('%s %10.2f %10.2f\n' % (recs[0], v1, v2))
fo.close()
fi.close()
