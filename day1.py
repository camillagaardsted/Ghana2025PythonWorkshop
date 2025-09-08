# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 09:42:14 2025

@author: Camilla
"""
# Variables
# It has a name and a datatype 
# and we usually define it the first time we assign a value to it
# str
name = 'Carlos Alcaraz'
# int
age= 22
is_spanish = True
is_danish = False
# float
bigmac_price_in_us_in_dollars = 5.79
game_engine_object = None
month=9
month='September'

# colletions - 4 built-in
# they are all iterables
# 1) list
# 2) dictionary
# 3) tuple
# 4) set 

# 1) list

color_list = ['red','blue','green']
number_of_elements=len(color_list)
# append is a method on out color_object  - 
color_list.append('pink')
#
color_list.append(['white','purple'])
# 
color_list.extend(['white','purple'])
# we wan't to remove element 4
color_list.remove(['white','purple'])
# a single element
color_list[1]

# slicing
color_list[1:4]

# let's take a string with a text

text='Carlos Alcaraz won the US Open in tennis yesterday'

text.lower()
text.index('U')

# strings in python support slicing
text[23:30]
# we can also take a string and use it as an iterable

letterlist=list(text.lower())

# we want to count the letters and make a dictionary to display the frequency

'a' in letterlist

letterlist.count('a')
letterlist.count('b')

# a dictionary - we have key and value 
# {}

letter_frequency = {'a':5,'b':0}

# create all letters from a to z in a dictionary

# for statement - we can loop over iterables

for i in range(10):
    print(i)
    
# a  range object is iterable
range_object=range(10)
    
# the built in functions in python
# print, len, range
# ord function gives the unicode character value for the chararcter

# 97
ord('a')
# 122
ord('z')

# here
chr(97)

# we need 122 also
for i in range(97,122+1):
    letter = chr(i)
    letter_frequency[letter] = letterlist.count(letter) 

# the tuple is a bit special - it's read only
# you cannot change it

student_tuple = ('Harry','Potter',14,True)

student_tuple[0]
# 'tuple' object does not support item assignment
student_tuple[0]='Voldemort'
# we see tuples a lot of places
# e.g the dimensions for a DataFrame in pandas

# final collections - the set
# elements are unique in a set 

letter_list=['a','b','a','c','d']

unique_letters=set(letter_list)

# if they are not equal - we know we have duplicates
len(unique_letters) == len(letter_list)

unique_letter_list=list(unique_letters)

my_set = {1,2,3,'a','b'}

# what is the intersection of our two sets?
my_set & unique_letters

# you can also add two lists

l1= [1,2,3]
l2=[1,8]

# we get a new list here
list_with_both=l1 + l2

l1[0]=-17

# references - when you work with lists
# you should be aware of that the variable
# is just a reference to the list 

l1= [1,2,3]
l2=[5,8]
# this is not a COPY - it's the same list in RAM they point to
# because it's a reference
l3 = l1

l3[1]=666

# if you want a copy of a list
# use copy
l3 = l1.copy()

l3[1]=42

# or use slicing - that also creates a new list

l3=l1[:]
l3[1]=42

# comprehensions
# while loop

# comprehensions
# we have nice feature in python
# to create a dictionary or a list in one single statement

# imagine - we wan't create a list with numbers up to 1 mio
# _ the thousands seperator
limit=1_000_000

# 64.5 ms 
%%timeit
number_list=[]
for i in range(1,limit+1):
     number_list.append(i)


# in one single line with comprehension expression
#56.6 ms
%%timeit
number_list_comp=[i for i in range(1,limit+1)]

# while loop for python
counter = 1
while counter < 10:
    print(counter)
    counter+=1

# our first lab
# please find this page on Github:
# https://github.com/camillagaardsted/Ghana2025PythonWorkshop
# Find the first lab called 
# Lab1_python_fundamentals_exercise.ipynb
# You decide whether you run python on your own machine
# or use Spyder on the lab machines in Denmark
# lab machines are available at labs.superusers.dk

# Just make a Python script file in Spyder  and type your code
# don't open the notebook exercise - it's just at notebook, så it displays nicely in the browser

# Feel free to just use your local Anaconda installation - you have Spyder installed there
# it's much easier than the connection to labs.superusers.dk

--------------------------------------------------------------------------------------------
Username	Password	Name			Email
---------------------------------------------------------------------------------------------
Kursist01	Pa55w.rd	Freda Attor		freda.attoh@statsghana.gov.gh
Kursist02	Pa55w.rd	Kwamena Leo Akafra	kwamena.arkafra@statsghana.gov.gh
Kursist03	Pa55w.rd	Peter Yeltume Mwinlaaru	peter.mwinlaaru@statsghana.gov.gh
Kursist04	Pa55w.rd	Simon T Onilimor	simon.onilimor@statsghana.gov.gh
Kursist05	Pa55w.rd	Dora Boadi		dora.boadi@statsghana.gov.gh
Kursist06	Pa55w.rd	Rubby Aworka		rubby.aworka@statsghana.gov.gh
Kursist07	Pa55w.rd	Samuel Quarcoo		samuel.quarcoo@statsghana.gov.gh
Kursist08	Pa55w.rd	Rachel Narki Anum	rachel.anum@statsghana.gov.gh
Kursist09	Pa55w.rd	Bernard Osei		bernard.osei@statsghana.gov.gh
Kursist10	Pa55w.rd	Ransford Barths		ransford.barths@statsghana.gov.gh
Kursist11	Pa55w.rd	Mercy Darkwah		mercy.darkwah@statsghana.gov.gh
Kursist12	Pa55w.rd	Samilia Koomson		samilia.mintah@statsghana.gov.gh
Kursist13	Pa55w.rd	Jacqueline Anum		jacqueline.anum@statsghana.gov.gh
Kursist14	Pa55w.rd	Sylvester Agyei-Boadi	sylvester.agyei-boadi@statsghana.gov.gh
Kursist15	Pa55w.rd	Ernest Enyan		enyan.ernest@statsghana.gov.gh
Kursist16	Pa55w.rd	Selaseh Akaho		selaseh.akaho@statsghana.gov.gh
Kursist17	Pa55w.rd	


#####################################################################
# the if statement 
#####################################################################

# input - it always read a string
age  = int(input('Please type your age:'))

if age > 18:
    print('adult')
else:
    print('Under 18 or equal to 18')

# we can run into problems here
# if user types a string or a float
age  = int(input('Please type your age:'))

if age > 18:
    print('adult')
elif  age == 18:
    print('excactly 18')
else:
    print('Under 18')

int('abc',base=16)


try:
    age  = int(input('Please type your age:'))
except:
    print('something went wrong!')



try:
    age  = int(input('Please type your age:'))
except ValueError:
    print('Please type an integer')






