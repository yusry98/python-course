# Import libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # for data visualization purposes
import seaborn as sns # for statistical data visualization
import warnings
warnings.filterwarnings('ignore')

# Read data
data = 'adult.csv'

df = pd.read_csv(data, header=None, sep=',\s')

df.shape

df.head()

# Rename column names
"""
We can see that the dataset does not have proper column names. The columns are 
merely labelled as 0,1,2.... and so on. We should give proper names to the columns
"""
col_names = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation', 'relationship',
             'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income']

df.columns = col_names

df.columns

# Preview the dataset
df.head()

# view summary of dataset
df.info()

# find categorical variables
categorical = [var for var in df.columns if df[var].dtype=='O']
print('There are {} categorical variables\n'.format(len(categorical)))
print('The categorical variables are :\n\n', categorical)

# View the categorical variables
df[categorical].head()

"""
Summary of categorical variables
1.There are 9 categorical variables.
2.The categorical variables are given by workclass, education, marital_status, occupation, relationship, race, sex, native_country and income.
3.income is the target variable.
"""

# Check missing values in categorical variables
df[categorical].isnull().sum()

# view frequency counts of values in categorical variables
for var in categorical:
    print(df[var].value_counts())

# view frequency distribution of categorical variables
for var in categorical:
    print(df[var].value_counts() / np.float(len(df)))

"""
Now, we can see that there are several variables like workclass, occupation and native_country 
which contain missing values. Generally, the missing values are coded as NaN and python will detect 
them with the usual command of df.isnull().sum().But, in this case the missing values are coded as ?. 
Python fail to detect these as missing values because it do not consider ? as missing values. So, I have to replace ? 
with NaN so that Python can detect these missing values.I will explore these variables and replace ? with NaN.
"""

# check labels in workclass variable
df.workclass.unique()

# check frequency distribution of values in workclass variable
df.workclass.value_counts()

# replace '?' values in workclass variable with `NaN`
df['workclass'].replace('?', np.NaN, inplace=True)

# again check the frequency distribution of values in workclass variable
df.workclass.value_counts()

# check labels in occupation variable
df.occupation.unique()

# check frequency distribution of values in occupation variable
df.occupation.value_counts()

# replace '?' values in occupation variable with `NaN`
df['occupation'].replace('?', np.NaN, inplace=True)

# again check the frequency distribution of values in occupation variable
df.occupation.value_counts()

# check labels in native_country variable
df.native_country.unique()

# check frequency distribution of values in native_country variable
df.native_country.value_counts()

# replace '?' values in native_country variable with `NaN`
df['native_country'].replace('?', np.NaN, inplace=True)

# again check the frequency distribution of values in native_country variable
df.native_country.value_counts()

# Check missing values in categorical variables again
df[categorical].isnull().sum()

"""
The number of labels within a categorical variable is known as cardinality.
A high number of labels within a variable is known as high cardinality. 
High cardinality may pose some serious problems in the machine learning model. 
So, I will check for high cardinality.
"""
# check for cardinality in categorical variables
for var in categorical:
    print(var, ' contains ', len(df[var].unique()), ' labels')

# find numerical variables
numerical = [var for var in df.columns if df[var].dtype!='O']
print('There are {} numerical variables\n'.format(len(numerical)))
print('The numerical variables are :', numerical)

# view the numerical variables
df[numerical].head()

"""
Summary of numerical variables
There are 6 numerical variables.
These are given by age, fnlwgt, education_num, capital_gain, capital_loss and hours_per_week.
All of the numerical variables are of discrete data type.
"""

# check missing values in numerical variables
df[numerical].isnull().sum()

# Declare feature vector and target variable
X = df.drop(['income'], axis=1)
y = df['income']

# split X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

# check the shape of X_train and X_test
X_train.shape, X_test.shape

# 34. check data types in X_train
X_train.dtypes

# 35. display categorical variables
categorical = [col for col in X_train.columns if X_train[col].dtypes == 'O']
print(categorical)

# 36. display numerical variables
numerical = [col for col in X_train.columns if X_train[col].dtypes != 'O']
print(numerical)

# 37. print percentage of missing values in the categorical variables in training set
X_train[categorical].isnull().mean()

# 38. print categorical variables with missing data
for col in categorical:
    if X_train[col].isnull().mean()>0:
         print(col, (X_train[col].isnull().mean()))

# 39. impute missing categorical variables with most frequent value
for df2 in [X_train, X_test]:
     df2['workclass'].fillna(X_train['workclass'].mode()[0], inplace=True)
     df2['occupation'].fillna(X_train['occupation'].mode()[0], inplace=True)
     df2['native_country'].fillna(X_train['native_country'].mode()[0], inplace=True)

# 40. Check mssing values in categorical variables in X_train
X_train[categorical].isnull().sum()

# 41. check missing values in categorical variables in X_test
X_test[categorical].isnull().sum()

# 42. check missing values in X_train
X_train.isnull().sum()

# 43. check missing values in X_test
X_test.isnull().sum()

# 44. print categorical variables
print(categorical)

# 45.
X_train[categorical].head()

# 46. import category encoders
import category_encoders as ce

# 47. encode remaining variables with one-hot encoding
encoder = ce.OneHotEncoder(cols=['workclass', 'education', 'marital_status', 'occupation', 'relationship',
                                 'race', 'sex', 'native_country'])
X_train = encoder.fit_transform(X_train)
X_test = encoder.transform(X_test)

# 48.
X_train.head()

# 49.
X_train.shape

# 50.
X_test.head()

# 51.
X_test.shape

# Feature Scaling
# 52.
cols = X_train.columns

# 53.
from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 54.
X_train = pd.DataFrame(X_train, columns=[cols])

# 55.
X_test = pd.DataFrame(X_test, columns=[cols])

# 56.
X_train.head()

# Model Training
# 57. train a Gaussian Naive Bayes classifier on the training set
from sklearn.naive_bayes import GaussianNB
# instantiate the model
gnb = GaussianNB()
# fit the model
gnb.fit(X_train, y_train)

# 58. Predict the results
y_pred = gnb.predict(X_test)
print(y_pred)

# 59. Check accuracy score
from sklearn.metrics import accuracy_score
print('Model accuracy score: {0:0.4f}'. format(accuracy_score(y_test, y_pred)))

# 60. Compare the train-set and test-set accuracy to check for overfitting
y_pred_train = gnb.predict(X_train)
print(y_pred_train)
# 61.
print('Training-set accuracy score: {0:0.4f}'. format(accuracy_score(y_train, y_pred_train)))

# Check for overfitting and underfitting
# 62. print the scores on training and test set
print('Training set score: {:.4f}'.format(gnb.score(X_train, y_train)))
print('Test set score: {:.4f}'.format(gnb.score(X_test, y_test)))
"""
The training-set accuracy score is 0.8067 while the test-set accuracy to be 0.8083. 
These two values are quite comparable. So, there is no sign of overfitting
"""

"""
Compare model accuracy with null accuracy¶
So, the model accuracy is 0.8083. But, we cannot say that our model is very good based on the above accuracy. We must compare it with the null accuracy. Null accuracy is the accuracy that could be achieved by always predicting the most frequent class.

So, we should first check the class distribution in the test set.
"""

# 63. check class distribution in test set
y_test.value_counts()
"""
We can see that the occurences of most frequent class is 7407. 
So, we can calculate null accuracy by dividing 7407 by total number 
of occurences.
"""

# 64. check null accuracy score
null_accuracy = (7407/(7407+2362))
print('Null accuracy score: {0:0.4f}'. format(null_accuracy))
"""
We can see that our model accuracy score is 0.8083 but null accuracy score is 
0.7582. So, we can conclude that our Gaussian Naive Bayes Classification model is 
doing a very good job in predicting the class labels.Now, based on the above analysis we 
can conclude that our classification model accuracy is very good. Our model is doing a very good 
job in terms of predicting the class labels.
"""

"""
But, it does not give the underlying distribution of values. Also, 
it does not tell anything about the type of errors our classifer is making.
We have another tool called Confusion matrix that comes to our rescue.
"""
# Print the Confusion Matrix and slice it into four pieces
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print('Confusion matrix\n\n', cm)
print('\nTrue Positives(TP) = ', cm[0,0])
print('\nTrue Negatives(TN) = ', cm[1,1])
print('\nFalse Positives(FP) = ', cm[0,1])
print('\nFalse Negatives(FN) = ', cm[1,0])

"""
The confusion matrix shows 5999 + 1897 = 7896 correct predictions and 
1408 + 465 = 1873 incorrect predictions.
In this case, we have:
True Positives (Actual Positive:1 and Predict Positive:1) - 5999
True Negatives (Actual Negative:0 and Predict Negative:0) - 1897
False Positives (Actual Negative:0 but Predict Positive:1) - 1408 (Type I error)
False Negatives (Actual Positive:1 but Predict Negative:0) - 465 (Type II error)
"""

# visualize confusion matrix with seaborn heatmap
cm_matrix = pd.DataFrame(data=cm, columns=['Actual Positive:1', 'Actual Negative:0'],
                                 index=['Predict Positive:1', 'Predict Negative:0'])
sns.heatmap(cm_matrix, annot=True, fmt='d', cmap='YlGnBu')


