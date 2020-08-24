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
topodir = os.path.join(cdir,'topo')
auxdir = os.path.join(cdir,'aux')
qinitdir = os.path.join(cdir,'qinit')

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


# initial surface topo (eta)
outfile= 'Mt_Tanh_log_eta.tt2'
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

# failure surface and surrounding topo (b)
outfile= 'src_quadratic_Mt_Tanh_b.tt2'
outfile = os.path.join(topodir,outfile)
dx = 1.0 #1 meter DEM
# grid [~0 , 10 km] X [-2.5 , 2.5 km]
xlower = -100.0 
xupper = 10.0e3 
ylower = -2.5e3
yupper =  2.5e3
nxpoints = int((xupper-xlower)/dx) + 1
nypoints = int((yupper-ylower)/dx) + 1
gt.topo2writer(outfile,src_quadratic_b,xlower,xupper,ylower,yupper,nxpoints,nypoints)

# depth
outfile= 'src_quadratic_Mt_Tanh_h.tt2'
outfile = os.path.join(qinitdir,outfile)
dx = 1.0 #1 meter DEM
# grid [~0 , 2 km] X [-1 , 1 km]
xlower = -100.0
xupper = 2.0e3 
ylower = -1.0e3
yupper =  1.0e3
nxpoints = int((xupper-xlower)/dx) + 1
nypoints = int((yupper-ylower)/dx) + 1
gt.topo2writer(outfile,src_quadratic_h,xlower,xupper,ylower,yupper,nxpoints,nypoints)


#phi file
outfile= 'Phi.tt2'
outfile = os.path.join(auxdir,outfile)
dx = 1.0 #1 meter DEM
# grid [~0 , 10 km] X [-2.5 , 2.5 km]
xlower = -100.0 
xupper = 10.0e3 
ylower = -2.5e3
yupper =  2.5e3
nxpoints = int((xupper-xlower)/dx) + 1
nypoints = int((yupper-ylower)/dx) + 1
gt.topo2writer(outfile,phi_uniform,xlower,xupper,ylower,yupper,nxpoints,nypoints)
