# -*- coding: utf-8 -*-

'''
command:
    python3 ch06_fiona/sec01_intro/g6_1_4_zipfile.py
写入多层数据
'''
import fiona

# with fiona.drivers():
#     for i, layername in enumerate(
#             fiona.listlayers(
#                 '/',
#                 vfs='zip://gdata/tmp/world_borders.zip')):
#         with fiona.open(
#                 '/',
#                 vfs='zip://gdata/tmp/world_borders.zip',
#                 layer=i) as src:
#             print(i, layername, len(src))


#
# import fiona
#
# with fiona.drivers():
#     for i, layername in enumerate(
#             fiona.listlayers('/', vfs='zip://gdata/world_borders.zip')):
#         with fiona.open('/', vfs='zip://gdata/world_borders.zip', layer=i) as src:
#             print(i, layername, len(src))
