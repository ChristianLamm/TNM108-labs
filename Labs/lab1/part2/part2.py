import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.cluster import AgglomerativeClustering


customer_data = pd.read_csv('part2/shopping_data.csv')

#print (customer_data.shape)
#print (customer_data.head())

# Remove columns
data = customer_data.iloc[:, 3:5].values

"""
# Show all data points uncolored
labels = range(1, 11)
plt.figure(figsize=(10, 7))
plt.subplots_adjust(bottom=0.1)
plt.scatter(data[:,0],data[:,1], label='True Position')
for label, x, y in zip(labels, data[:, 0], data[:, 1]):
 plt.annotate(label,xy=(x, y),xytext=(-3, 3),textcoords='offset points', ha='right',va='bottom')
#plt.show()
"""
"""
# Show dendrogram of clusters
linked = linkage(data, 'single')
labelList = range(1, 201)  # 200 data points, so labels 1-200
plt.figure(figsize=(10, 7))
dendrogram(linked,
 orientation='top',
 labels=labelList,
 distance_sort='descending',
 show_leaf_counts=True)
plt.show()
"""

"""
# Show colored dots in graph
cluster = AgglomerativeClustering(n_clusters=10, metric='euclidean', linkage='ward')
cluster.fit_predict(data)

plt.scatter(data[:,0],data[:,1], c=cluster.labels_, cmap='rainbow')
plt.show() 
"""

# Apply AgglomerativeClustering with optimal number of clusters
cluster = AgglomerativeClustering(n_clusters=5, metric='euclidean', linkage='ward')
cluster.fit_predict(data)

# Plot the clustered data
plt.figure(figsize=(10, 7))
plt.scatter(data[:,0], data[:,1], c=cluster.labels_, cmap='rainbow', s=50, alpha=0.6)
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('Customer Segments - Hierarchical Clustering')
plt.colorbar(label='Cluster')
plt.show()
