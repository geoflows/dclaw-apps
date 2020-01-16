# gate_release_example

## Overview 

this is an example simulation of a gate-release experiment. 

## Notes

#### before running:

* create input files needed (*eg.,* DEMs for geometry of the problem) 

```
> python setinit.py
```

#### to run the simulation:
```
make .output
```
or to run in the background via nice, without exiting if you log off or quit your terminal, with screen output into "run.log" with a name of your choice:
```
nohup nice make .output > run.log &
```

* to plot with python (setplot or setplot_1d)
```
make .plots
```

matlab plotting is not set-up here, but you can copy and modify m-files from the D-Claw matlab libraries.


