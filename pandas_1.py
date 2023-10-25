#Pandas is a Python library used for working with data sets.
#It has functions for analyzing, cleaning, exploring, and manipulating data.
#The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis".

import pandas as pd
#DataFrames
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df) 

#refer to the row index
print(df.loc[0])

#loading data from csv to a dtatframe
df = pd.read_csv('data.csv')

#to read a json file
df1=pd.read_json('data.json')

#CLEANING DATA

#removing empty rows
new_df=df.dropna()
#returns a new DataFrame

df.dropna(inplace = True)
#changes the original DataFrame

#replace specific columns in the original dataset
df["Calories"].fillna(130, inplace = True)

#or by mean, median or mode
x=df['Calories'].mean()
df["Calories"].fillna(x, inplace = True)

#to drop duplicates from the original DataFrame
df.drop_duplicates(inplace=True)


#show correlation between each column in the dataset
df.corr()

