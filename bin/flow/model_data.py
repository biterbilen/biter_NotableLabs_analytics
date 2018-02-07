from sklearn.mixture import GaussianMixture
import numpy as np

def model(X, y, max_iter=20):
    n_classes = len(np.unique(y))

    mod = GaussianMixture(n_components=n_classes, max_iter=max_iter)
    mod.fit(X)
    
    return mod

    