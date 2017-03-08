from osgeo import gdal

format = "GTiff"
driver = gdal.GetDriverByName(format)
metadata = driver.GetMetadata()
if gdal.DCAP_CREATE in metadata and metadata[gdal.DCAP_CREATE] == 'YES':
    print('Driver %s supports Creat() method.' % format)
if gdal.DCAP_CREATE in metadata and metadata[gdal.DCAP_CREATECOPY] == 'YES':
    print('Driver %s supports CreatCOPY() method.' % format)
