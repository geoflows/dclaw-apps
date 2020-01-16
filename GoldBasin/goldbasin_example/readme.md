---
title: goldbasin_example
description: simulate landslide at goldbasin site
---

# running this simulation

* Place required topography softlinks locally:
```
python setinit.py
```
Modify `setinit.py` based on the location of DEMs on your path
or you can modify `setrun.py` to point directly to DEMs. 

* Run the simulation:
```
make .output
```
Or, if you prefer, run in the background with `nohup` and `nice` (which prevents terminating the run if you log off or quit your terminal), and redirect screen output into `run.log` to keep a record of the run:
```
nohup nice make .output > run.log &
```

# plotting with matlab

* Execute matlab in inside the `_output` directory:
```
matlab> pwd
	/path/goldbasin_example/_output
```
* Results can be plotted with `plotclaw2.m`, and answer yes to use `setplot2.m`:
```
matlab> plotclaw2
matlab> yes
```
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
, the plots would use a colormap for the fluid pressure instead of the depth. 

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