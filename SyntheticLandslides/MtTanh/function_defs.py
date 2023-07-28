"""
setinit:
create synthetic topo DEMs

"""

import numpy as np


#---------------- functions for geometry to build DEMs ------------


def mt_tanh_log_eta(X,Y):
    """
    hyperbolic tangent mountain with log argument (slope in x, y-uniform)

    surface elevation, eta = 0.5*A(1-tanh(log(c*(x-x0))))  for x > x0
    """

    A = 2.e3 #height of mt.
    c = 0.5e-3 #propto slope
    x0 = 0.0 #summit location

    x0ind = np.where(X[0,:]<=x0)[0] #flat top of mt. if desired left of x0
    x1ind = np.where(X[0,:]>x0)[0]
    yind =  np.where(Y[:,0]<=1e16)[0] #uniform in y for now
    

    #pdb.set_trace()

    Z=np.zeros(np.shape(X))
    Z[np.ix_(yind,x0ind)] = A
    Z[np.ix_(yind,x1ind)] = 0.5*A*(1.0-np.tanh(np.log(c*(X[np.ix_(yind,x1ind)]-x0))))
    

    return Z

def mt_tanh_log_eta_r(X,Y):
    """
    hyperbolic tangent mountain with log argument (radially symetric)

    surface elevation, eta = 0.5*A(1-tanh(log(c*(r-r0))))  
    """

    A = 2.e3 #height of mt.
    c = 0.5e-3 #propto slope
    x0 = 0.0; y0 = 0.0 #summit location

    r2 = np.sqrt((X-x0)**2 + (Y-y0)**2)
    
    #pdb.set_trace()

    Z=np.zeros(np.shape(X))
    Z = 0.5*A*(1.0-np.tanh(np.log(c*r2)))
    

    return Z

def src_quadratic_b(X,Y):
    """
    failure surface/ quadratic to fit eta = mt_tanh_log_eta

    b = z0 + cx*(x-x0)^2 + cy*(y-y0)^2
    
    """

    cx = 0.5e-3
    cy = 0.1e-3
    x0 = 1100.
    y0 = 0.0
    z0 = 1600.

    # top surface
    eta = mt_tanh_log_eta(X,Y)

    # quadratic
    Z=np.zeros(np.shape(X))
    Z = z0 + cx*(X-x0)**2 + cy*(Y-y0)**2

    b = np.minimum(Z,eta)
    
    return b


def src_quadratic_h_v(X,Y):
    """
    failure surface/ quadratic to fit eta = mt_tanh_log_eta

    b = z0 + cx*(x-x0)^2 + cy*(y-y0)^2

    returns depth h = eta -b
    
    """

    cx = 0.5e-3
    cy = 0.5e-3
    x0 = 1100.
    y0 = 0.0
    z0 = 1600.

    # top surface
    eta = mt_tanh_log_eta(X,Y)

    # quadratic
    Z=np.zeros(np.shape(X))
    Z = z0 + cx*(X-x0)**2 + cy*(Y-y0)**2

    b = np.minimum(Z,eta)

    h = eta - b

    dx = abs(X[0,1]-X[0,0])

    volume = np.sum(h)*dx*dx
    print('source volume (million m^3): ', volume/1.e6)
    
    return (h,volume)

def src_quadratic_h(X,Y):
    """
    failure surface/ quadratic to fit eta = mt_tanh_log_eta

    b = z0 + cx*(x-x0)^2 + cy*(y-y0)^2

    returns depth h = eta -b
    
    """

    cx = 0.5e-3
    cy = 0.5e-3
    x0 = 1100.
    y0 = 0.0
    z0 = 1600.

    # top surface
    eta = mt_tanh_log_eta(X,Y)

    # quadratic
    Z=np.zeros(np.shape(X))
    Z = z0 + cx*(X-x0)**2 + cy*(Y-y0)**2

    b = np.minimum(Z,eta)

    h = eta - b

    dx = abs(X[0,1]-X[0,0])

    volume = np.sum(h)*dx*dx
    print('source volume (million m^3): ', volume/1.e6)
    
    return h

def src_quadratic_b_r(X,Y):
    """
    failure surface/ quadratic to fit eta = mt_tanh_log_eta_r

    b = z0 + cx*(x-x0)^2 + cy*(y-y0)^2
    
    """

    cx = 0.5e-3
    cy = 0.1e-3
    x0 = 1100.
    y0 = 0.0
    z0 = 1600.

    # top surface
    eta = mt_tanh_log_eta_r(X,Y)

    # quadratic
    Z=np.zeros(np.shape(X))
    Z = z0 + cx*(X-x0)**2 + cy*(Y-y0)**2

    b = np.minimum(Z,eta)
    
    return b


def src_quadratic_h_r_v(X,Y):
    """
    failure surface/ quadratic to fit eta = mt_tanh_log_eta

    b = z0 + cx*(x-x0)^2 + cy*(y-y0)^2

    returns depth h = eta -b
    
    """

    cx = 0.5e-3
    cy = 0.5e-3
    x0 = 1100.
    y0 = 0.0
    z0 = 1600.

    # top surface
    eta = mt_tanh_log_eta_r(X,Y)

    # quadratic
    Z=np.zeros(np.shape(X))
    Z = z0 + cx*(X-x0)**2 + cy*(Y-y0)**2

    b = np.minimum(Z,eta)

    h = eta - b

    dx = abs(X[0,1]-X[0,0])
    #print dx

    volume = np.sum(h)*dx*dx
    print('source volume (million m^3): ', volume/1.e6)
    
    return (h,volume)

def src_quadratic_h_r(X,Y):
    """
    failure surface/ quadratic to fit eta = mt_tanh_log_eta

    b = z0 + cx*(x-x0)^2 + cy*(y-y0)^2

    returns depth h = eta -b
    
    """

    cx = 0.5e-3
    cy = 0.5e-3
    x0 = 1100.
    y0 = 0.0
    z0 = 1600.

    # top surface
    eta = mt_tanh_log_eta_r(X,Y)

    # quadratic
    Z=np.zeros(np.shape(X))
    Z = z0 + cx*(X-x0)**2 + cy*(Y-y0)**2

    b = np.minimum(Z,eta)

    h = eta - b

    dx = abs(X[0,1]-X[0,0])
    print(dx)

    volume = np.sum(h)*dx*dx
    print('source volume (million m^3): ', volume/1.e6)
    
    return h
    

def phi_uniform(X,Y):

    """
    bed friction angle
    """
    phi = 40.0
    Z = np.ones(np.shape(X))
    Z = phi*Z
    deg2rad = np.pi/180.0
    Z = deg2rad*Z

    return Z





