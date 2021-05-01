#import matplotlib.pyplot as plt
import os
import numpy as np
#import clawtools.gaugedata as cg
#import geotools.topotools as gt
import clawtools.fortconvert as cf

xdam = (5.526e5,5.18325e6)
xconf = (5.7385e5,5.1945e6)
xpn = (5.76345e5,5.1958e6)
xps = (5.76388e5,5.1924e6)
xort = (5.602e5,5.215e6)
xash = (5.733e5,5.1772e6)

#infiles = ['GaugePuyallupSouth.txt','GaugePuyallupNorth.txt','GaugePuyallupConfluence.txt','GaugeOrting.txt','GaugeAshford.txt','GaugeAlderDam.txt']
infiles = ['GaugePuyallupSouth.txt','GaugePuyallupNorth.txt','GaugePuyallupConfluence.txt','GaugeOrting.txt']

#x = [xps,xpn,xconf,xort,xash,xdam]
x = [xps,xpn,xconf,xort]

f1 =52
f2 =65
frames = range(f1,f2+1)

pts = range(len(frames))

q0 = np.array([0,0,0,0,0,0,0,0,0])
Mps = np.loadtxt(infiles[0])
Mpn = np.loadtxt(infiles[1])
Mconf = np.loadtxt(infiles[2])
Mort = np.loadtxt(infiles[3])
#Mash = q0 #np.loadtxt(infiles[4])
#Mdam  = q0 #np.loadtxt(infiles[5])


for pt in pts:

	frame = frames[pt]
	framex = str(1000 + frame)
	framename = framex[1:]
	fqname = os.path.join('_output','fort.q0' + framename)
	ftname = os.path.join('_output','fort.t0' + framename)
	ftheader = cf.forttheaderread(ftname)
	t = ftheader['time']
	print('reading frame '+fqname)
	solutionlist = cf.fort2list(fqname,ftname)

	#q=cf.pointfromfort(xdam,solutionlist)
	#qn = np.hstack((t,q))
	#Mdam=np.vstack((Mdam,qn))

	q=cf.pointfromfort(xconf,solutionlist)
	qn = np.hstack((t,q))
	Mconf=np.vstack((Mconf,qn))

	q=cf.pointfromfort(xpn,solutionlist)
	qn = np.hstack((t,q))
	Mpn=np.vstack((Mpn,qn))

	q=cf.pointfromfort(xps,solutionlist)
	qn = np.hstack((t,q))
	Mps=np.vstack((Mps,qn))

	q=cf.pointfromfort(xort,solutionlist)
	qn = np.hstack((t,q))
	Mort=np.vstack((Mort,qn))

	#q=cf.pointfromfort(xash,solutionlist)
	#qn = np.hstack((t,q))
	#Mash=np.vstack((Mash,qn))

#np.savetxt('GaugeAlderDam.txt',Mdam)
np.savetxt('GaugePuyallupConfluence.txt',Mconf)
np.savetxt('GaugePuyallupNorth.txt',Mpn)
np.savetxt('GaugePuyallupSouth.txt',Mps)
np.savetxt('GaugeOrting.txt',Mort)
#np.savetxt('GaugeAshford.txt',Mash)

"""

"""






