"""
maketopo:

make some 'artificial' topo surrounding the flume area

"""

import numpy as np
import topotools as gt
import pylab
import os
import pdb

def zero(X,Y):

    yind1 =  np.where((Y[:,0]>=-0.5)&(Y[:,0]<=0.0))[0]
    yind2 =  np.where((Y[:,0]>=2.0)&(Y[:,0]<=2.5))[0]
    xind  =  np.where((X[0,:]>=-15.0)&(X[0,:]<=90.0))[0]

    Z = np.zeros(np.shape(X))

    return Z

def wallzero(X,Y):
    yind1 =  np.where((Y[:,0]>=-0.5)&(Y[:,0]<=0.0))[0]
    yind2 =  np.where((Y[:,0]>=2.0)&(Y[:,0]<=2.5))[0]
    xind  =  np.where((X[0,:]>=-15.0)&(X[0,:]<=82.5))[0]
    xhopperind = np.where((X[0,:]>=-15.0)&(X[0,:]<=0.0))[0]
    Z = np.zeros(np.shape(X))

    Z[np.ix_(yind1,xind)] = 1.6
    Z[np.ix_(yind2,xind)] = 1.6
    Z[np.ix_(yind1,xhopperind)] = 2.5
    Z[np.ix_(yind2,xhopperind)] = 2.5



    return Z

def zero_backstop(X,Y):

    yind1 =  np.where((Y[:,0]>=-0.5)&(Y[:,0]<=0.0))[0]
    yind2 =  np.where((Y[:,0]>=2.0)&(Y[:,0]<=2.5))[0]
    xind  =  np.where((X[0,:]>=-15.0)&(X[0,:]<=90.0))[0]

    xbackstopind  =  np.where(X[0,:]<=-4.0)[0]
    ybackstopind  =  np.where((Y[:,0]>=-0.5)&(Y[:,0]<=2.5))[0]

    Z = np.zeros(np.shape(X))

    Z[np.ix_(ybackstopind,xbackstopind)] = 2.5

    return Z

def wallzero_backstop(X,Y):
    yind1 =  np.where((Y[:,0]>=-0.5)&(Y[:,0]<=0.0))[0]
    yind2 =  np.where((Y[:,0]>=2.0)&(Y[:,0]<=2.5))[0]
    xind  =  np.where((X[0,:]>=-15.0)&(X[0,:]<=82.5))[0]
    xhopperind = np.where((X[0,:]>=-15.0)&(X[0,:]<=0.0))[0]
    Z = np.zeros(np.shape(X))

    xbackstopind  =  np.where(X[0,:]<=-4.0)[0]
    ybackstopind  =  np.where((Y[:,0]>=-0.5)&(Y[:,0]<=2.5))[0]

    Z[np.ix_(yind1,xind)] = 1.6
    Z[np.ix_(yind2,xind)] = 1.6
    Z[np.ix_(yind1,xhopperind)] = 2.5
    Z[np.ix_(yind2,xhopperind)] = 2.5

    Z[np.ix_(ybackstopind,xbackstopind)] = 2.5




    return Z


def flume_eta(X,Y):

    hopperlen = 4.7
    hmax = 1.9
    hoppertop = 3.3
    topangle = 17.0*np.pi/180.0
    flumeangle = 31.0*np.pi/180.0


    x0 = -hopperlen
    x2 = -hmax*np.cos(0.5*np.pi - flumeangle)
    x1 = x2 - hoppertop*np.cos(flumeangle-topangle)

    x3 = 0.0
    y2 = hmax*np.sin(0.5*np.pi - flumeangle)
    y1 = y2 - hoppertop*np.sin(flumeangle-topangle)
    slope0 = y1/(x1-x0)
    slope1 = (y2-y1)/(x2-x1)
    slope2 = -y2/(x3-x2)

    yind =  np.where((Y[:,0]<=2.0)&(Y[:,0]>=0.0))[0]
    x0ind = np.where((X[0,:]>=x0)&(X[0,:]<x1))[0]
    x1ind = np.where((X[0,:]>=x1)&(X[0,:]<x2))[0]
    x2ind = np.where((X[0,:]>=x2)&(X[0,:]<x3))[0]

    #pdb.set_trace()

    Z=np.zeros(np.shape(X))
    Z[np.ix_(yind,x0ind)] = (X[np.ix_(yind,x0ind)]-x0)*slope0
    Z[np.ix_(yind,x1ind)] =  y1+(X[np.ix_(yind,x1ind)]-x1)*slope1
    Z[np.ix_(yind,x2ind)] = -(x3-X[np.ix_(yind,x2ind)])*slope2

    return Z

def flume_eta_res(X,Y):

    hopperlen = 4.7
    hmax = 1.9
    hoppertop = 3.3
    topangle = 17.0*np.pi/180.0
    flumeangle = 31.0*np.pi/180.0


    x0 = -hopperlen
    x2 = -hmax*np.cos(0.5*np.pi - flumeangle)
    x1 = x2 - hoppertop*np.cos(flumeangle-topangle)

    x3 = 0.0
    y2 = hmax*np.sin(0.5*np.pi - flumeangle)
    y1 = y2 - hoppertop*np.sin(flumeangle-topangle)
    xm1 = x1 - y1*np.tan(0.5*np.pi - flumeangle)

    slope0 = y1/(x1-xm1)
    slope1 = (y2-y1)/(x2-x1)
    slope2 = -y2/(x3-x2)

    yind =  np.where((Y[:,0]<=2.0)&(Y[:,0]>=0.0))[0]
    xm1ind = np.where((X[0,:]>=xm1)&(X[0,:]<x1))[0]
    x1ind = np.where((X[0,:]>=x1)&(X[0,:]<x2))[0]
    x2ind = np.where((X[0,:]>=x2)&(X[0,:]<x3))[0]

    #pdb.set_trace()

    Z=np.zeros(np.shape(X))
    Z[np.ix_(yind,xm1ind)] = (X[np.ix_(yind,xm1ind)]-xm1)*slope0
    Z[np.ix_(yind,x1ind)] =  y1+(X[np.ix_(yind,x1ind)]-x1)*slope1
    Z[np.ix_(yind,x2ind)] = -(x3-X[np.ix_(yind,x2ind)])*slope2

    return Z

def flume_eta_res_half(X,Y):

    hopperlen = 4.7
    hmax = 1.9
    hoppertop = 3.3
    topangle = 17.0*np.pi/180.0
    flumeangle = 31.0*np.pi/180.0


    x0 = -hopperlen
    x2 = -hmax*np.cos(0.5*np.pi - flumeangle)
    x1 = x2 - hoppertop*np.cos(flumeangle-topangle)

    x3 = 0.0
    y2 = hmax*np.sin(0.5*np.pi - flumeangle)
    y1 = y2 - hoppertop*np.sin(flumeangle-topangle)
    xm1 = x1 - y1*np.tan(0.5*np.pi - flumeangle)
    xmhalf = 0.5*(x0 + xm1)


    slope0 = y1/(x1-xm1)
    slopehalf = y1/(x1-xmhalf)
    slope1 = (y2-y1)/(x2-x1)
    slope2 = -y2/(x3-x2)

    yind =  np.where((Y[:,0]<=2.0)&(Y[:,0]>=0.0))[0]
    xmhalfind = np.where((X[0,:]> xmhalf)&(X[0,:]<x1))[0]
    x1ind = np.where((X[0,:]>=x1)&(X[0,:]<x2))[0]
    x2ind = np.where((X[0,:]>=x2)&(X[0,:]<x3))[0]

    #pdb.set_trace()

    Z=np.zeros(np.shape(X))
    Z[np.ix_(yind,xmhalfind)] = (X[np.ix_(yind,xmhalfind)]-xmhalf)*slopehalf
    Z[np.ix_(yind,x1ind)] =  y1+(X[np.ix_(yind,x1ind)]-x1)*slope1
    Z[np.ix_(yind,x2ind)] = -(x3-X[np.ix_(yind,x2ind)])*slope2

    return Z



def flume_hm_res(X,Y):

    hopperlen = 4.7
    hmax = 1.9
    hoppertop = 3.3
    topangle = 17.0*np.pi/180.0
    flumeangle = 31.0*np.pi/180.0
    m0 = 0.61

    x0 = -hopperlen
    x2 = -hmax*np.cos(0.5*np.pi - flumeangle)
    x1 = x2 - hoppertop*np.cos(flumeangle-topangle)

    x3 = 0.0
    y2 = hmax*np.sin(0.5*np.pi - flumeangle)
    y1 = y2 - hoppertop*np.sin(flumeangle-topangle)
    xm1 = x1 - y1*np.tan(0.5*np.pi - flumeangle)

    slopem1 = y1/(x1-x0)
    slope0 = y1/(x1-x0)
    slope1 = (y2-y1)/(x2-x1)
    slope2 = -y2/(x3-x2)

    yind =  np.where((Y[:,0]<=2.0)&(Y[:,0]>=0.0))[0]
    xm1ind = np.where((X[0,:]>=xm1)&(X[0,:]<x0))[0]
    x0ind = np.where((X[0,:]>=x0)&(X[0,:]<x1))[0]
    x1ind = np.where((X[0,:]>=x1)&(X[0,:]<=x3))[0]

    Z=np.zeros(np.shape(X))
    #Z[np.ix_(yind,x1ind)] = m0*flume_eta(X[np.ix_(yind,x1ind)],Y[np.ix_(yind,x1ind)])
    Z[np.ix_(yind,x1ind)] = m0
    Z[np.ix_(yind,x0ind)] = m0*flume_eta(X[np.ix_(yind,x0ind)],Y[np.ix_(yind,x0ind)])/flume_eta_res(X[np.ix_(yind,x0ind)],Y[np.ix_(yind,x0ind)])


    return Z

#flat topo
outfile= 'ZeroTopo.tt2'
outfile = os.path.join('topo',outfile)
xlower = -10.0
xupper = 180
ylower = -10.0
yupper =  10.0
nxpoints = int((xupper-xlower)/0.1) + 1
nypoints = int((yupper-ylower)/0.1) + 1
gt.topo2writer(outfile,zero,xlower,xupper,ylower,yupper,nxpoints,nypoints)

#flat topo
outfile= 'ZeroTopoGate.tt2'
outfile = os.path.join('topo',outfile)
xlower = -8.0
xupper =  10.0
ylower =  0.0
yupper =  2.0
nxpoints = int((xupper-xlower)/0.005) + 1
nypoints = int((yupper-ylower)/0.005) + 1
gt.topo2writer(outfile,zero,xlower,xupper,ylower,yupper,nxpoints,nypoints)

#wall topo
outfile= 'Wall1Topo.tt2'
outfile = os.path.join('topo',outfile)
xlower = -15.0
xupper =  90.0
ylower =  -0.5
yupper =  0.0
nxpoints = int((xupper-xlower)/0.05) + 1
nypoints = int((yupper-ylower)/0.05) + 1
gt.topo2writer(outfile,wallzero,xlower,xupper,ylower,yupper,nxpoints,nypoints)

#wall topo
outfile= 'Wall2Topo.tt2'
outfile = os.path.join('topo',outfile)
xlower = -15.0
xupper =  90.0
ylower = 2.0
yupper = 2.5
nxpoints = int((xupper-xlower)/0.05) + 1
nypoints = int((yupper-ylower)/0.05) + 1
gt.topo2writer(outfile,wallzero,xlower,xupper,ylower,yupper,nxpoints,nypoints)

#test initial file
outfile= 'FlumeQinit.tt2'
outfile = os.path.join('topo',outfile)
xlower = -10.0
xupper =  1.0
ylower = -1.0
yupper =  3.0
nxpoints = int((xupper-xlower)/0.01) + 1
nypoints = int((yupper-ylower)/0.01) + 1
gt.topo2writer(outfile,flume_eta,xlower,xupper,ylower,yupper,nxpoints,nypoints)

#test initial file
outfile= 'FlumeQinit_res.tt2'
outfile = os.path.join('topo',outfile)
xlower = -10.0
xupper =  1.0
ylower = -1.0
yupper =  3.0
nxpoints = int((xupper-xlower)/0.01) + 1
nypoints = int((yupper-ylower)/0.01) + 1
gt.topo2writer(outfile,flume_eta_res,xlower,xupper,ylower,yupper,nxpoints,nypoints)

#test initial file
outfile= 'FlumeQinit_res_half.tt2'
outfile = os.path.join('topo',outfile)
xlower = -10.0
xupper =  1.0
ylower = -1.0
yupper =  3.0
nxpoints = int((xupper-xlower)/0.01) + 1
nypoints = int((yupper-ylower)/0.01) + 1
gt.topo2writer(outfile,flume_eta_res_half,xlower,xupper,ylower,yupper,nxpoints,nypoints)

#test initial file
outfile= 'FlumeQinit_m.tt2'
outfile = os.path.join('topo',outfile)
xlower = -10.0
xupper =  1.0
ylower = -1.0
yupper =  3.0
nxpoints = int((xupper-xlower)/0.01) + 1
nypoints = int((yupper-ylower)/0.01) + 1
gt.topo2writer(outfile,flume_hm_res,xlower,xupper,ylower,yupper,nxpoints,nypoints)






