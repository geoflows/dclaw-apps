"""
setinit:
create synthetic topo DEMs

"""

import numpy as np


#---------------- functions for geometry to build DEMs ------------


def LargeCap_eta(X,Y):
    """
    Large cap depth -- earth-centered Cartesian
    returns eta
    """

    #ramp slope
    theta = 23.0 
    thetarad = np.deg2rad(theta)

    #large cap
    r = 4.0e-2
    R = 8.0e-2
    #arbitrary position of circle center
    xc = R 
    yc = 0.0
    zc = R 

    # hemisphere sits above ramp by maximum r.
    # (x-xc)**2 + (y-yc)**2 + (z-zc)**2 = R**2 
    # z = zc - sqrt(R**2 -(y-yc)**2 - (x-xc)**2)

    #below: see diagram pdf
    Lc = np.sqrt(r*(2.0*R-r)) #chord length from back of cap to top of cap
    b = Lc*np.sin(thetarad) 
    a = Lc*np.cos(thetarad)
    c = (R-r)*np.sin(thetarad)
    d = (R-r)*np.cos(thetarad)

    #intersection of slope and hemisphere centerline
    x1 = xc - a + c
    z1 = zc + d

    #ramp:
    m = -np.tan(thetarad)
    Zramp = z1 + m*(X-x1) 

    #semi-circle
    D = np.sqrt((X-xc)**2 + (Y-yc)**2) #distance from sphere center (positive branch ok, may be below ramp)
    ind = np.where(D<R)
    Zs = np.zeros(np.shape(Zramp)) - 2*R #initialize below sphere
    Zs[ind] = zc + np.sqrt(R**2 - D[ind]**2)

    eta = np.maximum(Zramp,Zs)

    return eta

def LargeCap_b(X,Y):
    """
    Large cap depth -- earth-centered Cartesian
    returns eta
    """

    #ramp slope
    theta = 23.0 
    thetarad = np.deg2rad(theta)

    #large cap
    r = 4.0e-2
    R = 8.0e-2
    #arbitrary position of circle center
    xc = R 
    yc = 0.0
    zc = R 

    # hemisphere sits above ramp by maximum r.
    # (x-xc)**2 + (y-yc)**2 + (z-zc)**2 = R**2 
    # z = zc - sqrt(R**2 -(y-yc)**2 - (x-xc)**2)

    #below: see diagram pdf
    Lc = np.sqrt(r*(2.0*R-r)) #chord length from back of cap to top of cap
    b = Lc*np.sin(thetarad) 
    a = Lc*np.cos(thetarad)
    c = (R-r)*np.sin(thetarad)
    d = (R-r)*np.cos(thetarad)

    #intersection of slope and hemisphere centerline
    x1 = xc - a + c
    z1 = zc + d

    #ramp:
    m = -np.tan(thetarad)
    Zramp = z1 + m*(X-x1) 

    return Zramp

    






