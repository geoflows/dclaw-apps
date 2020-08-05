"""
Useful things for plotting GeoClaw results.
"""

from pyclaw.plotters import colormaps
from matplotlib.colors import Normalize
from pyclaw.geotools import topotools
from numpy import ma


# Colormaps from geoclaw
# Color attributes, single instance per run
# Colors
black = [0.0,0.0,0.0]
white = [1.0,1.0,1.0]
red = [1.0,0.0,0.0]
green = [0.0,1.0,0.0];
dark_green = [0.1,0.4,0.0];
light_green = [0.8,1.0,0.5];
blue = [0.0,0.0,1.0];
dark_blue = [0.2,0.2,0.7];
light_blue = [0.5,0.5,1.0];
blue_green = [0.0,1.0,1.0];
tan = [0.9,0.8,0.2];
tan = [0.8,0.5,0.2];
tan0 = [0.95,0.95,0.2];
tan1 = [0.9,0.9,0.2];
tan2 = [0.85,0.7,0.2]
tan3 = [0.8,0.5,0.2];
brown = [0.9,0.8,0.2];
gray5 = [0.5,0.5,0.5];
gray6 = [0.6,0.6,0.6];
gray7 = [0.7,0.7,0.7];
gray8 = [0.8,0.8,0.8];
gray9 = [0.9,0.9,0.9];
purple = [0.8,0.3,0.8];

green0 = [.05,0.2,.013];
green1 = [.056,0.24,.01];
green2 = [.068,0.3,.015];
green3 = [.075,.35,.014];
green4 = [.083,.4,.012];
green5 = [.09,.45,.01];
green6 = [.1,.5,.01];
green7 = [.11,.56,.017];
green8 = [.12,.63,.01];
green9 = [.136,.7,.007];
green10 = [.16,.78,.025];
green11 = [.17,.86,.017];
green12 = [.19,.93,.02];
green13 = [.188,.98,.01];
green14 = [.69,.98,.01];

yellow1= [.98,.96,.01];
tan1 = [.98,.83,.01];
tan2 = [.71,.62,.085];
tan3 = [.65,.56,.07];
tan4 = [.58,.50,.064];
tan5 = [.48,.415,.043];
tan6 = [0.42,0.36,0.038];
tan7 = [.36,.233,.029];

brown1=[.42,.167,.03];
brown2=[.2*.42,.2*.167,.2*.03]


# Colormaps
lakelevel=84.3
TSUNAMI_MAX_AMPLITUDE = 0.6

solid_frac_colormap = colormaps.make_colormap({0.0:dark_blue,
                                            #.33: blue,
                                            .50: white,
                                            1.0: brown1})

tsunami_colormap = colormaps.make_colormap({lakelevel-TSUNAMI_MAX_AMPLITUDE:blue,
                                            lakelevel+0.0:blue_green,
                                            lakelevel+TSUNAMI_MAX_AMPLITUDE:red})

tsunami_colormap2 = colormaps.make_colormap({-TSUNAMI_MAX_AMPLITUDE:blue,
                                            0.0:blue_green,
                                            TSUNAMI_MAX_AMPLITUDE:red})
tsunami_colormap_log = colormaps.make_colormap({-4:blue,
                                            0.0:white,
                                            6:red})

oso_debris_colormap = colormaps.make_colormap({0.0:white,
                                            10.0: light_blue,
                                            20.0: blue,
                                            30.0: dark_blue})

oso_debris_colormap_invert = colormaps.make_colormap({0.0:dark_blue,
                                            #10.0: blue,
                                            #20.0: light_blue,
                                            30.0: white})

oso_land_colormap_gray = colormaps.make_colormap({0.0: gray8,
                                           1.0: gray5})

oso_debris_colormap_liquefaction = colormaps.make_colormap({0.0:dark_blue,
                                            #.33: blue,
                                            #.66: light_blue,
                                            1.0: white})

oso_debris_colormap_white = colormaps.make_colormap({0.0:white,
                                            10.0: white,
                                            20.0: white,
                                            30.0: white})

oso_land_colormap = colormaps.make_colormap({0:green0,
                                            0.01: green1,
                                          0.02:green2,
                                          0.5*0.025:green3,
                                          0.5*0.05:green4,
                                          0.5*0.075:green5,
                                          0.5*0.100:green6,
                                          0.5*0.125:green7,
                                          0.5*0.150:green8,
                                          0.5*0.175:green9,
                                          0.5*0.200:green10,
                                          0.5*0.225:green11,
                                          0.5*0.250:green12,
                                          0.5*0.275:green13,
                                          0.5*0.300:green14,
                                          0.325: yellow1,
                                          0.70:tan1,
                                          0.75:tan2,
                                          0.80:tan3,
                                          0.85:tan4,
                                          0.90:tan5,
                                          0.95:tan6,
                                          1.0:tan7})

oso_land_colormap2 = colormaps.make_colormap({0:green0,
        0.01:green1,
        0.1:green14,
        0.2: yellow1,
        0.5:tan5,
        0.6:tan7,
1.0:brown1})

oso_land_colormap3 = colormaps.make_colormap({0:tan1,
        0.01:tan7,
        #0.1: tan3,
        #0.2: tan4,
        #0.5: tan5,
        0.4: brown1,
        #0.9:tan7,
1.0:brown1})

land1_colormap = colormaps.make_colormap({0.0:dark_green,
                                          1000.0:green,
                                          2000.0:light_green,
                                          4000.0:tan})

land2_colormap = colormaps.make_colormap({0:dark_green,
                                          50:green,
                                          100:light_green,
                                          200:tan})

runoutpad_colormap = colormaps.make_colormap({0.0:gray8,
                                              1.0:gray5})

water_land_colormap = colormaps.make_colormap({-1000:dark_blue,
                                               -500:blue,
                                               0:light_blue,
                                               .1:tan,
                                               5:tan,
                                               6:dark_green,
                                               1000:green,
                                               2000:light_green,
                                               4000:tan})

bathy1_colormap = colormaps.make_colormap({-1000:brown,
                                           0:tan,
                                           .1:dark_green,
                                           1000:green,
                                           2000:light_green})

bathy2_colormap = colormaps.make_colormap({-1000:brown,
                                           -100:tan,
                                           0:dark_green,
                                           .1:dark_green,
                                           1000:green,
                                           2000:light_green})

bathy3_colormap = colormaps.make_colormap({-1:[0.3,0.2,0.1],
                                           -0.01:[0.95,0.9,0.7],
                                           .01:[.5,.7,0],
                                           1:[.2,.5,.2]})

seafloor_colormap = colormaps.make_colormap({-1:[0.3,0.2,0.1],
                                              0:[0.95,0.9,0.7]})

land_colormap = colormaps.make_colormap({ 0:[0.95,0.9,0.7],
                                          1:[.2,.5,.2]})

km_colormap = colormaps.make_colormap({ 0:[1,1,1],
                                          1:[0,0,0]})



colormaps_list = {"tsunami":tsunami_colormap,"land1":land1_colormap,
             "land2":land2_colormap,"water_land":water_land_colormap,
"bathy1":bathy1_colormap,"bathy2":bathy2_colormap,"runoutpad":runoutpad_colormap,
"oso_land":oso_land_colormap,"liquefaction":oso_debris_colormap_liquefaction}

colorbar_list = {"landgray": oso_debris_colormap_invert,"liquefaction":oso_debris_colormap_liquefaction,"land":oso_land_colormap3,"km":km_colormap}

def plot_colormaps():
    r"""Plots all colormaps avaiable or the ones specified"""

    import numpy as np
    import matplotlib.pyplot as plt

    a = np.linspace(0, 1, 256).reshape(1,-1)
    a = np.vstack((a,a))

    nmaps = len(colormaps_list) + 1

    fig = plt.figure(figsize=(5,10))
    fig.subplots_adjust(top=0.99, bottom=0.01, left=0.2, right=0.99)

    for i,name in enumerate(colormaps_list):
        ax = plt.subplot(nmaps,1,i+1)
        plt.axis("off")
        plt.imshow(a, aspect='auto', cmap=colormaps_list[name], origin='lower')
        pos = list(ax.get_position().bounds)
        fig.text(pos[0] - 0.01, pos[1], name, fontsize=10, horizontalalignment='right')

def plot_colorbars():
    r"""Plots all colormaps avaiable or the ones specified"""

    import numpy as np
    import matplotlib.pyplot as plt

    a = np.linspace(0, 1, 256).reshape(1,-1)
    a = np.vstack((a,a))

    b=np.hstack((np.linspace(0,0,256/2),np.linspace(1,1,256/2))).reshape(1,-1)
    b = np.vstack((b,b))

    nmaps = len(colorbar_list) + 1

    fig0 = plt.figure(3,figsize=(14,5),dpi=100)
    ax0 = plt.subplot(1,1,1)
    plt.imshow(a, aspect=10,cmap=colorbar_list["landgray"], origin='lower')
    plt.yticks([])
    plt.xticks([0.,255.],["0","30"],fontsize=46)
    plt.xlabel(r"Deposit thickness (m)",fontsize=50)

    fig1 = plt.figure(0,figsize=(14,6),dpi=100)
    ax1 = plt.subplot(1,1,1)
    plt.imshow(a, aspect=10,cmap=colorbar_list["liquefaction"], origin='lower')
    plt.yticks([])
    plt.xticks([0.0,256./2.,255.],["0.0","0.5","1.0"],fontsize=46)
    plt.xlabel(r"Degree of debris liquefaction" "\n" r"($p_b/\rho g_z h$)",fontsize=50)

    fig2 = plt.figure(1,figsize=(14,5),dpi=100)
    ax2 = plt.subplot(1,1,1)
    plt.imshow(a, aspect=10,cmap=colorbar_list["land"], origin='lower')
    plt.yticks([])
    plt.xticks([0.0,256./2.,255.],["80","160","240"],fontsize=46)
    plt.xlabel(r"Elevation (m)",fontsize=50)

    fig3 = plt.figure(2,figsize=(14,5),dpi=100)
    ax3 = plt.subplot(1,1,1)
    plt.imshow(b, aspect=10,cmap=colorbar_list["km"], origin='lower')
    plt.yticks([])
    plt.xticks([0.0,256./2.,255.],["0","1","2"],fontsize=46)
    plt.xlabel(r"km",fontsize=50)
    #fig1.subplots_adjust(top=0.99, bottom=0.01, left=0.2, right=0.99)

    #for i,name in enumerate(colorbar_list):
    #    ax = plt.subplot(nmaps,1,i+1)
    #    plt.axis("off")
    #    plt.imshow(a, aspect='auto', cmap=colorbar_list[name], origin='lower')
    #    pos = list(ax.get_position().bounds)
        #fig.text(pos[0] - 0.01, pos[1], name, fontsize=10, horizontalalignment='right')

    plt.show()

land_colors = colormaps.make_colormap({0:[.5,.7,0], 1:[.2,.5,.2]})
# water_colors = colormaps.make_colormap({-1.:'r', 0.:[0, .8, .8], 1.: 'b'})
# land_colors = land2_colormap
water_colors = tsunami_colormap

# Plotting functions

# The drytol parameter is used in masking land and water and
# affects what color map is used for cells with small water depth h.
# The best value to use often depends on the application and can
# be set for an application by setting current_data.user.drytol in
# a beforeframe function, for example.  If it's not set by the user,
# the following default value is used (in meters):

drytol_default = 1.e-3
i_eta = 6

def topo(current_data):
   """
   Return topography = eta - h.
   Surface eta is assumed to be output as 4th column of fort.q files.
   """
   q = current_data.q
   h = q[:,:,0]
   eta = q[:,:,i_eta]
   topo = eta - h
   return topo

def land(current_data):
   """
   Return a masked array containing the surface elevation only in dry cells.
   """
   from numpy import ma
   drytol = getattr(current_data.user, 'drytol', drytol_default)
   #drytol = 5.e-2
   q = current_data.q
   h = q[:,:,0]
   eta = q[:,:,i_eta]
   land = ma.masked_where(h>drytol, eta)
   return land

def water(current_data):
   """Deprecated: use surface instead."""
   from numpy import ma
   drytol = getattr(current_data.user, 'drytol', drytol_default)
   q = current_data.q
   h = q[:,:,0]
   eta = q[:,:,i_eta]
   water = ma.masked_where(h<=drytol, eta)
   return water

def depth(current_data):
   """
   Return a masked array containing the depth of fluid only in wet cells.
   """
   from numpy import ma
   drytol = getattr(current_data.user, 'drytol', drytol_default)
   #drytol = 5.e-2
   q = current_data.q
   h = q[:,:,0]
   depth = ma.masked_where(h<=drytol, h)
   return depth

def surface(current_data):
   """
   Return a masked array containing the surface elevation only in wet cells.
   Surface is eta = h+topo, assumed to be output as 4th column of fort.q
   files.
   """
   from numpy import ma
   drytol = getattr(current_data.user, 'drytol', drytol_default)
   q = current_data.q
   h = q[:,:,0]
   eta = q[:,:,i_eta]
   water = ma.masked_where(h<=drytol, eta)
   return water

def surface_log(current_data):
   """
   Return a masked array containing the surface elevation only in wet cells.
   Surface is eta = h+topo, assumed to be output as 4th column of fort.q
   files.
   """
   import numpy as np
   from numpy import ma
   drytol = getattr(current_data.user, 'drytol', drytol_default)
   q = current_data.q
   h = q[:,:,0]
   eta = q[:,:,i_eta]
   water = ma.masked_where(h<=drytol, eta)
   water_log = np.sign(eta+1.07)*np.log2(np.abs(eta+1.07)+1.0)
   
   return water_log

def surface_or_depth(current_data):
   """
   Return a masked array containing the surface elevation where the topo is
   below sea level or the water depth where the topo is above sea level.
   Mask out dry cells.  Assumes sea level is at topo=0.
   Surface is eta = h+topo, assumed to be output as 4th column of fort.q
   files.
   """
   from numpy import ma, where
   drytol = getattr(current_data.user, 'drytol', drytol_default)
   q = current_data.q
   h = q[:,:,0]
   eta = q[:,:,i_eta]
   topo = eta - h
   surface = ma.masked_where(h<=drytol, eta)
   depth = ma.masked_where(h<=drytol, h)
   surface_or_depth = where(topo<0, surface, depth)
   return surface_or_depth

def velocity_u(current_data):
   """
   Return a masked array containing velocity u in wet cells.
   """
   from numpy import ma
   drytol = getattr(current_data.user, 'drytol', drytol_default)
   drytol = 1.0
   q = current_data.q
   h = q[:,:,0]
   hu = q[:,:,1]
   u = ma.masked_where(h<=drytol, hu/h)
   return u

def velocity_v(current_data):
   """
   Return a masked array containing velocity v in wet cells.
   """
   from numpy import ma
   drytol = getattr(current_data.user, 'drytol', drytol_default)
   drytol = 1.0
   q = current_data.q
   h = q[:,:,0]
   hv = q[:,:,2]
   v = ma.masked_where(h<=drytol, hv/h)
   return v

def velocity(current_data):
   """
   Return a masked array containing velocity v in wet cells.
   """
   from numpy import ma
   drytol = getattr(current_data.user, 'drytol', drytol_default)
   q = current_data.q
   h = q[:,:,0]
   hv = q[:,:,2]
   u = ma.masked_where(h<=drytol, hv/h)
   hv = q[:,:,2]
   v = ma.masked_where(h<=drytol, hv/h)
   return (u,v)


class TopoPlotData(object):
    def __init__(self, fname):
        self.fname = fname
        self.topotype = 3
        self.neg_cmap = None
        self.pos_cmap = None
        self.cmax = 100.
        self.cmin = -4000.
        self.climits = None
        self.figno = 200
        self.addcolorbar = False
        self.addcontour = False
        self.contour_levels = [0, 0]
        self.xlimits = None
        self.ylimits = None
        self.coarsen = 1
        self.imshow = True
        self.gridedges_show = True
        self.print_fname = True

    def plot(self):
        plot_topo_file(self)


def plot_topo_file(topoplotdata):
    """
    Read in a topo or bathy file and produce a pcolor map.
    """

    import os
    import pylab
    from pyclaw.data import Data

    fname = topoplotdata.fname
    topotype = topoplotdata.topotype
    if topoplotdata.climits:
        # deprecated option
        cmin = topoplotdata.climits[0]
        cmax = topoplotdata.climits[1]
    else:
        cmin = topoplotdata.cmin
        cmax = topoplotdata.cmax
    figno = topoplotdata.figno
    addcolorbar = topoplotdata.addcolorbar
    addcontour = topoplotdata.addcontour
    contour_levels = topoplotdata.contour_levels
    xlimits = topoplotdata.xlimits
    ylimits = topoplotdata.ylimits
    coarsen = topoplotdata.coarsen
    imshow = topoplotdata.imshow
    gridedges_show = topoplotdata.gridedges_show
    neg_cmap = topoplotdata.neg_cmap
    pos_cmap = topoplotdata.pos_cmap
    print_fname = topoplotdata.print_fname


    if neg_cmap is None:
        neg_cmap = colormaps.make_colormap({cmin:[0.3,0.2,0.1],
                                                0:[0.95,0.9,0.7]})
    if pos_cmap is None:
        pos_cmap = colormaps.make_colormap({    0:[.5,.7,0],
                                              cmax:[.2,.5,.2]})

    if abs(topotype) == 1:

        X,Y,topo = topotools.topofile2griddata(fname, topotype)
        topo = pylab.flipud(topo)
        Y = pylab.flipud(Y)
        x = X[0,:]
        y = Y[:,0]
        xllcorner = x[0]
        yllcorner = y[0]
        cellsize = x[1]-x[0]


    elif abs(topotype) == 3:

        file = open(fname, 'r')
        lines = file.readlines()
        ncols = int(lines[0].split()[0])
        nrows = int(lines[1].split()[0])
        xllcorner = float(lines[2].split()[0])
        yllcorner = float(lines[3].split()[0])
        cellsize = float(lines[4].split()[0])
        NODATA_value = int(lines[5].split()[0])

        print "Loading file ",fname
        print "   nrows = %i, ncols = %i" % (nrows,ncols)
        topo = pylab.loadtxt(fname,skiprows=6,dtype=float)
        print "   Done loading"

        if 0:
            topo = []
            for i in range(nrows):
                topo.append(pylab.array(lines[6+i],))
            print '+++ topo = ',topo
            topo = pylab.array(topo)

        topo = pylab.flipud(topo)

        x = pylab.linspace(xllcorner, xllcorner+ncols*cellsize, ncols)
        y = pylab.linspace(yllcorner, yllcorner+nrows*cellsize, nrows)
        print "Shape of x, y, topo: ", x.shape, y.shape, topo.shape

    else:
        raise Exception("*** Only topotypes 1 and 3 supported so far")


    if coarsen > 1:
        topo = topo[slice(0,nrows,coarsen), slice(0,ncols,coarsen)]
        x = x[slice(0,ncols,coarsen)]
        y = y[slice(0,nrows,coarsen)]
        print "Shapes after coarsening: ", x.shape, y.shape, topo.shape


    if topotype < 0:
        topo = -topo

    if figno:
        pylab.figure(figno)

    if topoplotdata.imshow:
            color_norm = Normalize(cmin,cmax,clip=True)
            xylimits = (x[0],x[-1],y[0],y[-1])
            #pylab.imshow(pylab.flipud(topo.T), extent=xylimits, \
            pylab.imshow(pylab.flipud(topo), extent=xylimits, \
                    cmap=cmap, interpolation='nearest', \
                    norm=color_norm)
    else:
        neg_topo = ma.masked_where(topo>0., topo)
        all_masked = (ma.count(neg_topo) == 0)
        if not all_masked:
            pylab.pcolormesh(x,y,neg_topo,cmap=neg_cmap)
            pylab.clim([cmin,0])
            if addcolorbar:
                pylab.colorbar()

        pos_topo = ma.masked_where(topo<0., topo)
        all_masked = (ma.count(pos_topo) == 0)
        if not all_masked:
            pylab.pcolormesh(x,y,pos_topo,cmap=pos_cmap)
            pylab.clim([0,cmax])
            if addcolorbar:
                pylab.colorbar()

    pylab.axis('scaled')


    if addcontour:
        pylab.contour(x,y,topo,levels=contour_levels,colors='k')

    if gridedges_show:
        pylab.plot([x[0],x[-1]],[y[0],y[0]],'k')
        pylab.plot([x[0],x[-1]],[y[-1],y[-1]],'k')
        pylab.plot([x[0],x[0]],[y[0],y[-1]],'k')
        pylab.plot([x[-1],x[-1]],[y[0],y[-1]],'k')

    if print_fname:
        fname2 = os.path.splitext(fname)[0]
        pylab.text(xllcorner+cellsize, yllcorner+cellsize, fname2, color='m')

    topodata = Data()
    topodata.x = x
    topodata.y = y
    topodata.topo = topo

    return topodata
