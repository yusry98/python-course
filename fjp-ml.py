X = data.iloc[:,:-1].values
print(X)

# Extracting dependent variable
Y = data.iloc[:,3].values
print(Y)

# Encoding independent variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(),[0])],remainder='passthrough')
X = np.array(ct.fit_transform(X))
print(X)

from sklearn.model_selection import train_test_split
X_train,X_test ,y_train,y_test = train_test_split(data.country, data.fraudulent ,test_size =0.2,random_state=1)
print(X_train)
print(X_test)
print(y_train)
print(y_test)

# feature scalling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
st_X = StandardScaler()
X_train = st_X.fit_transform(X_train)
X_test = st_X.fit_transform(X_test)
print(X_train)




