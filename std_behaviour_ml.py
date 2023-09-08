# Import library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# To read csv file
dataset = pd.read_csv('Student_Behaviour.csv')
print(dataset)

# Extracting independent variables
X = dataset.iloc[:, :-5].values
print(X)
# Extracting dependent variables
Y = dataset.iloc[:, 5].values  # Display column
print(Y)

# Handling missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:7])
X[:, 1:7] = imputer.transform(X[:, 1:7])
print(X)

# Encoding the independent variabble
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
print(X)