from posixpath import dirname
from h5py._hl.selections import PointSelection
import matplotlib
from numba.core import extending
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.ticker import FormatStrFormatter
import os
import sys

main_folder = "/Users/zakemil/Nextcloud/projects/plot"

sys.path.append(main_folder)

from gridtools import eval_func_meshgrid_3D, gen_meshgrid_3D



if __name__ == "__main__":

    func = "harm3d" #function name to plot

    """" ===== Plot parameters ====="""
    yrange = zrange = xrange = (-1,1)
    nptsx = nptsy = nptsz = 10


    surf3D_params = {   "xrange":   xrange,
                            "yrange":   yrange,
                            "vmin":     vmin,
                            "vmax":     vmax}


    """" ===== generate function on a grid ====="""


    xyz_mesh = gen_meshgrid_3D(xrange,yrange,zrange,nptsx,nptsy,nptsz)
    
    v3d     = eval_func_meshgrid_3D(xyz_mesh[0],xyz_mesh[1],xyz_mesh[2],func)


    """" ===== Plot and save ====="""


    plot_surf3D(xyz_mesh,v3d,surf3D_params)