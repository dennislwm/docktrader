#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
get_ipython().system('{sys.executable} -m pip install wget')
import wget
import pandas as pd
import os
import datetime
import csv
import xlrd
import pandas as pandas 


# In[6]:


# list of tickers to be processed
def GetStockTicker():
    strTicker = []
    strInput = input("Do you want to load sp500_constituents (y/n)?: ")
    if strInput in ('y', 'Y'):
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
    elif strInput in ('n', 'N'):
        strInput = input("Enter ticker(s) delimited by comma: ")
        for ticker in strInput.split(','):
            strTicker.append(ticker)
    else:
        print("Error: User response undefined")
    return strTicker


# In[7]:


def StockRowExcel(ticker, strExcelFile, objRow):
    dfSheet=pandas.read_excel(strExcelFile,sheet_name=ticker)
    if type(objRow) == int:
        print(dfSheet.iloc[objRow,:])
    else:
        print(dfSheet.loc[dfSheet.iloc[:,0] == objRow].transpose())


# In[8]:


def PieceStockTicker(ticker, save_location):
    # assert ticker is not empty
    if len(strTicker) == 0:
        return
    
    today = datetime.datetime.today()
    # files are saved to subfolder "yyyymm", since fundamental data doesn't change regularly, 
    # we download files to monthly folders, e.g. 202001 for January 2020
    path = save_location + '%02d' % today.year + '%02d' % today.month + '/'
    
    print('Reading excel files from ' + path)
    for i in ticker:
        #create the folder in which all of the dowloads will be saved
        if not os.path.exists(path):
            os.makedirs(path)
        print('Processing ' + i)
        #skip if ticker exists
        if os.path.exists(path + i + '_Annual_Incomestatement.xlsx') == True:
            #location of income statement
            Income_url = 'https://stockrow.com/api/companies/' + i + '/financials.xlsx?dimension=A&section=Income%20Statement&sort=desc'
            #read the income statement from specified location
            StockRowExcel(i, path + i + '_Annual_Incomestatement.xlsx', 'Revenue')
            StockRowExcel(i, path + i + '_Annual_Incomestatement.xlsx', 'EPS (Diluted)')
                
        if os.path.exists(path + i + '_Annual_BalanceSheet.xlsx') == True:
            #location of balance sheet
            Balance_url = 'https://stockrow.com/api/companies/' + i + '/financials.xlsx?dimension=A&section=Balance%20Sheet&sort=desc'
                
        if os.path.exists(path + i + '_Annual_StatementofCashFlows.xlsx') == True:
            #location of cash flows
            Cash_url = 'https://stockrow.com/api/companies/' + i + '/financials.xlsx?dimension=A&section=Cash%20Flow&sort=desc'
            #read the cash flows from specified location
            StockRowExcel(i, path + i + '_Annual_StatementofCashFlows.xlsx', 'Operating Cash Flow')
                
        if os.path.exists(path + i + '_Annual_Metrics.xlsx') == True:
            Metrics_url = 'https://stockrow.com/api/companies/' + i + '/financials.xlsx?dimension=A&section=Metrics&sort=desc'
            #read the metrics from specified location
            StockRowExcel(i, path + i + '_Annual_Metrics.xlsx', 'Free Cash Flow per Share')
            StockRowExcel(i, path + i + '_Annual_Metrics.xlsx', 'ROE')
            StockRowExcel(i, path + i + '_Annual_Metrics.xlsx', 'Debt/Equity')
            StockRowExcel(i, path + i + '_Annual_Metrics.xlsx', 'Market Cap')
            StockRowExcel(i, path + i + '_Annual_Metrics.xlsx', 'P/E ratio')
            StockRowExcel(i, path + i + '_Annual_Metrics.xlsx', 'P/B ratio')
            StockRowExcel(i, path + i + '_Annual_Metrics.xlsx', 'Dividend Yield')
                
    print('Excel Files Processed')


# In[9]:


strTicker = GetStockTicker()
print('No. of tickers:', len(strTicker))
PieceStockTicker(strTicker, save_location = 'd:/denbrige/180 FxOption/103 FxOptionVerBack/083 FX-Git-Pull/14winpython/notebooks/stockrow/')


# In[ ]:




