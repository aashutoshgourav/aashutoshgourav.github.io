#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


data1=pd.read_csv(r"C:\Users\Aashutosh Gourav\Documents\STOCK ANALYSIS\RELIANCE INDUSTRIES\Quote-Equity-RELIANCE-EQ-31-03-2020-to-31-03-2021.csv")


# In[3]:


data2=pd.read_csv(r"C:\Users\Aashutosh Gourav\Documents\STOCK ANALYSIS\TCS\Quote-Equity-TCS-EQ-31-03-2020-to-31-03-2021.csv")


# In[4]:


data3=pd.read_csv(r"C:\Users\Aashutosh Gourav\Documents\STOCK ANALYSIS\HDFC BANK\Quote-Equity-HDFCBANK-EQ-31-03-2020-to-31-03-2021.csv")


# In[5]:


data4=pd.read_csv(r"C:\Users\Aashutosh Gourav\Documents\STOCK ANALYSIS\INFOSYS\Quote-Equity-INFY-EQ-31-03-2020-to-31-03-2021.csv")


# In[6]:


data5=pd.read_csv(r"C:\Users\Aashutosh Gourav\Documents\STOCK ANALYSIS\HINDUSTAN UNILEVER\Quote-Equity-HINDUNILVR-EQ-31-03-2020-to-31-03-2021.csv")


# In[7]:


data1=data1.add_prefix('RI_')
data2=data2.add_prefix('TCS_')
data3=data3.add_prefix('HDFC_')
data4=data4.add_prefix('INFY_')
data5=data5.add_prefix('HUL_')


# In[8]:


data1


# In[9]:


data2


# In[10]:


data3


# In[11]:


data4


# In[12]:


data5


# In[13]:


print("PARAMETERS:")
a=data1.columns
for i in a:
    print(i.replace("RI_",""),end="   ")


# In[14]:


data1.describe()


# In[15]:


data2.describe()


# In[16]:


data3.describe()


# In[17]:


data4.describe()


# In[18]:


data5.describe()


# # COMPARISION OF RELIANCE INDUSTRIES WITH OTHER COMPANIES

# In[19]:


data1.columns


# In[20]:


data_Reliance_TCS=pd.merge(data1,data2,how='outer',left_on='RI_SNo',right_on='TCS_SNo')


# In[21]:


def compare_PE_RT(df):
    return int(df['RI_PE Ratio']>df['TCS_PE Ratio'])
def compare_OPS_RT(df):
    return int(df['RI_OPS']>=df['TCS_OPS'])
def compare_NOPS_RT(df):
    return int(df['RI_NOPS']>=df['TCS_NOPS'])
def compare_NPM_RT(df):
    return int(df['RI_NPM']>=df['TCS_NPM'])


# In[22]:


data_Reliance_TCS['PE Compare']=data_Reliance_TCS.apply(compare_PE_RT,axis=1)
data_Reliance_TCS['OPS Compare']=data_Reliance_TCS.apply(compare_OPS_RT,axis=1)
data_Reliance_TCS['NOPS Compare']=data_Reliance_TCS.apply(compare_NOPS_RT,axis=1)
data_Reliance_TCS['NPM Compare']=data_Reliance_TCS.apply(compare_NPM_RT,axis=1)


# In[23]:


data_Reliance_TCS


# In[24]:


sns.relplot(x='RI_PE Ratio',y='TCS_PE Ratio',hue='PE Compare',data=data_Reliance_TCS)


# In[25]:


sns.relplot(x='RI_OPS',y='TCS_OPS',hue='OPS Compare',data=data_Reliance_TCS)


# In[26]:


sns.relplot(x='RI_NOPS',y='TCS_NOPS',hue='NOPS Compare',data=data_Reliance_TCS)


# In[27]:


sns.relplot(x='RI_NPM',y='TCS_NPM',hue='NPM Compare',data=data_Reliance_TCS)


# In[28]:


data_Reliance_HDFC=pd.merge(data1,data3,how='outer',left_on='RI_SNo',right_on='HDFC_SNo')


# In[29]:


def compare_PE_RH(df):
    return int(df['RI_PE Ratio']>df['HDFC_PE Ratio'])
def compare_OPS_RH(df):
    return int(df['RI_OPS']>=df['HDFC_OPS'])
def compare_NOPS_RH(df):
    return int(df['RI_NOPS']>=df['HDFC_NOPS'])
def compare_NPM_RH(df):
    return int(df['RI_NPM']>=df['HDFC_NPM'])


# In[30]:


data_Reliance_HDFC['PE Compare']=data_Reliance_HDFC.apply(compare_PE_RH,axis=1)
data_Reliance_HDFC['OPS Compare']=data_Reliance_HDFC.apply(compare_OPS_RH,axis=1)
data_Reliance_HDFC['NOPS Compare']=data_Reliance_HDFC.apply(compare_NOPS_RH,axis=1)
data_Reliance_HDFC['NPM Compare']=data_Reliance_HDFC.apply(compare_NPM_RH,axis=1)


# In[31]:


data_Reliance_HDFC


# In[32]:


sns.relplot(x='RI_PE Ratio',y='HDFC_PE Ratio',hue='PE Compare',data=data_Reliance_HDFC)


# In[33]:


sns.relplot(x='RI_OPS',y='HDFC_OPS',hue='OPS Compare',data=data_Reliance_HDFC)


# In[34]:


sns.relplot(x='RI_NOPS',y='HDFC_OPS',hue='NOPS Compare',data=data_Reliance_HDFC)


# In[35]:


sns.relplot(x='RI_NPM',y='HDFC_NPM',hue='NPM Compare',data=data_Reliance_HDFC)


# In[36]:


data_Reliance_INFY=pd.merge(data1,data4,how='outer',left_on='RI_SNo',right_on='INFY_SNo')


# In[37]:


def compare_PE_RIN(df):
    return int(df['RI_PE Ratio']>df['INFY_PE Ratio'])
def compare_OPS_RIN(df):
    return int(df['RI_OPS']>=df['INFY_OPS'])
def compare_NOPS_RIN(df):
    return int(df['RI_NOPS']>=df['INFY_NOPS'])
def compare_NPM_RIN(df):
    return int(df['RI_NPM']>=df['INFY_NPM'])


# In[38]:


data_Reliance_INFY['PE Compare']=data_Reliance_INFY.apply(compare_PE_RIN,axis=1)
data_Reliance_INFY['OPS Compare']=data_Reliance_INFY.apply(compare_OPS_RIN,axis=1)
data_Reliance_INFY['NOPS Compare']=data_Reliance_INFY.apply(compare_NOPS_RIN,axis=1)
data_Reliance_INFY['NPM Compare']=data_Reliance_INFY.apply(compare_NPM_RIN,axis=1)


# In[39]:


sns.relplot(x='RI_PE Ratio',y='INFY_PE Ratio',hue='PE Compare',data=data_Reliance_INFY)


# In[40]:


sns.relplot(x='RI_OPS',y='INFY_OPS',hue='OPS Compare',data=data_Reliance_INFY)


# In[41]:


sns.relplot(x='RI_NOPS',y='INFY_NOPS',hue='NOPS Compare',data=data_Reliance_INFY)


# In[42]:


sns.relplot(x='RI_NPM',y='INFY_NPM',hue='NPM Compare',data=data_Reliance_INFY)


# In[43]:


data_Reliance_HUL=pd.merge(data1,data5,how='outer',left_on='RI_SNo',right_on='HUL_SNo')


# In[44]:


def compare_PE_RH(df):
    return int(df['RI_PE Ratio']>=df['HUL_PE Ratio'])
def compare_OPS_RH(df):
    return int(df['RI_OPS']>=df['HUL_OPS'])
def compare_NOPS_RH(df):
    return int(df['RI_NOPS']>=df['HUL_NOPS'])
def compare_NPM_RH(df):
    return int(df['RI_NPM']>=df['HUL_NPMP'])
data_Reliance_HUL['PE Compare']=data_Reliance_HUL.apply(compare_PE_RH,axis=1)
data_Reliance_HUL['OPS Compare']=data_Reliance_HUL.apply(compare_OPS_RH,axis=1)
data_Reliance_HUL['NOPS Compare']=data_Reliance_HUL.apply(compare_NOPS_RH,axis=1)
data_Reliance_HUL['NPM Compare']=data_Reliance_HUL.apply(compare_NPM_RH,axis=1)


# In[45]:


sns.relplot(x='RI_PE Ratio',y='HUL_PE Ratio',hue='PE Compare',data=data_Reliance_HUL)


# In[46]:


sns.relplot(x='RI_OPS',y='HUL_OPS',hue='OPS Compare',data=data_Reliance_HUL)


# In[47]:


sns.relplot(x='RI_NOPS',y='HUL_NOPS',hue='NOPS Compare',data=data_Reliance_HUL)


# In[48]:


sns.relplot(x='RI_NPM',y='HUL_NPMP',hue='NPM Compare',data=data_Reliance_HUL)


# # COMPARISION OF TATA CONSULTANCY SERVICES WITH OTHER COMPANIES

# In[49]:


data2.columns


# In[50]:


data_TCS_Reliance=pd.merge(data2,data1,how='outer',left_on='TCS_SNo',right_on='RI_SNo')


# In[51]:


def compare_PE_TR(df):
    return int(df['RI_PE Ratio']<df['TCS_PE Ratio'])
def compare_OPS_TR(df):
    return int(df['RI_OPS']<=df['TCS_OPS'])
def compare_NOPS_TR(df):
    return int(df['RI_NOPS']<=df['TCS_NOPS'])
def compare_NPM_TR(df):
    return int(df['RI_NPM']<=df['TCS_NPM'])
data_TCS_Reliance['PE Compare']=data_TCS_Reliance.apply(compare_PE_RT,axis=1)
data_TCS_Reliance['OPS Compare']=data_TCS_Reliance.apply(compare_OPS_RT,axis=1)
data_TCS_Reliance['NOPS Compare']=data_TCS_Reliance.apply(compare_NOPS_RT,axis=1)
data_TCS_Reliance['NPM Compare']=data_TCS_Reliance.apply(compare_NPM_RT,axis=1)


# In[52]:


data_TCS_Reliance


# In[53]:


sns.relplot(x='TCS_PE Ratio',y='RI_PE Ratio',hue='PE Compare',data=data_TCS_Reliance)


# In[54]:


sns.relplot(x='TCS_OPS',y='RI_OPS',hue='OPS Compare',data=data_TCS_Reliance)


# In[55]:


sns.relplot(x='TCS_NOPS',y='RI_NOPS',hue='NOPS Compare',data=data_TCS_Reliance)


# In[56]:


sns.relplot(x='TCS_NPM',y='RI_NPM',hue='NPM Compare',data=data_TCS_Reliance)


# In[57]:


data_TCS_HDFC=pd.merge(data2,data3,how='outer',left_on='TCS_SNo',right_on='HDFC_SNo')


# In[58]:


def compare_PE_TH(df):
    return int(df['HDFC_PE Ratio']<df['TCS_PE Ratio'])
def compare_OPS_TH(df):
    return int(df['HDFC_OPS']<=df['TCS_OPS'])
def compare_NOPS_TH(df):
    return int(df['HDFC_NOPS']<=df['TCS_NOPS'])
def compare_NPM_TH(df):
    return int(df['HDFC_NPM']<=df['TCS_NPM'])
data_TCS_HDFC['PE Compare']=data_TCS_HDFC.apply(compare_PE_TH,axis=1)
data_TCS_HDFC['OPS Compare']=data_TCS_HDFC.apply(compare_OPS_TH,axis=1)
data_TCS_HDFC['NOPS Compare']=data_TCS_HDFC.apply(compare_NOPS_TH,axis=1)
data_TCS_HDFC['NPM Compare']=data_TCS_HDFC.apply(compare_NPM_TH,axis=1)


# In[59]:


data_TCS_HDFC


# In[60]:


sns.relplot(x='TCS_PE Ratio',y='HDFC_PE Ratio',hue='PE Compare',data=data_TCS_HDFC)


# In[61]:


sns.relplot(x='TCS_OPS',y='HDFC_OPS',hue='OPS Compare',data=data_TCS_HDFC)


# In[62]:


sns.relplot(x='TCS_NOPS',y='HDFC_NOPS',hue='NOPS Compare',data=data_TCS_HDFC)


# In[63]:


sns.relplot(x='TCS_NPM',y='HDFC_NPM',hue='NPM Compare',data=data_TCS_HDFC)


# In[64]:


data_TCS_INFY=pd.merge(data2,data4,how='outer',left_on='TCS_SNo',right_on='INFY_SNo')


# In[67]:


def compare_PE_TI(df):
    return int(df['INFY_PE Ratio']<df['TCS_PE Ratio'])
def compare_OPS_TI(df):
    return int(df['INFY_OPS']<=df['TCS_OPS'])
def compare_NOPS_TI(df):
    return int(df['INFY_NOPS']<=df['TCS_NOPS'])
def compare_NPM_TI(df):
    return int(df['INFY_NPM']<=df['TCS_NPM'])
data_TCS_INFY['PE Compare']=data_TCS_INFY.apply(compare_PE_TI,axis=1)
data_TCS_INFY['OPS Compare']=data_TCS_INFY.apply(compare_OPS_TI,axis=1)
data_TCS_INFY['NOPS Compare']=data_TCS_INFY.apply(compare_NOPS_TI,axis=1)
data_TCS_INFY['NPM Compare']=data_TCS_INFY.apply(compare_NPM_TI,axis=1)


# In[69]:


data_TCS_INFY


# In[70]:


sns.relplot(x='TCS_PE Ratio',y='INFY_PE Ratio',hue='PE Compare',data=data_TCS_INFY)


# In[71]:


sns.relplot(x='TCS_OPS',y='INFY_OPS',hue='OPS Compare',data=data_TCS_INFY)


# In[72]:


sns.relplot(x='TCS_NOPS',y='INFY_NOPS',hue='NOPS Compare',data=data_TCS_INFY)


# In[73]:


sns.relplot(x='TCS_NPM',y='INFY_NPM',hue='NPM Compare',data=data_TCS_INFY)


# In[76]:


data_TCS_HUL=pd.merge(data2,data5,how='outer',left_on='TCS_SNo',right_on='HUL_SNo')


# In[78]:


def compare_PE_THUL(df):
    return int(df['HUL_PE Ratio']<df['TCS_PE Ratio'])
def compare_OPS_THUL(df):
    return int(df['HUL_OPS']<=df['TCS_OPS'])
def compare_NOPS_THUL(df):
    return int(df['HUL_NOPS']<=df['TCS_NOPS'])
def compare_NPM_THUL(df):
    return int(df['HUL_NPMP']<=df['TCS_NPM'])
data_TCS_HUL['PE Compare']=data_TCS_HUL.apply(compare_PE_THUL,axis=1)
data_TCS_HUL['OPS Compare']=data_TCS_HUL.apply(compare_OPS_THUL,axis=1)
data_TCS_HUL['NOPS Compare']=data_TCS_HUL.apply(compare_NOPS_THUL,axis=1)
data_TCS_HUL['NPM Compare']=data_TCS_HUL.apply(compare_NPM_THUL,axis=1)


# In[80]:


data_TCS_HUL


# In[81]:


sns.relplot(x='TCS_PE Ratio',y='HUL_PE Ratio',hue='PE Compare',data=data_TCS_HUL)


# In[82]:


sns.relplot(x='TCS_OPS',y='HUL_OPS',hue='OPS Compare',data=data_TCS_HUL)


# In[83]:


sns.relplot(x='TCS_NOPS',y='HUL_NOPS',hue='NOPS Compare',data=data_TCS_HUL)


# In[85]:


sns.relplot(x='TCS_NPM',y='HUL_NPMP',hue='NPM Compare',data=data_TCS_HUL)


# # COMPARISION OF HDFC BANK WITH OTHER COMPANIES

# In[86]:


data3.columns


# In[87]:


data_HDFC_Reliance=pd.merge(data3,data1,how='outer',left_on='HDFC_SNo',right_on='RI_SNo')


# In[89]:


def compare_PE_HR(df):
    return int(df['RI_PE Ratio']<df['HDFC_PE Ratio'])
def compare_OPS_HR(df):
    return int(df['RI_OPS']<=df['HDFC_OPS'])
def compare_NOPS_HR(df):
    return int(df['RI_NOPS']<=df['HDFC_NOPS'])
def compare_NPM_HR(df):
    return int(df['RI_NPM']<=df['HDFC_NPM'])
data_HDFC_Reliance['PE Compare']=data_HDFC_Reliance.apply(compare_PE_HR,axis=1)
data_HDFC_Reliance['OPS Compare']=data_HDFC_Reliance.apply(compare_OPS_HR,axis=1)
data_HDFC_Reliance['NOPS Compare']=data_HDFC_Reliance.apply(compare_NOPS_HR,axis=1)
data_HDFC_Reliance['NPM Compare']=data_HDFC_Reliance.apply(compare_NPM_HR,axis=1)


# In[90]:


data_HDFC_Reliance


# In[91]:


sns.relplot(x='HDFC_PE Ratio',y='RI_PE Ratio',hue='PE Compare',data=data_HDFC_Reliance)


# In[92]:


sns.relplot(x='HDFC_OPS',y='RI_OPS',hue='OPS Compare',data=data_HDFC_Reliance)


# In[93]:


sns.relplot(x='HDFC_NOPS',y='RI_NOPS',hue='NOPS Compare',data=data_HDFC_Reliance)


# In[94]:


sns.relplot(x='HDFC_NPM',y='RI_NPM',hue='NPM Compare',data=data_HDFC_Reliance)


# In[95]:


data_HDFC_TCS=pd.merge(data3,data2,how='outer',left_on='HDFC_SNo',right_on='TCS_SNo')


# In[96]:


def compare_PE_HT(df):
    return int(df['TCS_PE Ratio']<df['HDFC_PE Ratio'])
def compare_OPS_HT(df):
    return int(df['TCS_OPS']<=df['HDFC_OPS'])
def compare_NOPS_HT(df):
    return int(df['TCS_NOPS']<=df['HDFC_NOPS'])
def compare_NPM_HT(df):
    return int(df['TCS_NPM']<=df['HDFC_NPM'])
data_HDFC_TCS['PE Compare']=data_HDFC_TCS.apply(compare_PE_HT,axis=1)
data_HDFC_TCS['OPS Compare']=data_HDFC_TCS.apply(compare_OPS_HT,axis=1)
data_HDFC_TCS['NOPS Compare']=data_HDFC_TCS.apply(compare_NOPS_HT,axis=1)
data_HDFC_TCS['NPM Compare']=data_HDFC_TCS.apply(compare_NPM_HT,axis=1)


# In[97]:


data_HDFC_TCS


# In[98]:


sns.relplot(x='HDFC_PE Ratio',y='TCS_PE Ratio',hue='PE Compare',data=data_HDFC_TCS)


# In[99]:


sns.relplot(x='HDFC_OPS',y='TCS_OPS',hue='OPS Compare',data=data_HDFC_TCS)


# In[100]:


sns.relplot(x='HDFC_NOPS',y='TCS_NOPS',hue='NOPS Compare',data=data_HDFC_TCS)


# In[101]:


sns.relplot(x='HDFC_NPM',y='TCS_NPM',hue='NPM Compare',data=data_HDFC_TCS)


# In[102]:


data_HDFC_INFY=pd.merge(data3,data4,how='outer',left_on='HDFC_SNo',right_on='INFY_SNo')


# In[103]:


def compare_PE_HI(df):
    return int(df['INFY_PE Ratio']<df['HDFC_PE Ratio'])
def compare_OPS_HI(df):
    return int(df['INFY_OPS']<=df['HDFC_OPS'])
def compare_NOPS_HI(df):
    return int(df['INFY_NOPS']<=df['HDFC_NOPS'])
def compare_NPM_HI(df):
    return int(df['INFY_NPM']<=df['HDFC_NPM'])
data_HDFC_INFY['PE Compare']=data_HDFC_INFY.apply(compare_PE_HI,axis=1)
data_HDFC_INFY['OPS Compare']=data_HDFC_INFY.apply(compare_OPS_HI,axis=1)
data_HDFC_INFY['NOPS Compare']=data_HDFC_INFY.apply(compare_NOPS_HI,axis=1)
data_HDFC_INFY['NPM Compare']=data_HDFC_INFY.apply(compare_NPM_HI,axis=1)


# In[104]:


data_HDFC_INFY


# In[105]:


sns.relplot(x='HDFC_PE Ratio',y='INFY_PE Ratio',hue='PE Compare',data=data_HDFC_INFY)


# In[106]:


sns.relplot(x='HDFC_OPS',y='INFY_OPS',hue='OPS Compare',data=data_HDFC_INFY)


# In[107]:


sns.relplot(x='HDFC_NOPS',y='INFY_NOPS',hue='NOPS Compare',data=data_HDFC_INFY)


# In[108]:


sns.relplot(x='HDFC_NPM',y='INFY_NPM',hue='NPM Compare',data=data_HDFC_INFY)


# In[109]:


data_HDFC_HUL=pd.merge(data3,data5,how='outer',left_on='HDFC_SNo',right_on='HUL_SNo')


# In[111]:


def compare_PE_HHUL(df):
    return int(df['HUL_PE Ratio']<df['HDFC_PE Ratio'])
def compare_OPS_HHUL(df):
    return int(df['HUL_OPS']<=df['HDFC_OPS'])
def compare_NOPS_HHUL(df):
    return int(df['HUL_NOPS']<=df['HDFC_NOPS'])
def compare_NPM_HHUL(df):
    return int(df['HUL_NPMP']<=df['HDFC_NPM'])
data_HDFC_HUL['PE Compare']=data_HDFC_HUL.apply(compare_PE_HHUL,axis=1)
data_HDFC_HUL['OPS Compare']=data_HDFC_HUL.apply(compare_OPS_HHUL,axis=1)
data_HDFC_HUL['NOPS Compare']=data_HDFC_HUL.apply(compare_NOPS_HHUL,axis=1)
data_HDFC_HUL['NPM Compare']=data_HDFC_HUL.apply(compare_NPM_HHUL,axis=1)


# In[112]:


data_HDFC_HUL


# In[113]:


sns.relplot(x='HDFC_PE Ratio',y='HUL_PE Ratio',hue='PE Compare',data=data_HDFC_HUL)


# In[114]:


sns.relplot(x='HDFC_OPS',y='HUL_OPS',hue='OPS Compare',data=data_HDFC_HUL)


# In[115]:


sns.relplot(x='HDFC_NOPS',y='HUL_NOPS',hue='NOPS Compare',data=data_HDFC_HUL)


# In[116]:


sns.relplot(x='HDFC_NPM',y='HUL_NPMP',hue='NPM Compare',data=data_HDFC_HUL)


# # COMPARISION OF INFOSYS WITH OTHER COMPANIES

# In[117]:


data4.columns


# In[118]:


data_INFY_Reliance=pd.merge(data4,data1,how='outer',left_on='INFY_SNo',right_on='RI_SNo')


# In[119]:


def compare_PE_IR(df):
    return int(df['RI_PE Ratio']<df['INFY_PE Ratio'])
def compare_OPS_IR(df):
    return int(df['RI_OPS']<=df['INFY_OPS'])
def compare_NOPS_IR(df):
    return int(df['RI_NOPS']<=df['INFY_NOPS'])
def compare_NPM_IR(df):
    return int(df['RI_NPM']<=df['INFY_NPM'])
data_INFY_Reliance['PE Compare']=data_INFY_Reliance.apply(compare_PE_IR,axis=1)
data_INFY_Reliance['OPS Compare']=data_INFY_Reliance.apply(compare_OPS_IR,axis=1)
data_INFY_Reliance['NOPS Compare']=data_INFY_Reliance.apply(compare_NOPS_IR,axis=1)
data_INFY_Reliance['NPM Compare']=data_INFY_Reliance.apply(compare_NPM_IR,axis=1)


# In[120]:


data_INFY_Reliance


# In[121]:


sns.relplot(x='INFY_PE Ratio',y='RI_PE Ratio',hue='PE Compare',data=data_INFY_Reliance)


# In[122]:


sns.relplot(x='INFY_OPS',y='RI_OPS',hue='OPS Compare',data=data_INFY_Reliance)


# In[123]:


sns.relplot(x='INFY_NOPS',y='RI_NOPS',hue='NOPS Compare',data=data_INFY_Reliance)


# In[124]:


sns.relplot(x='INFY_NPM',y='RI_NPM',hue='NPM Compare',data=data_INFY_Reliance)


# In[125]:


data_INFY_TCS=pd.merge(data4,data2,how='outer',left_on='INFY_SNo',right_on='TCS_SNo')


# In[126]:


def compare_PE_IT(df):
    return int(df['TCS_PE Ratio']<df['INFY_PE Ratio'])
def compare_OPS_IT(df):
    return int(df['TCS_OPS']<=df['INFY_OPS'])
def compare_NOPS_IT(df):
    return int(df['TCS_NOPS']<=df['INFY_NOPS'])
def compare_NPM_IT(df):
    return int(df['TCS_NPM']<=df['INFY_NPM'])
data_INFY_TCS['PE Compare']=data_INFY_TCS.apply(compare_PE_IT,axis=1)
data_INFY_TCS['OPS Compare']=data_INFY_TCS.apply(compare_OPS_IT,axis=1)
data_INFY_TCS['NOPS Compare']=data_INFY_TCS.apply(compare_NOPS_IT,axis=1)
data_INFY_TCS['NPM Compare']=data_INFY_TCS.apply(compare_NPM_IT,axis=1)


# In[127]:


data_INFY_TCS


# In[128]:


sns.relplot(x='INFY_PE Ratio',y='TCS_PE Ratio',hue='PE Compare',data=data_INFY_TCS)


# In[129]:


sns.relplot(x='INFY_OPS',y='TCS_OPS',hue='OPS Compare',data=data_INFY_TCS)


# In[130]:


sns.relplot(x='INFY_NOPS',y='TCS_NOPS',hue='NOPS Compare',data=data_INFY_TCS)


# In[131]:


sns.relplot(x='INFY_NPM',y='TCS_NPM',hue='NPM Compare',data=data_INFY_TCS)


# In[132]:


data_INFY_HDFC=pd.merge(data4,data3,how='outer',left_on='INFY_SNo',right_on='HDFC_SNo')


# In[133]:


def compare_PE_IH(df):
    return int(df['HDFC_PE Ratio']<df['INFY_PE Ratio'])
def compare_OPS_IH(df):
    return int(df['HDFC_OPS']<=df['INFY_OPS'])
def compare_NOPS_IH(df):
    return int(df['HDFC_NOPS']<=df['INFY_NOPS'])
def compare_NPM_IH(df):
    return int(df['HDFC_NPM']<=df['INFY_NPM'])
data_INFY_HDFC['PE Compare']=data_INFY_HDFC.apply(compare_PE_IH,axis=1)
data_INFY_HDFC['OPS Compare']=data_INFY_HDFC.apply(compare_OPS_IH,axis=1)
data_INFY_HDFC['NOPS Compare']=data_INFY_HDFC.apply(compare_NOPS_IH,axis=1)
data_INFY_HDFC['NPM Compare']=data_INFY_HDFC.apply(compare_NPM_IH,axis=1)


# In[134]:


data_INFY_HDFC


# In[135]:


sns.relplot(x='INFY_PE Ratio',y='HDFC_PE Ratio',hue='PE Compare',data=data_INFY_HDFC)


# In[136]:


sns.relplot(x='INFY_OPS',y='HDFC_OPS',hue='OPS Compare',data=data_INFY_HDFC)


# In[137]:


sns.relplot(x='INFY_NOPS',y='HDFC_NOPS',hue='NOPS Compare',data=data_INFY_HDFC)


# In[138]:


sns.relplot(x='INFY_NPM',y='HDFC_NPM',hue='NPM Compare',data=data_INFY_HDFC)


# In[139]:


data_INFY_HUL=pd.merge(data4,data5,how='outer',left_on='INFY_SNo',right_on='HUL_SNo')


# In[144]:


def compare_PE_IHUL(df):
    return int(df['HUL_PE Ratio']<df['INFY_PE Ratio'])
def compare_OPS_IHUL(df):
    return int(df['HUL_OPS']<=df['INFY_OPS'])
def compare_NOPS_IHUL(df):
    return int(df['HUL_NOPS']<=df['INFY_NOPS'])
def compare_NPM_IHUL(df):
    return int(df['HUL_NPMP']<=df['INFY_NPM'])
data_INFY_HUL['PE Compare']=data_INFY_HUL.apply(compare_PE_IHUL,axis=1)
data_INFY_HUL['OPS Compare']=data_INFY_HUL.apply(compare_OPS_IHUL,axis=1)
data_INFY_HUL['NOPS Compare']=data_INFY_HUL.apply(compare_NOPS_IHUL,axis=1)
data_INFY_HUL['NPM Compare']=data_INFY_HUL.apply(compare_NPM_IHUL,axis=1)


# In[145]:


data_INFY_HUL


# In[146]:


sns.relplot(x='INFY_PE Ratio',y='HUL_PE Ratio',hue='PE Compare',data=data_INFY_HUL)


# In[147]:


sns.relplot(x='INFY_OPS',y='HUL_OPS',hue='OPS Compare',data=data_INFY_HUL)


# In[148]:


sns.relplot(x='INFY_NOPS',y='HUL_NOPS',hue='NOPS Compare',data=data_INFY_HUL)


# In[150]:


sns.relplot(x='INFY_NPM',y='HUL_NPMP',hue='NPM Compare',data=data_INFY_HUL)


# # COMPARISION OF HINDUSTAN UNILEVER WITH OTHER COMPANIES

# In[151]:


data5.columns


# In[152]:


data_HUL_Reliance=pd.merge(data5,data1,how='outer',left_on='HUL_SNo',right_on='RI_SNo')


# In[154]:


def compare_PE_HULR(df):
    return int(df['RI_PE Ratio']<df['HUL_PE Ratio'])
def compare_OPS_HULR(df):
    return int(df['RI_OPS']<=df['HUL_OPS'])
def compare_NOPS_HULR(df):
    return int(df['RI_NOPS']<=df['HUL_NOPS'])
def compare_NPM_HULR(df):
    return int(df['RI_NPM']<=df['HUL_NPMP'])
data_HUL_Reliance['PE Compare']=data_HUL_Reliance.apply(compare_PE_HULR,axis=1)
data_HUL_Reliance['OPS Compare']=data_HUL_Reliance.apply(compare_OPS_HULR,axis=1)
data_HUL_Reliance['NOPS Compare']=data_HUL_Reliance.apply(compare_NOPS_HULR,axis=1)
data_HUL_Reliance['NPM Compare']=data_HUL_Reliance.apply(compare_NPM_HULR,axis=1)


# In[155]:


data_HUL_Reliance


# In[156]:


sns.relplot(x='HUL_PE Ratio',y='RI_PE Ratio',hue='PE Compare',data=data_HUL_Reliance)


# In[158]:


sns.relplot(x='HUL_OPS',y='RI_OPS',hue='OPS Compare',data=data_HUL_Reliance)


# In[159]:


sns.relplot(x='HUL_NOPS',y='RI_NOPS',hue='NOPS Compare',data=data_HUL_Reliance)


# In[160]:


sns.relplot(x='HUL_NPMP',y='RI_NPM',hue='NPM Compare',data=data_HUL_Reliance)


# In[161]:


data_HUL_TCS=pd.merge(data5,data2,how='outer',left_on='HUL_SNo',right_on='TCS_SNo')


# In[162]:


def compare_PE_HULT(df):
    return int(df['TCS_PE Ratio']<df['HUL_PE Ratio'])
def compare_OPS_HULT(df):
    return int(df['TCS_OPS']<=df['HUL_OPS'])
def compare_NOPS_HULT(df):
    return int(df['TCS_NOPS']<=df['HUL_NOPS'])
def compare_NPM_HULT(df):
    return int(df['TCS_NPM']<=df['HUL_NPMP'])
data_HUL_TCS['PE Compare']=data_HUL_TCS.apply(compare_PE_HULT,axis=1)
data_HUL_TCS['OPS Compare']=data_HUL_TCS.apply(compare_OPS_HULT,axis=1)
data_HUL_TCS['NOPS Compare']=data_HUL_TCS.apply(compare_NOPS_HULT,axis=1)
data_HUL_TCS['NPM Compare']=data_HUL_TCS.apply(compare_NPM_HULT,axis=1)


# In[163]:


data_HUL_TCS


# In[164]:


sns.relplot(x='HUL_PE Ratio',y='TCS_PE Ratio',hue='PE Compare',data=data_HUL_TCS)


# In[165]:


sns.relplot(x='HUL_OPS',y='TCS_OPS',hue='OPS Compare',data=data_HUL_TCS)


# In[166]:


sns.relplot(x='HUL_NOPS',y='TCS_NOPS',hue='NOPS Compare',data=data_HUL_TCS)


# In[167]:


sns.relplot(x='HUL_NPMP',y='TCS_NPM',hue='NPM Compare',data=data_HUL_TCS)


# In[168]:


data_HUL_HDFC=pd.merge(data5,data3,how='outer',left_on='HUL_SNo',right_on='HDFC_SNo')


# In[169]:


def compare_PE_HULH(df):
    return int(df['HDFC_PE Ratio']<df['HUL_PE Ratio'])
def compare_OPS_HULH(df):
    return int(df['HDFC_OPS']<=df['HUL_OPS'])
def compare_NOPS_HULH(df):
    return int(df['HDFC_NOPS']<=df['HUL_NOPS'])
def compare_NPM_HULH(df):
    return int(df['HDFC_NPM']<=df['HUL_NPMP'])
data_HUL_HDFC['PE Compare']=data_HUL_HDFC.apply(compare_PE_HULH,axis=1)
data_HUL_HDFC['OPS Compare']=data_HUL_HDFC.apply(compare_OPS_HULH,axis=1)
data_HUL_HDFC['NOPS Compare']=data_HUL_HDFC.apply(compare_NOPS_HULH,axis=1)
data_HUL_HDFC['NPM Compare']=data_HUL_HDFC.apply(compare_NPM_HULH,axis=1)


# In[171]:


data_HUL_HDFC


# In[172]:


sns.relplot(x='HUL_PE Ratio',y='HDFC_PE Ratio',hue='PE Compare',data=data_HUL_HDFC)


# In[173]:


sns.relplot(x='HUL_OPS',y='HDFC_OPS',hue='OPS Compare',data=data_HUL_HDFC)


# In[174]:


sns.relplot(x='HUL_NOPS',y='HDFC_NOPS',hue='NOPS Compare',data=data_HUL_HDFC)


# In[175]:


sns.relplot(x='HUL_NPMP',y='HDFC_NPM',hue='NPM Compare',data=data_HUL_HDFC)


# In[176]:


data_HUL_INFY=pd.merge(data5,data4,how='outer',left_on='HUL_SNo',right_on='INFY_SNo')


# In[177]:


def compare_PE_HULI(df):
    return int(df['INFY_PE Ratio']<df['HUL_PE Ratio'])
def compare_OPS_HULI(df):
    return int(df['INFY_OPS']<=df['HUL_OPS'])
def compare_NOPS_HULI(df):
    return int(df['INFY_NOPS']<=df['HUL_NOPS'])
def compare_NPM_HULI(df):
    return int(df['INFY_NPM']<=df['HUL_NPMP'])
data_HUL_INFY['PE Compare']=data_HUL_INFY.apply(compare_PE_HULI,axis=1)
data_HUL_INFY['OPS Compare']=data_HUL_INFY.apply(compare_OPS_HULI,axis=1)
data_HUL_INFY['NOPS Compare']=data_HUL_INFY.apply(compare_NOPS_HULI,axis=1)
data_HUL_INFY['NPM Compare']=data_HUL_INFY.apply(compare_NPM_HULI,axis=1)


# In[178]:


data_HUL_INFY


# In[179]:


sns.relplot(x='HUL_PE Ratio',y='INFY_PE Ratio',hue='PE Compare',data=data_HUL_INFY)


# In[180]:


sns.relplot(x='HUL_OPS',y='INFY_OPS',hue='OPS Compare',data=data_HUL_INFY)


# In[181]:


sns.relplot(x='HUL_NOPS',y='INFY_NOPS',hue='NOPS Compare',data=data_HUL_INFY)


# In[182]:


sns.relplot(x='HUL_NPMP',y='INFY_NPM',hue='NPM Compare',data=data_HUL_INFY)


# # MERGING ALL DATA SET INTO ONE

# In[183]:


x=pd.merge(data_Reliance_TCS,data_HDFC_INFY,how='outer',left_on='TCS_SNo',right_on='HDFC_SNo')
data_all=pd.merge(x,data5,how='outer',left_on='TCS_SNo',right_on='HUL_SNo')


# In[192]:


data_all


# In[193]:


sns.pairplot(data_all)


# In[ ]:




