"""
Module to set up run time parameters for Clawpack.

The values set in the function setrun are then written out to data files
that will be read in by the Fortran code.

"""

import os
from pyclaw import data
import numpy as np


#------------------------------
def setrun(claw_pkg='geoclaw'):
#------------------------------

    """
    Define the parameters used for running Clawpack.

    INPUT:
        claw_pkg expected to be "geoclaw" for this setrun.

    OUTPUT:
        rundata - object of class ClawRunData

    """

    #assert claw_pkg.lower() == 'geoclaw',  "Expected claw_pkg = 'geoclaw'"
    ndim = 2
    rundata = data.ClawRunData(claw_pkg, ndim)

    #------------------------------------------------------------------
    # GeoClaw specific parameters:
    #------------------------------------------------------------------

    rundata = setgeo(rundata)   # Defined below


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
    # DEM limits
    import os
    import geotools.topotools as gt
    
    topopath=os.path.join(os.environ['TOPO'],'SpiritLake','dtm_spiritlakedomain_10m')
    bfile=os.path.join(topopath,'dtm_spiritlakedomain_10m.tt3')
    #bfile = os.path.join(topopath,'lakemissoula1265.tt3')
    a=gt.topoboundary(bfile)
    xll = a[0] #-10000.
    yll = a[2] # +10000.
    xu = a[1] #-5000.
    yu = a[3] # 1.58e6 + 10000. #a[3]

    header = gt.topoheaderread(bfile)
    cell = header['cellsize']
    coarsen = 1
    cell = cell*coarsen

    rc = 1 #factor of coarsening from DEM resolution
    r1 = 8
    r2 = 8/rc
    

    clawdata.xlower =  xll + 1.0*cell*r1*r2
    clawdata.xupper =  xu  - 1.0*cell*r1*r2

    clawdata.ylower =  yll + 1.0*cell*r1*r2
    clawdata.yupper =  yu  - 1.0*cell*r1*r2

    # Number of grid cells:
    clawdata.mx = int((clawdata.xupper-clawdata.xlower)/(cell*r1*r2*rc))
    clawdata.my = int((clawdata.yupper-clawdata.ylower)/(cell*r1*r2*rc))


    # ---------------
    # Size of system:
    # ---------------

    # Number of equations in the system:
    clawdata.meqn = 3

    # Number of auxiliary variables in the aux array (initialized in setaux)
    clawdata.maux = 3

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
        hours = 12.
        minutes = 0.
        final_seconds  = hours*3600. + minutes*60.
        clawdata.tfinal = final_seconds
        clawdata.nout = 144

    elif clawdata.outstyle == 2:
        # Specify a list of output times.
        clawdata.tout =  [10.0,53.0e3,55.e3]

        clawdata.nout = len(clawdata.tout)

    elif clawdata.outstyle == 3:
        # Output every iout timesteps with a total of ntot time steps:
        iout = 1
        ntot = 3
        clawdata.iout = [iout, ntot]



    # ---------------------------------------------------
    # Verbosity of messages to screen during integration:
    # ---------------------------------------------------

    # The current t, dt, and cfl will be printed every time step
    # at AMR levels <= verbosity.  Set verbosity = 0 for no printing.
    #   (E.g. verbosity == 2 means print only on levels 1 and 2.)
    clawdata.verbosity = 1



    # --------------
    # Time stepping:
    # --------------

    # if dt_variable==1: variable time steps used based on cfl_desired,
    # if dt_variable==0: fixed time steps dt = dt_initial will always be used.
    clawdata.dt_variable = 1

    # Initial time step for variable dt.
    # If dt_variable==0 then dt=dt_initial for all steps:
    clawdata.dt_initial = 1.e-8

    # Max time step to be allowed if variable dt used:
    clawdata.dt_max = 1e+99

    # Desired Courant number if variable dt used, and max to allow without
    # retaking step with a smaller dt:
    clawdata.cfl_desired = 0.4
    clawdata.cfl_max = 0.99

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
    clawdata.mwaves = 3

    # List of limiters to use for each wave family:
    # Required:  len(mthlim) == mwaves
    clawdata.mthlim = [4,4,4]

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
    mxnest = 3

    clawdata.mxnest = -mxnest   # negative ==> anisotropic refinement in x,y,t

    # List of refinement ratios at each level (length at least mxnest-1)
    clawdata.inratx = [r1,r2]
    clawdata.inraty = [r1,r2]
    clawdata.inratt = [r1,r2]


    # Specify type of each aux variable in clawdata.auxtype.
    # This must be a list of length maux, each element of which is one of:
    #   'center',  'capacity', 'xleft', or 'yleft'  (see documentation).

    clawdata.auxtype = ['center','center','yleft']


    clawdata.tol = -1.0     # negative ==> don't use Richardson estimator
    clawdata.tolsp = 0.5    # used in default flag2refine subroutine
                            # (Not used in geoclaw!)

    clawdata.kcheck = 2     # how often to regrid (every kcheck steps)
    clawdata.ibuff  = 4     # width of buffer zone around flagged points
    clawdata.cutoff = 0.7   # efficiency cutoff for grid generator
    clawdata.checkpt_iousr = 2800
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
    geodata.icoordsys = 1 #set to 2 for use with lat-lon coordinates on the sphere
    geodata.icoriolis = 0
    geodata.Rearth = Rearth

    # == settsunami.data values ==
    geodata.sealevel = 0.0
    geodata.drytolerance = 1.e-3
    geodata.wavetolerance = 5.e-2
    geodata.depthdeep = 1.e2
    geodata.maxleveldeep = 1
    geodata.ifriction = 1
    geodata.coeffmanning = 0.033
    geodata.frictiondepth = 10000.0

    # == settopo.data values ==

    # for topography, append lines of the form:
    #   [topotype, minlevel,maxlevel,t0,tend,fname]
    # minlevel and maxlevel specify the minimum and maximum level of refinement in
    #   the region specified by the topography file.
    # if minlevel and maxlevel are set to 1 and the total number of levels
    # refinement occurs `normally.' ie. based on flowgrades etc.
    # where topotype specifies the file format. See clawpack doc.
    # the time interval specifies when the refinement rule is specified

    geodata.topofiles = []
    import os


    topopath=os.path.join(os.environ['TOPO'],'SpiritLake')


    topofile1=os.path.join(topopath,'dtm_spiritlakedomain_10m','dtm_spiritlakedomain_10m.tt3')
    geodata.topofiles.append([3, 1, 3, 0.0, 1.e10, topofile1])

    #topofile2=os.path.join(topopath,'dtm_with_north_channel_cut','dtm_with_north_channel_cut.tt3')
    topofile2=os.path.join(topopath,'SpiritLake_south_channel','dtm_cps_channeleastarm','dtm_cps_channeleastarm.tt3')
    geodata.topofiles.append([3, 1, 3, 0.0, 1.e10, topofile2])
   

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


    qinitfileeta = os.path.join(topopath,'SpiritLake1050p4','spiritlake1050p4.tt3')
    geodata.qinitfiles.append([3,4,3,3,qinitfileeta])

    # == setauxinit.data values ==
    geodata.auxinitfiles = []

    # == setregions.data values ==
    geodata.regions = []
    # to specify regions of refinement append lines of the form
    #  [minlevel,maxlevel,t1,t2,x1,x2,y1,y2]
    #geodata.regions.append([])

    # == setgauges.data values ==
    geodata.gauges = []
    # for gauges append lines of the form  [gaugeno, x, y, t0, tf]
    #geodata.gauges.append([1, -155.056, 19.731, 50.e3, 60e3])

    # == setfixedgrids.data values ==
    geodata.fixedgrids = []
    # for fixed grids append lines of the form
    # Note: this is only for viewing output in non-AMR formats. This doesn't not affect the actual computation.
    # [t1,t2,noutput,x1,x2,y1,y2,xpoints,ypoints,\
    #  ioutarrivaltimes,ioutsurfacemax]


    #geodata.fixedgrids.append([0.0,1.e10,100,x1,x2,y1,y2,mx,my,0,0])

    # == setflowgrades.data values ==
    geodata.flowgrades = []
    # this can be used to specify refinement criteria, for non-tsunami problems.
    # for using flowgrades for refinement append lines of the form
    # [flowgradevalue, flowgradevariable, flowgradetype, flowgrademinlevel]
    # where:
    #flowgradevalue: floating point relevant flowgrade value for following measure:
    #flowgradevariable: 1=depth, 2= momentum, 3 = sign(depth)*(depth+topo) (0 at sealevel or dry land).
    #flowgradetype: 1 = norm(flowgradevariable), 2 = norm(grad(flowgradevariable))
    #flowgrademinlevel: refine to at least this level if flowgradevalue is exceeded.
    geodata.flowgrades.append([1.e-3, 1, 1, 3])
    geodata.flowgrades.append([1.e-8, 2, 1, 3])

    return rundata


if __name__ == '__main__':
    # Set up run-time parameters and write all data files.
    import sys

    if len(sys.argv) == 2:
        rundata = setrun(sys.argv[1])
    else:
        rundata = setrun()

    rundata.write()

