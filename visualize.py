# I'm not sure what the "python norms" of file naming is, but this file is dedicated to 
# visualizing and analyzing data (the step you do before data engineering I think)

import pandas as pd # data processing and analysis
import matplotlib # functions that visualize things
import numpy as np # linear algebra/scientific computing
import sklearn #collection of machine learning algorithms

# Since this is a Kaggle competition, I'm keeping the data dir the same
raw_data = pd.read_csv("kaggle/input/titanic/train.csv")
val_data = pd.read_csv("kaggle/input/titanic/test.csv")

"""
Data variable explanations:
-Survived | the thing we're predicting: 1 = survived, 0 = !survived
-PassengerId | unique id of a person
-Pclass | socio-economic status, 1=upper, 2=middle, 3=lower
-Name, Sex, Age -> self-explanatory
-SibSp | # of siblings and spouse
-Parch | # of parents and children
-Ticket, Fare, Cabin -> self-explanatory-ish
Embarked | port of embarkation: C=Cherbourg, Q=Queenstown, S=Southampton
"""

# Previewing data
dash = 100

print("Number of Training Examples: {}".format(raw_data.shape[0]))
print("Number of Testing Examples: {}".format(val_data.shape[0]))
print("-"*dash)

print("Train Fields: ",raw_data.columns) # reveals all the columsn in an array
print("Test Fields: ",val_data.columns)
print("-"*dash)

print(">>>>>>Train data<<<<<<")
print(raw_data.info()) # reveals columns, # of non-null fields, and the column datatype
print(raw_data.isnull().sum()) # tallies the null vlaues in the data set
print(raw_data.describe(include = 'all')) # prints out statistical data regarding the info
print(raw_data.head()) #prints first few rows of the data
print("-"*dash)

# print(">>>>>>Test data<<<<<<")
# print("Info:",val_data.info())
# print(val_data.isnull().sum())
# print(val_data.describe(include = 'all'))
# print(val_data.head())
# print("-"*dash)

"""
Findings:
- There are a lot of null columns (age, fare, cabin, embarked)
- Ticket/Passenger ID probably mean something, but it looks like gibberish to me (so I'll probably exclude it)
- There are so many cabin nulls, will probably drop that too

Dealing with nulls:
- Age | median
- Fare | median
- Embark | mode

Dropping:
- Cabin
- Ticket
- Passenger ID
"""