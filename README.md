# dclaw-apps
Repository of D-Claw or Geoclaw applications.

---
## Summary
Application folders should be added under a parent folder of some kind (*eg,* dclaw-apps/flume/gate-release2020).

Folders should have at the very least:
* setrun.py
* Makefile

Optionally they might have:
* matlab plotting files (*eg,* afterframe.m)
* python scripts to set-up, for instance, topography.

## D-Claw version
It's probably a good idea to make a note of the D-Claw code in the application directory...either the code commit that was used or (if I get more organized and have version releases of the code) a version or tag.  

## A few tips
* make sure the environment variable $CLAW points to the proper version of D-Claw code. (the uppermost directory of the repository, "D-Claw.") Or modify the Makefiles if you want to use another environment variable named other than $CLAW.
* its a good idea to have $CLAW/python/ in your $PYTHONPATH:
```
export PYTHONPATH=$CLAW/python:$PYTHONPATH
```
You can then import some tools from the dclaw python folder if they are useful:  
```
python> import dclaw
python> import dclaw.topotools as dt 
```  
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

