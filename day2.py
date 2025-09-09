# -*- coding: utf-8 -*-
"""
Spyder Editor

DAY 2
"""

print('Goodmorning - Welcome to the Python course')

# py launcher - nice cmdline application
# is installed with python from python.org
# reads from registry which global python installations you have
# make sure to register anaconda in registry also(checkmark in anaconda installation )

# the zip function got a new parameter called 
# strict - it's from 3.10+

# we are here in python 3.13.5
l1=[1,2,3]
l2=[5,6,7,8]
list(zip(l1,l2,strict=True))


l1=[1,2,3]
l2=[5,6,7,8]
list(zip(l1,l2,strict=False))

# python from python.org is installed here
# C:\Users\Administrator\AppData\Local\Programs\Python\Python313

# python.exe

# I will show you how to install python extension for 
# VSCode on one of the lab machines in Denmark

# the python environment extension now 
# is installed autmatically with the python extension 


# Time for exercises:
# https://github.com/camillagaardsted/Ghana2025PythonWorkshop/
# blob/main/Lab3_Virtual_environments.ipynb
# Lab 3 


#https://github.com/camillagaardsted/Ghana2025PythonWorkshop

# file extension ipynb
# it's not only python which uses notebooks
# you can use them for R, SQL, PowerShell, Scala ...

# VS Code Editor - can also handle notebooks
# requires an extension for Python

# VS Code Editor needs the Jupyter extension
# and python needs the ipykernel package

# Spyder is not so good an editor - 
#when you want to switch back and forth between environments

# spyder is actually a package for python

# spyder's interactive console requires some special
# package(s) to work spyder-kernels

# Lab 4

# https://github.com/camillagaardsted/Ghana2025PythonWorkshop/blob/main/Lab4_Jupyter_Notebooks.ipynb
# Please start with Exercise 3 - Notebooks in Spyder
# Run the Anaconda Prompt on your base environment
# then continue to exercise 1 when it's doing the installation 

############################################################
# Date and Datetime in Python 
############################################################

# In Python a Date is class  (think of it as a datatype)

import datetime as dt
# date is a function/method 
# and it is the constructor for the class called date
yesterday=dt.date(2025,9,8)

# the date class has 3 attributes/properties
# with year, month and day
yesterday.year
yesterday.month

dt.date(day=8,month=9,year=2025)

# we will get back to how to parse this and understand
# it as a date in python
'8 September 2025'

today=dt.date.today()

# what if the time also?
# we have another class for that 
current_time = dt.datetime(2025,9,9,12,21)

current_time = dt.datetime.now()

# there is one more dataclass in Python 
# that is timedelta - the time difference between two dates/datetimes

before_time=current_time
current_time = dt.datetime.now()

result_timediff=current_time - before_time

christmas_date =dt.date(2025,12,25)

days_to_christmas = christmas_date - today


# if we have a date like today variable 
# how do I print it nicely with month name

print(today)

# strftime
# f for format - we have a date/datetime
# and want to convert it to a string

today.strftime('%d_%m_%Y')


today.strftime('%d_%B_%Y')

next_month_from_today = today + dt.timedelta(days=30)

next_month_from_today.strftime('%d_%B_%Y')
timestamp=dt.datetime.now()
filename = f'datafile_{timestamp:%Y_%m_%d_%H_%M}.csv'

# How do we parse this string into a date?
date_as_string='8 September 2025'
date_from_string=dt.datetime.strptime(date_as_string, '%d %B %Y').date()

###################################################
# Lambda functions
###################################################

# standard function we create 
# it has a name

def get_first_element_on_list(number_list):
    return number_list[0]
    
numbers=[6,8,9,0,3]
result=get_first_element_on_list(numbers)

# lambda functions means we define them adhoc
# they only exist in a limited time
# and they don't have a name

sorted(numbers)
sorted(numbers,reverse=True)

word_list = "This is a test string from Andrew".split(' ')

sorted(word_list)
# we specify just the name of the function
# and then sorted function applies the function
# to each element to do the sorting
sorted(word_list,key=str.casefold)

# let's sort after the last letter in each word

def get_last_element_on_list(wordlist):
    return wordlist[-1]


sorted(word_list,key=get_last_element_on_list)

student_tuples = [
    ('john', 'A', 9),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

# it just sorts af the first element in the tuple
sorted(student_tuples)

sorted(student_tuples,key=get_last_element_on_list)

# then a lambda functions means 
# that we define a functions inside adhoc in call

sorted(student_tuples, key=lambda student : student[-1])

# Object oriented programming
# Discussing classes in Python 

# we have seen the Date and DateTime classes

# think of the class as datatype
# a class have name
# a class can have properties/attributes
# a class can have methods(functions)

import datetime 

timestamp=datetime.datetime.now()
# the timestamp is our object

# Lunch until 13.45

#####################################################
# Pandas
#####################################################

# user guide on the website
# https://pandas.pydata.org/docs/user_guide/indexing.html

import pandas as pd

pd.__version__


# Book about pandas - written by the founder of pandas
# https://wesmckinney.com/book/

# The best book is Pandas Cookbook 
# Pandas Cookbook: Practical recipes for scientific computing, time series, and exploratory data analysis using Python , Third Edition
# 

# Pandas 3.0 will soon arrive - is in dev/preview
# Pandas 2.0 was released in April 2023
# it was a new major version
# they have focused on better performance
# that means we now have a better option with big data
# they try to use pyarrow instead of numpy
# BUT for backward compatability they still support numpy 
# and that is also default 

# user guide is really nice - it covers topics 
# read one every day -and you will really make progress
# https://pandas.pydata.org/docs/user_guide/index.html#user-guide

# API - pandas 
# documentation for all classes, functions, methods etc
# https://pandas.pydata.org/docs/reference/index.html#api

#####################################################
# cheat sheet - we get back to that later
# https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

###############################################################
# Introduction to pandas - the basic building bricks 
###############################################################

# The Series is the fundamental class in Python
# together with the DataFrame


s1=pd.Series([12,89,45,34])    
    
# we want to define the index and the name

s1=pd.Series([12,89,45,34], name='Age',index=['a','b','c','d'])    

print(s1)

# a Series has some properties 
# the most important ones are

s1.dtype # int64
s1.name
s1.size
s1.index # this a list of values - it has Index as datatype


s2=pd.Series(['Bob','Adam','Joe'], name='Name')    

print(s2)
s2.dtype
s2.index

s2[0]
s2[0]='Alice'
# datatype is object - we can just put anything into this Series
s2[0]=['Alice','Bob']

# please specify the datatype for strings
# otherwise you will just get object
s2=pd.Series(['Bob','Adam','Joe'], name='Name',dtype='string')    
print(s2)
s2[0]=['Alice','Bob']

# Please note pandas 3 will default to str 
# and not object for strings - if you don't specify a datatype
# we will get back to examples with that

# We will now create a DataFrame

df = pd.DataFrame({'Name': ['Bob','Adam','Joe'],
                   'Age' : [12,89,45]},index=list('abc'))

print(df)
df.dtypes
# row index is a,b,c
df.index
df.columns
df.size
df.shape


import pandas as pd
s1=pd.Series([12,89,45,34], name='Age',index=['a','b','c','d'])    

# pandas has broadcasting feature
# so easy to do math
s3=s1 + 2

s1 + s3

s1+2 +s1

list('abc')

# Series 

s1

# indexing and selecting data from a Series
# we have [], loc and iloc
# Use loc and iloc
# single value from a Series
s1['b']

# iloc - the stands for integer
# index based from 0

s1.index
s1.iloc[1]
# loc uses the values from the index that means here a,b,c
s1.loc['a']

# loc with a list
s1.loc[['b','d']]
# endpoint is included for loc method
s1.loc['b':'d']

# we have iloc has also these posibilities
# Endpoint IS NOT included for iloc!!!
s1.iloc[0:2]

# DataFrame - has also iloc, loc, [] and . notation

import pandas as pd
df = pd.DataFrame({'Name': ['Bob','Adam','Joe','Lily'],
                   'Age' : [12,89,45,56],
                   'Country' : ['DK','GH','US','SW']},
                  index=list('abcd'))
df.columns
# for a dataframe the squarebrackets - should column names
s1=df['Age']

# pitfall in pandas - we will see the CoW later
s1.loc['c']=78

# df['Age'] the same as 
df.Age

# let's see loc and iloc for the DataFrame

df.columns # ['Name', 'Age', 'Country']
df.index # 'a', 'b', 'c', 'd']

# df.loc[<index>,<columns> ]

df.loc[['a','d','c'],'Age' ]

df.loc[['a','d','c'],'Age' ]=df.loc[['a','d','c'],'Age' ] + 1000

# string manipulations 

df['Name']=df['Name'].str.upper()
df['Name']=df['Name'].str.title()

# loc, iloc and [] for selection
# but also for data minpulation

# how do we filter on the values inside the df?
# we get a boolean Series here
s1 > 1000

df.loc[s1 > 1000]

df.loc[s1 > 1000, ['Country','Name']]

df.loc[df['Age']>1000]

df.loc[df['Age']>1000,['Country','Name']]

# what if we have several conditions like 
# we have Age above 1000 and country us

df[(df['Age']>1000)  & (df['Country']=='US')]

# pandas has another option for writing this 
# a much shorter syntax with the query method
# readable filter we have here
df.query("Age>100 and Country=='US'")

import numpy as np

df=pd.DataFrame(np.arange(100,142).reshape(6,7), columns=list('ABCDEFG'))

#  Lab 5 
# https://github.com/camillagaardsted/Ghana2025PythonWorkshop/blob/main/Lab5_Pandas_indexing_and_selection.ipynb

# Open the notebook in VSCode / Spyder/Jupyter
# if have notebooks
# or just run in Spyder











