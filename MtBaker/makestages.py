import os
import numpy as np
import dclaw.fortconvert as cf

#get current directory
pwd = os.path.abspath('./')

#location of output to be read (fort.qXXXX and fort.tXXXX)
fortoutputdir = os.path.join(pwd,'_output')

#directory to store time series output files
outdirname = os.path.join(pwd,'_timeseries')
if not os.path.isdir(outdirname):
	cmdstr = 'makedir '+outdirname
	os.system(cmdstr)

#time series locations (x,y). list directly or optionally read a file
x = [] # list of locations
xp1 = (5.7385e5,5.1945e6)
x.append(xp1)
xp2 = (5.76345e5,5.1958e6)
x.append(xp2)

#number of gauges (locations)
Ng = len(x) 
Ngs = range(1,Ng+1)

#create files to store time series, or read files if they exist
#for each file/location create array to be put in container list of arrays 
#files and arrays have columns t,q1,...,q8. One row for each frame number
Mlist = []
for ig in Ngs:
	tsfname = 'Gauge_'+str(ig)+'.txt'
	fname = os.path.join(outdirname,tsfname)
	if os.path.isfile(fname):
		M = np.loadtxt(fname)
	else:
		#this is a bit klugey and should be improved in the future
		#first row is nonsense at t = -1
		q0 = np.array([-1,0,0,0,0,0,0,0,0])
		M = q0

	Mlist.append(M)
	nrows = len(M)

# frame numbers (fort.qXXX0 - fort.qXXXN) f1 - f2.
#Note: f1 based on the size of M from above. To restrict range of fort files read, modify f1 
f1 = nrows-1 #note: begin at number of rows due to 0 index for fort.q0000
f2 = 360 #choose final frame (could count #fort. files instead)
frames = range(f1,f2+1) #which frames
frameN = range(len(frames)) #frame indices

#NOTE: this routine needs to complete to save progress of reading fort files: should probably be improved later
#loop through frames selected
for fi in frameN:

	frame = frames[fi]
	framex = str(1000 + frame)
	framename = framex[1:]
	fqname = os.path.join(fortoutputdir,'fort.q0' + framename)
	ftname = os.path.join(fortoutputdir,'fort.t0' + framename)
	ftheader = cf.forttheaderread(ftname)
	t = ftheader['time']
	print('reading frame '+fqname)
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


#save the arrays to files (THIS WILL OVERWRITE THE PREVIOUS TIME SERIES FILES)	
for ig in Ngs:
	M = Mlist[ig]
	tsfname = 'Gauge_'+str(ig)+'.txt'
	fname = os.path.join(outdirname,tsfname)
	np.savetxt(fname,M)








