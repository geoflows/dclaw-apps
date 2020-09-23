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


# initial failure surface b
outfile= 'Mt_Tanh_log_eta.tt2'
outfile = os.path.join(topodir,outfile)
dx = 1.0 #1 meter DEM
# grid [~0 , 10 km] X [-2.5 , 2.5 km]
xlower = -1000.0 
xupper = 25.0e3 
ylower = -10e3
yupper =  10e3
nxpoints = int((xupper-xlower)/dx) + 1
nypoints = int((yupper-ylower)/dx) + 1
gt.topo2writer(outfile,mt_tanh_log_eta,xlower,xupper,ylower,yupper,nxpoints,nypoints)

# initial surface eta (h+b)
outfile= 'Mt_Tanh_log_eta_gausshump.tt2'
outfile = os.path.join(qinitdir,outfile)
dx = 1.0 #1 meter DEM
# grid [~0 , 10 km] X [-2.5 , 2.5 km]
xlower = -100.0 
xupper = 2000.0 
ylower = -1000.0
yupper =  1000.0
nxpoints = int((xupper-xlower)/dx) + 1
nypoints = int((yupper-ylower)/dx) + 1
gt.topo2writer(outfile,mt_tanh_gauss_eta,xlower,xupper,ylower,yupper,nxpoints,nypoints)

# depth
# initial surface eta (h+b)
outfile= 'h_gausshump.tt2'
outfile = os.path.join(qinitdir,outfile)
dx = 1.0 #1 meter DEM
# grid [~0 , 10 km] X [-2.5 , 2.5 km]
xlower = -100.0 
xupper = 2000.0 
ylower = -1000.0
yupper =  1000.0
nxpoints = int((xupper-xlower)/dx) + 1
nypoints = int((yupper-ylower)/dx) + 1
gt.topo2writer(outfile,gauss_h,xlower,xupper,ylower,yupper,nxpoints,nypoints)


#phi file
outfile= 'Phi.tt2'
outfile = os.path.join(auxdir,outfile)
dx = 1.0 #1 meter DEM
# grid [~0 , 10 km] X [-2.5 , 2.5 km]
xlower = -1000.0 
xupper = 25.0e3 
ylower = -10e3
yupper =  10e3
nxpoints = int((xupper-xlower)/dx) + 1
nypoints = int((yupper-ylower)/dx) + 1
gt.topo2writer(outfile,phi_uniform,xlower,xupper,ylower,yupper,nxpoints,nypoints)

