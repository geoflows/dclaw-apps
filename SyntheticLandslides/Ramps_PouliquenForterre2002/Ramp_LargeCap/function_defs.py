"""
setinit:
create synthetic topo DEMs

"""

import numpy as np


#---------------- functions for geometry to build DEMs ------------


def LargeCap_h(X,Y):
    """
    Large cap depth -- bed normal direction
    returns depth h
    """

    r = 4.0e-2
    R = 8.0e-2
    xc = R
    yc = 0.0
    zc = -(R-r)

    # hemisphere sits above ramp by maximum r.
    # (x-xc)**2 + (y-yc)**2 + (z-zc)**2 = R**2 
    # z = zc - sqrt(R**2 -(y-yc)**2 - (x-xc)**2)

    xind = np.where((X[0,:]-xc)**2 < R**2)[0] #
    yind = np.where((Y[:,0]-yc)**2 < R**2)[0] # 
    

    #pdb.set_trace()

    Z=np.zeros(np.shape(X))
    y = Y[np.ix_(yind,xind)]
    x = X[np.ix_(yind,xind)]
    sqrtarg = np.maximum(R**2 -(y-yc)**2 - (x-xc)**2, 0.0)
    Z[np.ix_(yind,xind)]  = zc - np.sqrt(sqrtarg)
    #formula for whole circle gives negative values for outer x
    Z = np.maximum(Z,0.0)
    

    return Z


def zero_plane(X,Y):
    """
    Large cap depth -- bed normal direction
    returns zero file for convenience
    """

    #pdb.set_trace()

    Z=np.zeros(np.shape(X))
    
    
    return Z

def theta_23(X,Y):
    """
    ramp
    returns slope angle
    """

    #pdb.set_trace()

    Z=np.zeros(np.shape(X)) + 23.0
    
    
    return Z




