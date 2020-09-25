import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.interpolate as si
import dclaw.topotools as gt
import os
from function_defs import *

#grid
dx = 10.0 #1 meter DEM
# grid [~0 , 10 km] X [-2.5 , 2.5 km]
xlower = -100.0 
xupper = 10.0e3 
ylower = -2.5e3
yupper =  2.5e3
nxpoints = int((xupper-xlower)/dx) + 1
nypoints = int((yupper-ylower)/dx) + 1

x = np.linspace(xlower,xupper,nxpoints)
y = np.linspace(ylower,yupper,nypoints)
[X,Y] = np.meshgrid(x,y)

v_fn = mt_tanh_gauss_eta_v
eta_fn = mt_tanh_gauss_eta
b_fn = mt_tanh_log_eta

eta = eta_fn(X,Y)
b = b_fn(X,Y)
(etav,volume) = v_fn(X,Y)
volumeM = volume/1.e6

#small grid
dxS = 2.0
xlowerS =  0.0 
xupperS =  1.8e3 
ylowerS = -0.8e3
yupperS =  0.8e3
nxpointsS = int((xupperS-xlowerS)/dxS) + 1
nypointsS = int((yupperS-ylowerS)/dxS) + 1

xS = np.linspace(xlowerS,xupperS,nxpointsS)
yS = np.linspace(ylowerS,yupperS,nypointsS)
[XS,YS] = np.meshgrid(xS,yS)
#XS = X
#YS = Y
etaS = eta_fn(XS,YS)
bS = b_fn(XS,YS)
#etaS = eta
#bS = b
#import pdb; pdb.set_trace()

#------plot of topo (Mt. Tanh) ------------------------------------------------
        
#-------surface plots-------------------------
figno = 1
fig = plt.figure(figno,figsize=(16,8))
ax = fig.add_subplot(111, projection='3d')
#pdb.set_trace()
h=ax.plot_surface(X,Y,eta,rstride=1,cstride=1,linewidth=0.1,shade=True,cmap='Spectral')
#plt.axis([0,1000,-500,500])
plt.axis('equal')
plt.title("Mt. Tanh logX, Gaussian source. Volume (Mm3): %.2f" % volumeM)
#plt.title('Mt. Tanh logX')
plt.xlabel(r'$x$ (m)')
plt.ylabel(r'$y$ (m)')
#plt.zlabel('z (m)')
#hc=ax.contour(X,Y,eta,stride=0.1)
#hw=ax.plot_wireframe(X,Y,eta,rstride=1,cstride=1)
figname = os.path.join('figures','MtTanh_logX_surf.png')
plt.tight_layout()
plt.savefig(figname)
plt.close(fig)




#-------pcolor plots-------------------------
figno = 2
fig = plt.figure(figno,figsize=(12,8))
ax = fig.add_subplot(111)

h=ax.pcolor(X,Y,eta)
plt.title('Mt. Tanh logX Topography')
plt.xlabel(r'$x$ (m)')
plt.ylabel(r'$y$ (m)')
plt.axis([0,10e3,-2.5e3,2.5e3])
#hc=ax.contour(X,Y,Zbed,stride=0.1)
#hw=ax.plot_wireframe(X,Y,Zbed,rstride=1,cstride=1)
plt.colorbar(h,ax=ax)
figname = os.path.join('figures','MtTanh_logX_pcolor.png')
plt.tight_layout()
plt.savefig(figname)
plt.close(fig)

       

#--------------1 D fig-------------------------------------------------------
figno = 3
ptsm = int(nypoints/2.0)
fig = plt.figure(figno)

plt.plot(X[ptsm,:],eta[ptsm,:],'r')
plt.plot(X[ptsm,:],b[ptsm,:],'b')
plt.axis('equal')
plt.axis([0,5000,-10,2010])
plt.title("Mt. Tanh logX transect, Gaussian source. Volume (Mm3): %.2f" % volumeM)
plt.xlabel(r'$x$ (m)')
plt.ylabel(r'$z$ (m)')
plt.legend([r'$\eta$: topography',r'$b$: failure surface'])
figname = os.path.join('figures','MtTanh_logX_transect.png')
plt.tight_layout()
plt.savefig(figname)
plt.close(fig)



#-------volume plot of h (volume rendering failed)-------------------------
figno = 4
fig = plt.figure(figno,figsize=(16,8))
ax = Axes3D(fig)
#ax = fig.add_subplot(111, projection='3d')
#pdb.set_trace()
h=ax.plot_surface(XS,YS,bS,rstride=10,cstride=10,linewidth=0.2,shade=True)#,cmap='Spectral')
#plt.axis([xlowerS,xupperS,ylowerS,yupperS])
#plt.axis('equal')
volumeM = volume/1.e6
plt.title("Mt. Tanh logX, Gaussian source. Volume (Mm3): %.2f" % volumeM)
plt.xlabel(r'$x$ (m)')
plt.ylabel(r'$y$ (m)')
#plt.axis('equal')
#plt.zlabel('z (m)')
#hc=ax.contour(X,Y,eta,stride=0.1)
hw=ax.plot_wireframe(XS,YS,etaS,rstride=40,cstride=40)
figname = os.path.join('figures','MtTanh_logX_source.png')
#plt.tight_layout()
plt.savefig(figname)
plt.close(fig)
#

#--------------1 D fig-------------------------------------------------------
figno = 5
ptsm = int(nypoints/2.0)
fig = plt.figure(figno)

x1 = X[ptsm,:]
eta1 = eta[ptsm,:]
b1 = b[ptsm,:]

dedx = np.diff(eta1)/np.diff(x1)
dbdx = np.diff(b1)/np.diff(x1)
xd = x1[1:]

etas = np.rad2deg(np.arctan(dedx))
bs = np.rad2deg(np.arctan(dbdx))

plt.plot(xd,etas,'r')
plt.plot(xd,bs,'b')
#plt.axis('equal')
plt.axis([0,5000,-60,60])
plt.title('Mt. Tanh logX slope')
plt.xlabel(r'$x$ (m)')
plt.ylabel(r'slope angle (degrees)')
plt.legend([r'$\eta$: topography',r'$b$: failure surface'])
figname = os.path.join('figures','MtTanh_logX_slope.png')
plt.tight_layout()
plt.savefig(figname)
plt.close(fig)

plt.show()

