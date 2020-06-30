#!/usr/bin/env python
# coding: utf-8

# In[11]:


import json
import os
print(os.getcwd())
strRoot='D:\\denbrige\\180 FxOption\\103 FxOptionVerBack\\083 FX-Git-Pull\\14docktrader\\config\\'
with open(strRoot + 'iex.conf') as fJsn:
    jsnIEX = json.load(fJsn)
from iexfinance.stocks import Stock
objAapl = Stock("AAPL", output_format='pandas', token=jsnIEX['iextoken'])
objAapl.get_company()


# In[10]:


objAapl.get_insider_summary()


# In[4]:


objAapl.get_news()


# In[ ]:




