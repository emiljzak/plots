import numpy as np

import os
import sys
from mayavi import mlab
main_folder = "/home/emil/Desktop/projects/plots/"

sys.path.append(main_folder)

#from gridtools import eval_func_meshgrid_3D, gen_meshgrid_3D

def harm3d(x,y,z):
    return np.sin(x)*np.cos(y)*np.sin(z)

def coulomb3d(x,y,z):
    return x/np.sqrt(x**2+y**2+z**2)


def test_mayavi():

    x, y, z = np.mgrid[-10:10:20j, -10:10:20j, -10:10:20j]
    s = np.sin(x*y*z)/(x*y*z)

    scf = mlab.pipeline.scalar_field(x,y,z,s)
    mlab.pipeline.volume(scf)
    mlab.show()


def contour3d():

    npts = 50j
    grange = np.pi
    
    xmax = grange
    xmin = -1.0 * grange
    
    zmax = grange
    zmin = -1.0 * grange
    
    ymax = grange
    ymin = -1.0 * grange
    

    x, y, z = np.mgrid[xmin:xmax:npts, ymin:ymax:npts, zmin:zmax:npts]

    s = coulomb3d(x,y,z)

    mywf = mlab.contour3d(s, contours=[0.1,0.2], colormap='gnuplot',opacity=0.5) #[0.9,0.7,0.5,0.4]

    mlab.show()



if __name__ == "__main__":

    contour3d()