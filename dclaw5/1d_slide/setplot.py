
"""
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.

"""

import numpy as np
import matplotlib.pyplot as plt
import cmocean
import matplotlib as mpl

from clawpack.visclaw import geoplot
from clawpack.visclaw import colormaps
from clawpack.visclaw import gridtools 


import os,sys

sea_level = 100.

#--------------------------
def setplot(plotdata=None):
#--------------------------

    """
    Specify what is to be plotted at each frame.
    Input:  plotdata, an instance of pyclaw.plotters.data.ClawPlotData.
    Output: a modified version of plotdata.

    """


    import clawpack.dclaw.plot as dplot
    from numpy import linspace

    if plotdata is None:
        from clawpack.visclaw.data import ClawPlotData
        plotdata = ClawPlotData()


    plotdata.clearfigures()  # clear any old figures,axes,items data
    plotdata.format = 'binary'



    def timeformat(t):
        from numpy import mod
        hours = int(t/3600.)
        tmin = mod(t,3600.)
        min = int(tmin/60.)
        sec = int(mod(tmin,60.))
        timestr = '%s:%s:%s' % (hours,str(min).zfill(2),str(sec).zfill(2))
        return timestr

    def title_hours(current_data):
        from pylab import title
        t = current_data.t
        timestr = timeformat(t)
        title('t = %s' % timestr)


    #-----------------------------------------
    # Figure for surface
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Computational domain', figno=0)
    plotfigure.kwargs = {'figsize':(8,7)}
    plotfigure.show = False

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('pcolor')
    plotaxes.title = 'Surface'
    plotaxes.scaled = True


    def aa(current_data):
        from pylab import ticklabel_format, xticks, gca, cos, pi, savefig
        gca().set_aspect(1.)
        title_hours(current_data)
        ticklabel_format(useOffset=False)
        xticks(rotation=20)


    plotaxes.afteraxes = aa


    # Hillshade
    plotitem = plotaxes.new_plotitem(plot_type="2d_hillshade")
    plotitem.show = False
    plotitem.plot_var = dplot.eta
    plotitem.add_colorbar = False

    # Surface
    plotitem = plotaxes.new_plotitem(plot_type="2d_imshow")
    plotitem.plot_var = dplot.surface_solid_frac_lt03
    plotitem.add_colorbar = True
    plotitem.colorbar_kwargs = {
        "shrink": 0.9,
        "location": "bottom",
        "orientation": "horizontal",
    }
    plotitem.colorbar_label = "Surface (m)"
    plotitem.imshow_cmap = cmocean.cm.curl
    plotitem.imshow_cmin = 90
    plotitem.imshow_cmax = 110
    # Debris
    plotitem = plotaxes.new_plotitem(plot_type="2d_imshow")
    plotitem.plot_var = dplot.solid_frac_gt03
    plotitem.imshow_cmap = cmocean.cm.turbid
    plotitem.imshow_cmin = 0.3
    plotitem.imshow_cmax = 1
    plotitem.add_colorbar = False

    #-----------------------------------------
    # Figure for water / landslide separately
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Landslide/water surface', figno=1)
    plotfigure.figsize=(8,8)
    plotfigure.facecolor='w'

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('pcolor')
    plotaxes.axescmd = 'axes([.15,.5,.7,.45])'
    plotaxes.title = 'Landslide / Water'
    plotaxes.scaled = False
    plotaxes.xlimits = [-3e3,3e3]
    plotaxes.ylimits = [-50,50]

    def pure_water(current_data):
        q = current_data.q
        h = q[0,:,:]
        hm = q[3,:,:]
        eta = dplot.eta(current_data)
        with np.errstate(divide="ignore", invalid="ignore"):
            m = hm / h
        water = np.where(np.logical_and(h>1e-3, m<0.1), 
                         eta, np.nan)
        #import pdb; pdb.set_trace()
        return water
        
    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    #plotitem.plot_var = geoplot.surface
    #plotitem.plot_var = geoplot.surface_or_depth
    #plotitem.show = False
    plotitem.plot_var = pure_water
    plotitem.pcolor_cmap = geoplot.tsunami_colormap
    plotitem.pcolor_cmin = sea_level - 20.
    plotitem.pcolor_cmax = sea_level + 20.
    plotitem.add_colorbar = True
    plotitem.amr_celledges_show = [0,0,0]
    plotitem.patchedges_show = 0

    def landslide(current_data):
        q = current_data.q
        h = q[0,:,:]
        hm = q[3,:,:]
        eta = dplot.eta(current_data)
        with np.errstate(divide="ignore", invalid="ignore"):
            m = hm / h
        landslide = np.where(np.logical_and(h>1e-3, m>0.1), 
                         h, np.nan)
        #import pdb; pdb.set_trace()
        return landslide
        
    # Landslide
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    #plotitem.plot_var = geoplot.surface
    #plotitem.plot_var = geoplot.surface_or_depth
    #plotitem.show = False
    plotitem.plot_var = landslide
    cmap_mass = colormaps.make_colormap({0.:'w', 1.:'brown'})
    plotitem.pcolor_cmap = cmap_mass
    plotitem.pcolor_cmin = 0.
    plotitem.pcolor_cmax = 80.
    plotitem.add_colorbar = True
    plotitem.amr_celledges_show = [0,0,0]
    plotitem.patchedges_show = 0
    
    def land(current_data):
       """
       Return a masked array containing the surface elevation only in dry cells.
       """
       drytol = 1e-3
       q = current_data.q
       h = q[0,...]
       eta = q[-1,...]
       land = np.ma.masked_where(h>drytol, eta)
       #import pdb; pdb.set_trace()
       #land = eta - h # everywhere
       return land

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    #plotitem.show = False
    plotitem.plot_var = land
    plotitem.pcolor_cmap = geoplot.land_colors
    plotitem.pcolor_cmin = 0.0
    plotitem.pcolor_cmax = 400.0
    plotitem.add_colorbar = False
    plotitem.amr_celledges_show = [0]
    plotitem.patchedges_show = 0


    #-----------------------------------------
    # Figure for cross section compared to 1d_radial
    #-----------------------------------------

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('radial slice')
    plotaxes.axescmd = 'axes([.1,.1,.8,.3])'
    plotaxes.title = 'Transect'
    #plotaxes.scaled = True

    def plot_xsec(current_data):
        from pylab import plot,linspace,zeros,ones,legend,xlabel,\
                            sqrt,grid,xlim,fill_between
        from pylab import nan,where,ylim,loadtxt,arange
        from clawpack.pyclaw import Solution
        pd = current_data.plotdata
        frameno = current_data.frameno
        framesoln = Solution(frameno, path=pd.outdir, file_format=pd.format)

        xout = linspace(-3e3,3e3,1000)
        yout = ones(xout.shape) # near x-axis
        rout = xout
        
        #xout = linspace(-3e3,3e3,1000)
        #yout = xout
        #rout = xout * sqrt(2)
        
        etaout = gridtools.grid_output_2d(framesoln, -1, xout, yout)
        hout = gridtools.grid_output_2d(framesoln, 0, xout, yout)
        zetaout = where(hout>0.001, etaout, nan)
        Bout = etaout - hout
        hmout = gridtools.grid_output_2d(framesoln, 3, xout, yout)
        with np.errstate(divide="ignore", invalid="ignore"):
            mout = hmout / hout
        water = where(mout<0.1, etaout, nan)
        landslide = where(mout>0.1, etaout, nan)
        #plot(xout, etaout, 'm')
        fill_between(rout,Bout,water,color=[.4,.4,1])
        fill_between(rout,Bout,landslide,color='brown')
        #plot(xout, Bout, 'g')
        fill_between(rout,Bout,0,color='g')
        plot(-rout,landslide,'k')

    plotaxes.afteraxes = plot_xsec

    #-----------------------------------------
    # Figure for depth
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Depth', figno=2)
    plotfigure.show = False
    
    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('pcolor')
    plotaxes.title = 'Water or landslide depth'
    plotaxes.scaled = True
    plotaxes.xlimits = [-3e3,3e3]
    plotaxes.ylimits = [-3e3,3e3]

    def water_or_landslide_depth(current_data):
        q = current_data.q
        h = q[0,:,:]
        hm = q[3,:,:]
        with np.errstate(divide="ignore", invalid="ignore"):
            m = hm / h
        water = np.where(np.logical_and(h>1e-3, m<0.1), 
                         h, np.nan)
        import pdb; pdb.set_trace()
        return water
        
    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    #plotitem.plot_var = geoplot.surface
    #plotitem.plot_var = geoplot.surface_or_depth
    #plotitem.show = False
    plotitem.plot_var = 0
    plotitem.pcolor_cmap = colormaps.white_red
    plotitem.pcolor_cmin = 0.
    plotitem.pcolor_cmax = 100.
    plotitem.add_colorbar = True
    plotitem.amr_celledges_show = [0,0,0]
    plotitem.patchedges_show = 0

    def land(current_data):
       """
       Return a masked array containing the surface elevation only in dry cells.
       """
       drytol = 1e-3
       q = current_data.q
       h = q[0,...]
       eta = q[-1,...]
       land = np.ma.masked_where(h>drytol, eta)
       #import pdb; pdb.set_trace()
       #land = eta - h # everywhere
       return land

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    #plotitem.show = False
    plotitem.plot_var = land
    plotitem.pcolor_cmap = geoplot.land_colors
    plotitem.pcolor_cmin = 0.0
    plotitem.pcolor_cmax = 400.0
    plotitem.add_colorbar = False
    plotitem.amr_celledges_show = [0]
    plotitem.patchedges_show = 0


    #-----------------------------------------
    # Figure for mass fraction
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Mass Fraction', figno=6)
    plotfigure.kwargs = {'figsize':(8,7)}
    plotfigure.show = False

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('pcolor')
    plotaxes.title = 'mass fraction'
    plotaxes.scaled = True

    plotaxes.scaled = True
    plotaxes.xlimits = [-3e3,3e3]
    plotaxes.ylimits = [-3e3,3e3]

    def mass_frac(current_data):
        q = current_data.q
        h = q[0,:,:]
        hm = q[3,:,:]
        with np.errstate(divide="ignore", invalid="ignore"):
            m = hm / h
        mwet = np.where(h > 0.01, m, np.nan) 
        return mwet
        
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.plot_var = mass_frac
    plotitem.pcolor_cmap = colormaps.blue_yellow_red
    plotitem.pcolor_cmin = 0.
    plotitem.pcolor_cmax = 0.65
    plotitem.add_colorbar = True
    plotitem.amr_celledges_show = [0,0,0]
    plotitem.patchedges_show = 0

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    #plotitem.show = False
    plotitem.plot_var = land
    plotitem.pcolor_cmap = geoplot.land_colors
    plotitem.pcolor_cmin = 0.0
    plotitem.pcolor_cmax = 400.0
    plotitem.add_colorbar = False
    plotitem.amr_celledges_show = [0]
    plotitem.patchedges_show = 0

    
    
    # Figure for scatter plot
    # -----------------------

    plotfigure = plotdata.new_plotfigure(name='scatter', figno=3)
    plotfigure.show = False

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.xlimits = [0, 3e3*np.sqrt(2)]
    plotaxes.ylimits = 'auto'
    plotaxes.title = 'Scatter plot'
    plotaxes.grid = True

    # Set up for item on these axes: scatter of 2d data
    plotitem = plotaxes.new_plotitem(plot_type='1d_from_2d_data')
    
    def h_vs_r(current_data):
        # Return radius of each grid cell and p value in the cell
        from pylab import sqrt
        x = current_data.x
        y = current_data.y
        r = np.sqrt(x**2 + y**2)
        q = current_data.q
        h = q[0,:,:]
        return r,h

    plotitem.map_2d_to_1d = h_vs_r
    plotitem.plot_var = 0
    plotitem.plotstyle = '.'
    plotitem.color = 'b'
    plotitem.kwargs = {'markersize':1}
    plotitem.show = True       # show on plot?

    
    # ------------------------------------
    # Figure for plot to check 1d symmetry
    # ------------------------------------

    plotfigure = plotdata.new_plotfigure(name='1d flip', figno=7)
    #plotfigure.show = False

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.xlimits = [0, 3e3]
    plotaxes.ylimits = 'auto'
    #plotaxes.title = 'Plot vs. x or -x'
    plotaxes.title = 'h(x) - h(-x)'
    plotaxes.grid = True

    # Set up for item on these axes: scatter of 2d data
    
    def h_vs_x(current_data):
        # Return radius of each grid cell and p value in the cell
        from pylab import sqrt
        x = current_data.x
        y = current_data.y
        q = current_data.q
        h = q[0,:,:]
        return x,h

    def h_vs_minusx(current_data):
        # Return radius of each grid cell and p value in the cell
        from pylab import sqrt
        x = current_data.x
        y = current_data.y
        q = current_data.q
        h = q[0,:,:]
        return -x,h

    def h_symdiff_vs_x(current_data):
        # Return radius of each grid cell and p value in the cell
        from pylab import sqrt, flipud
        x = current_data.x
        y = current_data.y
        q = current_data.q
        h = q[0,:,:]
        hdiff = h - flipud(h)
        #import pdb; pdb.set_trace()
        return x,hdiff

    plotitem = plotaxes.new_plotitem(plot_type='1d_from_2d_data')
    plotitem.show = False
    plotitem.map_2d_to_1d = h_vs_x
    plotitem.plot_var = 0
    plotitem.plotstyle = 'b+'
    plotitem.kwargs = {'markersize':3}

    plotitem = plotaxes.new_plotitem(plot_type='1d_from_2d_data')
    plotitem.show = False
    plotitem.map_2d_to_1d = h_vs_minusx
    plotitem.plot_var = 0
    plotitem.plotstyle = 'rx'
    plotitem.kwargs = {'markersize':3}

    plotitem = plotaxes.new_plotitem(plot_type='1d_from_2d_data')
    #plotitem.show = False
    plotitem.map_2d_to_1d = h_symdiff_vs_x
    plotitem.plot_var = 0
    plotitem.plotstyle = 'ro'
    plotitem.kwargs = {'markersize':3}


    # Plots of timing (CPU and wall time):

    def make_timing_plots(plotdata):
        import os
        from clawpack.visclaw import plot_timing_stats
        try:
            timing_plotdir = plotdata.plotdir + '/_timing_figures'
            os.system('mkdir -p %s' % timing_plotdir)
            units = {'comptime':'minutes', 'simtime':'minutes', 'cell':'millions'}
            plot_timing_stats.make_plots(outdir=plotdata.outdir, make_pngs=True,
                                          plotdir=timing_plotdir, units=units)
            os.system('cp %s/timing.* %s' % (plotdata.outdir, timing_plotdir))
        except:
            print('*** Error making timing plots')

    otherfigure = plotdata.new_otherfigure(name='timing',
                    fname='_timing_figures/timing.html')
    otherfigure.makefig = make_timing_plots


    #-----------------------------------------

    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via pyclaw.plotters.frametools.printframes:

    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    plotdata.print_framenos = 'all'        # list of frames to print
    plotdata.print_gaugenos = 'all'          # list of gauges to print
    plotdata.print_fignos = 'all'            # list of figures to print
    plotdata.html = True                     # create html files of plots?
    plotdata.html_homelink = '../README.html'   # pointer for top of index
    plotdata.latex = True                    # create latex file of plots?
    plotdata.latex_figsperline = 2           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False           # also run pdflatex?
    plotdata.parallel = True                 # make multiple frame png's at once

    return plotdata
