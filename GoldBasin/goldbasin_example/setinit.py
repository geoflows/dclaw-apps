"""
maketopo:

create a topo directory with links to topo files and initialization files
this requires that you have an environment variable $TOPO set, and 
topography files in $TOPO for the Gold Basin area. Modify this routine accordingly
to link to topography. You can create soft links or move your topography into the local 
directoris. Alternatively, modify setrun.py accordingly to find your input DEMs.


If you have other files, modify 
this and your setrun.py accordingly.

"""

import numpy as np
import dclaw.topotools as gt
import os
#import pylab
#import pdb

cdir = os.path.abspath(os.environ['PWD'])
#path to your DEM data, assuming you have a topo env. variable. set or modify if not
topodata=os.environ['TOPO']

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
# set a path to your topography data for this app. (modify accordingly)
ntopofiles = 1
topotarget = [0]*ntopofiles
topofname = [0]*ntopofiles

topotargetpath = os.path.join(topodata,'gold_basin','Cannon','HeadMidLobe_n80p2_ascii')
topotarget[0] = os.path.join(topotargetpath,'headmidlobe_n80p2_topo_with_slip_surface.tt3')
topofname[0] = os.path.join(topodir,'topodomain.tt3')

for i in xrange(0,ntopofiles):
    if not os.path.isfile(topofname[i]):
        execstr = 'ln -s '+topotarget[i] +' '+topofname[i]
        os.system(execstr)

#----------SOLUTION INITIAL CONDITIONS (qinit)---------------------------------
nqinitfiles = 2
qinittarget = [0]*nqinitfiles
qinitfname = [0]*nqinitfiles

qinittargetpath = os.path.join(topodata,'gold_basin','Cannon','HeadMidLobe_n80p2_ascii')
qinittarget[0] = os.path.join(qinittargetpath,'headmidlobe_n80p2_src_topo_subset.tt3')
qinitfname[0] = os.path.join(qinitdir,'eta_init.tt3')

qinittarget[1] = os.path.join(topotargetpath,'m0_62_gold_basin_slide_subset.tt2')
qinitfname[1] = os.path.join(qinitdir,'m0_init.tt2')

for i in xrange(0,nqinitfiles):
    if not os.path.isfile(qinitfname[i]):
        execstr = 'ln -s '+qinittarget[i] +' '+qinitfname[i]
        os.system(execstr)










