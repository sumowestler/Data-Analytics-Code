# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 03:26:13 2022

@author: sumow
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <=== format of read_csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=";")

## Getting a sumarry of the data
data.info()

## Working with calculations
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6
ProfitPerItem = 21.11 - 11.73

#Mathematical operations on tableu

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem


ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
CostPerTransaction = NumberOfItemsPurchased * CostPerItem
SellingPricePerTransaction = NumberOfItemsPurchased * SellingPricePerItem

# CostPerTransaction Column Calculation

#CostPerTransaction = CostPerItem * NumberofItemsPurchased
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

## Adding the CostPerTransaction as a new column to the dataframe

# data['CostPerTransaction'] = CostPerTransaction or

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#Sales per Transaction

data["SalesPerTransaction"] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Per Transaction

# Profit calculation = sales - cost

data['ProfitPerTransaction'] = data["SalesPerTransaction"] - data["CostPerTransaction"]

#Markup = sales - cost / cost

data["Markup"] = (data['ProfitPerTransaction']) / data["CostPerTransaction"]


## Using Rounder method to clean data by dictating number of signifigant figures.
## Rounding Markup
RoundMarkup = round(data["Markup"], 2)

data["Markup"] = RoundMarkup


## Combining columns of data

my_date = 'Day'+'-'+'Month'+'-'+'Year'

#Checking column data type
print(data['Day'].dtype)

#Change columns type

day = data['Day'].astype(str)
year = data['Year'].astype(str)

print(day.dtype)

my_date = day+'-'+data['Month']+'-'+year

data['date'] = my_date

## UYsing ioc to view specific columns and row

data.iloc[0] # Views the row with index = 0
data.iloc[0:3] # First three rows
data.iloc[-5]

data.head(1000) # Brings in the first 1000 rows

# Bring in all rows

data.iloc[1:100]
# Bring in a specific colunm row pair

data.iloc[4,2]

# Using split to split the  clinets keyword fioelds.
# new_var = column.str.split('sep', expand = True)

## Epand= True allows split to work through all variables.

split_col = data['ClientKeywords'].str.split(',' , expand = True )

# Creating new column in client kieywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

# Using the replace funtion to get rid of columns.

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']', '')

#Usding the lower funtion to change item to lowercase
data[' ItemDescription'] = data['ItemDescription'].str.lower()

#Adding data to the main data file by merging
#Bringing in a new data set

data_seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#Merging Filee:  merge_df = pd.merge(df_old, df_new, on = 'key')
data = pd.merge(data, data_seasons, on = 'Month')


# Dropping Columns 

# df = df.drop('columname', axis = 1)

data  = data.drop('ClientKeywords', axis = 1)

#doing the same for day

data = data.drop('Day', axis = 1)

# Drop year and month 

data = data.drop(['Year', 'Month'], axis=1)

# Exporting data to a csv file
# Index is requred when there are no unique transaction id, so change it to true if you need one
# It will be saved in the same working directory
data.to_csv('ValueInc_Cleaned.csv', index= False)