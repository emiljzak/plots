import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def plot_cont2D_analytic(func,xrange,yrange,vmin,vmax,ncont,nptsx,nptsy,cont2D_params):
    """ Produces contour plot for an analytic function of type v = f(x,y) """

    """
    Args:
        f: str: name of external function to plot
        xrange,yrange: tuple (xmin,xmax): x,y-range for the plot
        vmin,vmax: float : value range for the plot
        ncont:      int: number of contours
        nptsx,nptsy: int: number of sampling points along x,y

        kwargs:

    Comments:
        1)

    """
    figsizex = 4.0 #size of the figure on screen
    figsizey = 4.0 #size of the figure on screen
    resolution = 200 #resolution in dpi

    fig = plt.figure(figsize=(figsizex, figsizey), dpi=resolution,
                     constrained_layout=True)
    grid_fig = gridspec.GridSpec(ncols=1, nrows=1, figure=fig)

    ax1 = fig.add_subplot(grid_fig[0, 0], projection='rectilinear')

    x1d = np.linspace(xrange[0], xrange[1], nptsx, endpoint=True, dtype=float)
    y1d = np.linspace(yrange[0], yrange[1], nptsy, endpoint=True, dtype=float)

    x2d,y2d = np.meshgrid(x1d,y1d)

    #v2d = eval(func + f"({x2d}" + "," + f"{y2d})") #dynamic call
    
    v2d = harm2d(x2d,y2d)

    plot_cont_1 = ax1.contourf( x2d, y2d, v2d, 
                                ncont, cmap = 'jet', vmin=vmin, vmax=vmax)

    ax1.set_xticklabels(cont2D_params['xticks']) 
    ax1.set_yticklabels(cont2D_params['yticks']) 

    plt.show()
    plt.legend()  
    fig.savefig("2d_cont_cart_analytic.pdf" ,\
                bbox_inches='tight')
    plt.close()

""" --------- EXAMPLE ANALYTIC FUNCTIONS ------------"""
def harm2d(x,y):
    return np.sin(x)*np.cos(y)

if __name__ == "__main__":

    function = "harm2d"

    xmax = 5.0
    ymax = 5.0
    xrange = (-xmax, xmax)
    yrange = (-ymax, ymax)

    vmin = -1.0
    vmax = 1.0
    ncont = 100
    nptsx = 200
    nptsy = 200

    cont2D_params = {}
    cont2D_params = { "xticks": list(np.linspace(xrange[0],xrange[1],10)),
                      "yticks": list(np.linspace(yrange[0],yrange[1],5))  }

    plot_cont2D_analytic(function,xrange,yrange,vmin,vmax,ncont,nptsx,nptsy,cont2D_params)