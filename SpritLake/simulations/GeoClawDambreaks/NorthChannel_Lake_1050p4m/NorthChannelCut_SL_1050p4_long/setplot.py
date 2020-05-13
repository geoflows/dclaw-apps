
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


import local_dplot as ld
import dclaw.dplot as dd

#import dclaw.scalebar as sb
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
from matplotlib.font_manager import FontProperties

ft2m = 0.3048
dadj = 4.e3

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
        ax = plt.gca()
        t = current_data.t
        
        pylab.title('%4.2f seconds' % t, fontsize=20)
        #pylab.title(r'$m-m_{crit}=-0.02$',fontsize=40)
        pylab.title('')
        pylab.xticks(fontsize=15)
        pylab.yticks(fontsize=15)

        ts = (r't = %4.1f s' % t)
        #pylab.text()
        
        #pylab.text(5.99e5+200.,4.889e6-300.+dadj,ts,bbox={'facecolor':'white','alpha':1.0,'pad':10},fontsize=20)

        #fp = FontProperties()
        #fp.set_size(24)
        #sc = (r"2 km")
        #sz = 2000.0
        #asb =  AnchoredSizeBar(ax.transData,sz,sc,loc=1,pad=0.1, borderpad=0.5, sep=5,frameon=True,prop=fp)
        #asb.patch.set_boxstyle("square,pad=0.")
        
        #mypatch = asb.size_bar.get_children()[0]
        #mypatch.set_patch_effects([Stroke(joinstyle='miter',
                                  #capstyle='butt')]) # override 
        #ax.add_artist(asb)

        #img = Image.open('scale.gif')
        #im = plt.imshow(img)
        
        #ax.annotate((r'10 km'))
        #pylab.xlabel('meters')
        #pylab.ylabel('meters')
        pylab.axis('off')
        pylab.axis('equal')
        plt.tight_layout()
    #-----------------------------------------
    # Figure for pcolor plot
    #-----------------------------------------
    figkwargs = dict(figsize=(12,12),dpi=200,)
    plotfigure = plotdata.new_plotfigure(name='pcolor', figno=0)
    #plotfigure.set_dpi(200)
    plotfigure.show = True
    plotfigure.kwargs = figkwargs
    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('pcolor')
    plotaxes.scaled = True
    plotaxes.afteraxes = fixup
    plotaxes.title ='Surface'


    # land contour
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.plot_var = ld.topo
    plotitem.add_colorbar = False
    #plotitem.kwargs = {'fontsize':20}
    lst = range(10,30)
    flst=[1e2*float(i) for i in lst]
    
    plotitem.contour_levels = flst
    plotitem.amr_contour_colors = ['k','k','k']  # color on each level
    plotitem.kwargs = {'linestyles':'solid','linewidths':1}
    plotitem.amr_contour_show = [0,1,0]
    plotitem.amr_gridlines_show = [1,0,0,0,0]
    plotitem.gridedges_show = 0
    plotitem.show = True

    # water color
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.show = True
    plotitem.plot_var = ld.depth
    plotitem.pcolor_cmap = ld.oso_debris_colormap
    plotitem.pcolor_cmin = 0.0
    plotitem.pcolor_cmax = 10.0
    plotitem.add_colorbar = False
    #plotitem.kwargs = {'fontsize':20}
    plotitem.amr_gridlines_show = [0,0,0,0,0]
    plotitem.gridedges_show = 0


    # Land color
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.plot_var = ld.land
    plotitem.pcolor_cmap = ld.oso_land_colormap
    plotitem.pcolor_cmin = 1000.0
    plotitem.pcolor_cmax = 2500.0
    plotitem.add_colorbar = False
    plotitem.amr_gridlines_show = [1,0,0,0,0]
    plotitem.kwargs = {'linewidth':0.001}
    plotitem.gridedges_show = 0
    #plotaxes.ylimits = [4.885e6,4.889e6+dadj]
    #plotaxes.xlimits = [5.99e5,6.04e5+dadj]


    #add quiver plot
    plotitem = plotaxes.new_plotitem(plot_type='2d_quiver')
    plotitem.show = False
    plotitem.quiver_var_x = ld.velocity_u
    plotitem.quiver_var_y = ld.velocity_v
    plotitem.quiver_coarsening = 10
    plotitem.kwargs = {'units':'width','scale':5000.0,'width':0.001}
    plotitem.quiver_key_show=False


    #-----------------------------------------

    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via pyclaw.plotters.frametools.printframes:

    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    plotdata.print_framenos = 'all'#[0,575]      # list of frames to print
    plotdata.print_gaugenos = 'all'        # list of gauges to print
    plotdata.print_fignos = 'all'            # list of figures to print
    plotdata.html = True                     # create html files of plots?
    plotdata.html_homelink = '../README.html'   # pointer for top of index
    plotdata.latex = True                    # create latex file of plots?
    plotdata.latex_figsperline = 1           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False         # also run pdflatex?

    return plotdata

