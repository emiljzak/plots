from posixpath import dirname
from h5py._hl.selections import PointSelection
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.ticker import FormatStrFormatter
import os
import sys
from numpy.core.overrides import array_function_from_dispatcher
from numpy.lib.arraypad import pad

from sympy.polys.densebasic import dmp_include
from sympy.simplify.radsimp import fraction

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
    
    ax1.set_title(  label               = cont2D_params['title_text'],
                    fontsize            = cont2D_params['title_size'],
                    color               = cont2D_params['title_color'],
                    verticalalignment   = cont2D_params['title_vertical'],
                    horizontalalignment = cont2D_params['title_horizontal'],
                    #position            = cont2D_params[ "title_position"],
                    pad                 = cont2D_params['title_pad'],
                    backgroundcolor     = cont2D_params['title_background'],
                    fontname            = cont2D_params['title_fontname'],
                    fontstyle           = cont2D_params['title_fontstyle'])

    ax1.set_xlabel( xlabel              = cont2D_params['xlabel'],
                    fontsize            = cont2D_params['xlabel_size'],
                    color               = cont2D_params['label_color'],
                    loc                 = cont2D_params['xlabel_loc'],
                    labelpad            = cont2D_params['xlabel_pad'] )

    ax1.set_ylabel(cont2D_params['ylabel'])

 
    ax1.set_xticks(cont2D_params['xticks']) #positions of x-ticks
    ax1.set_yticks(cont2D_params['yticks']) #positions of y-ticks

    ax1.set_xticklabels(cont2D_params['xticks'],fontsize=8) #x-ticks labels
    ax1.set_yticklabels(cont2D_params['yticks']) #y-ticks labels

    ax1.xaxis.set_major_formatter(FormatStrFormatter(cont2D_params['xlabel_format'])) #set tick label formatter 
    ax1.yaxis.set_major_formatter(FormatStrFormatter(cont2D_params['ylabel_format']))

    fig.colorbar(   mappable            = cont2D_params['cbar_mappable'],
                    ax                  = ax1, 
                    orientation         = cont2D_params['cbar_orientation'],
                    label               = cont2D_params['cbar_label'],
                    fraction            = cont2D_params['cbar_fraction'],
                    aspect              = cont2D_params['cbar_aspect'],
                    shrink              = cont2D_params['cbar_shrink'],
                    pad                 = cont2D_params['cbar_pad'],
                    panchor             = cont2D_params['cbar_panchor'],
                    
                    ticks               = cont2D_params['cbar_ticks'],
                    drawedges           = cont2D_params['cbar_drawedges'],
                    format              = cont2D_params['cbar_format'])

    if cont2D_params['save'] == True:
        fig.savefig(    fname       = cont2D_params['save_name'],
                        dpi         = cont2D_params['save_dpi'],
                        orientation = cont2D_params['save_orientation'],
                        bbox_inches = cont2D_params['save_bbox_inches'],
                        pad_inches  = cont2D_params['save_pad_inches']
                        )

    plt.legend()
    plt.show()
    plt.close()



if __name__ == "__main__":

    function = "harm2d"

    """" ===== Plot parameters ====="""
    nptsx = 200
    nptsy = 200

    xmax    = 5.0
    ymax    = 5.0
    xrange  = (-xmax, xmax)
    yrange  = (-ymax, ymax)

    vmin    = -1.0
    vmax    = 1.0
    ncont   = 100

    cmap = matplotlib.cm.jet #jet, cool, etc
    norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)

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
                        "title_fontname":   'Helvetica', #'Sans' | 'Courier' | '
                        "title_background": "None",   

                        ### LABELS ###
                        "xlabel":           "x",
                        "ylabel":           "y",
                        "xlabel_format":    '%.2f',
                        "ylabel_format":    '%.1f',
                        "label_color":      'red',
                        "xlabel_size":       12,
                        "ylabel_size":       12,   
                        "xlabel_pad":       None,     
                        "ylabel_pad":       None,
                        "xlabel_loc":       "center",  #left, right         
                        "xticks":           list(np.linspace(xrange[0],xrange[1],4)),
                        "yticks":           list(np.linspace(yrange[0],yrange[1],8)), 
                                            
                        ### COLORBAR ###: see https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html
                        "cbar_mappable":       matplotlib.cm.ScalarMappable(norm=norm, cmap=cmap),
                        "cbar_orientation":   'horizontal', #vertical #note that orientation overrides panchor
                        "cbar_label":         "Some units",   
                        "cbar_fraction":      1.0, #fraction of the original axes to be displayed in the colorbar
                        "cbar_aspect":        20, #ratio of long to short dimensions
                        "cbar_shrink":        1.00, #shrink the colorbar
                        "cbar_pad":           0.15, #distance of colorbar from the adjacent plot axis
                        "cbar_panchor":       (0.3,0.2), #TThe anchor point of the colorbar parent axes. If False, the parent axes' anchor will be unchanged. Defaults to (1.0, 0.5) if vertical; (0.5, 0.0) if horizontal.
                        
                        "cbar_ticks":         None, #or list of custom ticks: list(np.linspace(vmin,vmax,10))
                        "cbar_drawedges":     False, #draw edges of colorbar
                        "cbar_label":         "some title", #title on long axis of colorbar
                        "cbar_format":         '%.1f', #format of tick labels


                        ### SAVE PROPERTIES ###       
                        "save":             True,
                        "save_name":        "cont2D.pdf",
                        "save_dpi":         'figure', #float or 'figure' for same resolution as figure
                        "save_orientation": 'landscape', #portrait
                        "save_bbox_inches": 'tight', #or float in inches - which portion of the figure to save?
                        "save_pad_inches":   0.1,


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