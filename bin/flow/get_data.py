from glob import glob as gg
import re

import pandas as pd

import fcsparser

def get_X(idir, pattern='*.fcs', verbose=False):
    """ read input X """
    fnames = gg(idir + pattern)
    X = None
    for f in fnames:
        meta, dta = fcsparser.parse(f, meta_data_only=False, reformat_meta=True)
        name = meta['$FIL'] + '_' + str(dta.shape[0])
        dtax = pd.DataFrame({'name':name, 
                             'event':dta.index + 1, 
                             'wellid':re.split('-', meta['WellID'])[2]})
        dta  = pd.concat([dta, dtax], axis=1)
        X    = pd.concat([X, dta], ignore_index=True)
        if verbose:
            print f, dta.shape, X.shape
    return X

def test_get_X():
    idir = "../../data/live_dead_debris/"
    X = get_X(idir, '*9.fcs', verbose=True)
    print '\ntest_get_X filenames ending with 9...', 'shape:', X.shape, '\n', X.head(3).iloc[:,0:5]
    X = get_X(idir, verbose=True)
    print '\ntest_get_X all filenames...', 'shape:', X.shape, '\n', X.head(3).iloc[:,0:5]
    return

def get_y(ifile, n=None): 
    """ read input y """ 
    y = pd.read_csv(ifile, nrows=n)
    return y

def test_get_y():
    """ tested """
    ifile = "../../data/live_dead_debris/live_dead_debris__labels.csv"   
    y = get_y(ifile, 10)
    print '\ntest_get_y with 10 rows...', 'shape:', y.shape, '\n', y.head(2).iloc[:,0:5]
    y = get_y(ifile)
    print '\ntest_get_y all...', 'shape:', y.shape, "\n", y.head(2).iloc[:,0:5]
    
def get_input(idir=None, ifile=None, dta=None, split_xy=False, pattern='*.fcs', verbose=False):
    """ read input from file and/or split"""
    if dta is None:
        X   = get_X(idir, pattern=pattern, verbose=verbose)
        y   = get_y(ifile)
        dta = pd.merge(X, y)
    if split_xy:
        y = dta['label']
        X = dta.drop(['name', 'event', 'label', 'wellid'], axis=1)
        return X, y
    else:
        return dta
                 
def test_get_input():
    idir = "../../data/live_dead_debris/"
    ifile = "../../data/live_dead_debris/live_dead_debris__labels.csv"  
    dta = get_input(idir, ifile, split_xy=False, pattern='*9.fcs', verbose=True)
    print '\ntest_get_input split_xy=False ...', 'shape dta:', dta.shape, \
          '\n', dta.head(2).iloc[:,0:5]
    X, y = get_input(dta=dta, split_xy=True, verbose=True)
    print '\ntest_get_input split_xy=True...', 'shape X y:', X.shape, y.shape, \
        '\n', y.head(2).iloc[0:5], \
        '\n', X.head(3).iloc[:,0:5]

