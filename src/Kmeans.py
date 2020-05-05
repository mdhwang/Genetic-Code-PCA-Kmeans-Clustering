from sklearn.cluster import KMeans
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def Kmeans(pca_data):
    X = pca_data
    kmeans = KMeans(n_clusters=7, random_state=0).fit(X)


    cen = kmeans.cluster_centers_

    fig = plt.figure(figsize=(10,10))
    fig.suptitle("K Means Clustering of PCA Charts of n = 3",fontsize = 36,)
    fig.subplots_adjust(hspace=0.4, wspace=0.4)
    plot = sns.scatterplot(pca_data[:,0], 
                            pca_data[:,1], 
                            hue=kmeans.predict(X),
                            palette="Set1")
    plot = sns.scatterplot(cen[:,0],
                            cen[:,1],
                            hue=kmeans.predict(cen),
                            palette="Set1",
                            s=1000,
                            alpha=.25)
    plot.legend_.remove()
    plt.xlabel('Principal Component 1',fontsize=16)
    plt.ylabel('Principal Component 2',fontsize=16)