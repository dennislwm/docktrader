#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.path


# In[2]:


import backtrader as bt
bt.__path__


# In[3]:


import sys
get_ipython().system('{sys.executable} -m pip install backtrader[plotting]')


# In[4]:


import sys
get_ipython().system('{sys.executable} -m pip install pyEX')
import pyEX
import json
import os
strRoot='D:\\denbrige\\180 FxOption\\103 FxOptionVerBack\\083 FX-Git-Pull\\14docktrader\\config\\'
with open(strRoot + 'iex.conf') as fJsn:
    jsnIEX = json.load(fJsn)
strVersion = 'v1'
objEx = pyEX.Client(api_token=jsnIEX['iextoken'], version=strVersion)
objEx.companyDF('AAPL')


# In[5]:


objEx.earningsDF('AAPL')


# In[29]:


# unfortunately, pyex has the same issue as iexfinance where you cannot retrieve past historical earnings, cf, bs

