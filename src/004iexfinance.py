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


# In[12]:


import json
import os
print(os.getcwd())
strRoot='D:\\denbrige\\180 FxOption\\103 FxOptionVerBack\\083 FX-Git-Pull\\14docktrader\\config\\'
with open(strRoot + 'iex.conf') as fJsn:
    jsnIEX = json.load(fJsn)


# In[4]:


import sys
get_ipython().system('{sys.executable} -m pip install --upgrade pip')
get_ipython().system('{sys.executable} -m pip install iexfinance')
from iexfinance.stocks import Stock
objAapl = Stock("AAPL", output_format='pandas', token=jsnIEX['iextoken'])
objAapl.get_balance_sheet()


# In[ ]:




