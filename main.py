import pandas as pd # data processing and analysis
# import matplotlib # functions that visualize things
import numpy as np # linear algebra/scientific computing
import sklearn #collection of machine learning algorithms


# Competition is on Kaggle, but wanted to have something ML on GitHub
raw_data = pd.read_csv("kaggle/input/titanic/train.csv")
val_data = pd.read_csv("kaggle/input/titanic/test.csv")

"""
Data Analysis:
-PassengerId | unique id of a person
-Survived | dependent variable: 1 = survived, 0 = !survived
-Pclass | socio-economic status, 1=upper, 2=middle, 3=lower
-Name, Sex, Age -> self-explanatory
-SibSp | # of siblings and spouse
-Parch | # of parents and children
-Ticket, Fare, Cabin -> self-explanatory-ish
Embarked | C=Cherbourg, Q=Queenstown, S=Southampton

Things not worth considering:
-PassengerId + Ticket | random unique identifiers don't provide more info
-Cabin | way too many null values 

Dealing with nulls:
-Age | median
-Embark | mode
"""

dash = 20

print("Number of Training Examples: {}".format(raw_data.shape[0]))
print("Number of Testing Examples: {}".format(val_data.shape[0]))
print("-"*dash)

print("Train Fields: ",raw_data.columns)
print("Test Fields: ",val_data.columns)
print("-"*dash)

print("Null train data: ")
# print("Info:",raw_data.info())
print(raw_data.isnull().sum())
print(raw_data.describe(include = 'all'))
print("-"*dash)

print("Null test data: ")
# print("Info:",val_data.info())
print(val_data.isnull().sum())
print(val_data.describe(include = 'all'))
print("-"*dash)


# print(raw_data.sample(3))