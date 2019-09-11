# Real-Estate-Predictor


**How does this work ?** 

This program uses a multiple regression model to predict house prices per unit area. 
It makes use of a matrix of "Beta" regression coefficients that multiply with the independent data to produce predicted values for the 
dependent variable. 


**What can this program work on?**

The current version relies on beta coefficients found from a sample dataset of prices of homes per unit area in Taiwan. 
The dataset was found [here](https://archive.ics.uci.edu/ml/datasets/Real+estate+valuation+data+set)

Since the coefficents are calculated using sample dataset on houses in Taiwan, this model will presently only work for Taiwan.

**How can I get this to work for other cities?**

You would have to find another dataset with house prices and all the other parameters. Once you find this data, the csv file needs to be in
the format that the given dataset file is. 

After this use the Real Estate Analysis file and change the input file for the dataframe. Once this is done, run the file and get the new 
Beta coefficients. Update these in the main.py (inside the function) and run to get the results. 

Note at the moment the file needs to be in exactly the same format as the dataset given to avoid errors

**What updates or improvements are planned?**

I expected to add a GUI interface to make this more user friendly. 
Also there are plans to reduce the need to modify data files when wanting to use this program for any other city than Taiwan.

The aim is to make this application more user friendly for those not well trained in data cleaning.
