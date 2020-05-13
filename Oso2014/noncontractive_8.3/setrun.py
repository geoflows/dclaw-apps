"""
Module to set up run time parameters for Clawpack.

The values set in the function setrun are then written out to data files
that will be read in by the Fortran code.

"""

import os
from pyclaw import data
import numpy as np


#------------------------------
def setrun(claw_pkg='digclaw'):
#------------------------------

    """
    Define the parameters used for running Clawpack.

    INPUT:
        claw_pkg expected to be "geoclaw" for this setrun.

    OUTPUT:
        rundata - object of class ClawRunData

    """

    #assert claw_pkg.lower() == 'digclaw',  "Expected claw_pkg = 'digclaw'"
    ndim = 2
    rundata = data.ClawRunData(claw_pkg, ndim)

    #------------------------------------------------------------------
    # GeoClaw specific parameters:
    #------------------------------------------------------------------

    rundata = setgeo(rundata)   # Defined below

    #------------------------------------------------------------------
    # DigClaw specific parameters:
    #------------------------------------------------------------------

    rundata = setdig(rundata)   # Defined below

    #------------------------------------------------------------------
    # Standard Clawpack parameters to be written to claw.data:
    #   (or to amr2ez.data for AMR)
    #------------------------------------------------------------------

    clawdata = rundata.clawdata  # initialized when rundata instantiated


    # Set single grid parameters first.
    # See below for AMR parameters.


    # ---------------
    # Spatial domain:
    # ---------------

    # Number of space dimensions:
    clawdata.ndim = ndim

    # Lower and upper edge of computational domain:


    clawdata.xlower = 424000.0
    clawdata.xupper = 426000.0

    clawdata.ylower = 141800.0
    clawdata.yupper = 143600.0


    # Number of grid cells:
    clawdata.mx = 72
    clawdata.my = 66


    # ---------------
    # Size of system:
    # ---------------

    # Number of equations in the system:
    clawdata.meqn = 7

    # Number of auxiliary variables in the aux array (initialized in setaux)
    clawdata.maux = 10

    # Index of aux array corresponding to capacity function, if there is one:
    clawdata.mcapa = 0



    # -------------
    # Initial time:
    # -------------

    clawdata.t0 = 0.0


    # -------------
    # Output times:
    #--------------

    # Specify at what times the results should be written to fort.q files.
    # Note that the time integration stops after the final output time.
    # The solution at initial time t0 is always written in addition.

    clawdata.outstyle = 1

    if clawdata.outstyle==1:
        # Output nout frames at equally spaced times up to tfinal:
        clawdata.nout = 130
        clawdata.tfinal = 130.0

    elif clawdata.outstyle == 2:
        # Specify a list of output times.
        clawdata.tout =  [0.0,10.0,70.0,600.0,1200.0]

        clawdata.nout = len(clawdata.tout)

    elif clawdata.outstyle == 3:
        # Output every iout timesteps with a total of ntot time steps:
        iout = 1
        ntot = 100
        clawdata.iout = [iout, ntot]



    # ---------------------------------------------------
    # Verbosity of messages to screen during integration:
    # ---------------------------------------------------

    # The current t, dt, and cfl will be printed every time step
    # at AMR levels <= verbosity.  Set verbosity = 0 for no printing.
    #   (E.g. verbosity == 2 means print only on levels 1 and 2.)
    clawdata.verbosity = 0



    # --------------
    # Time stepping:
    # --------------

    # if dt_variable==1: variable time steps used based on cfl_desired,
    # if dt_variable==0: fixed time steps dt = dt_initial will always be used.
    clawdata.dt_variable = 1

    # Initial time step for variable dt.
    # If dt_variable==0 then dt=dt_initial for all steps:
    clawdata.dt_initial = 1.e-16

    # Max time step to be allowed if variable dt used:
    clawdata.dt_max = 1e+99

    # Desired Courant number if variable dt used, and max to allow without
    # retaking step with a smaller dt:
    clawdata.cfl_desired = 0.25
    clawdata.cfl_max = 0.5

    # Maximum number of time steps to allow between output times:
    clawdata.max_steps = 100000




    # ------------------
    # Method to be used:
    # ------------------

    # Order of accuracy:  1 => Godunov,  2 => Lax-Wendroff plus limiters
    clawdata.order = 1

    # Transverse order for 2d or 3d (not used in 1d):
    clawdata.order_trans = 0

    # Number of waves in the Riemann solution:
    clawdata.mwaves = 5

    # List of limiters to use for each wave family:
    # Required:  len(mthlim) == mwaves
    clawdata.mthlim = [4,4,4,4,4,4]

    # Source terms splitting:
    #   src_split == 0  => no source term (src routine never called)
    #   src_split == 1  => Godunov (1st order) splitting used,
    #   src_split == 2  => Strang (2nd order) splitting used,  not recommended.
    clawdata.src_split = 1


    # --------------------
    # Boundary conditions:
    # --------------------

    # Number of ghost cells (usually 2)
    clawdata.mbc = 2

    # Choice of BCs at xlower and xupper:
    #   0 => user specified (must modify bcN.f to use this option)
    #   1 => extrapolation (non-reflecting outflow)
    #   2 => periodic (must specify this at both boundaries)
    #   3 => solid wall for systems where q(2) is normal velocity

    clawdata.mthbc_xlower = 1
    clawdata.mthbc_xupper = 1

    clawdata.mthbc_ylower = 1
    clawdata.mthbc_yupper = 1


    # ---------------
    # AMR parameters:
    # ---------------


    # max number of refinement levels:
    mxnest = 2

    clawdata.mxnest = -mxnest   # negative ==> anisotropic refinement in x,y,t

    # List of refinement ratios at each level (length at least mxnest-1)
    clawdata.inratx = [8,4,8]
    clawdata.inraty = [8,4,8]
    clawdata.inratt = [8,4,8]


    # Specify type of each aux variable in clawdata.auxtype.
    # This must be a list of length maux, each element of which is one of:
    #   'center',  'capacity', 'xleft', or 'yleft'  (see documentation).

    clawdata.auxtype = ['center','center','yleft','center','center','xleft','yleft','xleft','yleft']


    clawdata.tol = -1.0     # negative ==> don't use Richardson estimator
    clawdata.tolsp = 0.5    # used in default flag2refine subroutine
                            # (Not used in geoclaw!)

    clawdata.kcheck = 3     # how often to regrid (every kcheck steps)
    clawdata.ibuff  = 3     # width of buffer zone around flagged points
    clawdata.cutoff = 0.7   # efficiency cutoff for grid generator
    clawdata.checkpt_iousr = 10000000
    clawdata.restart = False
    # More AMR parameters can be set -- see the defaults in pyclaw/data.py

    return rundata
    # end of function setrun
    # ----------------------

def setgeo(rundata):
    """
    Set GeoClaw specific runtime parameters.
    For documentation see ....
    """

    try:
        geodata = rundata.geodata
    except:
        print "*** Error, this rundata has no geodata attribute"
        raise AttributeError("Missing geodata attribute")

    geodata.variable_dt_refinement_ratios = True

    # == setgeo.data values ==
    R1=6357.e3 #polar radius
    R2=6378.e3 #equatorial radius
    Rearth=.5*(R1+R2)
    geodata.igravity = 1
    geodata.gravity = 9.81
    geodata.icoordsys = 1
    geodata.icoriolis = 0
    geodata.Rearth = Rearth

    # == settsunami.data values ==
    geodata.sealevel = -1000.
    geodata.drytolerance = 1.e-3
    geodata.wavetolerance = 5.e-2
    geodata.depthdeep = 1.e2
    geodata.maxleveldeep = 1
    geodata.ifriction = 1
    geodata.coeffmanning = 0.033
    geodata.frictiondepth = 0.01

    # == settopo.data values ==
    # set a path variable for the base topo directory for portability
    import os
    topo=os.environ['TOPO']
    topopath = os.path.join(topo,'stillaguamish')

    topofile1= 'oso_2013_m.tt2'
    topopath1 = os.path.join(topopath,topofile1)

    slipdir = 'SendMay6'
    basename = 'poly2ec'

    topofile2 = basename+'_burnin2013_m.tt2'
    topopath2 = os.path.join(topopath,slipdir,topofile2)



    geodata.topofiles = []
    geodata.topofiles.append([2, 1, 4, -1.0, 1.e10, topopath1])
    geodata.topofiles.append([2, 4, 4, -1.0, 1.e10, topopath2])
    #geodata.topofiles.append([2, 4, 4, -1.0, 1.e10, topopath3])
    #geodata.topofiles.append([2, 4, 4, -1.0, 1.e10, topopath4])

    # == setdtopo.data values ==
    # == setdtopo.data values ==
    geodata.dtopofiles = []
    # for moving topography, append lines of the form:
    #   [topotype, minlevel,maxlevel,fname]

    #geodata.dtopofiles.append([1,3,3,'subfault.tt1'])

    # == setqinit.data values ==
    geodata.qinitfiles = []
    # for qinit perturbations append lines of the form
    #   [qinitftype,iqinit, minlev, maxlev, fname]

    #qinitftype: file-type, same as topo files, ie: 1, 2 or 3
    #The following values are allowed for iqinit:
        #n=1,mq perturbation of q(i,j,n)
        #n=mq+1: surface elevation eta is defined by the file and results in h=max(eta-b,0)
    #initfile = os.path.join(topopath,'nofkstill_prefailure_eta_large-3.tt2')

    initfile = os.path.join(topopath,slipdir,basename+'_h_m.tt2')
    geodata.qinitfiles.append([2,1,3,3,initfile])


    geodata.auxinitfiles = []

    # == setregions.data values ==
    geodata.regions = []
    # to specify regions of refinement append lines of the form
    #  [minlevel,maxlevel,t1,t2,x1,x2,y1,y2]
    ft2m = 0.3048
    xlow = 1392016.909*ft2m
    ylow = 471124.084*ft2m
    xhi = 1394398.231*ft2m
    yhi = 469324.389*ft2m
    geodata.regions.append([4,4,-10.0,10.e3,xlow,xhi,ylow,yhi])
    #geodata.regions.append([4,4,-10.0,10.e3,0.9580e6,0.9583e6,1.8342e6,1.8352e6])

    # == setgauges.data values ==
    geodata.gauges = []
    # for gauges append lines of the form  [gaugeno, x, y, t0, tf]
    #geodata.gauges.append([1, -155.056, 19.731, 50.e3, 60e3])

    # == setfixedgrids.data values ==
    geodata.fixedgrids = []
    # for fixed grids append lines of the form
    # [t1,t2,noutput,x1,x2,y1,y2,xpoints,ypoints,\
    #  ioutarrivaltimes,ioutsurfacemax]
    #geodata.fixedgrids.append([54.e3,55.e3,100,-101.,-96.,14.,19.,1000,1000,0,0])

    # == setflowgrades.data values ==
    geodata.flowgrades = []
    # for using flowgrades for refinement append lines of the form
    # [flowgradevalue, flowgradevariable, flowgradetype, flowgrademinlevel]
    # where:
    #flowgradevalue: floating point relevant flowgrade value for following measure:
    #flowgradevariable: 1=depth, 2= momentum, 3 = sign(depth)*(depth+topo) (0 at sealevel or dry land).
    #flowgradetype: 1 = norm(flowgradevariable), 2 = norm(grad(flowgradevariable))
    #flowgrademinlevel: refine to at least this level if flowgradevalue is exceeded.
    #geodata.flowgrades.append([1.e-5, 3, 1, 4])
    geodata.flowgrades.append([0.01, 1, 1, 3])

    return rundata

def setdig(rundata):
    """
    Set DigClaw specific runtime parameters.
    For documentation see ....
    """

    try:
        digdata = rundata.digdata
    except:
        print "*** Error, this rundata has no digdata attribute"
        raise AttributeError("Missing digdata attribute")

    #set non-default values if needed
    digdata.c1 = 1.0
    digdata.rho_f = 1100.0
    digdata.rho_s = 2700.0
    digdata.phi_bed = 36.0
    digdata.phi_int = 36.0
    digdata.mu = 0.005
    digdata.m0 = 0.64
    digdata.m_crit = 0.64
    permeability = 1.0e-8
    digdata.kappita = permeability
    digdata.alpha_c = 0.03
    digdata.delta = 0.01
    digdata.bed_normal = 0
    digdata.phys_tol = rundata.geodata.drytolerance
    digdata.entrainment = 0
    digdata.entrainment_rate = 0.0
    digdata.sigma_0 = 1.e3

    digdata.init_ptype = 0
    digdata.init_pmax_ratio = 1.00e0
    digdata.init_ptf = 0.0
    digdata.init_ptf2= 0.0

    #to reduce to shallow water equations, uncomment the following
    #digdata.c1= 0.0
    #digdata.phi_int = 0.0
    #digdata.phi_bed = 0.0
    #digdata.kappita = 0.0
    #digdata.mu = 0.0



    return rundata


if __name__ == '__main__':
    # Set up run-time parameters and write all data files.
    import sys

    if len(sys.argv) == 2:
        rundata = setrun(sys.argv[1])
    else:
        rundata = setrun()

    rundata.write()

