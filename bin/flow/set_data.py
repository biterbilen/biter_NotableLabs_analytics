from fcsparser.api import FCSParser

def set_output(ifle, pred, idir='./', odir='./', verbose=False):
    fcs_file = FCSParser(idir + ifle)
    fcs_file = FCSParser(idir + ifle)
    
    index = [ pred == 'live' ] #TODO check
    subset_fcs_file = fcs_file.clone(data=fcs_file.data[index])
    subset_fcs_file.write_to_file(odir + 'subset_' + ifle)
    
    if verbose:
        print 'fcs_file:', fcs_file.data.shape, fcs_file.data[0][:3]
        print 'subset_fcs_file:', subset_fcs_file.data.shape, subset_fcs_file.data[0][:3]

    
def test_set_output():
    ifle  = 'Well_C03.fcs'
    idir  = '../../data/live_dead_debris/'
    odir  = './'
    pred = 'dummy'
    set_output(ifle, pred, idir, odir=odir, verbose=True)
    
