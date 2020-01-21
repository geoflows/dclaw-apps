"""
setinit:
this routine creates local directories and sets softlinks for the topo and q-init DEMs
used by setrun.py

this requires that you have an environment variable $TOPO set, and 
topography files in $TOPO for the Gold Basin area. Modify this routine accordingly
based on your directory path/names for topography -- see targetpaths below

If you have other files, modify 
this and your setrun.py accordingly.

"""

import numpy as np
import dclaw.topotools as gt
import os
#import pylab
#import pdb


cdir = os.path.abspath(os.environ['PWD'])

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#----CHANGE THE FOLLWOING PATH(S) FOR YOU LOCAL SET-UP
#path to your DEM data, assuming you have a topo env. variable. set or modify if not
topodata=os.environ['TOPO']
#full path to topography data
topotargetpath = os.path.join(topodata,'gold_basin','Yuankun','Topo_with_slide_and_river')
qinittargetpath = os.path.join(topodata,'gold_basin','Yuankun','Topo_with_slide_and_river')
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#---create local directories for data if they do not exist----------
indatadir=os.path.join(cdir,'init_data')
topodir = os.path.join(cdir,indatadir,'topo')
auxdir = os.path.join(cdir,indatadir,'aux')
qinitdir = os.path.join(cdir,indatadir,'qinit')

if not os.path.isdir(indatadir):
    execstr = 'mkdir '+indatadir
    os.system(execstr)
if not os.path.isdir(topodir):
    execstr = 'mkdir '+topodir
    os.system(execstr)
if not os.path.isdir(auxdir):
    execstr = 'mkdir '+auxdir
    os.system(execstr)
if not os.path.isdir(qinitdir):
    execstr = 'mkdir '+qinitdir
    os.system(execstr)

#-----------TOPOGRAPHY DATA--------------------------------------
def makelinks_topo():
    ntopofiles = 1
    topotarget = [0]*ntopofiles
    topofname = [0]*ntopofiles

    topotarget[0] = os.path.join(topotargetpath,'topo_with_slip_surface_and_riverbed.tt3')
    topofname[0] = os.path.join(topodir,'topodomain_w_riverbed.tt3')

    for i in xrange(0,ntopofiles):
        if not os.path.isfile(topofname[i]):
            execstr = 'ln -s '+topotarget[i] +' '+topofname[i]
            os.system(execstr)

#----------SOLUTION INITIAL CONDITIONS (qinit)---------------------------------
def makelinks_qinit():
    nqinitfiles = 8
    qinittarget = [0]*nqinitfiles
    qinitfname = [0]*nqinitfiles

    qinittarget[0] = os.path.join(qinittargetpath,'topo_landslide_subset.tt3')
    qinitfname[0] = os.path.join(qinitdir,'eta_init_landslide.tt3')

    qinittarget[1] = os.path.join(qinittargetpath,'topo_river_surface_subset_200cm.tt3')
    qinitfname[1] = os.path.join(qinitdir,'eta_init_river_200cm.tt3')

    qinittarget[2] = os.path.join(qinittargetpath,'topo_river_surface_subset_50cm.tt3')
    qinitfname[2] = os.path.join(qinitdir,'eta_init_river_50cm.tt3')

    qinittarget[3] = os.path.join(qinittargetpath,'m0_river_subset_200cm.tt3')
    qinitfname[3] = os.path.join(qinitdir,'m0_init_river_200cm.tt3')

    qinittarget[4] = os.path.join(qinittargetpath,'m0_river_subset_50cm.tt3')
    qinitfname[4] = os.path.join(qinitdir,'m0_init_river_50cm.tt3')

    qinittarget[5] = os.path.join(qinittargetpath,'m0_landslide_0.62.tt3')
    qinitfname[5] = os.path.join(qinitdir,'m0_init_landslide_0.62.tt3')

    qinittarget[6] = os.path.join(qinittargetpath,'topo_landslide_subset_less1meter.tt3')
    qinitfname[6] = os.path.join(qinitdir,'eta_init_landslide_less1meter.tt3')

    qinittarget[7] = os.path.join(qinittargetpath,'topo_river_surface_subset_333m.tt3')
    qinitfname[7] = os.path.join(qinitdir,'eta_init_river_clipped.tt3')

    for i in xrange(0,nqinitfiles):
        if not os.path.isfile(qinitfname[i]):
            execstr = 'ln -s '+qinittarget[i] +' '+qinitfname[i]
            os.system(execstr)


#------------BUILD INITIALIZATION CONDITIONS FOR PURE WATER RIVER------------------
def build_eta_DEMs():
    """ note: this creates initialization files for eta that are "clipped" 
              or lowered, from the topography data. Interpolation discrepancies otherwise 
              lead to a very thin layer or water or landslide material everywhere.
    """

    infile = os.path.join(qinittargetpath,'topo_landslide_subset.tt3')
    outfile = os.path.join(qinittargetpath,'topo_landslide_subset_less1meter.tt3')
    lower_DEM(infile,outfile,1.00)

    infile  = os.path.join(qinittargetpath,'topo_river_surface_subset_200cm.tt3')
    outfile = os.path.join(qinittargetpath,'topo_river_surface_subset_333m.tt3')
    clip_DEM(infile,outfile,333.)

def build_water_DEMs():
    infile = os.path.join(qinittargetpath,'topo_river_surface_subset_200cm.tt3')
    outfile = os.path.join(qinittargetpath,'m0_river_subset_200cm.tt3')
    make_m0_DEM(infile,outfile,0.0)

    infile = os.path.join(qinittargetpath,'topo_river_surface_subset_50cm.tt3')
    outfile = os.path.join(qinittargetpath,'m0_river_subset_50cm.tt3')
    make_m0_DEM(infile,outfile,0.0)

    infile = os.path.join(qinittargetpath,'topo_landslide_subset.tt3')
    outfile = os.path.join(qinittargetpath,'m0_landslide_0.62.tt3')
    make_m0_DEM(infile,outfile,0.62)

def make_m0_DEM(infile,outfile,m0):

    if (not os.path.isfile(outfile)):
        (X,Y,Z) = gt.topofile2griddata(infile)
        Z = 0.*Z + m0
        gt.griddata2topofile(X,Y,Z,outfile,topotype=3)

def lower_DEM(infile,outfile,dZ):

    if (not os.path.isfile(outfile)):
        (X,Y,Z) = gt.topofile2griddata(infile)
        Z = Z - dZ
        gt.griddata2topofile(X,Y,Z,outfile,topotype=3)

def clip_DEM(infile,outfile,elevation):

    if (not os.path.isfile(outfile)):
        (X,Y,Z) = gt.topofile2griddata(infile)
        Z[np.where(Z>elevation)] = -9999
        gt.griddata2topofile(X,Y,Z,outfile,topotype=3)

if __name__=='__main__':

    build_eta_DEMs()
    build_water_DEMs()


    makelinks_topo()
    makelinks_qinit()











