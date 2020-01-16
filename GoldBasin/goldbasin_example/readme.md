---
title: goldbasin_example
description: simulate landslide at goldbasin site
---

# running this simulation

* to place needed topography softlinks locally:
```
python setinit.py
```
modify setinit.py based on the location of DEMs on your path
or you can modify setrun.py to point directly to DEMs 

* to run the simulation:
```
make .output
```
or to run in the background via nice, without exiting if you log off or quit your terminal, with screen output into "run.log" with a name of your choice:
```
nohup nice make .output > run.log &
```

* to plot
```
matlab> plotclaw2
matlab> yes
```

for plotting you can modify m-files.