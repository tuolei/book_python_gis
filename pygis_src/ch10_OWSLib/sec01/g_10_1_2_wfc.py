# -*- coding: utf-8 -*-

from owslib.wfs import WebFeatureService

wfs11 = WebFeatureService(url='http://geoserv.weichand.de:8080/geoserver/wfs', version='1.1.0')
print(wfs11.identification.title)

[print(operation.name) for operation in wfs11.operations]

print(list(wfs11.contents))

response = wfs11.getfeature(typename='bvv:gmd_ex', bbox=(4500000, 5500000, 4500500, 5500500),
                            srsname='urn:x-ogc:def:crs:EPSG:31468')

out = open('/tmp/data.gml', 'wb')
out.write(bytes(response.read(), 'UTF-8'))
out.close()
