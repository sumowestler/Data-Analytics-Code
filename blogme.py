# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 03:05:22 2022

@author: sumow
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Reading Excel files.
data = pd.read_excel('C:/Users/sumow/the_complete_tableu/articles.xlsx')

# summary of the data

data.describe()

#summary of the columns
data.info()

#Counting the number of articles per source.count is used for data agregation
#format  of groupby: dt.groupby(['column_to_group'])['column_to_count'].count()

data.groupby(['source_id'])['article_id'].count()

#How many reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

#Dropping column
data = data.drop('engagement_comment_plugin_count' , axis =1)


# functions in python

def thisFuntion():
    print('This is my first function')

thisFuntion()

#this is a fucntion with variables

def aboutMe(name, surname, location):
    print('This is '+ name + '  My surname is ' + surname+ '  I am from '+ location  )
    return name, surname, location
    
a = aboutMe('Emerick', 'Martin', 'South Africa')

#Using for loops in functions

def favFood(food):
    for x in food:
        print('Top food is '+ x)

fastfood = ['burgers', 'pizza', 'pi']

favFood(fastfood)

# Creating a keyword flag

keyword = 'crash'

# Create a for loop to isolate each title.

# length = len(data)
# keyword_flag = []
# for x in range(0, length):
#     heading = data['title'][x]
#     if keyword in heading:
#         flag = 1
#     else:
#         flag = 0
#     keyword_flag.append(flag)
    
# Creating a function

def keywordFlag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range(0, length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag

keywordflag = keywordFlag('murder')

#creating a new column in data dataframe

data['keyword_flag'] = pd.Series(keywordflag)

#Playing around with classes 

class Car:
    type = 'automobile' #class attributes
    def __init__(self, name, make, color):
        self.carname = name
        self.carmake = make
        self.carcolor = color

mycar = Car('gclass', 'mercedes', 'black')

#for attributes in a class

carname = mycar.carname
carmake= mycar.carmake
carcolor = mycar.carcolor

#Sentiment analysis

# VADER is an analysis sentiment lexicon that can be used for sentiment analysis.

# SentimentIntensityAnalyzer

#initialize the analyzer

sent_int = SentimentIntensityAnalyzer()

text = data['title'][16]
sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

# sentimetn analysis to all titles using for loops

title_neg_setiment = []
title_pos_sentimet = []
title_nue_setiment = []

length = len(data)

for x in range(0, length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos= 0
        neu = 0
    title_neg_setiment.append(neg)
    title_nue_setiment.append(neu)
    title_pos_sentimet.append(pos)
    
title_neg_setiment = pd.Series(title_neg_setiment)
title_nue_setiment = pd.Series(title_nue_setiment)
title_pos_sentimet = pd.Series(title_pos_sentimet)

data['title_neg_setiment'] = title_neg_setiment
data['title_pos_sentimet'] = title_pos_sentimet
data['title_nue_setiment'] = title_nue_setiment

#writing the data to excel file

data.to_excel('blogme_clean.xlsx', sheet_name='blogmedata', index=(False))
