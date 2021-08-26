import numpy as np    
from scipy.interpolate import SmoothSphereBivariateSpline, griddata,LinearNDInterpolator,NearestNDInterpolator


def format_float(x):
   return 0

"""
Possible cases:
1) (x, y, z, v) data, where x,y,z span cartesian cube, i.e. regular cartesian grid
2) (x, y, z, v) data, where x,y,z span arbitrary 2-surface, sphere in particular, i.e. irregular cartesian grid"""

"""To do: compare different interpolators on 2D data in terms of i/o"""

def interp_2D_xyv(x,y,v):
    dens_interp = NearestNDInterpolator((x,y), v)


def gen_meshgrid_2D(xrange,yrange,nptsx,nptsy):
    """
    nptsx,nptsy: int: number of sampling points along x,y
    """
    x1d = np.linspace(xrange[0], xrange[1], nptsx, endpoint=True, dtype=float)
    y1d = np.linspace(yrange[0], yrange[1], nptsy, endpoint=True, dtype=float)

    x2d,y2d = np.meshgrid(x1d,y1d)
    return x2d,y2d

def eval_func_meshgrid_2D(x2d,y2d,func):

    v2d = eval(func+"(x2d,y2d)") #dynamic call
    #v2d = tanh2d(x2d,y2d) #static call
    return v2d

    """ --------- EXAMPLE ANALYTIC FUNCTIONS ------------"""
def harm2d(x,y):
    return np.sin(x)*np.cos(y)

def tanh2d(x,y):
    return np.tanh(x*y)