#!/usr/bin/python
"""
convert a fort.q file into a dem file for a component of q
"""

import numpy as np
import geotools.topotools as gt
import clawtools.fortconvert as cf
import os
import sys

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

def makeinit(comp):
    """
    x1=6.145e5 - 200.
    x2=6.194e5 
    y1=4.899e6 -260. -500.
    y2=4.907e6 + 1300.0

    mx = int(x2-x1) + 2
    my = int(y2-y1) + 2
    #nplots = [44]
    """

    outputname = 'topo_' + str(comp) + '.'

    cf.convertfortdir('topotype',nplots=[80],outputname=outputname,\
            components=comp,outdir='sisters_subdomain_init',fortdir='fortuniform_sisters')
    """
    cf.convertfortdir('topotype',nplots=nplots,outputname='fort.hu.',\
        components=2,outdir='fortall_sisters',fortdir='_output',topotype=3,\
        xll=x1,yll=y1,cellsize=1.0,ncols=mx,nrows=my)

    cf.convertfortdir('topotype',nplots=nplots,outputname='fort.hv.',\
        components=3,outdir='fortall_sisters',fortdir='_output',topotype=3,\
        xll=x1,yll=y1,cellsize=1.0,ncols=mx,nrows=my)

    cf.convertfortdir('topotype',nplots=nplots,outputname='fort.hm.',\
        components=4,outdir='fortall_sisters',fortdir='_output',topotype=3,\
        xll=x1,yll=y1,cellsize=1.0,ncols=mx,nrows=my)

    cf.convertfortdir('topotype',nplots=nplots,outputname='fort.p.',\
        components=5,outdir='fortall_sisters',fortdir='_output',topotype=3,\
        xll=x1,yll=y1,cellsize=1.0,ncols=mx,nrows=my)
    """

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
    comp = n
    makeinit(comp)
