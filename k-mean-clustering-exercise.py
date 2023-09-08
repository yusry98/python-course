# https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/?

# Import libraries
import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('clustering.csv')
data.head()

"""
We will be taking only two variables from the data – “LoanAmount” and “ApplicantIncome”. 
This will make it easy to visualize the steps as well. Let’s pick these two variables and 
visualize the data points
"""
X = data[["LoanAmount","ApplicantIncome"]]
#Visualise data points
plt.scatter(X["ApplicantIncome"],X["LoanAmount"],c='black')
plt.xlabel('AnnualIncome')
plt.ylabel('Loan Amount (In Thousands)')
plt.show()

"""
Steps 1 and 2 of K-Means were about choosing the number of clusters (k) and selecting random centroids for each cluster. 
We will pick 3 clusters and then select random observations from the data as the centroids
"""
# Step 1 and 2 - Choose the number of clusters (k) and select random centroid for each cluster
#number of clusters
K=3
# Select random observation as centroids
Centroids = (X.sample(n=K))
plt.scatter(X["ApplicantIncome"],X["LoanAmount"],c='black')
plt.scatter(Centroids["ApplicantIncome"],Centroids["LoanAmount"],c='red')
plt.xlabel('AnnualIncome')
plt.ylabel('Loan Amount (In Thousands)')
plt.show()
"""
Here, the red dots represent the 3 centroids for each cluster. Note that we have chosen these points randomly 
and hence every time you run this code, you might get different centroids
"""

# Next, we will define some conditions to implement the K-Means Clustering algorithm
# Step 3 - Assign all the points to the closest cluster centroid
# Step 4 - Recompute centroids of newly formed clusters
# Step 5 - Repeat step 3 and 4

diff = 1
j=0

while(diff!=0):
    XD=X
    i=1
    for index1,row_c in Centroids.iterrows():
        ED=[]
        for index2,row_d in XD.iterrows():
            d1=(row_c["ApplicantIncome"]-row_d["ApplicantIncome"])**2
            d2=(row_c["LoanAmount"]-row_d["LoanAmount"])**2
            d=np.sqrt(d1+d2)
            ED.append(d)
        X[i]=ED
        i=i+1

    C=[]
    for index,row in X.iterrows():
        min_dist=row[1]
        pos=1
        for i in range(K):
            if row[i+1] < min_dist:
                min_dist = row[i+1]
                pos=i+1
        C.append(pos)
    X["Cluster"]=C
    Centroids_new = X.groupby(["Cluster"]).mean()[["LoanAmount","ApplicantIncome"]]
    if j == 0:
        diff=1
        j=j+1
    else:
        diff = (Centroids_new['LoanAmount'] - Centroids['LoanAmount']).sum() + (Centroids_new['ApplicantIncome'] - Centroids['ApplicantIncome']).sum()
        print(diff.sum())
    Centroids = X.groupby(["Cluster"]).mean()[["LoanAmount","ApplicantIncome"]]

"""
These values might vary every time we run this. Here, we are stopping the training when the 
centroids are not changing after two iterations. We have initially defined the diff as 1 
and inside the while loop, we are calculating this diff as the difference between the centroids 
in the previous iteration and the current iteration.When this difference is 0, we are stopping the training.
"""

# Visualize the clusters
color=['blue','green','cyan']
for k in range(K):
    data=X[X["Cluster"]==k+1]
    plt.scatter(data["ApplicantIncome"],data["LoanAmount"],c=color[k])
plt.scatter(Centroids["ApplicantIncome"],Centroids["LoanAmount"],c='red')
plt.xlabel('Income')
plt.ylabel('Loan Amount (In Thousands)')
plt.show()
# The red dots represent the centroid of each cluster.