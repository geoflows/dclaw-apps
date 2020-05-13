#!/usr/bin/python

"""
plotinfo.py plots information about the dynamics/geometry etc.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
plt.rc('text',usetex=True)
plt.rc('font', family='serif')
fontsize = 22.0
toffset = 0.0
figno = 0

def plotarea():
    fname = os.path.join('_output','fort.amr')
    outname = 'DebrisArea.txt'
    if os.path.isfile(outname):
        os.system('rm '+outname)
    cmdstr = 'grep \'total area\' ' +fname + ' >> ' + outname

    a=os.system(cmdstr)

    raw = np.genfromtxt(outname,dtype='str')

    T = raw[:,3]
    A = raw[:,7]

    TA = np.vstack((T.astype(np.float),A.astype(np.float)))

    TA = np.transpose(TA)

    plt.figure(figno)
    plt.plot(TA[:,0]-toffset,TA[:,1])
    figno = figno+1

def plotF():
    fname = os.path.join('_output','fort.amr')
    outname = 'Fnet.txt'
    if os.path.isfile(outname):
        os.system('rm '+outname)
    cmdstr = 'grep \'F_net\' ' +fname + ' >> ' + outname

    a=os.system(cmdstr)

    raw = np.genfromtxt(outname,dtype='str')

    #import pdb;pdb.set_trace()
    T = raw[:,3]
    F_x = raw[:,6]
    F_y = raw[:,7]
    F_z = raw[:,8]

    TF = np.vstack((T.astype(np.float),F_x.astype(np.float),F_y.astype(np.float),F_z.astype(np.float)))

    TF = np.transpose(TF)

    plt.figure(0)
    plt.plot(TF[:,0]-toffset,TF[:,1],'b',TF[:,0]-toffset,TF[:,2],'r',TF[:,0]-toffset,TF[:,3],'k')
    #plt.axis([50,120,-8e11,8e11])
    plt.axis([10,200,-8e11,8e11])
    plt.legend(['$F_{east}$','$F_{north}$','$F_{vertical}$'],loc='lower right')
    plt.title('Net force exerted on landslide')
    #figno = figno+1

def plotkinetic():
    fname = os.path.join('_output','fort.amr')
    outname = 'DebrisEnergy.txt'
    if os.path.isfile(outname):
        os.system('rm '+outname)
    cmdstr = 'grep \'total kinetic\' ' +fname + ' >> ' + outname

    a=os.system(cmdstr)

    raw = np.genfromtxt(outname,dtype='str')

    T = raw[:,3]
    A = raw[:,7]

    TA = np.vstack((T.astype(np.float),A.astype(np.float)))

    TA = np.transpose(TA)

    plt.figure(2)
    plt.plot(TA[:,0]-toffset,TA[:,1])
    plt.title('Total kinetic energy (contractive case)')


def plotenergy():
    porder =15
    fname = os.path.join('_output','fort.amr')
    outname = 'DebrisKinetic.txt'
    if os.path.isfile(outname):
        os.system('rm '+outname)
    cmdstr = 'grep \'total kinetic\' ' +fname + ' >> ' + outname
    a=os.system(cmdstr)
    raw = np.genfromtxt(outname,dtype='str')

    T = raw[:,3]
    K = raw[:,7]
    TK = np.vstack((T.astype(np.float),K.astype(np.float)))
    TK = np.transpose(TK)

    outname = 'DebrisPotential.txt'
    if os.path.isfile(outname):
        os.system('rm '+outname)
    cmdstr = 'grep \'total potential work\' ' +fname + ' >> ' + outname
    a=os.system(cmdstr)
    raw = np.genfromtxt(outname,dtype='str')

    T = raw[:,3]
    PE = raw[:,8]
    W = raw[:,9]

    T = np.array(T.astype(np.float))-toffset
    PE = np.array(PE.astype(np.float))
    W = np.array(W.astype(np.float))

    tp = np.linspace(-toffset,328.0,140)
    te = np.interp(tp,T,PE + TK[:,1])
    w   = np.interp(tp,T,W)

    pte = np.polyfit(tp,te,porder)
    pw = np.polyfit(tp,w,porder)
    pdedtpoly = np.polyder(pte,1)

    theta = np.linspace(0,np.pi,120)
    R = 60.0
    t = 60.0 + R*np.cos(theta)
    t = np.linspace(0.0,320.0,120)

    epoly = np.polyval(pte,t)
    wpoly = np.polyval(pw,t)
    dedtpoly = np.polyval(pdedtpoly,t)

    tanphi = -dedtpoly/wpoly
    phi = 180.0*np.arctan(tanphi)/np.pi

    plt.figure(1)
    plt.plot(t,phi)
    plt.xlabel(r'$t$ $(s)$')
    plt.ylabel(r'$\arctan(-\frac{d\sum E/dt}{\sum \sigma_{zz}||\vec{v}||})$')
    plt.title(r'Effective friction angle (degrees)')
    #plt.axis([5,85,0.,50])

    plt.figure(2)
    plt.plot(TK[:,0],TK[:,1],'r',T,PE,'b',T,TK[:,1]+PE,'k')
    plt.title('Energy (contractive case)')
    plt.legend(['Kinetic','Potential','Total'],loc='center left')

    plt.figure(3)
    plt.plot(t,wpoly,'k',T,W,'r.')

    plt.figure(4)
    plt.plot(t,epoly,'k',T,PE+TK[:,1],'b.')


def plotcenterofmass():
    porder = 15
    fname = os.path.join('_output','fort.amr')
    outname = 'DebrisCenterMass.txt'
    if os.path.isfile(outname):
        os.system('rm '+outname)
    cmdstr = 'grep \'center of mass\' ' +fname + ' >> ' + outname
    a=os.system(cmdstr)
    raw = np.genfromtxt(outname,dtype='str')

    #import pdb; pdb.set_trace()
    T = raw[:,3]
    X = raw[:,8]
    Y = raw[:,9]

    TXY = np.vstack((T.astype(np.float),X.astype(np.float),Y.astype(np.float)))

    TXY = np.transpose(TXY)


    T = TXY[:,0]
    X = TXY[:,1]
    Y = TXY[:,2]

    plt.figure(1)
    plt.plot(X,Y,'r')
    plt.plot(X[0],Y[0],'ro')
    plt.plot(X[-1],Y[-1],'r>')
    plt.grid(True)
    plt.title(r'Path of center of mass: $\vec{X_c}(t)=(X_c(t),Y_c(t))$')
    plt.xlabel(r'$X_c(t)$ $(m)$',fontsize=fontsize)
    plt.ylabel(r'$Y_c(t)$ $(m)$')

    tend=T[-1]
    #ts = np.linspace(0.0,320.0,120)
    ts = np.linspace(0.0,tend,120)
    dt = ts[1]-ts[0]

    xs = np.interp(ts,T,X- X[0])
    ys = np.interp(ts,T,Y- Y[0])
    ts2 = 0.5*(ts[0:-1]+ts[1:])

    px = np.polyfit(ts,xs,porder)
    py = np.polyfit(ts,ys,porder)
    xp = np.polyval(px,ts2)
    yp = np.polyval(py,ts2)

    plt.figure(2)
    plt.plot(ts2-toffset,np.sqrt(xp**2+yp**2))
    plt.axis([0,100,0,900])
    plt.title('Displacement of the center of mass vs. time')
    plt.xlabel(r'$t$ $(s)$')
    plt.ylabel(r'$||\vec{X}_c(t)-\vec{X}_c(0)||$ $(m)$')

    pdxdt = np.polyder(px,1)
    pdydt = np.polyder(py,1)
    ts3 = np.linspace(10.,tend-10.,120)
    dxdt = np.polyval(pdxdt,ts3)
    dydt = np.polyval(pdydt,ts3)

    fig=plt.figure(3)
    ax = fig.gca()
    plt.plot(dxdt,dydt,'r')
    plt.grid(True)
    plt.plot(dxdt[0],dydt[0],'ro')
    plt.plot(dxdt[-1],dydt[-1],'r<')
    plt.plot(0,0,'ko',markersize=12)
    plt.title(r'Center of mass velocity $d\vec{X}_c/dt = \vec{V}_c$ (phase plane)')
    plt.xlabel(r'$dX_c/dt$ $(m/s)$')
    plt.ylabel(r'$dY_c/dt$ $(m/s)$')


    plt.figure(4)
    plt.plot(ts3-toffset,np.sqrt(dxdt**2 + dydt**2))
    plt.title('Center of mass velocity magnitude vs. time')
    plt.xlabel(r'$t$ $(s)$')
    plt.ylabel(r'$||d\vec{X}_c/dt||=||\vec{V}_c||$')

    pd2xdt2 = np.polyder(px,2)
    pd2ydt2 = np.polyder(py,2)
    d2xdt2 = np.polyval(pd2xdt2,ts3)
    d2ydt2 = np.polyval(pd2ydt2,ts3)

    plt.figure(5)
    plt.plot(d2xdt2,d2ydt2,'r')
    plt.plot(d2xdt2[0],d2ydt2[0],'ro')
    plt.plot(d2xdt2[-1],d2ydt2[0-1],'r<')
    plt.title('Center of mass acceleration (phase plane)')
    plt.plot(0,0,'ko',markersize=12)
    plt.grid(True)
    plt.xlabel(r'$d^2X_c/dt^2$ $(m/s^2)$')
    plt.ylabel(r'$d^2Y_c/dt^2$ $(m/s^2)$')

    plt.figure(6)
    mm=.85e11
    plt.plot(ts3-toffset,np.sqrt(d2xdt2**2+d2ydt2**2)*mm,'k',ts3-toffset,d2xdt2*mm,'b',ts3-toffset,d2ydt2*mm,'r')
    plt.title(r'Center of mass acceleration ($\times$ mass)')
    plt.axis([10,200,-8e11,8e11])
    plt.xlabel(r'$t$ $(s)$')
    plt.ylabel(r'$m/s^2$')
    plt.legend([r'$||d^2\vec{X_c}/dt^2||$',r'$d^2X_c/dt^2$',r'$d^2Y_c/dt^2$'],loc='lower right')

    plt.figure(7)
    dt = ts3[1]-ts3[0]
    dvdt = np.diff(np.sqrt(dxdt**2 + dydt**2))/dt
    ts4 = 0.5*(ts3[0:-1]+ts3[1:])
    plt.plot(ts4-toffset,dvdt)
    plt.title(r'Rate change of speed')
    plt.ylabel(r'$d||\vec{V_c}||/dt$ $(m/s)$')
    plt.xlabel(r'$t$ $(s)$')

    plt.figure(8)
    plt.plot(T-toffset,X-X[0],'k.',T-toffset,Y-Y[0],'k.')
    plt.plot(ts2-toffset,xp,'b',ts2-toffset,yp,'r')
    plt.title('poly fit test')
    plt.axis([0,120,-800,800])





    #import pdb; pdb.set_trace()



if __name__ == '__main__':
    #plotarea()
    #plotkinetic()
    plotcenterofmass()
    plotF()
    #plotenergy()
    plt.show()


