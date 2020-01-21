---
title: goldbasin_w_river
description: simulation of a hypothetical landslide at goldbasin site with river near toe
---
# Overview

A simulation of a hypothetical landslide at goldbasin site with a river (water) near the toe. Developed by Yuankun Xu and David George. 

### DEM files:

File description (required DEMs)

1. topo_with_slip_surface_and_riverbed.tt3 
    * A large topography file that includes both riverbed and landslide slip surface 
    * Landslide volume of this example is 2.1x10^6 m^3

2.  topo_landslide_subset.tt3 
    * Topography of the landslide upper surface. It is in a rectangular shape that tightly covers the landslide area
    * Landslide body is defined as (2) minus (1)

3. topo_river_surface_subset_50cm.tt3
    * Topography of the river surface. It is in a rectangular shape that tightly covers the river area. River depth is set as 50 cm. The river is defined as (3) minus (1)

4.  topo_river_surface_subset_200cm.tt3
    * Same as (3) but the river depth is 200 cm

# Preprocessing

Place required topography softlinks locally:
```
python setinit.py
```
Modify `setinit.py` based on the location of DEMs on your path
or you can modify `setrun.py` to point directly to DEMs. 

Note: this setinit.py creates some modified DEMs for the river and landslide surface

# Running/producing output

From your application directory:
```
make .output
```
Or, if you prefer, run in the background with `nohup` and `nice` (which prevents terminating the run if you log off or quit your terminal), and redirect screen output into `run.log` to keep a record of the run:
```
nohup nice make .output > run.log &
```

# Plotting with matlab

* Execute matlab in inside the `_output` directory:
```
matlab> pwd
/path/goldbasin_example/_output
```
* Add the m-files in the parent directory of `_output`:
```
matlab> addpath ../
```
* Results can be plotted with `plotclaw2.m`, and answer yes to use `setplot2.m`:
```
matlab> plotclaw2
plotclaw2  plots 2d results from clawpack or amrclaw
Execute setplot2 (default = no)? yes
```
You can then advance through each frame or output time. The interactive menu provides some options:
```
Hit <return> for next plot, or type k, r, rr, j, i, q, or ? 
```
enter `?` for explanation. Note, if you enter `k`, matlab enters a debug mode and no longer accepts `return` but instead type `dbcont` to continue plotting.   
* Modify the local .m-files to your liking. For example, choose the perspective in `afterframe.m`:

```
% overhead/map view with labeling
mapview_label_gca;

% oblique (3D) perspective (uncomment the following):
%obliqueview_gca;

```
or, you can modify the axis properties in `obliqueview_gca.m`.

* Choose the variable in the solution vector q used for the color-scale in the plots in `setplot2.m:` 
```
mq =1;                       % which component of q to plot
```
would color the flow based on the flow depth. If you set
```
mq = 5;						% which component of q to plot
```
the plots would use a colormap for the fluid pressure instead of the depth. 

* The colormaps are specified in `setprob.m`:

```
if mq==6
    flow_colormap = z_velocity;
elseif mq==5
    flow_colormap =zDigPressure;
elseif mq == 1
    flow_colormap = z_depth;
elseif mq==4
    flow_colormap = z_m;
elseif mq==2
    flow_colormap = z_velocity2;
else
    flow_colormap = z_eta;
end
```
You can modify the `flow_colormaps` chosen or defined in `setprob.m` to your liking. Note that the colormaps are used for a discrete or 'binned' scalebar, which is issued in `afterframe.m`:
```
hcbar = colorbar_discrete(flow_colormap,hsurf.Parent);

ylabel(hcbar,'flow depth (m)')
```