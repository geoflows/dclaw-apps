---
title: MtBaker
description: simulations of landslides, lahars and lake inundation for Mt. Baker
---
# Overview

Multiple landslide sources from near Sherman Crater. Leads to lahars that flow east and west. Inundation of Baker Lake occurs for some sources

### Relevant/unique parameters for this simulation

* m0 set by files to 0.62.
* the manning coefficient for the fluid phase is: `geodata.coeffmanning = 0.060 `


# Preprocessing

### Required DEM files:

* all simulations

1. mtbaker_dtm_10m_adj_dams.tt3: 10 m file with some dam adjustmets.

2. demn49w123_13as_subset.tt3: 8 m DEM for western reach to the coast.

3. bakerlake220p8_10mbuffer.tt3: Baker Lake surface 220.8 m.

4. m0_bakerlake_10mbuffer.tt3: m0 = 0 for Baker Lake.

5. lakeshannon126p55_10mbuffer_edit.tt3: Lake Shannon surface 126.55 m.

* sources:

1. Finn source: finnfig9_de1_topo_with_slip_surface.tt3

This source leads to inundation of Baker Lake.

2. Demming source: deming_n70_topo_with_slip_surface.tt3

# Simulations:

1. Baker_finn_src_wlakes/ -- Finn source with lakes and lake inundation. Flow travels eastward from source.

2. Baker_demming_src_wlakes/ -- Demming source with lakes. Limited lake inundation. Flow travels westward into Nooksack river basin toward Puget Sound.  Simulation time: 2 hours.

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
/path_to_mt_baker_simulation/_output
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

% oblique (3D) perspectives (example):
%obliqueview_gca;

```
or, you can modify the axis properties in `obliqueview_gca.m`.

* Choose the variable in the solution vector q used for the color-scale in the plots in `setplot2.m:` 
```
mq =1;                       % which component of q to plot
```
would color the flow based on the flow depth. If you set
```
mq = 4;						% which component of q to plot
```
the plots would use a colormap for the solid-volume fraction instead of the depth. 

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

# Plotting with python

Plotting with python can be done by issuing 
```
make .plots
```
which executes setplot.py. 

Note: setplot.py is not currently adapted for this application, but can be modified to your needs. Developing setplot.py for this application as an example is planned in the future.