import os
import numpy as np
import dclaw.fortconvert as cf
"""
this routine creates time series output at chosen locations from fort.q files.
for time series with higher time resolution than fort output use the gauge feature prior to runtime
script is intended to be run from top-level simulation directory above _output/.
"""

#get current directory
pwd = os.path.abspath('./')

#location of output to be read (fort.qXXXX and fort.tXXXX)
fortoutputdir = os.path.join(pwd,'_output')

#directory to store time series output files
outdirname = os.path.join(pwd,'_timeseries')
if not os.path.isdir(outdirname):
	cmdstr = 'mkdir '+outdirname
	os.system(cmdstr)

#time series locations (x,y). list directly or optionally read a file
xlower = 511024.0
xupper = 608976.0
ylower = 5361024.0
yupper = 5425976.0
x = [] # list of locations
xp1 = (xlower + 500, ylower + 500)
x.append(xp1)
xp2 = (xlower + 1000, ylower + 1000)
x.append(xp2)

#number of gauges (locations)
Ng = len(x) 
Ngs = list(range(Ng))

#create files to store time series, or read files if they exist
#for each file/location create array to be put in container list of arrays 
#files and arrays have columns t,q1,...,q8. One row for each frame number

#Note: this routine assumes that all preexisting time series files have the same number of rows/frames
Mlist = []
for ig in Ngs:
	tsfname = 'Gauge_'+str(ig)+'.txt'
	fname = os.path.join(outdirname,tsfname)
	if os.path.isfile(fname):
		M = np.loadtxt(fname)
	else:
		#create array and add first row for t=0.
		fqname = os.path.join(fortoutputdir,'fort.q0000')
		ftname = os.path.join(fortoutputdir,'fort.t0000')
		ftheader = cf.forttheaderread(ftname)
		t = ftheader['time']
		print(('reading frame '+fqname))
		solutionlist = cf.fort2list(fqname,ftname)
		xig = x[ig]
		qig=cf.pointfromfort(xig,solutionlist)
		tqig = np.hstack((t,qig))
		M = np.reshape(tqig,(1,9))

	nrows = len(M)
	Mlist.append(M)
	

# frame numbers (fort.qXXX0 - fort.qXXXN) f1 - f2.
#Note: f1 based on the size of M from above. To restrict range of fort files read, modify f1 
f1 = nrows #note: begin at number of rows due to 0 index for fort.q0000
f2 = 3 #choose final frame (could count #fort. files instead)
frames = list(range(f1,f2+1)) #which frames
frameN = list(range(len(frames))) #frame indices

#NOTE: this routine needs to complete to save progress of reading fort files: should probably be improved later
#loop through frames selected
for fi in frameN:
	frame = frames[fi]
	framex = str(1000 + frame)
	framename = framex[1:]
	fqname = os.path.join(fortoutputdir,'fort.q0' + framename)
	ftname = os.path.join(fortoutputdir,'fort.t0' + framename)
	print(('reading frame '+fqname))
	ftheader = cf.forttheaderread(ftname)
	t = ftheader['time']
	solutionlist = cf.fort2list(fqname,ftname)

	#loop through number of points (gauges) to find in frame/solution
	for ig in Ngs:
		#location of gauge
		xig = x[ig]
		#solution at gauge
		qig=cf.pointfromfort(xig,solutionlist)
		tqig = np.hstack((t,qig))
		M = Mlist[ig]
		M=np.vstack((M,tqig))
		Mlist[ig] = M


#save the arrays to files (THIS WILL OVERWRITE THE PREVIOUS TIME SERIES FILES)	
for ig in Ngs:
	M = Mlist[ig]
	tsfname = 'Gauge_'+str(ig)+'.txt'
	fname = os.path.join(outdirname,tsfname)
	np.savetxt(fname,M)








