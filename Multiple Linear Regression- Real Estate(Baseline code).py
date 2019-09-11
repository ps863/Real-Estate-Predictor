#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Multiple linear regression real estate data set 


# In[6]:


import numpy as np
import pandas as pd
import csv 
from numpy.linalg import inv


# In[7]:


df=pd.read_csv("Real estate valuation - Test.csv")
df= df.drop('X1 transaction date', 1)  # Getting rid of transaction date data 
df= df.drop('No', 1) # Remove number column 


# In[8]:


housePrice=df.iloc[:,6] # dataFrame with only house price per area 
hf= np.array(housePrice) # Transform dataframe to a numpy array
hf=hf.reshape((414,1)) # Numpy array in he form of column vector with house prices 


# In[9]:


independentVariables= df.iloc[:,0:6]
idv= np.array(independentVariables)# array with all x values 




#Determination of Beta or coefficient for multiple linear regression
#(xTx)^-1 (xTY)
# Where xT is transpose of x and x is the independent variable matrix 
# where Y is the output value , in this case house price per unit area 

independentVariables= df.iloc[:,0:6]
idv= np.array(independentVariables)

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
#print(coeff)
#print (np.dot(idv,coeff))





#Using numpy matrices 
housePriceMatrix= np.matrix(hf)
indepedentVariableMatrix= np.matrix(idv)
#(xTx)^-1 (xTY)
def coeffCalc2(independentVarMat,dependentVarMat):
    x= independentVarMat
    y= dependentVarMat
    xT= x.getT()
    part1=(xT*x)
    part1Inverse= part1.getI()
    coeffMat= part1Inverse*xT*y
    return coeffMat


print(coeffCalc2(indepedentVariableMatrix,housePriceMatrix))
    

