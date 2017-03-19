# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 20:57:17 2017

@author: lkejji
"""
import international_trade as itrade
months=["01","02","03","04","05","06","07","08","09","10","11","12"]
#months=["01","02","03"]
years=["2016"]

exports=itrade.download_censusInternationalTradeData_exports(years,months)
imports=itrade.download_censusInternationalTradeData_imports(years,months)

##save data in csv files
itrade.save(exports,"exports")
itrade.save(imports,"imports")


## Compare current data to archived data

#lastupdate=itrade.get_LastRevisionDate("http://www.census.gov/data/developers/data-sets/international-trade.html")
#if itrade.is_different(lastupdate):
    #itrade.store_changes()
