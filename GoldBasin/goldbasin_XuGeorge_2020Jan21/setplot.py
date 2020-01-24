
"""
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.

"""


from pyclaw.data import Data
import matplotlib.pyplot as plt
#plt.rc('text',usetex=True)
#plt.rc('font', family='serif')

import dclaw.dplot as dd 
local_dplot = dd

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
             gaugenos='all', format_string='wo', add_labels=False)


    def fixup(current_data):
        import pylab

        #addgauges(current_data)
        #addgauges(current_data)
        t = current_data.t #-10.0
        #pylab.title('%4.2f seconds' % t, fontsize=20)
        #pylab.title(r'$m-m_{crit}=-0.02$',fontsize=40)
        #pylab.title(r't = %4.1f s' % t)
        pylab.title('')
        pylab.xticks(fontsize=15)
        pylab.yticks(fontsize=15)
        pylab.axis('off')
        ts = (r't = %4.1f s' % t)

        #pylab.text(6.95e5+200,1.202e6-1000,ts,style='italic',bbox={'facecolor':'white','alpha':1.0,'pad':10},fontsize=30)
        #pylab.text(425250-3000,141850+1500,ts,style='italic',bbox={'facecolor':'white','alpha':1.0,'pad':10},fontsize=30)

        #pylab.text(424100,142000,'90',style='italic',bbox={'facecolor':'white','alpha':1.0,'pad':10},fontsize=20)
        #pylab.text(424020,142720,'90',style='italic',bbox={'facecolor':'white','alpha':1.0,'pad':10},fontsize=20)

        #pylab.text(424300,141840,'120',style='italic',bbox={'facecolor':'white','alpha':1.0,'pad':10},fontsize=20)
        #pylab.text(424100,142880,'120',style='italic',bbox={'facecolor':'white','alpha':1.0,'pad':10},fontsize=20)

        #pylab.text(424030,143500,'270',style='italic',bbox={'facecolor':'white','alpha':1.0,'pad':10},fontsize=20)

        #pylab.axis('off')
        #pylab.text(424200,142100,'530',style='italic',bbox={'facecolor':'red','alpha':0.5,'pad':10})
        #pylab.text(424600,142200,'530',style='italic',bbox={'facecolor':'red','alpha':0.5,'pad':10})
        #pylab.text(425800,142500,'530',style='italic',bbox={'facecolor':'red','alpha':0.5,'pad':10})

        #pylab.text(424500,142400,'river',style='italic',bbox={'facecolor':'blue','alpha':0.5,'pad':10})
        #pylab.text(424200,142220,'river',style='italic',bbox={'facecolor':'blue','alpha':0.5,'pad':10})
        #pylab.text(425600,142850,'river',style='italic',bbox={'facecolor':'blue','alpha':0.5,'pad':10})
        plt.tight_layout()
    #-----------------------------------------
    # Figure for pcolor plot
    #-----------------------------------------
    figkwargs = dict(figsize=(8,8),dpi=200,)
    plotfigure = plotdata.new_plotfigure(name='pcolor', figno=0)
    #plotfigure.set_dpi(200)
    plotfigure.show = False
    plotfigure.kwargs = figkwargs
    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('pcolor')
    plotaxes.scaled = True
    plotaxes.afteraxes = fixup
    plotaxes.title ='Surface'


    # Debris
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.plot_var = dd.solid_frac
    plotitem.add_colorbar = False
    #plotitem.kwargs = {'fontsize':20}
    lst = range(0,1000,50)
    flst=[1e-3*float(i) for i in lst]
    
    
    plotitem.contour_levels = flst
    
    #plotitem.amr_contour_colors = ['r','r','r']  # color on each level
    plotitem.kwargs = {'linestyles':'solid','linewidths':1}
    plotitem.amr_contour_show = [0,0,1]
    plotitem.amr_gridlines_show = [1,1,0,0,0]
    plotitem.gridedges_show = 0
    plotitem.show = False

    # Debris
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.show = True
    #plotitem.plot_var = dd.liquefaction_ratio
    plotitem.pcolor_cmap = local_dplot.solid_frac_colormap
    plotitem.plot_var = dd.solid_frac
    #plotitem.plot_var = dd.particle_size
    #plotitem.pcolor_cmap = local_dplot.oso_debris_colormap_liquefaction
    plotitem.pcolor_cmin = 0.0#.55#0.615
    plotitem.pcolor_cmax = 1.0
    plotitem.add_colorbar = True
    #plotitem.kwargs = {'fontsize':20}
    plotitem.amr_gridlines_show = [1,0,0,0,0]
    plotitem.gridedges_show = 0


    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.plot_var = dd.land
    plotitem.pcolor_cmap = local_dplot.oso_land_colormap2
    plotitem.pcolor_cmin = 0.0
    plotitem.pcolor_cmax = 2000.0
    plotitem.add_colorbar = False
    plotitem.amr_gridlines_show = [1,1,0,0,0]
    plotitem.kwargs = {'linewidth':0.001}
    plotitem.gridedges_show = 1
    plotaxes.xlimits = [703278-200,704698+3200]
    plotaxes.ylimits = [1199653-2500,1200600+500]

    # add contour lines of bathy if desired:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.show = True
    plotitem.plot_var = local_dplot.topo
    #plotitem.contour_levels = [300*ft2m,400*ft2m,880*ft2m]
    #plotitem.contour_levels = [-1.07,100,200,300,400,500,600,700,800,900,1000]
    plotitem.contour_levels = [-1.07]
    plotitem.amr_contour_colors = ['w']  # color on each level
    plotitem.kwargs = {'linestyles':'solid','linewidths':2}
    plotitem.amr_contour_show = [0,0,1]
    #plotitem.gridlines_show = [1,0,0,0,0]
    #plotitem.gridedges_show = 0
    #plotaxes.xlimits = [424.e3,427.e3]
    #plotaxes.ylimits = [141.8e3,143.6e3]

    #add quiver plot
    plotitem = plotaxes.new_plotitem(plot_type='2d_quiver')
    plotitem.show = False
    plotitem.quiver_var_x = local_dplot.velocity_u
    plotitem.quiver_var_y = local_dplot.velocity_v
    plotitem.quiver_coarsening = 10
    plotitem.kwargs = {'units':'width','scale':1000.0,'width':0.001}
    plotitem.quiver_key_show=False

    
    #==============================================================
        #-----------------------------------------
    # Figure for pcolor plot
    #-----------------------------------------
    figkwargs = dict(figsize=(10,16),dpi=300,)
    plotfigure = plotdata.new_plotfigure(name='pcolor2', figno=10)
    #plotfigure.set_dpi(200)
    plotfigure.show = True
    plotfigure.kwargs = figkwargs
    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('pcolor')
    plotaxes.scaled = True
    plotaxes.afteraxes = fixup
    plotaxes.title ='Surface Elevation'


    # Debris
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.show = True
    #plotitem.plot_var = dd.liquefaction_ratio
    #plotitem.pcolor_cmap = local_dplot.tsunami_colormap2
    plotitem.pcolor_cmap = local_dplot.tsunami_colormap_log
    #plotitem.plot_var = local_dplot.water
    plotitem.plot_var = local_dplot.surface_log
    #plotitem.plot_var = dd.particle_size
    #plotitem.pcolor_cmap = local_dplot.oso_debris_colormap_liquefaction
    #plotitem.pcolor_cmin = 0.0-10.0
    #plotitem.pcolor_cmax = 0.0+10.0
    plotitem.pcolor_cmin = -4.
    plotitem.pcolor_cmax = 6.

    plotitem.add_colorbar = False
    #plotitem.kwargs = {'fontsize':20}
    plotitem.amr_gridlines_show = [1,0,0,0,0]
    plotitem.gridedges_show = 1


    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.plot_var = dd.land
    plotitem.pcolor_cmap = local_dplot.oso_land_colormap2
    plotitem.pcolor_cmin = 0.0
    plotitem.pcolor_cmax = 2000.0
    plotitem.add_colorbar = False
    plotitem.amr_gridlines_show = [1,0,0,0,0]
    plotitem.kwargs = {'linewidth':0.001}
    plotitem.gridedges_show = 0
    #plotaxes.xlimits = [424.e3,427.e3]
    #plotaxes.ylimits = [141.8e3,143.6e3]

    # add contour lines of bathy if desired:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.show = True
    plotitem.plot_var = local_dplot.topo
    #plotitem.contour_levels = [300*ft2m,400*ft2m,880*ft2m]
    plotitem.contour_levels = [-1.07]#,100,200,300,400,500]
    plotitem.amr_contour_colors = ['w']  # color on each level
    plotitem.kwargs = {'linestyles':'solid','linewidths':2}
    plotitem.amr_contour_show = [0,0,1]
    #plotitem.gridlines_show = [1,0,0,0,0]
    #plotitem.gridedges_show = 0
    #plotaxes.xlimits = [424.e3,427.e3]
    #plotaxes.ylimits = [141.8e3,143.6e3]

    #add quiver plot
    plotitem = plotaxes.new_plotitem(plot_type='2d_quiver')
    plotitem.show = False
    plotitem.quiver_var_x = local_dplot.velocity_u
    plotitem.quiver_var_y = local_dplot.velocity_v
    plotitem.quiver_coarsening = 10
    plotitem.kwargs = {'units':'width','scale':1000.0,'width':0.001}
    plotitem.quiver_key_show=False

    #-----------------------------------------
    # Figures for gauges
    #-----------------------------------------
    """
    plotfigure = plotdata.new_plotfigure(name='Surface', figno=300, \
                    type='each_gauge')
    plotfigure.clf_each_gauge = True

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    #plotaxes.xlimits = [51.5e3,56.5e3]
    plotaxes.xlimits = 'auto'
    #plotaxes.ylimits = [-.02,0.5]
    plotaxes.title = 'Surface'

    # Plot surface:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.plot_var = 0#6
    plotitem.plotstyle = 'b-'
    plotitem.show = False
    """

    #-----------------------------------------

    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via pyclaw.plotters.frametools.printframes:

    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    plotdata.print_framenos = 'all'#range(0,130,10)#[0]#'all'#[0,20,40,100]#'all'#[50,52,54]#range(20,30)#'all'#[10,40,55,70,130]      # list of frames to print
    plotdata.print_gaugenos = 'all'        # list of gauges to print
    plotdata.print_fignos = 'all'            # list of figures to print
    plotdata.html = True                     # create html files of plots?
    plotdata.html_homelink = '../README.html'   # pointer for top of index
    plotdata.latex = True                    # create latex file of plots?
    plotdata.latex_figsperline = 1           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False         # also run pdflatex?

    return plotdata

