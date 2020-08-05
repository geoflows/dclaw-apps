

import matplotlib.pyplot as plt
import os
import numpy as np
#import clawtools.gaugedata as cg
#import geotools.topotools as gt
#import clawtools.fortconvert as cf
fsizea = 24
infiles = ['GaugePuyallupSouth.txt','GaugePuyallupNorth.txt','GaugePuyallupConfluence.txt','GaugeOrting.txt','GaugeAshford.txt','GaugeAlderDam.txt']
fignos = [1,2,3,4,5,6]
figno=0
for infile in infiles:
	figno = figno+1
	M = np.loadtxt(infile)

	plt.figure(infile)
	ts = M[1:-1,0]
	tm = ts/60.
	h = M[1:-1,1]

	plt.plot(tm,h,linewidth=1,marker='.',color='k')
	plt.xlabel('time (minutes)',fontsize=fsizea)
	plt.ylabel('flow depth (m)',fontsize=fsizea)
	plt.xticks(fontsize=fsizea-2)
	plt.yticks(fontsize=fsizea-2)

	titlestr = 'Gauge location '+str(figno)
	plt.title(titlestr,fontsize=fsizea)
	plt.tight_layout()



plt.show()