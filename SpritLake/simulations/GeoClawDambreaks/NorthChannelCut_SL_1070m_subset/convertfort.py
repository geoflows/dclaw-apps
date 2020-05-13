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

    pts = [7,10,11,12,1010]
    xpts = [586475.7664,584743.5377,572116.0213,580391.0424,589808.0244]
    ypts = [1483303.757,1484475.693,1485888.437,1486712.609,1481951.479]

    for pt in range(len(pts)):
        name = str(pts[pt])
        dirname = 'fortDEM_' + name
        dirname2 = 'fort_uniform' + name
        dirname2 = os.path.join('UniformGrids',dirname2)

        x1 = xpts[pt] - 5000.
        x2 = xpts[pt] + 5000.
        y1 = ypts[pt] - 5000.
        y2 = ypts[pt] + 5000.
        mx = int((x2-x1)/100.) + 2
        my = int((y2-y1)/100.) + 2
    #nplots = [44]

    #    cf.convertfortdir('topotype',nplots=nplots,outputname='fort.h.',\
    #        components=1,outdir=dirname,fortdir='_output',topotype=3,xll=x1,\
    #        yll=y1,cellsize=100.0,ncols=mx,nrows=my)

    #    cf.convertfortdir('topotype',nplots=nplots,outputname='fort.b.',\
    #        components='topo',outdir=dirname,fortdir='_output',topotype=3,xll=x1,\
    #        yll=y1,cellsize=100.0,ncols=mx,nrows=my)

        cf.convertfortdir('fortuniform',nplots=nplots,outputname='fort.q',\
            components='all',outdir=dirname2,fortdir='_output',xlower=x1,\
            xupper=x2,ylower=y1,yupper=y2,mx=mx,my=my)

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
    nplots = range(0,n+1)
    maketopoh_subset(nplots)
