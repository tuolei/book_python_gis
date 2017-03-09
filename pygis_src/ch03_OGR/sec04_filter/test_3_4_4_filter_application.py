# # -*- coding: utf-8 -*-
# import os
#
# from osgeo import ogr
#
# os.chdir('/home/liujx/gdata')
#
# result = dsSites.ExecuteSQL("select count(*) from sites where cover = 'grass'")
# result.GetFeatureCount()
# result.GetFeature(0).GetFiled(0)
# dsSite.ReleaseResultSet(result)
#
# result = ds.ExecuteSQL("select distinct from sites")
# resultFeat = result.GetNextFeature()
# while resultFeat:
#     print(resultFeat.GetField(0))
#     resultFeat = result.GetNextFeature()
# ds.ReleaseResultSet(result)
#
# coverLayer = ds.ExecuteSQL('select distinct  cover from sites')
# coverFeat = coverLayer.GetNextFeature()
# while coverFeat:
#     cntLayer = ds.ExecuteSQL("select count(*) from sites where cover = ' " + coverFeat.GetField(0) + " ' ")
#     print(coverFeat.GetField(0) + ' ' + print(coverFeat.Getfield(0) + ' ' +  cntLayer.GetFeature(0).GetFieldAsString(0)
#     ds.ReleaseResultSet(cntLayer)
#     coverFeat = coverLayer.GetNextFeature()
# ds.ReleaseResultSet(coverLayer)
