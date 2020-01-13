"""
makeaux:

make auxiliary input files

"""

import numpy as np
import topotools as gt
import pylab
import os
import pdb


def phi(X,Y):

    """
    bed friction angle
    """
    Z = np.ones(np.shape(X))
    Z = 40.7*Z
    deg2rad = np.pi/180.0
    Z = deg2rad*Z

    return Z

def flume_gaterelease_phi(X,Y):

    """
    bed friction angle
    based on bumpy and smooth
    """

    deg2rad = np.pi/180.0

    yind  =  np.where((Y[:,0]<=20.0)&(Y[:,0]>=-20.0))[0]
    #x1ind  = np.where(X[0,:]<6.0)[0] #hopper
    x2ind =  np.where(X[0,:]>82.5)[0] #runout pad
    x1ind  = np.where(X[0,:]<-4.65)[0]

    Z = 41.7*np.ones(np.shape(X))
    Z[np.ix_(yind,x1ind)] = 41.7
    Z[np.ix_(yind,x2ind)] = 32.

    Z = deg2rad*Z

    return Z

def flume_theta(X,Y):

    """
    angle theta in flume
    """
    deg2rad = np.pi/180.0
    flumelen = 78.0
    flumerad = 10.0
    theta1 = 31.0
    theta2 = 2.5

    D2 = flumelen + flumerad*(theta1 - theta2)*deg2rad


    yind =  np.where((Y[:,0]<=20.0)&(Y[:,0]>=-20.0))[0]
    x1ind = np.where(X[0,:]<=flumelen)[0]
    x2ind = np.where((X[0,:]>flumelen)&(X[0,:]<D2))[0]
    x3ind = np.where(X[0,:]>=D2)[0]

    Z=np.zeros(np.shape(X))
    Z[np.ix_(yind,x1ind)] = theta1
    Z[np.ix_(yind,x3ind)] = theta2
    Z[np.ix_(yind,x2ind)] = theta1 - (X[np.ix_(yind,x2ind)]-flumelen)/(deg2rad*flumerad)
    Z = deg2rad*Z

    return Z



#phi file
outfile= 'FlumePhi.tt2'
outfile = os.path.join('aux',outfile)
xlower = -15.0
xupper = 180.0
ylower = -15.0
yupper =  15.0
nxpoints = int((xupper-xlower)/1.0) + 1
nypoints = int((yupper-ylower)/1.0) + 1
gt.topo2writer(outfile,flume_gaterelease_phi,xlower,xupper,ylower,yupper,nxpoints,nypoints)


#phi file
outfile= 'FlumeTheta.tt2'
outfile = os.path.join('aux',outfile)
xlower = -15.0
xupper = 180.0
ylower = -15.0
yupper =  15.0
nxpoints = int((xupper-xlower)/0.1) + 1
nypoints = int((yupper-ylower)/0.1) + 1
gt.topo2writer(outfile,flume_theta,xlower,xupper,ylower,yupper,nxpoints,nypoints)



