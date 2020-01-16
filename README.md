---
title: dclaw-apps
subltitle: Repository of D-Claw or Geoclaw applications.
description: D-Claw is an extension of Clawpack for granular-fluid flows. See [github/geoflows/D-Claw](https://github.com/geoflows/D-Claw).
---

# Summary
Application folders should be added under a parent folder of some kind (*eg,* dclaw-apps/flume/gate-release2020). See the [D-Claw repository](https://github.com/geoflows/D-Claw), [geofclaw.org](http://www.geoclaw.org), and [clawpack.org](http://www.clawpack.org) for instructions to run or develop and contribute new applications.

Folders should have at the very least:
* setrun.py
* Makefile

Optionally they might have:
* matlab plotting files (*eg,* afterframe.m, setplot2.m)
* python plotting files (setplot.py)
* python scripts to set-up, for instance, topography.

**Note: some applications in this repository are used for ongoing collaborations and work in progress. Additionally, some may require proprietary data. Therefore, depending on the application, not all required data may be available. Check with dgeorge@uw.edu for info.**

## D-Claw version
It's probably a good idea to make a note of the D-Claw code in the application directory...either the code commit that was used or (if I get more organized and have version releases of the code) a version or tag.  

## Running D-Claw apps
see the README in [D-Claw repository](https://github.com/geoflows/D-Claw), and links to further documentation provided therein. Look for readme files in specific application folders as well.  

## Plotting results
#### matlab

TIP: For a given application, it is useful to relocate some of the m-files (*eg.,* afterframe.m, setplot2.m, setprob.m, beforeframe.m etc.) included with D-Claw to your local working application directory, where you can modify them to suit you present purposes without modifying your D-Claw source files (note that files in $CLAW/matlabgeo should take precedent over files of the same name in $CLAW/matlab. Unifying these directories is planned in the future, but they currently coexist so that the D-Claw source code can be used to run Geoclaw v4.x applications...more about that in the future). 

TIP: Note that D-Claw output and these locally modified .m-files (in your application directory) must both be located by matlab, but they are not usually in the same directory. For instance, if the output sub-directory is the current directory where matlab is running, *ie.,*
```
matlab> pwd
/path/to/myapplication/_output
```
then you can issue,
```
matlab> addpath ../
```
to get the local .m-files in the output's parent directory, myapplication/, to the top of your path (*ie.* Matlab will add the absolute path for ../ to the top of your path).

NOTE: you could alternatively place your local m-files in the output directory...but this is not recommended if you want your local m-files to be part of a repository, as the output directory is best ignored by git, as it is with the applications in the [geoflows/dclaw-apps](https://github.com/geoflows/dclaw-apps).

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

* Modify the local .m-files to your liking. For example, choose the perspective in `afterframe.m`. (See examples in specific applications)

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


#### python

Python can alternatively be used to produce mapview 2d plots, using setplot.py and matplotlib. See [clawpack.org](http://www.clawpack.org) and [github/clawpack/visclaw](https://gihub.com/clawpack/visclaw) for more information about plotting with python. Note that Clawpack's v5.x python libraries may not be compatible with D-Claw v4.x output. 

## Development

If you would like to make contributions to D-Claw or dclaw-apps, please follow the development workflow used for Clawpack, described at [www.clawpack.org/developers](http://www.clawpack.org/developers.html). In summary, please fork the repositories to your own github account, and issue pull requests on a feature branch to github/geoflows, *eg,*:

```
git clone git://github.com/geoflows/dclaw-apps.git
cd D-Claw
git remote add username htpps://github.com/username/dlcaw-apps.git
```
or if you have ssh keys and want to avoid typing your password when you push to github:

```
git remote add username git@github.com:username/dclaw-apps.git
```
Develop in a branch other than master:
```
git checkout -b my_branch
```
And then push to your repository:
```
git push username my_branch
```
Issue pull requests to geoflows/D-Claw from your repository to contribute to D-Claw. Update your master branches from geoflows/D-Claw:
```
git pull origin master
```
If you prefer, rename origin to something easy to remember ("geoflows" or "upstream" or similar):
```
git remote rename origin geoflows
```

## License

D-Claw inherits the Clawpack licenses and user agreements. 

