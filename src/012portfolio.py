#!/usr/bin/env python
# coding: utf-8

# In[16]:


import sys
print(sys.version)
get_ipython().system('{sys.executable} -m pip install --upgrade pip')
get_ipython().system('{sys.executable} -m pip install iexfinance')
get_ipython().system('{sys.executable} -m pip install --no-deps empyrical')
get_ipython().system('{sys.executable} -m pip install --no-deps pandas-datareader')
get_ipython().system('{sys.executable} -m pip show scipy')
get_ipython().system('{sys.executable} -m pip install pyfolio')
from datetime import datetime
from iexfinance.stocks import get_historical_data
from iexfinance.stocks import Stock
import numpy as numpy
import pandas as pandas
try:
    import google.colab
    IN_COLAB = True
    print("The package pyfolio works in Google Colab, but not in WinPython")
except:
    IN_COLAB = False
if (IN_COLAB):
    import pyfolio as pyfolio
else:
    print("pyfolio not installed")


# In[17]:


# get iextoken
import json
import os
print(os.getcwd())
def GetIexToken():
    strRoot='D:\\denbrige\\180 FxOption\\103 FxOptionVerBack\\083 FX-Git-Pull\\14docktrader\\config\\'
    strToken=''
    try:
        with open(strRoot + 'iex.conf') as fJsn:
            jsnIEX = json.load(fJsn)
        strToken=jsnIEX['iextoken']
        print("Found IEX Token from config")
    except:
        strToken=input("Enter IEX Token: ")
    return strToken
strToken=GetIexToken()


# In[18]:


# list of tickers to be processed
def GetStockTicker(blnSp500=False):
    strTicker = []
    if blnSp500 == True:
        strStockFile = "stockrow/sp500_constituents.csv"
        if os.path.exists(strStockFile) == True:
            file=open(strStockFile, "r")
            reader = csv.reader(file)
            #skip header
            next(reader) 
            for line in reader:
                strTicker.append(line[0])
        else:
            print("Error: " + strStockFile + " undefined")
    else:
        strInput = input("Enter ticker(s) delimited by comma: ")
        for ticker in strInput.split(','):
            strTicker.append(ticker)
    return strTicker

def IexStockAsset(ticker):
    # assert ticker is not empty
    if len(ticker) == 0:
        return
    
    start=datetime(2019, 2, 9)
    end=datetime(2020,2,11)
    
    dfRet = pandas.DataFrame(columns=ticker)
    
    for i in ticker:
        ohlc = get_historical_data(i, start, end, output_format='pandas', token=strToken)
        ohlc.columns=["Open", "High", "Low", i, "Volume"]
        dfRet[i] = ohlc[i]
        
    return dfRet


# In[19]:


strTicker = GetStockTicker()
print('No. of tickers:', len(strTicker))
dfRisky = IexStockAsset(strTicker)
dfReturns = dfRisky.pct_change().dropna()
print(dfReturns)
intRisky = len(strTicker)
print(intRisky)
dblWeights = intRisky * [1 / intRisky]
PortfolioReturns = pandas.Series(numpy.dot(dblWeights, dfReturns.T), index=dfReturns.index)
print(dfReturns.T)
print(PortfolioReturns)
pyfolio.create_simple_tear_sheet(PortfolioReturns)


# In[ ]:




