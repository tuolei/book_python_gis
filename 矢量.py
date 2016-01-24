
# 
inshp='world_borders.shp'
from osgeo import ogr
datasource=ogr.Open(inshp)
driver = datasource.GetDriver()
driver.name

dir(datasource)

driver = ogr.GetDriverByName('ESRI Shapefile')

# 使用driver打开数据
import sys
from osgeo import ogr
inshp = 'world_borders.shp'
driver = ogr.GetDriverByName('ESRI Shapefile')
dataSource = driver.Open(inshp,0)
if dataSource is None:
    print('could not open')    

print('done') 

# Python中的Layer的方法
inshp='world_borders.shp'
from osgeo import ogr
datasource = ogr.Open(inshp)   
layer = datasource.GetLayer(0)
dir(layer)

n = layer.GetFeatureCount()
print('feature count:',n)

extent = layer.GetExtent()
print('extent:',extent)
print('ul:',extent[0],extent[3])
print('lr:',extent[1],extent[2])

# tu ceng de shu xing
layerdef = layer.GetLayerDefn()
for i in range(layerdef.GetFieldCount()):
    defn = layerdef.GetFieldDefn(i)
    print(defn.GetName(),defn.GetWidth(),defn.GetType(),defn.GetPrecision())

# 获取图层中的要素
from osgeo import ogr
inshp='world_borders.shp'
datasource = ogr.Open(inshp)
layer = datasource.GetLayer(0)
feature = layer.GetFeature(0)
print(feature.GetField('Name'))--------------------------------------

feat = layer.GetNextFeature()
while feat:
    feat = layer.GetNextFeature()

layer.ResetReading()

# 获取要素的属性
feat=layer.GetFeature(0)
feat.keys()
fid=feat.GetField('AREA')
print(fid)

for i in range(feature.GetFieldCount()):
    print(feature.GetField(i))
    
layerdef = layer.GetLayerDefn()
for i in range(layerdef.GetFieldCount()):
    defn = layerdef.GetFieldDefn(i)
    print(defn.GetName(),defn.GetWidth(),defn.GetType(),defn.GetPrecision())
    
# 要素的形状
geom = feature.GetGeometryRef()
geom.GetGeometryName()
geom .GetGeometryCount()
geom.GetPointCount()
geom.GetX()
geom.GetY()
print(geom)
print(geom.ExportToWkt())
polygon=geom.GetGeometryRef(0)
polygon.GetGeometryName()
polygon.GetPointCount()
polygon.GetX(0)
polygon.GetY(0)
polygon.GetZ(0)
print(polygon.ExportToWkt())

layer.GetSpatialRef()
layer.GetExtent()

geom.GetEnvelope()
geom.GetSpatialReference()

geom.GetArea()

# 删除矢量数据
import os
from osgeo import ogr
driver=ogr.GetDriverByName('ESRI Shapefile')
out_shp = 'world_borders.shp'
if os.path.exists(out_shp):
    driver.DeleteDataSource(out_shp)
    
if os.path.exists(out_shp):
    driver.DeleteDataSource(out_shp)
ds2 =driver.CreateDataSource(out_shp)
layer2=ds2.CreateLayer('test',geom_type=ogr,wkbPoint)

fieldDefn = ogr.FieldDefn('id',ogr.OFTString)
fieldDefn.SetWidth(4)
layer2.CreateField(fieldDefn)

featureDefn =layer.GetLayerDefn()
feature=ogr.Feature(featureDefn)

point=ogr.Geometry(ogr.wkbPoint)
point.SetPoint(0,123,123)
feature.SetGeometry(point)

feature.SetField('id',23)------------------------------ No such field: 'id'

layer2.CreateFeature(feature)
ds2.Destroy()


# 快速开始
from osgeo import ogr as ogr
import datetime 

data=[[0,3333317.0,5684892.0,'Hans','true'],[1,3333417.0,5684891.0,'Fritz','true'],[2,3333317.0,5684992.0,'Willi','false'],[3,3333417.0,5684992.0,'Walter','false']]

driver = ogr.GetDriverByName('ESRI Shapefile')
output="points.shp"
datasource=driver.CreateDataSource(output)
layer = datasource.CreateLayer(output,geom_type=ogr.wkbPoint)

field_ID = ogr.FieldDefn()
field_ID.SetName('ID')
field_ID.SetType(ogr.OFTInteger)
field_ID.SetWidth(1)
layer.CreateField(field_ID)
field_TEXT = ogr.FieldDefn('TEXT',ogr.OFTString)
field_TEXT.SetWidth(20)
layer.CreateField(field_TEXT)
field_FLOAT = ogr.FieldDefn('FLOAT',ogr.OFTReal)
field_FLOAT.SetWidth(10)
field_FLOAT.SetPrecision(2)
layer.CreateField(field_FLOAT)
field_DATE=ogr.FieldDefn('DATE',ogr.OFTDate)
field_DATE.SetWidth(8)
layer.CreateField(field_DATE)
field_BOOL=ogr.FieldDefn('BOOLEAN',ogr.OFTString)
field_BOOL.SetWidth(5)
layer.CreateField(field_BOOL)
feature = ogr.Feature(layer.GetLayerDefn())

for ID,X,Y,TEXT,BOOLEAN in data:
    DATE = datetime.date.today()
    wkt = "POINT("+str(X) + " " +str(Y) + ")"
    point = ogr.CreateGeometryFromWkt(wkt)
    feature.SetGeometryDirectly(point)
    feature.SetField('ID',ID)
    feature.SetField('TEXT',TEXT)
    feature.SetField('FLOAT',X)
    feature.SetField('BOOLEAN',BOOLEAN)
    layer.CreateFeature(feature)
    
feature.Destroy()
datasource.Destroy()
print("Feature <" + "> successfully created.")
del output

# 4.3.3使用OGR创建要素几何形状# -*- coding: utf-8 -*-
import os
os.chdir('/home/liujx/gdata')

from osgeo import ogr
inshp='world_borders.shp'
datasource = ogr.Open(inshp)
layer = datasource.GetLayer(0)
layer.GetSpatialRef()
layer.GetExtent()

frature = layer.GetFeature(0)
geom =feature.GetGeometryRef()
geom.GetEnvelope()
geom.GetSpatialReference()

geom.GetArea()


# 创建点要素
from osgeo import ogr
point = ogr.Geometry(ogr.wkbPoint)
point.AddPoint(10,20)
print(type(point))
print(point)

# 创建线要素
from osgeo import ogr
line = ogr.Geometry(ogr.wkbLineString)
line.AddPoint(10,20)
line.AddPoint(20,30)
line.AddPoint(10,30)
print(type(line))
print(line)

line.SetPoint(1,50,50)
print(line)

print(line.GetPointCount())

print(line.GetX(0))
print(line.GetY(0))

# 创建多边形要素
from osgeo import ogr
ring = ogr.Geometry(ogr.wkbLinearRing)
ring.AddPoint(10,10)
ring.AddPoint(50,0)
ring.AddPoint(50,50)
ring.AddPoint(0,10)

ring.CloseRings()--------------------------------使ring封闭的CloseRing()方法

polygon = ogr.Geometry(ogr.wkbPolygon)
polygon.AddGeometry(ring)

ring = polygon.GetGeometryRef(0)
print(ring)

# 4.3.4使用OGR中拷贝的方法创建新的Shapefile

# 在datasource层次创建数据
from osgeo import ogr
import os,math
inshp = 'world_borders.shp'
ds = ogr.Open(inshp)
driver = ogr.GetDriverByName("ESRI Shapefile")
outputfile = 'world_borders.shp'
if os.access(outputfile,os.F_OK):
    driver.DeleteDataSource(outputfile)
    
pt_cp = driver.CopyDataSource(ds,outputfile)
pt_cp.Release()

# 在layer层次拷贝数据
from osgeo import ogr
import os,math
inshp='world_borders.shp'
ds = ogr.Open(inshp)
driver =ogr.GetDriverByName("ESRI Shapefile")
outputfile = 'world_borders_copy2.shp'
if os.access(outputfile,os.F_OK):
    driver.DeleteDataSource(outputfile)
    
layer = ds.GetLayer()

newds = driver.CreateDataSource(outputfile)

pt_layer = newds.CopyLayer(layer,'abcd')
newds.Destroy()

# 在feature层次拷贝数据
from osgeo import ogr
import os,math
inshp = 'world_borders.shp'
ds = ogr.Open(inshp)
driver = ogr.GetDriverByName("ESRI Shapefile")
outputfile = 'world_borders_copy3.shp'
if os.access(outputfile,os.F_OK):
    driver.DeleteDataSource(outputfile)
    
    
    
newds = driver.CreateDataSource(outputfile)

layernew = newds.CreateLayer('worldcopy',None,ogr.wkbLineString)
layer = ds.GetLayer()
extent = layer.GetExtent()
print(extent)
feature = layer.GetNextFeature()
while feature is not None:
    layernew.CreateFeature(feature)
    feature = layer.GetNextFeature()

newds.Destroy()

# 4.3.5使用OGR创建数据集的集合形状

# 创建点状数据集
from osgeo import ogr
import os ,math
driver = ogr.GetDriverByName("ESRI Shapefile")

extfile='world_borders.shp'
point_coors = [[300,450],[750,700],[1200,450],[750,200],[750,450]]
print(point_coors)
driver = ogr.GetDriverByName("ESRI Shapefile")
if os.access(extfile,os.F_OK):
    driver.DeleteDataSource(extfile)
    
    
newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('point',None,ogr.wkbPoint)
for aa in point_coors:
    wkt = 'POINT (' + str(aa[0]) + ' ' + str(aa[1]) + ')'
    geom = ogr.CreateGeometryFromWkt(wkt)
    feat = ogr.Feature(layernew.GetLayerDefn())
    feat.SetGeometry(geom)
    layernew.CreateFeature(feat)
    
newds.Destroy()

# 创建线状数据集
from osgeo import ogr 
import os, math 
driver =ogr.GetDriverByName("ESRI Shapefile")

extfile = 'world_borders.shp'
point_coors = [300,450,750,700,1200,450,750,200]
print(point_coors)
driver = ogr.GetDriverByName("ESRI Shapefile")
if os.access(extfile,os.F_OK):
    driver.DeleteDataSource(extfile)

newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('point',None,ogr.wkbLineString)

wkt = 'LINESTRING (%f %f %f %f %f %f %f %f %f %f)'  % (point_coors[0],point_coors[1],point_coors[2],point_coors[3],point_coors[4],point_coors[5],point_coors[6],point_coors[7],point_coors[0],point_coors[1])
print(wkt)
geom = ogr.CreateGeometryFromWkt(wkt)
feat = ogr.Feature(layernew.GetLayerDefn())
feat.SetGeometry(geom)
layernew.CreateFeature(feat)
newds.Destroy()

# 创建多边形数据集
from osgeo import ogr
import os,math
driver = ogr.GetDriverByName("ESRI Shapefile")

extfile = 'woeld_borders.shp'
if os.access(extfile,os.F_OK):
    driver.DeleteDataSource(extfile)
    
extent=[400,1100,300,600]

newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('rect',None,ogr.wkbPolygon)
width = math.fabs(extent[1]-extent[0])
height = math.fabs(extent[3]-extent[3])
tw = width/2
th = width/2
extnew = extent[0]+tw
wkt = 'POLYGON ((%f %f %f %f %f %f %f %f %f %f ))' % (extent[0],extent[3],extent[1],extent[3],extent[1],extent[2],extent[0],extent[2],extent[0],extent[3])

geom = ogr.CreateGeometryFromWkt(wkt)
feat = ogr.Feature(layernew.GetLayerDefn())
feat.SetGeometry(geom)
layernew.CreateFeature(feat)
newds.Destroy()

# 4.3.6 OGR中属性字段定义与使用

# 在OGR中定义属性字段与赋值
from osgeo import ogr
import os,math
driver =ogr.GetDriverByName("ESRI Shapefile")

extfile = 'world_borders.shp'
if os.access(extfile,os.F_OK):
    driver.DeleteDataSource(extfile)
    
extent= [400,1100,300,600]

newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('rect',None,ogr.wkbPolygon)

fieldcnstr = ogr.FieldDefn("fd",ogr.OFTString)
fieldcnstr.SetWidth(32)
layernew.CreateField(fieldcnstr)
fieldf = ogr.FieldDefn("f",ogr.OFTReal)
layernew.CreateField(fieldf)

wkt = 'POLYGON ((%f %f %f %f %f %f %f %f %f %f ))' % (extent[0],extent[3],extent[1],extent[3],extent[1],extent[2],extent[0],extent[2],extent[0],extent[3])

geom = ogr.CreateGeometryFromWkt(wkt)
feat = ogr.Feature(layernew.GetLayerDefn())
feat.SetField('fd',"2")
feat.SetGeometry(geom)
layernew.CreateFeature(feat)
newds.Destroy()

# 定义字段的位置
extfile = 'world_borders.shp'
if os.access(extfile,os.F_OK):
    driver.DeleteDataSource(extfile)
    
newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('rect3',None,ogr.wkbPolygon)
fieldcnstr = ogr.FieldDefn('fd',ogr.OFTString)
fieldcnstr.SetWidth(36)
fieldf = ogr.FieldDefn("f",ogr.OFTReal)
laydef = layernew.GetLayerDefn()
laydef.AddFieldDefn(fieldcnstr)
laydef.AddFieldDefn(fieldf)

news.Destroy()

# 4.3.8  使用OGR创建Shapefile

ds2 = driver.CreatedataSource('test,shp')
layer2 = ds2.CreateLayer('test',geom_type=ogr.wkbPoint)

driver.DeleteDataSource('test.shp')

fieldDefn = ogr.FieldDefn('id',ogr.OFTString)
fieldDefn.SetWidth(4)
layer.CreatField(fieldDefn)

featureDefn = layer.GetLayerDefn()
feature = ogr.Feature(featureDefn)

feature.SetGeometry(point)

feature.SetField('id',23)

layer.CreateFeature(feature)


# 4.3.8

point=ogr.Geometry(ogr.wkbPOint)
point.AddPoint(10,20)






# 4.4   OGR库的一些细节

# 4.4.1  关于获取要素

import struct
from osgeo import ogr
from numpy import array  

import sys
endian_name =sys.byteorder

wkbXDR = '>'
wkbNDR = '>'

def choose(bool,a,b):
    return (bool and [a] or [b]) [0]
    
BTOR = choose(endian_name == 'little',wkbNDR,wkbNDR)

def up_endian_type(wkb):
    endian_t = struct.unpack('b',wkb[0]) [0]
    endian = choose(endian_t,'<','>')
    wkbtype=struct.unpack(endian+'I',wkb[1:5])[0]
    return endian,wkbtype,endian_t
    
def up_len(wkb,beg,endian):
    return struct.unpack(endian+'I',wkb[beg:beg+4]) [0]
    
def up_point(wkb):
    endian,wkbtype,et=up_endian_type(wkb)
    points = struct.unpack(endian+"2d",wkb[5:])
    return points
    
def up_point(wkb):
    endian,wkbtype,et=up_endian_type(wkb)
    length = up_len(wkb,5,endian)
    points = array('d',wkb[9:9+lenght*16])
    if endian != BTOR:points.byteswap()
    return points
    
def up_point(wkb):
    points=[]
    ptr = 0
    for i in range(ringcount):
        lenghth = up_len(wkb,ptr,endian)
        ps = array('d',wkb[ptr+4:ptr+4+length*16])
        if endian != BTOR : byteswap()
        points.append(ps)
        ptr += 4+length*16
    return points,ptr
    
def up_polygon(wkb,sub=-1):
    if sub == -1:
        ringcount = up_len(wkb,5,endian)
        points = up_linearring(wkb[9:],ringcount,endian)[0]
        return points
    else:
        points =[]
        ptr = 5
        ringcount = up_len(wkb,ptr,endian)
        ps,ringlen = up_linearring(wkb[ptr+4:],ringcount,endian)
        points.append(ps)
        ptr += 4+ringlen
        return points,ptr
        
def up_mpoint(wkb):
    endian,wkbtype,et=up_endian_type(wkb)
    subcount = up_len(wkb,5,endian)
    points = []
    ptr =9
    for i in range(subcount):
        subps = up_point(wkb[ptr:])
        points.append(subps)
        ptr += 9+len(subps)*8
    return points
    
def up_mlinestring(wkb):
    endian,wkbtype,et=up_endian_type(wkb)
    subcount = up_len(wkb,5,endian)
    points = []
    ptr =9
    for i in range(subcount):
        subps = up_point(wkb[ptr:])
        points.append(subps)
        ptr += 9+len(subps)*8
    return points
    
def up_mpolygon(wkb):
    endian,wkbtype,et=up_endian_type(wkb)
    subcount = up_len(wkb,5,endian)
    points = []
    ptr =9
    for i in range(subcount):
        subps,size = up_polygon(wkb[ptr:],i)
        points.append(subps)
        ptr += size
    return points
    
fun_map = {
        ogr.wkbPoint : up_point,
        ogr.wkbLineString : up_linestring,
        ogr.wkbPolygon : up_polygon,
        ogr.wkbMultipoint : up_mpoint,
        ogr.wkbMultiLineString : up_mlinestring,
        ogr.wkbMultiPolyon : up_mpolygon
        }
        
def WkbUnPacker(wkb):
    endian,wkbtype,et=up_endian_type(wkb)
    foo = fun_map[wkbtype]
    points = foo(wkb)
    return [endian_t,wkbtype,points]
    
if __name__  == "__main__":
    import time 
    ds = ogr.Open("world_borders.shp")
    layer =ds.GetLayer()
    begt = time.time()
    
    featture = layer.GetNextFeature()
    
    while feature is not None:
        geom = feature .GetGeometryRef()
        wkb = geom.ExportToWkt()
        wkbarr = WkbUnPacker(wkb)
        feature = layer.GetNextFeature()
    print time.time()-begt
    
# 4.4.2 OGR中国层概念的深入理解

import os
import math
from osgeo import ogr
driver = ogr.GetDriverByName("ESRI Shapefile")
extfile = 'world_borders.shp'
if os.access(extfile,os.F_OK):
    driver.DeleteDataSource(extfile)
newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('rectkkk',None,ogr.wkbPolygon)
extent=[0,0,300,300]
tw = 100
th= 100
wkt = 'POLYGON ((%f %f %f %f %f %f %f %f %f %f ))' % (extent[0],extent[3],extent[0]+tw,extent[3],extent[0]+tw,extent[3]-th,extent[0],extent[3]-th,extent[0],extent[3])
print(wkt)
geom = ogr.CreateGeometryFromWkt(wkt)
feat = ogr.Feature(layernew.GetLayerDefn())
feat.SetGeometry(geom)
feat.SetField('rectnnn',None)                                              )
feat.SetField('f',127,546)
layernew.CreateFeature(feat)
newds.Destroy()
ds = ogr.Open('world_borders.shp')
print(ds.GetLayerCount())
layer = ds.GetLayer(0)
print(layer.GetName())
layer = ds.GetLayerByName('rectkkk')


# 4.4.3生成多层Layer

import os
import math
from osgeo import ogr
driver = ogr.GetDriverByName("ESRI Shapefile")
extfile = 'world_borders.shp'
if os.access(extfile,os.F_OK):
    driver.DeleteDataSource(extfile)
newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('rectkkk',None,ogr.wkbPolygon)
extent=[0,0,300,300]
tw = 100
th= 100
wkt = 'POLYGON ((%f %f %f %f %f %f %f %f %f %f ))' % (extent[0],extent[3],extent[0]+tw,extent[3],extent[0]+tw,extent[3]-th,extent[0],extent[3]-th,extent[0],extent[3])
print(wkt)
geom = ogr.CreateGeometryFromWkt(wkt)
feat = ogr.Feature(layernew.GetLayerDefn())
feat.SetGeometry(geom)
layernew.CreateFeature(feat)
layernew2 = newds.CreateLayer('rectaaa',None,ogr.wkbPoint)
wktp = 'POINT (%f %f)' % (70.4,220.34)
geom2 = ogr.CreateGeometryFromWkt(wktp)
feat2 = ogr.Feature(layernew2.GetLayerDefn())
feat2.SetGeometry(geom2)
layernew2.CreateFeature(feat2)
newds.Destroy()




import os 
import math
from osgeo import ogr
driver = ogr.GetDriverByName("MapInfo File")
extfile = 'mi.tab'
if os.access(extfile,os.F_OK):
    driver.DeleteDataSource(extfile)
newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('mi.tab',None,ogr.wkbPolygon)
fieldid = ogr.FieldDefn('FID',ogr.OFTInteger)
layernew.CreateField(fieldid)
extent=[0,0,300,300]
tw = 100
th = 100
wkt = 'POLYGON ((%f %f %f %f %f %f %f %f %f %f ))' % (extent[0],extent[3],extent[0]+tw,extent[3],extent[0]+tw,extent[3]-th,extent[0],extent[3]-th,extent[0],extent[3])
print(wkt)
geom = ogr.CreateGeometryFromWkt(wkt)
feat = ogr.Feature(layernew.GetLayerDefn())
feat.SetGeometry(geom)
layernew.CreateFeature(feat)
layernew2 = newds.CreateLayer('mitabaaa',None,ogr.wkbPoint)
fieldid2 = ogr.FieldDefn('FID',ogr.OFTInteger)
layernew2.CreateField(fieldid2)
wktp = 'POINT (%f %f)' % (70.4,220.34)
geom2 = ogr.CreateGeometryFromWkt(wktp)
feat2 = ogr.Feature(layernew2.GetLayerDefn())
feat2.SetGeometry(geom2)
layernew2.CreateFeature(feat2)
newds.Destroy()




from osgeo import ogr,os,math
ogr.GetDriver
driver = ogr.GetDriverByName("ESRI Shapefile")
extfile = 'mi'
if os.access(extfile,os.F_OK):
    driver.DeleteDataSource(extfile)
newds = driver.CreateDataSource(extfile)
layernew = newds.CreateDataLayer('mitab',None,ogr.wkbPolygon)
fieldid = ogr.FieldDefn('FID',ogr.OFTInterger)
layernew.CreateField(field)
extent=[0,0,300,300]
tw = 100
th = 100
wkt = 'POLYGON ((%f %f %f %f %f %f %f %f %f %f ))' % (extent[0],extent[3],extent[0]+tw,extent[3],extent[0]+tw,extent[3]-th,extent[0],extent[3]-th,extent[0],extent[3])
print(wkt)
geom = ogr,CreateGeometryFromwkt(wkt)
feat = ogr.Feature(layernew.GetLayerDefn())
feat.SetGeometry(geom)
layernew.CreateFeature(feat)
wktp = 'POINT (%f %f)' % (70.4,220.34)
geom2 = ogr.CreateGeometryFromWkt(wktp)
feat2 = ogr.Feature(layernew2.GetLayerDefn())
feat2.setGeometry(geom2)
layernew2.CreateFeature(feat2)
newds.Destroy()






# 4.5过滤器




# 4.5.1根据属性条件选择要素
from osgeo import ogr
import os
shpfile = 'world_borders.shp'
ds = ogr.Open(shpfile)
layer = ds.GetLayer(0)
lyr_count= layer.GetFeatureCount()
print(lyr_count)
layer.SetAttributeFilter("AREA > 800000")
lyr_count= layer.GetFeatureCount()
print(lyr_count)

# 根据属性条件生成要素
driver = ogr.GetDriverByName("ESRI Shapefile")
extfile = 'world_borders.shp'
if os.access(extfile,os.F_OK):
    driver.DeleteDataSource(extfile)
newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('rect',None,ogr.wkbPolygon)
feat = layer.GetNextFeature()
while feat is not None:
    layernew.createFeature(feat)
    feat = layer.GetNextFeature()
newds.Destroy()

# 4.5.2空间过滤器Spatial filters
import os 
from osgeo import ogr
def create_shp_by_layer(shp,layer):
    outputfile = shp
    if os.access(outputfile,os.F_OK):
        driver.DeleteDataSource(outputfile)
        newds = driver.CreateDataSource(outputfile)
        pt_layer = newds.CopyLayer(layer,'')
        newds.Destroy()
        
driver = ogr.GetDriverByName("ESRI Shapefile")
world_shp ='world_borders.shp'
cover_shp= 'world_borders.shp'
world_ds = ogr.Open(world_shp)
cover_ds = ogr.Open(cover_shp)
world_layer =world_ds.GetLayer(0)
cover_layer = cover_ds.GetLayer(0)
print(world_layer.GetFeatureCount())
cover_feats = cover_layer.GetNextFeature()

poly = cover_feats.GetGeometryRef()
world_layer.SetSpatialFilter(poly)
print(type(world_layer))
out_shp = 'sel_res.shp'
create_shp_by_layer(out_shp,world_layer)

world_layer.SetSpatialFilterRect(50,60,25,35)
print(world_layer.GetFeatureCount())

out_shp ='world_borders.shp'
create_shp_by_layer(out_shp,world_layer)


# 4.5.3在OGR中使用SQL语句进行查询

import os
from osgeo import ogr
def create_shp_by_layer(shp,layer):
    outputfile = shp
    if os.access(outputfile,os.F_OK):
        driver.DeleteDataSource(outputfile)
    newds = driver.CreateDataSource(outputfile)
    pt_layer = newds.CopyLayer(layer,'')
    newds.Destroy()

driver = ogr.GetDriverByName("ESRI Shapefile")
world_shp = 'world_borders.shp'
world_ds = ogr.Open(world_shp)
world_layer = world_ds.GetLayer()
world_layer_name = world_layer.GetName()
print(world_layer.GetFeatureCount())
result = world_ds.ExecuteSQL("select * from %s where AREA > 100000 order by AREA desc" % (world_layer_name))

resultFeat = result.GetNextFeature()
while resultFeat:
    print(resultFeat.GetField('AREA'))
    resultFeat = result.GetNextFeature()

out_shp = 'xx_world_borders.shp'
create_shp_by_layer(out_shp,result)
world_ds.ReleaseResultSet(result)


# 4.5.4 应用(待定)
result = dsSites.ExecuteSQL("select count(*) from sites where cover = 'grass'")
result.GetFeatureCount()
result.GetFeature(0).GetFiled(0)
dsSite.ReleaseResultSet(result)

result = ds.ExecuteSQL("select distinct from sites")
resultFeat = result.GetNextFeature()
while resultFeat:
    print(resultFeat.GetField(0))
    resultFeat = result.GetNextFeature()
ds.ReleaseResultSet(result)

coverLayer = ds.ExecuteSQL('select distinct  cover from sites')
coverFeat = coverLayer.GetNextFeature()
while coverFeat:
    cntLayer = ds.ExecuteSQL("select count(*) from sites where cover = ' " + coverFeat.GetField(0) + " ' ")
    print(coverFeat.GetField(0) + ' ' + print(coverFeat.Getfield(0) + ' ' +  cntLayer.GetFeature(0).GetFieldAsString(0)
    ds.ReleaseResultSet(cntLayer)
    coverFeat = coverLayer.GetNextFeature()
ds.ReleaseResultSet(coverLayer)


