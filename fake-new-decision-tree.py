# importing libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter("ignore")

# import dataset
df=pd.read_csv('news.csv')
print(df)

# View info of the dataframe
df.info()

# Check for null values. Use the is null method for it.
df.isnull().sum()
# We can see that all values are 0. It shows that there are no null values in the dataset. So we can move further without changing anything in the dataset.

# View the shape. This shaping method gives the number of rows and the number of columns in it.
print("There are {} rows and {} columns.".format(df.shape[0],df.shape[1]))

"""
The statistical description shows details like count (non-null values in the column), mean, standard deviation, 
minimum value, maximum values, and finally percentiles of the values in that column. 
"""
# View the statistical description of the data frame
df.describe()

"""
In our data frame, we have only one numerical column so it will give a description for only one column. 
But we don’t need this column for building our model.
"""
#Let's drop unimportant columns
df=df.drop(['Unnamed: 0'],axis=1)
# Now view the final updated data frame.
df

"""
Let us see how much Real news and how much Fake news was there in the dataset. 
The value counts method actually returns the count of a particular variable in a given feature.
"""
df['label'].value_counts()
# probability is almost 0.5 for the news being fake

# Visualize the count plot using the seaborn library.
plt.figure(figsize=(5,10));
sns.countplot(df['label']);

"""
For creating a model, first, we have to define x and y in which x contains all 
independent features of the dataset and y contains a dependent feature that is labelled.
"""
x = df.iloc[ : , :-1].values
y = df.iloc[ : , -1].values

"""
As we are working with text data, we have to use a count vectorizer for it. It is actually 
used to transform our text into a vector on the basis of the frequency of each word which means 
how many times the word is repeated in the entire text.

It is available in the sci-kit learn library.

Fit_transform is used on the training dataset because it will scale our training data and learn the 
scaling parameters. With this, our model will learn the mean and variance of the features that are 
there in this training dataset. These parameters are used to work with test data.
"""
# Import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
vect=CountVectorizer(stop_words="english",max_features=1000)
x1=vect.fit_transform(x[:,0]).todense()
x2=vect.fit_transform(x[:,1]).todense()
x_mat=np.hstack((x1,x2))
#Let’s view the final matrix that was created.
print(x_mat)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(x_mat,y,random_state=1000)

# Training the Decision Tree Classification model on the Training set
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(criterion='entropy')
model.fit(x_train,y_train)

# Predicting the Test set results
y_pred=model.predict(x_test)

"""
Now we will see the accuracy and confusion matrix for the model that we built.
For that import accuracy_score and confusion_matrix from the sci-kit learn library.
from sklearn.metrics import accuracy_score,confusion_matrix
"""
# Accuracy
from sklearn.metrics import accuracy_score,confusion_matrix
accuracy = accuracy_score(y_pred,y_test)*100
print("Accuracy of the model is {:.2f}".format(accuracy))

# Confusion matrix
confusion_matrix(y_pred,y_test)


