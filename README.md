---
title: dclaw-apps
subltitle: Repository of D-Claw or Geoclaw applications.
description: D-Claw is an extension of Clawpack for granular-fluid flows. See [github/geoflows/D-Claw](https://github.com/geoflows/D-Claw).
---

# Summary

Application folders of D-Claw simulations. This repository provides examples for setting-up your own D-Claw applications. These are also useful for testing your D-Claw installation. 
See the [D-Claw repository](https://github.com/geoflows/D-Claw), [geoclaw.org](http://www.geoclaw.org), [clawpack.org](http://www.clawpack.org), and individual application folders for more instructions.


Application folders should have at the very least:
* setrun.py
* Makefile
* readme.md (specific information/instructions for each application)

Optionally they might have:
* matlab plotting files (*eg,* afterframe.m, setplot2.m)
* python plotting files (setplot.py)
* python scripts to set-up, for instance, topography.

* See CONTENTS in this repository for a brief outline of what is here. This should be updated if you add applications (see Development below).

**Note: some applications in this repository are used for ongoing collaborations and work in progress. Additionally, some may require proprietary data. Therefore, depending on the application, not all required data may be available. Check with dgeorge@uw.edu for info.**


# Running D-Claw apps
see the README in the [D-Claw repository](https://github.com/geoflows/D-Claw), and links to further documentation provided therein. Look for readme files in specific application folders as well.  

# Plotting results
### matlab

Matlab can be used to plot D-Claw output. From the output directory, use
```
matlab> plotclaw2
```
then follow the interactive menu to produce plots for each frame.

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


### python

Python can alternatively be used to produce mapview 2D or 1D cross-sectional plots, as describe above, with:
```
make .plots
```
or
```
make plots
```
Make uses setplot.py and matplotlib.  Modify the routine setplot.py to your needs. 

See README files and individual applications in this repository for more examples of how to use python plotting.

# Development

* If you would like to make contributions to dclaw-apps, please follow the development workflow used for Clawpack, described at [www.clawpack.org/developers](http://www.clawpack.org/developers.html). In summary, please fork the repositories to your own github account, and issue pull requests on a feature branch to github/geoflows, *eg,*:

```
git clone https://github.com/geoflows/dclaw-apps.git
cd dclaw-apps
git remote add username https://github.com/username/dclaw-apps.git
```
or if you have ssh keys and want to avoid typing your password when you push to github:

```
git remote add username git@github.com:username/dclaw-apps.git
```
These settings can be modified in your local working repository at anytime with `git remote set-url`.

* Develop in a branch other than master:
```
git checkout -b my_branch
```
Make your changes, and then push to your repository on github:
```
git push username my_branch
```
* Issue pull requests from your branch and repository on github.com (username/dclaw-apps) to contribute features or fixes to the master branch at geoflows/dclaw-apps. 

* Update your master branches from geoflows/dclaw-apps:
```
git pull origin master
```
and then 
```
git push username master
```
to update your git remote. It is recommended that you do not commit to your own master branches, so that your master branches are easily updated from the geoflows repository.

If you prefer, rename origin to something easy to remember ("geoflows" or "upstream" or similar):
```
git remote rename origin geoflows
```

## Adding your own application folders

Application/simulations added to this repository should be placed in a parent folder with a descriptive name. That way if you or other users alter the simulations slightly and contribute those applications, they can be grouped together in a parent directory.

Applications should have at the very least:
* setrun.py
* Makefile
* readme.md (specific information/instructions for each application)

Optionally they might have:
* matlab plotting files (*eg,* afterframe.m, setplot2.m)
* python plotting files (setplot.py)
* python scripts to set-up, for instance, topography.

Please also add an entry to the CONTENTS.md file in the repository parent directory. 

## License

dclaw-apps code inherits the Clawpack licenses and user agreements. 

