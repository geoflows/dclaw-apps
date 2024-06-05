
"""
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from clawpack.visclaw.data import ClawPlotData
from clawpack.clawutil.data import ClawData
import os,sys


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
        plotdata = ClawPlotData()


    plotdata.clearfigures()  # clear any old figures,axes,items data
    plotdata.format = 'binary'

    # Get D-Claw and Geoclaw attributes for dplot
    # These four lines are necessary for using much of the 
    # current dplot
    plotdata.add_attribute('geoclaw_data', ClawData())
    plotdata.geoclaw_data.read('geoclaw.data',force=True)
    plotdata.add_attribute('dclaw_data', ClawData())
    plotdata.dclaw_data.read('setdclaw.data',force=True)



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
        title('Eta %s after initiation' % timestr)


    def aa_eta(current_data):
        from pylab import ticklabel_format, xticks, gca, cos, pi, savefig
        gca().set_aspect(1.)
        title_hours(current_data)
        ticklabel_format(useOffset=False)
        xticks(rotation=20)

    def aa(current_data):
        from pylab import ticklabel_format, xticks, gca, cos, pi, savefig
        gca().set_aspect(1.)
        ticklabel_format(useOffset=False)
        xticks(rotation=20)
    #-----------------------------------------
    # Figure for Q
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Q', figno=0)
    plotfigure.kwargs = {'figsize':(7,15), 'layout':'constrained','dpi':300}
    plotfigure.show = True


    #-----------------------------------------
    # Subplot for eta
    #-----------------------------------------
    plotaxes = plotfigure.new_plotaxes('eta')
    plotaxes.axescmd = "subplot(711)"
    plotaxes.title = 'Eta'
    plotaxes.scaled = True

    plotaxes.afteraxes = aa_eta

    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = dplot.eta
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 100
    plotitem.imshow_cmap = mpl.colormaps['cividis']
    plotitem.add_colorbar = True
    plotitem.amr_patchedges_show = [True, True, True]
    plotitem.amr_patchedges_color = ['blue', 'magenta', 'green'] 

    #-----------------------------------------
    # Subplot for depth
    #-----------------------------------------
    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('depth')
    plotaxes.axescmd = "subplot(712)"
    plotaxes.title = 'Depth'
    plotaxes.scaled = True

    plotaxes.afteraxes = aa

    # Depth
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = dplot.depth
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 5
    plotitem.imshow_cmap = mpl.colormaps['inferno']
    plotitem.add_colorbar = True


    #-----------------------------------------
    # Subplot for m
    #-----------------------------------------
    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('m')
    plotaxes.axescmd = "subplot(713)"
    plotaxes.title = 'Solid Fraction'
    plotaxes.scaled = True

    plotaxes.afteraxes = aa

    # m
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = dplot.solid_frac
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 1
    plotitem.imshow_cmap = mpl.colormaps['Oranges']
    plotitem.add_colorbar = True
    plotitem.amr_patchedges_show = [False, False, False]

    #-----------------------------------------
    # Subplot for velocity
    #-----------------------------------------
    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('vel')
    plotaxes.axescmd = "subplot(714)"
    plotaxes.title = 'Velocity'
    plotaxes.scaled = True

    plotaxes.afteraxes = aa

    # m
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = dplot.velocity_magnitude
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 5
    plotitem.imshow_cmap = mpl.colormaps['Greens']
    plotitem.add_colorbar = True
    plotitem.amr_patchedges_show = [False, False, False]

    #-----------------------------------------
    # Subplot for normalized pressure
    #-----------------------------------------
    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('pressure')
    plotaxes.axescmd = "subplot(715)"
    plotaxes.title = 'Pb/Phydro'
    plotaxes.scaled = True

    plotaxes.afteraxes = aa

    # m
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = dplot.basal_pressure_over_hydrostatic
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 2
    plotitem.imshow_cmap = mpl.colormaps['PuOr']
    plotitem.add_colorbar = True
    plotitem.amr_patchedges_show = [False, False, False]

    #-----------------------------------------
    # Subplot for Entrainable material
    #-----------------------------------------
    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('entrainable')
    plotaxes.axescmd = "subplot(716)"
    plotaxes.title = 'Entrained material'
    plotaxes.scaled = True

    plotaxes.afteraxes = aa

    # m
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = dplot.b_eroded
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 5
    plotitem.imshow_cmap = mpl.colormaps['viridis']
    plotitem.add_colorbar = True
    plotitem.amr_patchedges_show = [False, False, False]

    #-----------------------------------------
    # Fraction species 1
    #-----------------------------------------
    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('species')
    plotaxes.axescmd = "subplot(717)"
    plotaxes.title = 'Species 1'
    plotaxes.scaled = True

    plotaxes.afteraxes = aa

    # m
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = dplot.species1_fraction
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 1
    plotitem.imshow_cmap = mpl.colormaps['PiYG']
    plotitem.add_colorbar = True
    plotitem.amr_patchedges_show = [False, False, False]

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
