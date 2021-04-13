#!/usr/bin/env python
# coding: utf-8

# # Welcome to Jupyter!

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('fivethirtyeight')

df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv', parse_dates=['Date'])
df['Total Cases'] = df[['Confirmed', 'Recovered', 'Deaths']].sum(axis=1)


# In[2]:


# Worldwide Cases

worldwide_df = df.groupby(['Date']).sum()
w = worldwide_df.plot(figsize=(10,5))
w.set_xlabel('Date')
w.set_ylabel('# of Cases')
w.title.set_text('Worldwide Covid Insight')

plt.show()


# In[3]:


eth_df = df[df['Country']=='Ethiopia'].groupby(['Date']).sum()

e = eth_df.plot(figsize=(10,5))
e.set_xlabel('Date')
e.set_ylabel('# of Cases')
e.title.set_text('Ethiopia Covid Insight')

plt.show()


# In[4]:


us_df = df[df['Country']=='US'].groupby(['Date']).sum()

w = us_df.plot(figsize=(10,5))
w.set_xlabel('Date')
w.set_ylabel('# of Cases')
w.title.set_text('US Covid Insight')

plt.show()


# In[5]:


eth_df = df[df['Country']=='Ethiopia'].groupby(['Date']).sum()
us_df = df[df['Country']=='US'].groupby(['Date']).sum()

fig = plt.figure(figsize=(12,5))
ax = fig.add_subplot(111)

ax.plot(worldwide_df[['Total Cases']], label = 'Worldwide')
ax.plot(eth_df[['Total Cases']], label = 'Ethiopia')
ax.plot(us_df[['Total Cases']], label = 'US')
ax.set_xlabel('Date')
ax.set_ylabel('# of Cases')
ax.title.set_text('Ethiopia vs US vs Worldwide Cases')

plt.legend(loc = 'upper right')
plt.show()


# In[10]:


# Ethiopia Daily Cases and Deaths
eth_df = eth_df.reset_index()
eth_df['Daily Confirmed'] = eth_df['Confirmed'].sub(eth_df['Confirmed'].shift())
eth_df['Daily Deaths'] = eth_df['Deaths'].sub(eth_df['Deaths'].shift())


fig = plt.figure(figsize=(16,16))
ax = fig.add_subplot(111)

ax.bar(eth_df['Date'], eth_df['Daily Confirmed'], color = 'b', label = 'Ethiopia Daily Confirmed Cases')
ax.bar(eth_df['Date'], eth_df['Daily Deaths'], color = 'r', label = 'Ethiopia Daily Deaths')
ax.set_xlabel('Date')
ax.set_ylabel('# of ppl affected')
ax.title.set_text('Ethiopia Daily Cases and Deaths')

plt.legend(loc='upper left')
plt.show()


# In[ ]:





# This repo contains an introduction to [Jupyter](https://jupyter.org) and [IPython](https://ipython.org).
# 
# Outline of some basics:
# 
# * [Notebook Basics](../examples/Notebook/Notebook%20Basics.ipynb)
# * [IPython - beyond plain python](../examples/IPython%20Kernel/Beyond%20Plain%20Python.ipynb)
# * [Markdown Cells](../examples/Notebook/Working%20With%20Markdown%20Cells.ipynb)
# * [Rich Display System](../examples/IPython%20Kernel/Rich%20Output.ipynb)
# * [Custom Display logic](../examples/IPython%20Kernel/Custom%20Display%20Logic.ipynb)
# * [Running a Secure Public Notebook Server](../examples/Notebook/Running%20the%20Notebook%20Server.ipynb#Securing-the-notebook-server)
# * [How Jupyter works](../examples/Notebook/Multiple%20Languages%2C%20Frontends.ipynb) to run code in different languages.

# You can also get this tutorial and run it on your laptop:
# 
#     git clone https://github.com/ipython/ipython-in-depth
# 
# Install IPython and Jupyter:
# 
# with [conda](https://www.anaconda.com/download):
# 
#     conda install ipython jupyter
# 
# with pip:
# 
#     # first, always upgrade pip!
#     pip install --upgrade pip
#     pip install --upgrade ipython jupyter
# 
# Start the notebook in the tutorial directory:
# 
#     cd ipython-in-depth
#     jupyter notebook
