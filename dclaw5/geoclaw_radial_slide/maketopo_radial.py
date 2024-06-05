
from pylab import *
from clawpack.geoclaw import topotools
from clawpack.visclaw import colormaps
from clawpack.geoclaw.data import Rearth  # radius of earth
from clawpack.clawutil.data import ClawData
from scipy.interpolate import interp1d


# # Radially symmetric landslide (and tsunami)

m0 = 0.63  # mass fraction in landslide

r0 = 0.     # left boundary (center of radially symmetric)
r1 = 1100.  # top of landslide
r2 = 1300.
r3 = 1600.  # toe of landslide
r4 = 2000.  # start of flat
r5 = 5000.*sqrt(2)   # right boundary for radial coordinate

B4 = B5 = 0 # flat region
Bslope = 25 # degrees
B3 = (r4 - r3) * sin(Bslope * pi/180)
B1 = (r4 - r1) * sin(Bslope * pi/180)
B2 = (r4 - r2) * sin(Bslope * pi/180)
B0 = B1
etaslope = 40 # degrees
eta2 = B1

rr = array([r0,r1,r2,r3,r4,r5])
Br = array([B0,B1,B2,B3,B4,B5])
etar = Br.copy()
etar[2] = eta2

def make_plots():
    figure(figsize=(10,3))
    fill_between(rr,Br,etar,color='brown')
    plot(rr,Br,'g')
    grid(True)
    #axis('equal')
    plot([r1,r1],[0,500],'k--')
    text(r1,-20,'r1\n%.0f' % r1,va='top',ha='center')
    plot([r2,r2],[0,500],'k--')
    text(r2,-20,'r2\n%.0f' % r2,va='top',ha='center')
    plot([r3,r3],[0,500],'k--')
    text(r3,-20,'r3\n%.0f' % r3,va='top',ha='center')
    plot([r4,r4],[0,500],'k--')
    text(r4,-20,'r4\n%.0f' % r4,va='top',ha='center')
    axis([0,3000,-100,500])
    fname = '1d_topo.png'
    savefig(fname)
    print('Created ',fname)

    basal = topotools.Topography('basal_topo.tt3',3)
    basal.plot()
    title('Basal topo')
    fname = 'basal_topo.png'
    savefig(fname)
    print('Created ',fname)

    eta = topotools.Topography('surface_topo.tt3',3)
    eta.plot()
    title('Surface topo eta')
    fname = 'surface_topo.png'
    savefig(fname)
    print('Created ',fname)

    h = eta.Z - basal.Z
    figure()
    pcolormesh(eta.X,eta.Y,h,cmap=colormaps.white_red)
    axis('equal')
    colorbar()
    title('Landslide depth')
    fname = 'landslide_depth.png'
    savefig(fname)
    print('Created ',fname)
    

landslide_depth = eta2 - B2
print('Maximum landslide depth: %.2f m' % landslide_depth)

#x1d, z1d = loadtxt('1d_radial/celledges.data',skiprows=1,unpack=True)
B1d_func = interp1d(rr, Br, bounds_error=False, fill_value = Br[-1])

def basal(x,y):
    """
    Cartesian: x,y in meters
    """
    import numpy as np
    x0 = 0.
    y0 = 0.
    d = np.sqrt((x-x0)**2 + (y-y0)**2)
    z = B1d_func(d)
    return z

eta1d_func = interp1d(rr, etar, bounds_error=False, fill_value = etar[-1])

def eta(x,y):
    """
    Cartesian: x,y in meters
    """
    import numpy as np
    x0 = 0.
    y0 = 0.
    d = np.sqrt((x-x0)**2 + (y-y0)**2)
    z = eta1d_func(d)
    return z


m1d_func = interp1d(rr, etar, bounds_error=False, fill_value = 0.)

def mfrac(x,y):
    """
    mass fraction
    Cartesian: x,y in meters
    """
    import numpy as np
    x0 = 0.
    y0 = 0.
    d = np.sqrt((x-x0)**2 + (y-y0)**2)
    eta = eta1d_func(d)
    B = B1d_func(d)
    mfrac = where(eta-B > 0, m0, 0.)
    return mfrac


xylim2d = 4e3

def maketopo():
    """
    Output topography file for the entire domain
    """
    nxpoints = 501
    nypoints = 501
    xlower= -xylim2d
    xupper=  xylim2d
    ylower= -xylim2d
    yupper=  xylim2d
    outfile= "basal_topo.tt3"
    topotools.topo3writer(outfile,basal,xlower,xupper,ylower,yupper,nxpoints,nypoints)
    outfile= "mass_frac.tt3"
    topotools.topo3writer(outfile,mfrac,xlower,xupper,ylower,yupper,nxpoints,nypoints)

def make_surface():
    """
    Output surface topography file for the entire domain
    (Could be for smaller region)
    """
    nxpoints = 501
    nypoints = 501
    xlower= -xylim2d
    xupper=  xylim2d
    ylower= -xylim2d
    yupper=  xylim2d
    outfile= "surface_topo.tt3"
    topotools.topo3writer(outfile,eta,xlower,xupper,ylower,yupper,nxpoints,nypoints)

if __name__=='__main__':
    maketopo()
    make_surface()
    make_plots()
