# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 12:50:10 2023

@author: 52331
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:40:11 2023

@author: 52331
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans

X = np.array([[1, 2],
              [5, 8],
              [1.5, 1.8],
              [8, 8],
              [1, 0.6],
              [9, 11]])

kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)
colors = ["g.","r.","c.","y."]

for i in range(len(X)):
    print("Coordinacion:",X[i], "etiqueta:", labels[i])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)


plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)

plt.show()
