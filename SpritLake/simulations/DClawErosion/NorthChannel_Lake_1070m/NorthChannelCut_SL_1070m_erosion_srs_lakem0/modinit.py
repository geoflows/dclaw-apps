#!/usr/bin/python
"""
convert a fort.q file into a dem file for a component of q
"""

import numpy as np
import geotools.topotools as gt
import clawtools.fortconvert as cf
import os
import sys
#import numpy.ma as ma

#os.chdir('_output')

#--------------file grid parameters--------------------------------------------
    #ci is cells to shrink dem output from amr domain


    #--cells from dem reference to get to corner of amr domain


def makescatter():
    cf.convertfortdir('scattered',range(71),outputname='fort.xyq',\
        components='all',outdir='fortconverted',fortdir='_output')

def makerefined():
    cf.convertfortdir('fortrefined',[0],outputname='fort.q',\
        components='all',outdir='fortrefined',fortdir='_output')

def makeuniform():
    cf.convertfortdir('fortuniform',[0],outputname='fort.q',\
        components='all',outdir='fortuniform',fortdir='_output')

def maketopob():
    cf.convertfortdir('topotype',120,outputname='fort.topo.',\
        components='topo',outdir='forttopo',fortdir='_output',topotype='gdal')

#def maketopoeta():
#    cf.convertfortdir('topotype',120,outputname='fort.eta.',\
#        components='eta',outdir='forteta',fortdir='_output',topotype='gdal')

def maketopoh():
    cf.convertfortdir('topotype',outputname='fort.h.',\
        components=1,outdir='forth',topotype=2)

def maketopoeta():
    cf.convertfortdir('topotype',outputname='fort.eta.',\
        components=7,outdir='forth',topotype=2)

def maketopoq():
    cf.convertfortdir('topotype',120,outputname='fort.quniform.',\
        components='all',outdir='fortquniform',fortdir='_output',topotype='gdal')




#--------------------output at 30 mins------------------------------------------
def dem1():
    framenumber = 1
    outfile = 'depth_t1800s_ft.tt2'

    (X,Y,Q)=cf.fort2griddata(framenumber,xll,yll,cellsize,ncols,nrows)
    print 'converting file to feet'
    X = X*m2ft
    Y = Y*m2ft
    Q = Q*m2ft
    gt.griddata2topofile(X,Y,Q,outfile)


    infile = 'depth_t1800s_ft.tt2'
    outfile = 'depth_t1800s_ft.asc'
    gt.esriheader(infile,outfile)

#--------------------output at initial time-------------------------------------
def dem2():
    framenumber = 0
    outfile = 'depth_t0s_ft.tt2'

    (X,Y,Q)=cf.fort2griddata(framenumber,xll,yll,cellsize,ncols,nrows)
    print 'converting file to feet'
    X = X*m2ft
    Y = Y*m2ft
    Q = Q*m2ft
    gt.griddata2topofile(X,Y,Q,outfile)

    infile = 'depth_t0s_ft.tt2'
    outfile = 'depth_t0s_ft.asc'
    gt.esriheader(infile,outfile)

def maketopoh_subset(nplots):
    x1=6.145e5 - 200.
    x2=6.194e5 
    y1=4.899e6 -260.
    y2=4.907e6 + 1300.0

    mx = int(x2-x1) + 2
    my = int(y2-y1) + 2
    #nplots = [44]

    cf.convertfortdir('topotype',nplots=nplots,outputname='fort.h.',\
        components=1,outdir='forth_sisters',fortdir='_output',topotype=3,xll=x1,yll=y1,cellsize=1.0,ncols=mx,nrows=my)

def expandinit(ncomp):
    """
    x1=6.145e5 - 200.
    x2=6.194e5 
    y1=4.899e6 -260. -500.
    y2=4.907e6 + 1300.0

    mx = int(x2-x1) + 2
    my = int(y2-y1) + 2
    #nplots = [44]
    """

    dirname = 'sisters_subdomain_init'
    comps = [1,ncomp]
    for comp in comps:

    
        outfilename = 'topo_' + str(comp) + '_aug2.0080'
        outfilename2 = 'topo_' + str(comp) + '_aug2_div.0080'
        infilename = 'topo_' + str(comp) + '_aug.0080'
        outname = os.path.join(dirname,outfilename)
        outname2 = os.path.join(dirname,outfilename2)
        inname = os.path.join(dirname,infilename)

        print ('reading: '+inname)
        (X,Y,Z) = gt.topofile2griddata(inname)
        (nrows,ncols) = np.shape(Z)
        print ('expanding grid')
        x0 = X[0,0]
        xu = X[0,-1]
        y0 = Y[-1,0]
        yu = Y[0,0]
        dx = X[0,1]-X[0,0]
        dy = Y[0,0]-Y[1,0]

        xa0 = np.array(x0-dx).reshape(1,1)
        xau = np.array(xu+dx).reshape(1,1)
        ya0 = np.array(y0-dy).reshape(1,1)
        yau = np.array(yu+dy).reshape(1,1)

        YL = Y[:,0] 
        YL = YL.reshape(nrows,1)
        YR = Y[:,-1]
        YR = YR.reshape(nrows,1)

        YU = Y[0,:] + dy
        YU = YU.reshape(1,ncols)
        YU = np.hstack((yau,YU,yau))

        Y0 = Y[-1,:] - dy
        Y0 = Y0.reshape(1,ncols)
        Y0 = np.hstack((ya0,Y0,ya0))

        XL = X[:,0] - dx
        XL = XL.reshape(nrows,1)
        XR = X[:,-1] + dx
        XR = XR.reshape(nrows,1)

        XU = X[0,:]
        XU = XU.reshape(1,ncols)
        XU = np.hstack((xa0,XU,xau))
        X0 = XU

        ZL = 0.0*XL
        ZR = 0.0*XR

        ZU = 0.0*YU
        Z0 = 0.0*Y0

        print 'shapes:'
        print np.shape(X)
        print np.shape(XL)
        print np.shape(XR)
        print np.shape(XU)
        print np.shape(X0)
        print '-----------'

        X = np.hstack((XL,X,XR))
        X = np.vstack((XU,X,X0))

        Y = np.hstack((YL,Y,YR))
        Y = np.vstack((YU,Y,Y0))

        Z = np.hstack((ZL,Z,ZR))
        Z = np.vstack((ZU,Z,Z0))

        if comp==1:
            H = np.copy(Z)

        for i in xrange(nrows):
            for j in xrange(ncols):
                if H[i,j] <= 1.e-3:
                    Z[i,j] = 0.0

        print ('writing: '+outfilename)
        gt.griddata2topofile(X,Y,Z,outname)


        for i in xrange(nrows):
            for j in xrange(ncols):
                if H[i,j] > 1.e-3:
                    Z[i,j] = Z[i,j]/H[i,j]
           

        print ('writing: '+outfilename2)
        gt.griddata2topofile(X,Y,Z,outname2)



if __name__=='__main__':

    #dem1()
    #dem2()
    #makescatter()
    #makeuniform()
    #maketopob()
    #maketopoeta()
    #maketopoq()
    #maketopoh()
    #maketopoall()
    n = int(sys.argv[1])
    expandinit(n)
