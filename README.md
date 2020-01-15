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

## D-Claw version
It's probably a good idea to make a note of the D-Claw code in the application directory...either the code commit that was used or (if I get more organized and have version releases of the code) a version or tag.  

## Tips for running D-Claw
see also the [D-Claw repository](https://github.com/geoflows/D-Claw).

### environment variables

* make sure the environment variable $CLAW points to the D-Claw code (the uppermost directory of the repository, "D-Claw.") (Or modify the Makefiles if you want to use an environment variable other than $CLAW. For bash shells:
```
export CLAW=/somedir/D-Claw
```

* if you are using multiple versions of Clawpack (*eg.,* Clawpack 5.x or GeoClaw and D-Claw), you might want to use, if you don't already, the [environment modules](http://modules.sourceforge.net/) package, which can dynamically set or change your environment under a given shell, to make sure you have a compatible set of paths/versions of software (*eg.*, $PATH, $CLAW, $PYTHONPATH, $MATLABPATH).

### python
* its a good idea to have $CLAW/python/ in your $PYTHONPATH:
```
export PYTHONPATH=$CLAW/python:$PYTHONPATH
```
You can then import some tools from the D-Claw python folder if they are useful:  
```
python> import dclaw
python> import dclaw.topotools as dt 
```  

### matlab
* if you are going to use matlab plotting with D-Claw, be sure that your $MATLABPATH contains $CLAW/matlabgeo and then $CLAW/matlab
```
export MATLABPATH=$CLAW/matlabgeo:$CLAW/matlab:$MATLABPATH
```
* if you are using matlab and "plotclaw2.m", note that output and local .m-files must both be located by matlab, but they are not usually in the same directory. If the output directory is your current directory where matlab is running, you can
```
matlab> addpath ../
```
to get the local .m-files in the output's parent directory correctly on your path. (Matlab will add the absolute path for ../)


* if you are using multiple versions of Clawpack (*eg.,* Clawpack 5.x or GeoClaw and D-Claw), you might want to use, if you don't already, the [environment modules](http://modules.sourceforge.net/) package, which can dynamically change your environment variables (such as $PATH, $CLAW, $PYTHONPATH, $MATLABPATH) for your running shell, to make sure all paths are correct and compatible.

