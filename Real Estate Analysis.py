#!/usr/bin/env python
# coding: utf-8

# In[78]:


"""
This Project uses multiple linear regression model to analyze and predict house prices in Hong Kong. 

The data comes from a University of California, Irvene dataset available for use on the public domain.



"""


# In[79]:


import numpy as np 
import pandas as pd
from numpy.linalg import inv 
import csv


# In[80]:


df = pd.read_csv('Real estate valuation data set.csv') # Read Provided Dataset
df = df.drop('X1 transaction date',1) # Get rid of data 
df = df.drop('No',1) # Drops the number column


# In[81]:


housePrice=df.iloc[:,5] # dataFrame with only house price per area 
hf= np.array(housePrice) # Transform dataframe to a numpy array 
hf=hf.reshape((len(hf),1)) # Numpy array in he form of column vector with house prices 


# In[82]:


# Populate a column full of 1s to allow for the intercept value to be accounted for 

df.insert(loc = 0, column = 'Ones' ,value = 1)





# In[84]:


independentVariables= df.iloc[:,0:6]
idv= np.array(independentVariables)# array with all x values which are the independent factors  


# In[85]:


#Determination of Beta or coefficient for multiple linear regression
#(xTx)^-1 (xTY)
# Where xT is transpose of x and x is the independent variable matrix 
# where Y is the output value , in this case house price per unit area 

def coefficientCalculator(independentVar,dependentVar):
    x=independentVar
    y=dependentVar
    xT= np.transpose(x)
    part1= xT.dot(x)
    inversePart1= inv(part1)
    part2= inversePart1.dot(xT)
    coeff= part2.dot(y)
    return coeff

coeff= coefficientCalculator(idv,hf)

