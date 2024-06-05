"""
setinit:
create synthetic topo DEMs

"""

import numpy as np
import clawpack.dclaw.topotools as gt
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


# initial surface (eta) (note: this uses same function as topo for eta)
outfile= 'Mt_Tanh_log_eta_1m.tt2'
outfile = os.path.join(qinitdir,outfile)
dx = 1.0 #1 meter DEM
# grid [~0 , 10 km] X [-2.5 , 2.5 km]
xlower = -100.0 
xupper = 2.0e3 
ylower = -1.0e3
yupper =  1.0e3
nxpoints = int((xupper-xlower)/dx) + 1
nypoints = int((yupper-ylower)/dx) + 1
gt.topo2writer(outfile,mt_tanh_log_eta,xlower,xupper,ylower,yupper,nxpoints,nypoints)

# initial depth (note: optional file if initialization by depth for testing)
outfile= 'src_quadratic_Mt_Tanh_h_1m.tt2'
outfile = os.path.join(qinitdir,outfile)
dx = 1.0 #1 meter DEM
# grid [~0 , 2 km] X [-1 , 1 km]
xlower = -100.0 
xupper = 2.0e3 
ylower = -1e3
yupper =  1e3
nxpoints = int((xupper-xlower)/dx) + 1
nypoints = int((yupper-ylower)/dx) + 1
gt.topo2writer(outfile,src_quadratic_h,xlower,xupper,ylower,yupper,nxpoints,nypoints)


# failure surface and surrounding topo on fine DEM near src (b)
outfile= 'src_quadratic_Mt_Tanh_b_1m.tt2'
outfile = os.path.join(topodir,outfile)
dx = 1.0 #1 meter DEM
# grid [~0 , 10 km] X [-2.5 , 2.5 km]
xlower = -150.0 
xupper = 3.0e3 
ylower = -1.5e3
yupper =  1.5e3
nxpoints = int((xupper-xlower)/dx) + 1
nypoints = int((yupper-ylower)/dx) + 1
gt.topo2writer(outfile,src_quadratic_b,xlower,xupper,ylower,yupper,nxpoints,nypoints)

# failure surface and surrounding topo for domain (coarse) (b)
outfile= 'src_quadratic_Mt_Tanh_b_10m.tt2'
outfile = os.path.join(topodir,outfile)
dx = 10.0 #1 meter DEM
# grid [~0 , 10 km] X [-2.5 , 2.5 km]
xlower = -1000.0 
xupper = 25.0e3 
ylower = -10e3
yupper =  10e3
nxpoints = int((xupper-xlower)/dx) + 1
nypoints = int((yupper-ylower)/dx) + 1
gt.topo2writer(outfile,src_quadratic_b,xlower,xupper,ylower,yupper,nxpoints,nypoints)

#phi file (optional variable friction)
outfile= 'Phi_10m.tt2'
outfile = os.path.join(auxdir,outfile)
dx = 10.0 #10 meter DEM
# grid [~0 , 10 km] X [-2.5 , 2.5 km]
xlower = -1000.0 
xupper = 25.0e3 
ylower = -10e3
yupper =  10e3
nxpoints = int((xupper-xlower)/dx) + 1
nypoints = int((yupper-ylower)/dx) + 1
gt.topo2writer(outfile,phi_uniform,xlower,xupper,ylower,yupper,nxpoints,nypoints)

