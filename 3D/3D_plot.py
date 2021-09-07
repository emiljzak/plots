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

from gridtools import eval_func_meshgrid_2D, gen_meshgrid_2D


    """" ===== generate function on a grid ====="""

    yrange = zrange = xrange = (1,3)
    nptsx = nptsy = nptsz = 3
    xyz_mesh = gen_meshgrid_3D(xrange,yrange,zrange,nptsx,nptsy,nptsz)
    
    v3d     = eval_func_meshgrid_3D(x2d,y2d,func)


    """" ===== Plot and save ====="""
    plot_cont2D_analytic(x2d,y2d,v2d,cont2D_params)