'''
Created on Feb 13, 2017

@author: kejji
'''

import pandas as pd
#import requests
#from bs4 import BeautifulSoup
#from datetime import datetime
import numpy as np

## returns dataframe with the data needed exports
def download_censusInternationalTradeData_exports(years,months):
    #df=pd.DataFrame(columns=['DISTRICT','DIST_NAME','E_COMMODITY','ALL_VAL_MO','ALL_VAL_YR','VES_VAL_MO','VES_VAL_YR','YEAR','MONTH'])
    d=[]
    for year in years:
        for month in months:
            url="http://api.census.gov/data/timeseries/intltrade/exports?get=CTY_CODE,CTY_NAME,ALL_VAL_MO&YEAR="+year+"&MONTH="+month+""
            df = pd.read_json(url)
            df.columns=["CTY_CODE","CTY_NAME","ALL_VAL_MO","YEAR","MONTH"]
            df=df.replace("","nodata")
            df=df.drop(0)
            d.append(df)
            #df3=df3.drop(0)
            #d2f=df2.drop(1)
        d=pd.concat(d, axis=0)
    return d

## returns dataframe with the data needed imports
def download_censusInternationalTradeData_imports(years,months):
    #df=pd.DataFrame(columns=['DISTRICT','DIST_NAME','E_COMMODITY','ALL_VAL_MO','ALL_VAL_YR','VES_VAL_MO','VES_VAL_YR','YEAR','MONTH'])
    d=[]
    for year in years:
        for month in months:
            url="http://api.census.gov/data/timeseries/intltrade/imports?get=CTY_CODE,CTY_NAME,GEN_VAL_MO&YEAR="+year+"&MONTH="+month+""
            df = pd.read_json(url)
            df.columns=["CTY_CODE","CTY_NAME","GEN_VAL_MO","YEAR","MONTH"]
            df=df.replace("","nodata")
            df=df.drop(0)
            d.append(df)
            #df3=df3.drop(0)
            #d2f=df2.drop(1)
        d=pd.concat(d, axis=0)
    return d
    
def save(df,filename):
    df=df.pivot_table(df,index=["CTY_CODE","CTY_NAME","YEAR"],columns="MONTH",aggfunc=np.sum,fill_value=0)
    df.to_csv(filename+".csv")
