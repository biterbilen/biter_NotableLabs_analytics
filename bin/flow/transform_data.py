import numpy as np

def hlog(x, b=500):
    x if (x<b) else np.log(x)

def transform(dta, type='hlog', b=500, channels=None):
    if type == 'hlog':
        f = lambda(x): [xi if (xi<b) else np.log(xi) for xi in x]
    elif type == 'arcsinh':
        f = lambda(x): np.arcsinh(x) 
    tdta = dta.loc[:,channels].apply(f)

    return tdta
