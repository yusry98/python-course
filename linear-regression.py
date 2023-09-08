# Start by drawing a scatter plot:
# importing libraries
import matplotlib.pyplot as plt
# Create array to store data points
from yellowbrick import regressor

x = [5,7,8,7,2,17,2,9,4,11,12,9,6] # 13 cars - x-axis represents age
y = [99,86,87,88,111,86,103,87,94,78,77,85,86] #y-axis represents spee
# Data points
plt.scatter(x, y) # Simple scatter 2D GRAPH
plt.show() # Display scatter graph


# linear regression
# importing libraries
import matplotlib.pyplot as plt
from scipy import stats
# Create array to store data points
x = [5,7,8,7,2,17,2,9,4,11,12,9,6] # 13 cars - x-axis represents age
y = [99,86,87,88,111,86,103,87,94,78,77,85,86] #y-axis represents speed
# Execute a method that returns some important key values of Linear Regression
slope, intercept, r, p, std_err = stats.linregress(x,y)
# Create a function that uses the slope and intercept values to return a new value
def myfunc(x):
    return slope * x + intercept
mymodel = list(map(myfunc, x)) # Run each value of the x array through the function
# This will result in a new array with new values for the y-axis
plt.scatter(x, y) # Draw the original scatter plot
plt.plot(x,mymodel) # Draw the line of linear regression
plt.show() # Display scatter graph


# linear regression
# Predict the speed of a 10 years old car
# importing libraries
import matplotlib.pyplot as plt
from scipy import stats
# Create array to store data points
x = [5,7,8,7,2,17,2,9,4,11,12,9,6] # 13 cars - x-axis represents age
y = [99,86,87,88,111,86,103,87,94,78,77,85,86] #y-axis represents speed
# Execute a method that returns some important key values of Linear Regression
slope, intercept, r, p, std_err = stats.linregress(x,y)
# Create a function that uses the slope and intercept values to return a new value
def myfunc(x):
    return slope * x + intercept
speed = myfunc(10)
print(speed)
mymodel = list(map(myfunc, x)) # Run each value of the x array through the function
# This will result in a new array with new values for the y-axis
plt.scatter(x, y) # Draw the original scatter plot
plt.plot(x,mymodel) # Draw the line of linear regression
plt.show() # Display scatter graph

# linear regression
# To predict the employee salary based on their experience
import matplotlib.pyplot as plt
from scipy import stats
x = [2,5,3,8,9,10,15,20,25,30] #Employee year of experience
y = [1000,2500,2100,3500,4000,4200,5000,6000,7000,8000] #Employee Salary
# Execute a method that returns some important key values of Linear Regression
slope, intercept, r, p, std_err = stats.linregress(x,y)
# Create a function that uses the slope and intercept values to return a new value
def myfunc(x):
    return slope * x + intercept
year1 = myfunc(1)
print('1 year experience salary: ',round(year1,2))
year10 = myfunc(10)
print('10 year experience salary: ',round(year10,2))
year12 = myfunc(12)
print('12 year experience salary: ',round(year12,2))
year33 = myfunc(33)
print('33 year experience salary: ',round(year33,2))
year40 = myfunc(40)
print('40 year experience salary: ',round(year40,2))
mymodel = list(map(myfunc, x)) # Run each value of the x array through the function
# This will result in a new array with new values for the y-axis
plt.scatter(x, y) # Draw the original scatter plot
plt.plot(x,mymodel) # Draw the line of linear regression
plt.show() # Display scatter graph


x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]
slope, intercept, r, p, std_err = stats.linregress(x, y)
print(r)
# The result: 0.013 indicates a very bad relationship
# and tells us that this data set is not suitable for linear regression


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:,:-1].values # Independent variable
y = dataset.iloc[:,-1].values # Dependent variable
print(dataset)
print(X)
print(y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
print('X_train : ', X_train)
print('y_train : ', y_train)
print('X_test : ', X_test)
print('y_test : ', y_test)

plt.scatter(X_train, y_train, color = 'red')
plt.scatter(X_train, regressor.predict(X_train), color = 'green')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show





















