from sklearn.mixture import GaussianMixture
import numpy as np

def model(X, y, max_iter=20):
    n_classes = len(np.unique(y))

    #np.concatenate((X,y[:, np.newaxis]), axis=1)

    mod            = GaussianMixture(n_components=n_classes, max_iter=max_iter)
    # initialize means with known class labels
    #mod.means_init = np.array([X[y == i].mean(axis=0) for i in range(n_classes)])

    mod.fit(X)
    
    return mod

    