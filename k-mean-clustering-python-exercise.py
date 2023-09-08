# https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/?

# importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# reading the data and looking at the first five rows of the data
data=pd.read_csv("Wholesale customers data.csv")
data.head()

"""
We have the spending details of customers on different products like Milk, Grocery, Frozen, Detergents, etc. 
Now, we have to segment the customers based on the provided details. Before doing that, let’s pull out some 
statistics related to the data
"""
# statistics of the data
data.describe()

"""
Here, we see that there is a lot of variation in the magnitude of the data. 
Variables like Channel and Region have low magnitude whereas variables like Fresh, Milk, Grocery, etc. 
have a higher magnitude.Since K-Means is a distance-based algorithm, this difference of magnitude can 
create a problem. So let’s first bring all the variables to the same magnitude
"""

# standardizing the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# statistics of scaled data
pd.DataFrame(data_scaled).describe()

# defining the kmeans function with initialization as k-means++
kmeans = KMeans(n_clusters=2, init='k-means++')

# fitting the k means algorithm on scaled data
kmeans.fit(data_scaled)

# inertia on the fitted data
kmeans.inertia_

"""
We got an inertia value of almost 2600. Now, let’s see how we can use the elbow curve to 
determine the optimum number of clusters in Python.We will first fit multiple k-means models 
and in each successive model, we will increase the number of clusters. We will store the inertia 
value of each model and then plot it to visualize the result
"""

# fitting multiple k-means algorithms and storing the values in an empty list
SSE = []
for cluster in range(1,20):
    kmeans = KMeans(n_jobs = -1, n_clusters = cluster, init='k-means++')
    kmeans.fit(data_scaled)
    SSE.append(kmeans.inertia_)

# converting the results into a dataframe and plotting them
frame = pd.DataFrame({'Cluster':range(1,20), 'SSE':SSE})
plt.figure(figsize=(12,6))
plt.plot(frame['Cluster'], frame['SSE'], marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')

# k means using 5 clusters and k-means++ initialization
kmeans = KMeans(n_jobs = -1, n_clusters = 5, init='k-means++')
kmeans.fit(data_scaled)
pred = kmeans.predict(data_scaled)

# value count of points in each of the above-formed clusters
frame = pd.DataFrame(data_scaled)
frame['cluster'] = pred
frame['cluster'].value_counts()

