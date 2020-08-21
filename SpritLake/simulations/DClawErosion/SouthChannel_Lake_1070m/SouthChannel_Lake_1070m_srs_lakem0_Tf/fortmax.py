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

def makemax():

    
    fortdir = 'fortuniform_sisters'
    cwd=os.getcwd()
    cwd=os.path.abspath(cwd)
    forts = os.listdir(fortdir)

    outname = os.path.join('fort.qmax87')
    fort0 ='fort.q0030'
    fortname = os.path.join(fortdir,fort0)
    Qheader = cf.fortqheaderread(fortname)
    Q=np.loadtxt(fortname,skiprows=9)
    Qmax = Q
    (rows,cols) = np.shape(Q)

    for fort in forts:
        if fort[0:6]=='fort.q':
            fortname = os.path.join(fortdir,fort)
            print 'reading: '+fortname
            Q=np.loadtxt(fortname,skiprows=9)

            for i in xrange(rows):
                z = Q[i,0]
                zmax = Qmax[i,0]
                if (z>zmax):
                    #print z
                    Qmax[i,0:] = Q[i,0:]
    	
    fout=cf.fortqheaderwrite(Qheader,outname,closefile=False)
    fout.write("\n")
    for i in xrange(rows):
        for j in xrange(cols):
            fout.write("%s " % float(Qmax[i,j]))
        fout.write("\n")
    print 'writing: '+outname
    fout.close()

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

    makemax()
