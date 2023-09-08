import pandas
from sklearn import linear_model

df = pandas.read_csv('cars.csv')

x = df[['Weight','Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(x,y)

# predicted the C02 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)


# Predict CO2 Values
# The task in the Multiple Regression chapter was to predict the CO2 emission from a car when you only know its weight
# When the data set is scaled, you will have to use the scale when you predict values:

# Predict the CO2 emission from a 1.3 liter car that weights 2300 kilograms:

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()
df = pandas.read_csv('cars2.csv')

X = df[['Weight','Volume']]
y = df[['CO2']]

scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)



