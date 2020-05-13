
"""
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.

"""

from pyclaw.geotools import topotools
from pyclaw.data import Data
import matplotlib.pyplot as plt
#plt.rc('text',usetex=True)
#plt.rc('font', family='serif')


import local_dplot

ft2m = 0.3048

#--------------------------
def setplot(plotdata):
#--------------------------

    """
    Specify what is to be plotted at each frame.
    Input:  plotdata, an instance of pyclaw.plotters.data.ClawPlotData.
    Output: a modified version of plotdata.

    """


    from pyclaw.plotters import colormaps, geoplot
    from numpy import linspace

    plotdata.clearfigures()  # clear any old figures,axes,items data


    # To plot gauge locations on pcolor or contour plot, use this as
    # an afteraxis function:

    def addgauges(current_data):
        from pyclaw.plotters import gaugetools
        gaugetools.plot_gauge_locations(current_data.plotdata, \
             gaugenos='all', format_string='ko', add_labels=True)


    def fixup(current_data):
        import pylab
        #addgauges(current_data)
        t = current_data.t -10.0
        #pylab.title('%4.2f seconds' % t, fontsize=20)
        #pylab.title(r'$m-m_{crit}=-0.02$',fontsize=40)
        pylab.title('')
        pylab.xticks(fontsize=15)
        pylab.yticks(fontsize=15)

        ts = (r't = %4.1f s' % t)

        pylab.text(425370,141830,ts,style='italic',bbox={'facecolor':'white','alpha':1.0,'pad':10},fontsize=50)


        pylab.text(424100,142000,'90',style='italic',bbox={'facecolor':'white','alpha':1.0,'pad':10},fontsize=30)
        pylab.text(424020,142720,'90',style='italic',bbox={'facecolor':'white','alpha':1.0,'pad':10},fontsize=30)

        pylab.text(424300,141840,'120',style='italic',bbox={'facecolor':'white','alpha':1.0,'pad':10},fontsize=30)
        pylab.text(424100,142880,'120',style='italic',bbox={'facecolor':'white','alpha':1.0,'pad':10},fontsize=30)

        pylab.text(424030,143500,'270',style='italic',bbox={'facecolor':'white','alpha':1.0,'pad':10},fontsize=30)

        pylab.axis('off')
        #pylab.text(424200,142100,'530',style='italic',bbox={'facecolor':'red','alpha':0.5,'pad':10})
        #pylab.text(424600,142200,'530',style='italic',bbox={'facecolor':'red','alpha':0.5,'pad':10})
        #pylab.text(425800,142500,'530',style='italic',bbox={'facecolor':'red','alpha':0.5,'pad':10})

        #pylab.text(424500,142400,'river',style='italic',bbox={'facecolor':'blue','alpha':0.5,'pad':10})
        #pylab.text(424200,142220,'river',style='italic',bbox={'facecolor':'blue','alpha':0.5,'pad':10})
        #pylab.text(425600,142850,'river',style='italic',bbox={'facecolor':'blue','alpha':0.5,'pad':10})

    #-----------------------------------------
    # Figure for pcolor plot
    #-----------------------------------------
    figkwargs = dict(figsize=(18,12),dpi=1200)
    plotfigure = plotdata.new_plotfigure(name='pcolor', figno=0)
    plotfigure.show = True
    plotfigure.kwargs = figkwargs
    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('pcolor')
    plotaxes.scaled = True
    plotaxes.afteraxes = fixup
    plotaxes.title ='Surface'

    # Debris
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.show = True
    plotitem.plot_var = local_dplot.depth
    plotitem.pcolor_cmap = local_dplot.oso_debris_colormap
    plotitem.pcolor_cmin = 0.0
    plotitem.pcolor_cmax = 20.0
    plotitem.add_colorbar = False
    plotitem.amr_gridlines_show = [0,0,0,0,0]
    plotitem.gridedges_show = 0

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.plot_var = local_dplot.land
    plotitem.pcolor_cmap = local_dplot.oso_land_colormap2
    plotitem.pcolor_cmin = 75.0
    plotitem.pcolor_cmax = 250.0
    plotitem.add_colorbar = False
    plotitem.amr_gridlines_show = [1,0,0,0,0]
    plotitem.kwargs = {'linewidth':0.001}
    plotitem.gridedges_show = 0
    plotaxes.xlimits = [424.e3,426.e3]
    plotaxes.ylimits = [141.8e3,143.6e3]

    # add contour lines of bathy if desired:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.show = True
    plotitem.plot_var = local_dplot.topo
    #plotitem.contour_levels = [300*ft2m,400*ft2m,880*ft2m]
    plotitem.contour_levels = [60,90,120,150,180,210,240,270,300]
    plotitem.amr_contour_colors = ['k']  # color on each level
    plotitem.kwargs = {'linestyles':'solid','linewidths':2}
    plotitem.amr_contour_show = [1,0,0]
    #plotitem.gridlines_show = [1,0,0,0,0]
    #plotitem.gridedges_show = 0
    plotaxes.xlimits = [424.e3,426.e3]
    plotaxes.ylimits = [141.8e3,143.6e3]

    #add quiver plot
    plotitem = plotaxes.new_plotitem(plot_type='2d_quiver')
    plotitem.show = True
    plotitem.quiver_var_x = local_dplot.velocity_u
    plotitem.quiver_var_y = local_dplot.velocity_v
    plotitem.quiver_coarsening = 10
    plotitem.kwargs = {'units':'width','scale':1000.0,'width':0.001}
    plotitem.quiver_key_show=False


    #-----------------------------------------

    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via pyclaw.plotters.frametools.printframes:

    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    plotdata.print_framenos = 'all'     # list of frames to print
    plotdata.print_gaugenos = 'all'        # list of gauges to print
    plotdata.print_fignos = 'all'            # list of figures to print
    plotdata.html = True                     # create html files of plots?
    plotdata.html_homelink = '../README.html'   # pointer for top of index
    plotdata.latex = True                    # create latex file of plots?
    plotdata.latex_figsperline = 1           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False         # also run pdflatex?

    return plotdata

