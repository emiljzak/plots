from posixpath import dirname
from h5py._hl.selections import PointSelection
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.ticker import FormatStrFormatter
import os
import sys

main_folder = "/Users/zakemil/Nextcloud/projects/plot"

sys.path.append(main_folder)

from gridtools import eval_func_meshgrid_2D, gen_meshgrid_2D

def plot_cont2D_analytic(x2d,y2d,v2d,cont2D_params):
    """ Produces contour plot for an analytic function of type v = f(x,y) """

    """
    Args:
        x2d: np.array of size (nptsx,nptsy): x-coordinates of each point in the rectangular grid
        y2d: np.array of size (nptsx,nptsy): y-coordinates of each point in the rectangular grid
        v2d: array of size (nptsx,nptsy): function values at each point of the rectangular grid
        xrange,yrange: tuple (xmin,xmax): x,y-range for the plot
        vmin,vmax: float : value range for the plot
        ncont:      int: number of contours


        kwargs:

    Comments:
        1)

    """
    figsizex = cont2D_params['figsize_x'] #size of the figure on screen
    figsizey = cont2D_params['figsize_y']  #size of the figure on screen
    resolution = cont2D_params['resolution']  #resolution in dpi

    fig = plt.figure(figsize=(figsizex, figsizey), dpi=resolution,
                     constrained_layout=True)
    grid_fig = gridspec.GridSpec(ncols=1, nrows=1, figure=fig)

    ax1 = fig.add_subplot(grid_fig[0, 0], projection='rectilinear')


    plot_cont_1 = ax1.contourf( x2d, y2d, v2d, 
                                cont2D_params['ncont'], 
                                cmap = 'jet', 
                                vmin = cont2D_params['vmin'],
                                vmax = cont2D_params['vmax'])
    
    ax1.set_title(  cont2D_params['title_text'],
                    fontsize            = cont2D_params['title_size'],
                    color               = cont2D_params['title_color'],
                    verticalalignment   = cont2D_params['title_vertical'],
                    horizontalalignment = cont2D_params['title_horizontal'],
                    #position            = cont2D_params[ "title_position"],
                    pad                 = cont2D_params['title_pad'],
                    backgroundcolor     = cont2D_params['title_background'],
                    fontstyle           = cont2D_params['title_fontstyle'])

    ax1.set_xlabel(cont2D_params['xlabel'])
    ax1.set_ylabel(cont2D_params['ylabel'])

 
    ax1.set_xticks(cont2D_params['xticks']) #positions of x-ticks
    ax1.set_yticks(cont2D_params['yticks']) #positions of y-ticks

    ax1.set_xticklabels(cont2D_params['xticks'],fontsize=8) #x-ticks labels
    ax1.set_yticklabels(cont2D_params['yticks']) #y-ticks labels

    ax1.xaxis.set_major_formatter(FormatStrFormatter(cont2D_params['xlabel_format'])) #set tick label formatter 
    ax1.yaxis.set_major_formatter(FormatStrFormatter(cont2D_params['ylabel_format']))

    ax1.legend()

    if cont2D_params['save'] == True:
        fig.savefig("2d_cont_cart_analytic.pdf" ,\
                    bbox_inches='tight')
    plt.legend()
    plt.show()
    plt.close()



if __name__ == "__main__":

    function = "harm2d"

    """" ===== Plot parameters ====="""
    nptsx = 200
    nptsy = 200

    xmax = 5.0
    ymax = 5.0
    xrange = (-xmax, xmax)
    yrange = (-ymax, ymax)

    vmin = -1.0
    vmax = 1.0
    ncont = 100

    cont2D_params = {   "xrange":   xrange,
                        "yrange":   yrange,
                        "vmin":     vmin,
                        "vmax":     vmax,
                        "ncont":    ncont,

                        ### TITLE ###
                        "title_text":       "Title",
                        "title_color":      "blue",
                        "title_size":       15,
                        "title_vertical":   "baseline", #vertical alignment of the title: {'center', 'top', 'bottom', 'baseline', 'center_baseline'}
                        "title_horizontal": "center", #{'center', 'left', 'right'},
                        #"title_position":   (pos_x,pos_y), #manual setting of title position
                        "title_pad":        None, #offset from the top of the axes given in points 
                        "title_fontstyle":  'normal', #{'normal', 'italic', 'oblique'}
                        "title_background": "None",          
                        ### LABELS ###
                        "xlabel":           "x",
                        "ylabel":           "y",
                        "xlabel_format":    '%.2f',
                        "ylabel_format":    '%.1f',
                        "xticks":           list(np.linspace(xrange[0],xrange[1],4)),
                        "yticks":           list(np.linspace(yrange[0],yrange[1],8)), 

                        ### SAVE PROPERTIES ###       
                        "save":             False,

                        ### FIGURE PROPERTIES ###    
                        "figsize_x":        3.5,
                        "figsize_y":        3.5,
                        "resolution":       200
                        }



    """" ===== generate function on the grid ====="""
    x2d,y2d = gen_meshgrid_2D(xrange,yrange,nptsx,nptsy)
    v2d     = eval_func_meshgrid_2D(x2d,y2d)


    """" ===== Plot and save ====="""
    plot_cont2D_analytic(x2d,y2d,v2d,cont2D_params)