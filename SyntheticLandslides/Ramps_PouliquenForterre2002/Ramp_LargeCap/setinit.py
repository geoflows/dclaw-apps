"""
setinit:
create synthetic topo DEMs

"""

import numpy as np
import dclaw.topotools as gt
import os

from function_defs import *

cdir = os.path.abspath(os.environ['PWD'])

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
## for other files (eg friction)
if not os.path.isdir(auxdir):
    execstr = 'mkdir '+auxdir
    os.system(execstr)
if not os.path.isdir(qinitdir):
    execstr = 'mkdir '+qinitdir
    os.system(execstr)


# initial eta
outfile= 'LargeCap_eta_23.tt2'
outfile = os.path.join(qinitdir,outfile)
dx = 0.001 #1 mm DEM
# grid
xlower =  0.0
xupper =  0.5 
ylower = -0.5
yupper =  0.5
nxpoints = int((xupper-xlower)/dx) + 1
nypoints = int((yupper-ylower)/dx) + 1
gt.topo2writer(outfile,LargeCap_eta,xlower,xupper,ylower,yupper,nxpoints,nypoints)

# initial eta bed normal
outfile= 'LargeCap_eta_bn.tt2'
outfile = os.path.join(qinitdir,outfile)
dx = 0.001 #1 mm DEM
# grid
xlower =  0.0
xupper =  0.5 
ylower = -0.5
yupper =  0.5
nxpoints = int((xupper-xlower)/dx) + 1
nypoints = int((yupper-ylower)/dx) + 1
gt.topo2writer(outfile,LargeCap_eta_bn,xlower,xupper,ylower,yupper,nxpoints,nypoints)


# ramp for large cap
outfile= 'LargeCap_b_23.tt2'
outfile = os.path.join(topodir,outfile)
dx = 0.001 #1 mm DEM
# grid
xlower = -1.0
xupper =  5.0 
ylower = -1.0
yupper =  1.0
nxpoints = int((xupper-xlower)/dx) + 1
nypoints = int((yupper-ylower)/dx) + 1
gt.topo2writer(outfile,LargeCap_b,xlower,xupper,ylower,yupper,nxpoints,nypoints)




