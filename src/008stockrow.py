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


# In[2]:


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


# In[3]:


# https://stockrow.com/api/companies/AAPL/financials.xlsx?dimension=A&section=Income%20Statement&sort=desc
def StockRowPull(ticker, save_location):
    # assert ticker is not empty
    if len(strTicker) == 0:
        return
    
    today = datetime.datetime.today()
    # files are saved to subfolder "yyyymm", since fundamental data doesn't change regularly, 
    # we download files to monthly folders, e.g. 202001 for January 2020
    path = save_location + '%02d' % today.year + '%02d' % today.month + '/'
    
    print('Beginning Download to ' + path)
    for i in ticker:
        #create the folder in which all of the dowloads will be saved
        if not os.path.exists(path):
            os.makedirs(path)
        print('Processing ' + i)
        #skip if ticker exists
        if os.path.exists(path + i + '_Annual_Incomestatement.xlsx') == False:
            #location of income statement
            Income_url = 'https://stockrow.com/api/companies/' + i + '/financials.xlsx?dimension=A&section=Income%20Statement&sort=desc'
            #download the income statement to previously specified location
            try:
                wget.download(Income_url, path + i + '_Annual_Incomestatement.xlsx', bar=None)
            except:
                print('Warning: Not Found ' + i + '_Annual_Incomestatement.xlsx')
                
        if os.path.exists(path + i + '_Annual_BalanceSheet.xlsx') == False:
            #location of balance sheet
            Balance_url = 'https://stockrow.com/api/companies/' + i + '/financials.xlsx?dimension=A&section=Balance%20Sheet&sort=desc'
            #download the balance sheet
            try:
                wget.download(Balance_url, path + i + '_Annual_BalanceSheet.xlsx', bar=None)
            except:
                print('Warning: Not Found ' + i + '_Annual_BalanceSheet.xlsx')
                
        if os.path.exists(path + i + '_Annual_StatementofCashFlows.xlsx') == False:
            #location of cash flows
            Cash_url = 'https://stockrow.com/api/companies/' + i + '/financials.xlsx?dimension=A&section=Cash%20Flow&sort=desc'
            #download cash flows
            try:
                wget.download(Cash_url, path + i + '_Annual_StatementofCashFlows.xlsx', bar=None)
            except:
                print('Warning: Not Found ' + i + '_Annual_StatementofCashFlows.xlsx')
                
        if os.path.exists(path + i + '_Annual_Metrics.xlsx') == False:
            Metrics_url = 'https://stockrow.com/api/companies/' + i + '/financials.xlsx?dimension=A&section=Metrics&sort=desc'
            #download cash flows
            try:
                wget.download(Metrics_url, path + i + '_Annual_Metrics.xlsx', bar=None)
            except:
                print('Warning: Not Found ' + i + '_Annual_Metrics.xlsx')
                
    print('Files Downloaded')


# In[4]:


strTicker = GetStockTicker()
print('No. of tickers:', len(strTicker))
StockRowPull(strTicker, save_location = 'd:/denbrige/180 FxOption/103 FxOptionVerBack/083 FX-Git-Pull/14winpython/notebooks/stockrow/')


# In[ ]:




