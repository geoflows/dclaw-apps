---
title: goldbasin_example
description: simulate landslide at goldbasin site
---

# running this simulation

* to place required topography softlinks locally:
```
python setinit.py
```
modify setinit.py based on the location of DEMs on your path
or you can modify setrun.py to point directly to DEMs 

* to run the simulation:
```
make .output
```
or to run in the background via nice, without exiting if you log off or quit your terminal, with screen output into "run.log":
```
nohup nice make .output > run.log &
```

# plotting with matlab

```
matlab> plotclaw2
matlab> yes
```

Modify the local .m-files to your liking. For example:

* choose the perspective in afterframe.m:

```
% overhead/map view with labeling
mapview_label_gca;

% oblique (3D) perspective (uncomment the following):
%obliqueview_gca;

```
Or modify the axis properties in `obliqueview_gca.m`.

* choose the variable in the solution vector q used for the color-scale in the plots in `setplot2.m:` 
```
mq =1;                       % which component of q to plot
```
For instance, set
```
mq = 5;						% which component of q to plot
```
would use a colorscale based on the fluid pressure. 

* set colormaps in `setprob.m`:

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
modify the `flow_colormaps` defined in `setprob.m` to your liking. Note that the colormaps are used for a discrete or 'binned' scalebar, set in `afterframe.m`:
```
hcbar = colorbar_discrete(flow_colormap,hsurf.Parent);

ylabel(hcbar,'flow depth (m)')
```