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


# initial depth
outfile= 'LargeCap_h.tt2'
outfile = os.path.join(qinitdir,outfile)
dx = 0.1e-2 #1 meter DEM
# grid
xlower = -0.1
xupper =  5.0 
ylower = -0.6
yupper =  0.6
nxpoints = int((xupper-xlower)/dx) + 1
nypoints = int((yupper-ylower)/dx) + 1
gt.topo2writer(outfile,LargeCap_h,xlower,xupper,ylower,yupper,nxpoints,nypoints)

# plane (file for theta...just 0).
outfile= 'ramp_zero.tt2'
outfile = os.path.join(auxdir,outfile)
dx = 0.05 #1 meter DEM
# grid
xlower = -0.1
xupper =  5.0 
ylower = -0.6
yupper =  0.6
nxpoints = int((xupper-xlower)/dx) + 1
nypoints = int((yupper-ylower)/dx) + 1
gt.topo2writer(outfile,zero_plane,xlower,xupper,ylower,yupper,nxpoints,nypoints)




