import numpy as np    


def format_float(x):
   return 0

def gen_meshgrid_2D(xrange,yrange,nptsx,nptsy):
    """
    nptsx,nptsy: int: number of sampling points along x,y
    """
    x1d = np.linspace(xrange[0], xrange[1], nptsx, endpoint=True, dtype=float)
    y1d = np.linspace(yrange[0], yrange[1], nptsy, endpoint=True, dtype=float)

    x2d,y2d = np.meshgrid(x1d,y1d)
    return x2d,y2d

def eval_func_meshgrid_2D(x2d,y2d):

    #v2d = eval(func + f"({x2d}" + "," + f"{y2d})") #dynamic call
    
    v2d = tanh2d(x2d,y2d)
    return v2d

    """ --------- EXAMPLE ANALYTIC FUNCTIONS ------------"""
def harm2d(x,y):
    return np.sin(x)*np.cos(y)

def tanh2d(x,y):
    return np.tanh(x*y)