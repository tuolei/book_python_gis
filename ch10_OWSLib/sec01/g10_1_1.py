from owslib.wms import WebMapService

wms = WebMapService('http://wms.jpl.nasa.gov/wms.cgi', version='1.1.1')
print(wms.identification.type)
print(wms.identification.title)
print(list(wms.contents))
