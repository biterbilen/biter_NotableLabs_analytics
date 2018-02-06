from sklearn.model_selection import train_test_split

from get_data import get_input

def split(dta, test_size=None, stratify=False, verbose=False):
    X, y = get_input(dta=dta, split_xy=True, verbose=True)
    
    # TODO fixme this does not work
    if stratify:
        stratify = y
    else:
        stratify = None
    X_train, X_test, y_train, y_test = train_test_split(X, 
                                                        y, 
                                                        test_size=test_size, 
                                                        stratify=y)
    if verbose:
        print 'X_train_shape:', X_train.shape, 'X_test_shape:', X_test.shape, \
            '\n', y_train.describe(), '\n', y_train[0:5], \
            '\n', y_test.describe(),  '\n', y_test[0:5]
            
    return X_train, X_test, y_train, y_test         
                
def test_split():
    idir = "../../data/live_dead_debris/"
    ifile = "../../data/live_dead_debris/live_dead_debris__labels.csv"  
    dta = get_input(idir, ifile, split_xy=False, pattern='*9.fcs', verbose=True)

    print '\nstratify=False:\n'
    split(dta, stratify=False, verbose=True)
    print '\nstratify=True: FIXME does not work\n'
    split(dta, stratify=True, verbose=True)
    print '\ntest_size=0.1:\n'
    split(dta, test_size=0.1, verbose=True)

    