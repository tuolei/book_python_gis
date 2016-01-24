4.2使用GDAL获取栅格数据集信息

4.2.1开始使用GDAL

导入GDAL
早期的版本（1.5以前），用下面的语句导入
import gdal
1.6以后：
from osgeo import gdal
为了保持兼容性，用下面的语句导入
try：
    import gdal
except:
    from oegeo import gdal

驱动

注册 栅格数据
gdal.AllRegister()
driver = gdal.GetDriverByName('HFA')
driver.Register()
判断deiver是否注册成功
gdal.AllRegister()
driver = gdal.GetDriverByName('HFA')
driver.Register()
driver = gdal.GetDriverByName('GeoTiff')
driver == None


查看系统支持的数据模式
from osgeo import gdal
drv_count = gdal.GetDriverCount()
for idx in range(drv_count):
    driver = gdal.GetDriver(idx)
    print("%10s:%s" % (driver.ShortName,driver.LongName))

4.2.2打开已有的GeoTIF文件
打开一个数据集
from osgeo import gdal
dataset = gdal.Open("m510121.tif")
dir(dataset)

4.2.3读取遥感影像的信息

读取影响的元数据
from osgeo import gdal
dataset = gdal.Open("m510121.tif")
dataset.GetMetadata()

GetDescription()获得栅格的描述信息
from osgeo import gdal
dataset = gdal.Open("m510121.tif")
dataset.GetDescription()

获取栅格数目
from osgeo import gdal
dataset = gdal.Open("m510121.tif")
dataset.RasterCount

影像大小
img_width,img_height = dataset.RasterXSize,dataset.RasterYSize
img_width,img_height

获得空间参考
dataset.GetGeoTransform()

获得投影信息
dataset.GetProjection()


4.2.4使用GDAL获取栅格数据波段信息

获取数据集的波段
from osgeo import gdal
dataset = gdal.Open("m510121.tif")
dataset.RasterCount
band=dataset.GetRasterBand(1)

查看波段的基本信息
band=dataset.GetRasterBand(1)
dir(band)

获取波段的大小
band.XSize
band.YSize
band.DataType

获取波段数据的属性
band.GetNoDataValue()
band.GetMaximum()
band.GetMinimum()
band.ComputeRasterMinMax()


4.3访问波段中的数据

4.3.1波段数据类型
from osgeo import gdalconst
dir(gdalconst)

band.DataType

4.3.2访问数据集的数据

from osgeo import gdal
dataset= gdal.Open("m510121.tif")
help(dataset.ReadRaster)
help(dataset.ReadAsArray)

4.3.3读取波段中的数据

ReadRaster()的函数细节
from osgeo import gdalconst
from osgeo import gdal
from gdalconst import *
dataset = gdal.Open("m510121.tif")
band = dataset.GetRasterBand(1)
band.ReadAsArray(100,100,5,5,100,100)

ReadAsArray的原型
help(band.ReadAsArray)

栅格数据范围的处理
band.XSize
band.YSize
band.ReadAsArray(95,100,5,5)

4.3.4读取栅格数据的方式和效率
from osgeo import gdal
import time
dataset = gdal.Open("m510121.tif")
band = dataset.GetRasterBand(1)
width=dataset.RasterXSize
height= dataset.RasterYSize
bw=128
bh= 128
bxsize = width/bw
bysize = width/bh
band.ReadAsArray(0,0,width,height)
start = time.time()
band.ReadAsArray(0,0,width,height)
print (time.time()-start)
start2 = time.time()
for i in range(bysize):
    for j in range(bxsize):
        band.ReadAsArray(bw*j,bh*i,bw,bh)
print (time.time()-start2)
start3 = time.time()
for j in range(bxsize):
    for i in range(bysize):
        band.ReadAsArray(bw*j,bh*i,bw,bh)
print (time.time()-start3)

4.3.5地图代数
from osgeo import gdal
import numpy
dataset = gdal.Open("m510121.tif")
band2 = dataset.GetRasterBand(2)
band3 = dataset.GetRasterBand(3)
cols = 100
rows = 100
data2 = band2.ReadAsArray(0,0,rows).astype(numpy.float16)
data3 = band3.ReadAsArray(0,0,rows).astype(numpy.float16)
mask = numpy.greater(data2 + data3,0)
ndvi = numpy.choose(mask,(-99,(data3-data2)/(data3+data2)))
mask = numpy.greater(data2 + data3,0)
ndvi = numpy.choose(mask,(-99,(data3-data2)/(data3+data2)))



4.4颜色空间与调色板

4.4.3  ColorMap颜色定义
from osgeo import gdal
dataset = gdal.Open("m510121.tif")
band = dataset.GetRasterBand(1)
colormap = band.GetRasterColorTable()
colormap.GetPaletteInterPretation()
colormap.Getcount()

4.4.4访问索引图像中的数据


4.5创建与保存栅格数据

from osgeo import gdal
format = "GTiff"
driver = gdal.GetDriverByName(format)
matedata = driver.GetMetadata()

4.5.1使用CreateCopy函数创建影像
import gdal
src_filename = "m510101.tif"
dst_filename = "m510101_copy.tif"
src_ds = gdal.Open(src_filename)
dst_ds = driver.CreateCopy(dst_filename,src_ds,0)

dst_filename2 = "m510101_copy2.tif"
dst_ds = driver.CreateCopy(dst_filename2,src_ds,0,['TILED = YES','COMPRESS=PACKBITS'])

dst_filename3 = "m510121_copy3.tif"
dst_ds = driver.CreateCopy(dst_filename3,src_ds,0,['TILED = YES','COMPRESS=PACKBITS'])

4.5.2使用Create函数创建影像(有问题)

import gdal
driver = gdal.GetDriverByName('GTiff')
dst_filename =  'tmp.tif'
dst_ds = driver.Create(dst_filename,512,512,1,gdal.GDT_Byte)


import numpy,osr
dst_ds.SetGeoTransform([444720,30,0,3751320,0,-30])
srs = osr.SpatialReference()
srs.SetUTM(11,1)
srs.SetWellKnownGeogCS('NAD27')
dst_ds.SetProjection(srs.ExportToWkt())
raster = numpy.zeros((512,512))
dst_ds.GetRasterBand(1).WriteArray(raster)


4.5.3创建多波段图像

创建3波段GTiff的例子，多波段影像的创建方式与之类似
from osgeo import gdal
import numpy
dataset = gdal.Open("m510101.tif")
width = dataset.RasterXSize
height = dataset.RasterYSize
datas = dataset.ReadAsArray(0,0,width,height)

driver = gdal.GetDriverByName("GTiff")
tods = driver.Create("M51C004002.tif",width,height,3,options=["INTERLEAVE=PIXEL"])
tods.WriteRaster(0,0,width,height,datas.tostring(),width,height,band_list=[1,2,3])
  
向tods写入数据时，需要转换数据类型datas.tostringa().如果需要读取数据，使用下面的数据：
datas = dataset.ReadData(0,0,width,height)  -------------------------------------------------------------------------------------    
    
分波段处理
datas = []
for i in range(3):
    band = dataset.GetRasterBand(i+1)
    data = band.ReadAsArray(0,0,width,height)
    datas.append(Numpy.reshape(data,(1,-1)))
    atas = Numpy.conceteate(datas)  
    

4.5.4 

GDAL写操作的其他问题
import osr
tods.SetGeoTransform([444720,30,0,3751320,0,-30])
srs = osr.SpatiaReference()
srs.SetUTM(11,1)
srs.SetWellKownGeogCS('m510101.tif')
tods.setProjection(srs.ExportTowkt())

4.5.6逐块处理

GDAL对影像进行逐块处理方法
xBlocksize = 64
yBlocksize = 64
for i in range(0,rows,yBlockSize):
    if i + yBlockSize < rows:
        numRows = yBlockSize
    else:
        numRows = rows - i
for j in range(0,cols,xBlockSize）:
    if j + xBlockSize < cols:
        numRows = xBlockSize
    else:
        numCols = cols - j
data = band.ReadAsArray(j,i,numCols,numRows)

outBand.WriteArray(outdate,j,i)


4.6 GDAL 其它问题
4.6.1 GDAL和Pillow的互操作

使用GDAL读取数据
from osgeo import gdal
dataset = gdal.Open("m510101.tif")
dataz_arr = dataset.ReadAsArray(30,70,5,5)
type(data_arr)
data_arr

data_arr.tostring()

使用Pillow获取数据
from PIL import Image
im = Imamg.open('m510101.tif')
region = im.corp((30,70,35,75))
region.tostring()


import numpy as np
data = dataset.ReadAsArray(30,70,5,5)
datas = [i for i in data]
from numpy import reshape
datas = [reshape(i,(-1,1)) for i in data]
datas = np.concatenate(datas,1)
datas.tostring()

从波段看
r,g,b = region.split()
r.tostring()
band = dataset.getRasterBand(1)
band.ReadRaster(30,70,5,5)


 从写数据来看
help(dataset.WriteRaster)
help(band.WriteRaster)
help(band.WriteArray)
  
  
PIL中对数据的写入用的是paste
help(im.paste)
PIL 还有个好东西----fromstring
help(Image.fromstring)


help(im.paste)
help(Image.fromstring)



























获取数据集的波段
from osgeo import gdal
dataset = gdal.Open("M51C004002.tif")
dataset.RasterCount
band = dataset.GetRasterBand(3)


查看波段的基本信息
from osgeo import gdal
dataset = gdal.Open("M51C004002.tif")
band = dataset.GetRasterBand(3)
dir(band)

 
 
 获取波段的大小
band.XSize
band.YSize
band.DataType



获取波段数据的属性
band.GetNoDataValue()
band.GetMaximum()
band.GetMinimum()
band.ComputeRasterMinMax()



