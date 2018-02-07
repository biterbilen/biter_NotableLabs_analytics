from sklearn.mixture import GaussianMixture

def predict(mod, X, clusters_to_classes=False):
    preds = mod.predict(X) 
    return preds
    
