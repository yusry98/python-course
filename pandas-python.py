"""
-Pandas is a Python library.
-Pandas is used to analyze data.
-Analyzing, cleaning, exploring, and manipulating data.
-The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis"
    and was created by Wes McKinney in 2008.

Why Use Pandas?
Pandas allows us to analyze big data and make conclusions based on statistical theories.
Pandas can clean messy data sets, and make them readable and relevant.
Relevant data is very important in data science.
Data Science: is a branch of computer science where we study how to store, use and analyze data for deriving information from it.

What Can Pandas Do?
Pandas gives you answers about the data. Like:
-Is there a correlation between two or more columns?
-What is average value?
-Max value?
-Min value?
Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values. This is called cleaning the data
"""

# To import Pandas
import pandas as pd

# Display the pandas library version
print(pd.__version__)

# DataFrame is a structure that contains two-dimensional data and its corresponding labels.
# DataFrames are widely used in data science, machine learning, scientific computing, and @many other data-intensive fields.
# DataFrames are similar to SQL tables or the spreadsheets that you work with in Excel or Calc.

# To import Pandas
import pandas as pd

# Create a car dictionary
car_dictionary = {
    'cars' : ['BMW','Mercedes','McLaren','Jaguar','Porsche'],
    'years' : [2021,2022,2019,2018,2017]
}

# know the datatype of car dictionary
print(type(car_dictionary))
print(car_dictionary)

mycar_dataframe = pd.DataFrame(car_dictionary)
print(mycar_dataframe)
print(type(mycar_dataframe))

print(mycar_dataframe)
print(mycar_dataframe.iloc[3][0])
print(mycar_dataframe['cars'][3])
print(mycar_dataframe['years'][3])
print(mycar_dataframe.loc[3])


# Make a data frame for animal food purchase
import pandas as pd
purchase_1 = pd.Series({'name':'Lee','item purchase': 'dog food','cost': 12.50})
purchase_2 = pd.Series({'name':'Yusoof','item purchase': 'cat food','cost': 10})
purchase_3 = pd.Series({'name':'Wong','item purchase': 'dog food','cost': 13.50})
purchase_4 = pd.Series({'name':'Danial','item purchase': 'fish food','cost': 20.50})
purchase_5 = pd.Series({'name':'Meiya','item purchase': 'tiger food','cost': 21.70})
pdf = pd.DataFrame(
                   [purchase_1,purchase_2,purchase_3,purchase_4,purchase_5],
                   index=['Store 1','Store 2','Store 3','Store 4','Store 5']
                   )
print(pdf.head())
print(pdf.loc['Store 5'])

# Modify the existing label
pdf2 = pd.DataFrame([pdf.loc['Store 2']],index=['Store 10'])
print(pdf)
print(pdf2)

# Fetch only cost information from store 10
print(pdf2.loc['Store 10','cost'])
# Purchase cost for all the store
print(pdf.loc[:,['cost']]) # all the cost will display

# transpose column & row
print(pdf.T)

# Fetch all cost from the store
print(pdf.T.loc['cost'])
print(pdf.T.loc['name'])

# Series data structure
# It is one dimensional array holding data of any type

# Create a simple pandas series from a list
import pandas as pd
marks = [108,98,76,88,67]
print(type(marks))
print(pd.Series(marks))

names = ['David','John','Michael','James','Sue']
names_series = pd.Series(names)
print(names_series)

names = ['David','John','Michael',None,None]
names_series = pd.Series(names)
print(names_series)

# Create one label for panda series
names = ['David','John','Michael','James','Sue']
names_series = pd.Series(names,index=['x','y','z','a','b'])
print(names_series[2])

# Create price list
import pandas as pd

product_price = [25.55,40.99,12.50,15.00,13.49,12.55,40.12,35.12,12.00,47.99]
product_price_series = pd.Series(product_price,index=['Handbag','Watch','Shoes','Keychain','Table','Chair','Rack','Shelf','Pan','Jug'])
print(product_price_series)

# Find total price of all the product
total = 0
for i in product_price_series:
    total += i
print('Total price of all product = ',round(total,2))
print('Total price of all product = ',total)

# Find sum of all value using numpy library
import numpy as np
total = np.sum(product_price_series)
print(total)

# Convert the dictionary to series
car_dictionary ={
    'cars' : ['BMW','Mercedes','McLaren','Jaguar','Porsche'],
    'years' : [2021,2022,2019,2018,2017]
}
car_dictionary_series = pd.Series(car_dictionary)
print(car_dictionary_series)

car_dictionary2 = {
    'car1':'BMW',
    'car2':'Mercedes',
    'car3':'Jaguar',
    'car4':'Nissan'
}
car_dictionary2_series = pd.Series(car_dictionary2)
print(car_dictionary2_series)

# INDEX location
print(car_dictionary2_series.iloc[3])
print(car_dictionary2_series.loc['car3'])

# Count total number of data
print('Total number of data in the series ',len(car_dictionary2))

import numpy as np
import pandas as pd
my_series = pd.Series(np.random.randint(0,1000,500))
print(my_series)
print(my_series.head())
print(my_series.head(100))

# copy one dataframe to another dataframe
copy_dataframe = pdf.copy()
print(copy_dataframe)

# Deleting information from dataframe
del copy_dataframe['item purchase']
print(copy_dataframe)

# Deleting row information from the dataframe
copy_dataframe=copy_dataframe.drop('Store 2')
print(copy_dataframe)

# skip the column
copy_dataframe2 = copy_dataframe.drop('name',axis=1)
print(copy_dataframe2)

# Load file into the dataframe
"""
A CSV (comma-separated values) file is a text file that has a 
specific format which allows data to be saved in a table structured format.
"""

import pandas as pd
df = pd.read_csv('NASA.csv')
print(df)
print(df.head())
print(df.head(20))
print(df.tail()) # display the top 5 from the bottom
print(df.tail(10))









