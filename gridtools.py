import numpy as np    
from scipy.interpolate import SmoothSphereBivariateSpline, griddata,LinearNDInterpolator,NearestNDInterpolator
import itertools

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

    x2d,y2d = np.meshgrid(x1d,y1d,indexing='ij')
    return x2d,y2d

def gen_meshgrid_3D(xrange,yrange,zrange,nptsx,nptsy,nptsz):
    """
    nptsx,nptsy,nptsz: int: number of sampling points along x,y,z
    returns xyz: array (nptsx,nptsy,nptsz, 3): cartesian 3D grid indexed independently in each dimension
    """
    x1d = np.linspace(xrange[0], xrange[1], nptsx, endpoint=True, dtype=float)
    y1d = np.linspace(yrange[0], yrange[1], nptsy, endpoint=True, dtype=float)
    z1d = np.linspace(zrange[0], zrange[1], nptsz, endpoint=True, dtype=float)

    xyz= np.meshgrid(x1d,y1d,z1d,indexing='ij')
    return xyz

def gen_cartgrid_3D(xrange,yrange,zrange,nptsx,nptsy,nptsz):
    """
    nptsx,nptsy,nptsz: int: number of sampling points along x,y,z
    returns xyz: array (nptsx*nptsy*nptsz, 3): flattened cartesian 3D grid
    """
    x1d = np.linspace(xrange[0], xrange[1], nptsx, endpoint=True, dtype=float)
    y1d = np.linspace(yrange[0], yrange[1], nptsy, endpoint=True, dtype=float)
    z1d = np.linspace(zrange[0], zrange[1], nptsz, endpoint=True, dtype=float) #creates a sequence of numbers (nptsz,)

    grid_1d_merged = [x1d, y1d, z1d]
    print("Shape of merged 1d grid: " + str(np.shape(grid_1d_merged)))
    print("Merged 1d grid: ")
    print(grid_1d_merged)
    xyz  = np.array(list(itertools.product(*grid_1d_merged))) #cartesian product of 1D grids
    return xyz 

def eval_func_meshgrid_2D(x2d,y2d,func):

    v2d = eval(func+"(x2d,y2d)") #dynamic call
    #v2d = tanh2d(x2d,y2d) #static call
    return v2d

def eval_func_meshgrid_3D(x3d,y3d,z3d,func):

    v3d = eval(func+"(x3d,y3d,z3d)") #dynamic call

    return v3d

    """ --------- EXAMPLE ANALYTIC FUNCTIONS ------------"""
def harm2d(x,y):
    return np.sin(x)*np.cos(y)

def harm3d(x,y,z):
    return np.sin(x)*np.cos(y)*np.sin(z)

def tanh2d(x,y):
    return np.tanh(x*y)


if __name__ == "__main__":
    """ TESTS of gridtools"""
    yrange = zrange = xrange = (1,3)
    nptsx = nptsy = nptsz = 3
    xyz_mesh = gen_meshgrid_3D(xrange,yrange,zrange,nptsx,nptsy,nptsz)
    print(xyz_mesh[0].shape)

    """ BASE TEST OF VECTOR SHAPES AND TRANSFORMATIONS"""
    X_seq = xyz_mesh[0].reshape(-1) #sequence of numbers
    X_seqT = X_seq.T
   
    X_row = xyz_mesh[0].reshape(1,-1) #row vector
    X_rowT = X_row.T  

    X_column = xyz_mesh[0].reshape((-1,1)) #column vector
    X_columnT = X_column.T

    print("Shape of X_seq:" + str(X_seq.shape))
    print("Shape of X_seqT:" + str(X_seqT.shape))

    print("Shape of X_row:" + str(X_row.shape))
    print("Shape of X_rowT:" + str(X_rowT.shape))

    print("Shape of X_column:" + str(X_column.shape))
    print("Shape of X_columnT:" + str(X_columnT.shape))

    print("Ordering after reshape for xyz_mesh is: " + str(X_row))
    print("Ordering after reshape for xyz_mesh is: " + str(X_column))

    s1  = np.einsum('ij,ji->',X_row,X_column) #returns a scalar
    s1a = np.einsum('ij,ji->i',X_row,X_column) #returns 1-element sequence
    s2  = np.dot(X_row,X_column) #returns array of size (1,1)

    print("Shape of np.einsum result is: " + str(s1.shape))
    print("Shape of np.einsum2 result is: " + str(s1a.shape))
    print("Shape of np.dot result is: " + str(s2.shape))
    print(s1,s2[0,0])

 

    xyz_flat = gen_cartgrid_3D(xrange,yrange,zrange,nptsx,nptsy,nptsz)    
    print(xyz_flat.shape)