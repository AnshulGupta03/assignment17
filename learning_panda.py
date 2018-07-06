#Q.1 - Create a dataframe with your name , age , mail id and phone number and add your friends’s information to the same.
import pandas as pd
import numpy as np
print("Question 1:\n")
print("empty dataframe:")
df = pd.DataFrame()
print(df)
context = {
        'name':['anmol','aman','riya'],
        'age':[13,20,15],
        'email':['anmol@gmail.com','aman@gmail.com','riya@gmail.com'],
        'phone_no':[9992021212,9991291345,1234967543]
        }
print("\n\nDataframe after adding information:")
df = pd.DataFrame(context)
print(df)


print("\n\n")




#Q.2 - Import the data and print the following :
#a.) First 5 rows of Dataframe 
#b.) First 10 rows of the Dataframe 
#c.) find basic statistics on the particular dataset. 
#d.) Find the last 5 rows of the dataframe 
#e.) Extract the 2nd column and find basic statistics on it

print("Question 2:\n")
file = pd.read_csv("weather.csv")

print("First 5 rows:\n",file.head())
print("\n\nFirst 10 rows:\n",file.head(10))
print("\n\nBasic statistics:\n")
print("descibe:\n",file.describe(include='all'))
print("sum:\n",file.sum())
print("mean:\n",file.mean())
print("\n\nLast 5 rows:\n",file.tail())
print("\n\nBasic statistics of 2nd column:\n",file.loc[:,['Location']].describe())

