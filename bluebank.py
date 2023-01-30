# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 23:06:30 2022

@author: sumow
"""

## We are working on a json file. Works like a dictionary.
# Anoconda has a pre-intalled libray for dealing with this.

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# Method 1 to read json data
json_file = open('loan_data_json.json')
# Loading file
data = json.load(json_file)

# Other method to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    print(data)

# tranform to dataframe

loandata = pd.DataFrame(data)

# finding unique values for the purpose column
loandata['purpose'].unique()

# describing the data, gives you the basic statistics for data
loandata.describe()

#describe the data for a specific column
loandata['int.rate'].describe()
loandata.info()

loandata['fico'].describe()
loandata['dti'].describe()
# json file lists anual income as a natural log, import numbpy to get the anual income

#Using EXP() to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

# Working with arrays
#1d array
arr = np.array([1,2,3,4])

# 0d array
arr = np.array(43)

#2d array
arr = np.array([[1,2,3], [4,5,6]])

# working with if statement
a = 40
b = 500 

if b > a:
    print("b is greater than a")
# Lets add more conditions

a = 40
b= 500
c = 1000
if b > a and  b < c:
    print("b is greater than a but less than c")
    
# What if a condition is not met?

a = 40
b = 500
c = 20

if b > a and  b < c:
    print("b is greater than a but less than c")
else:
    print('No conditions met')
    
# another condition diferent metrics

a = 40
b = 0
c = 30

if b > a and b < c:
    print('b is greater than a but less than c')
elif b > a and b > c:
    print('b is greater and a and c')
else:
    print('no conditions met')

    
# using or
a = 40
b = 500
c = 30

if b > a or b < c:
    print('b is greater than a but less than c')
else:
    print('no conditions met')

# fico score

fico = 350

# fico >= 300 and < 400:
# 'Very Poor'
# fico >= 400 and ficoscore < 600:
# 'Poor'
# fico >= 601 and ficoscore < 660:
# 'Fair'
# fico >= 660 and ficoscore < 780:
# 'Good'
# fico >=780:
# 'Excellent'

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico <= 601 and fico < 600:
    ficocat = 'Fair'
elif fico >= 600 and fico < 700:
    ficocat = 'Good'
elif fico >= 700:
    ficocat = 'Excellent'
else:
    ficocat = 'Unkonwn'
print(ficocat)

# For loops

fruits = ['apple', 'pear', 'banana']

for x in fruits:
    print(x)

for x in range(0, 3):
    y = fruits[x] + 'for sale'
    print(y)
    
# applying for loops to loan data

# using for loop for data



# testing error
length = len(loandata)
ficocat = []
for x in range(0, length):
    catagory = 'red'

    try:    
        if catagory >= 300 and catagory < 400:
            cat = 'Very Poor'
        elif catagory >= 400 and catagory < 600:
            cat = 'Poor'
        elif catagory >= 601 and catagory < 660:
            cat = 'Fair'
        elif catagory >= 660 and catagory < 700:
             cat = 'Good'
        elif catagory >= 700:
             cat = 'Excellent'
        else:
             cat = 'Unknown'
    except:
        cat = 'Uknown'
   
    ficocat.append(cat)
ficocat = pd.Series(ficocat)

loandata['fico.category'] = ficocat


# df.loc as conditional statement
#df.loc[df[colomunname] condtion, newcolumname] = 'value if the condition is met

#for interest rates, a new column is wanted. If the rate >0.12 then high, else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

# Number of loans/ rows by fico.category
# size reperesents the number of rows

catplot = loandata.groupby(['fico.category']).size()
# Groupby allows you to know the frequency of certain rows meeting a specifc category. It also allows you to sort series by a specific metric
catplot.plot.bar(color = 'green', width = 0.1)
plt.show()

purposeplot = loandata.groupby(['purpose']).size()
purposeplot.plot.bar(color = 'red', width = 0.2)
plt.show()

# Scatter plot

ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = 'orange')
plt.show()

#Writing to csv
loandata.to_csv('loan_cleaned.csv', index = True)


