# import libraries
import numpy as np
import pandas as pd

#%% read data and clean dataset from Nan  infinity or a value too large for dtype('float64')
data = pd.read_csv('framingham.csv')
print(data)

print(data.info())

def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)
clean_dataset(data)

#%% prepare data
y = data.TenYearCHD
y= y.iloc[0:3000]
x_data = data.drop("TenYearCHD",axis = 1)
# %% normalization
x = (x_data - np.min(x_data))/(np.max(x_data)-np.min(x_data)).values
x = x.iloc[0:3000]

#train_test_split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2,random_state=42)

x_train = x_train.T
x_test = x_test.T
y_train = y_train.T
y_test = y_test.T

print("x_train: ",x_train.shape)
print("x_test: ",x_test.shape)
print("y_train: ",y_train.shape)
print("y_test: ",y_test.shape)

#%% sklearn with LR
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(x_train.T,y_train.T)
print("test accuracy {}".format(lr.score(x_test.T,y_test.T)))