import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def PCAFreq(freqTable,preprocessing):
    '''
    Takes in frequency table dict, converts to nparray, normalizes data, runs PCA for 
    2 principal components and returns data for plotting.
    '''
    
    # Convert dict to nparray
    arr = np.array([list(x.values()) for x in freqTable])
    arr = arr.astype(float)

    if preprocessing == "Normalize":
        # Normalize values
        X = arr / np.linalg.norm(arr)
    elif preprocessing == "Standardize":
        # Standardize values
        scaler = StandardScaler()
        scaler.fit(arr)
        X = scaler.transform(arr)
    else:
        X = arr

    pca = PCA(n_components=2)
    model = pca.fit_transform(X)
    return model