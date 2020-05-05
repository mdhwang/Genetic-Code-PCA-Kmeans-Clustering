import numpy as np
from sklearn.decomposition import PCA

def PCAFreq(freqTable):
    X = np.array([list(x.values()) for x in freqTable])
    pca = PCA(n_components=2)
    model = pca.fit_transform(X)
    return model