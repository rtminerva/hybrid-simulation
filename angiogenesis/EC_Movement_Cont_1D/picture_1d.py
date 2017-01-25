import matplotlib.pyplot as plt 
import numpy
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

def pic_1d(coef,set,sol):
    c_sol = numpy.zeros(set['Nx']/2+1) #to save values at time step k (we are calculating at time step k+1)
    n_sol = numpy.zeros(set['Nx']/2) #to save values at time step k (we are calculating at time step k+1)
    b_sol = numpy.zeros(set['Nx']/2) #to save values at time step k (we are calculating at time step k+1)
    
    id = 0
    for ind, v in enumerate(sol['c']):
        if ind % 2 == 0:
            c_sol[id] = sol['c'][ind]
            id += 1
    id = 0
    for ind, v in enumerate(sol['n']):
        if ind % 2 != 0:
            n_sol[id] = sol['n'][ind]
            id += 1
    id = 0
    for ind, v in enumerate(sol['b']):
        if ind % 2 != 0:
            b_sol[id] = sol['b'][ind]
            id += 1        

    '''Blood Vessel Growth (TIP and STALK)'''
    plt.figure(1)
    axes = plt.gca()
    axes.set_xlim([0,1])
    axes.set_ylim([0,2.5])
    plt.title('%s%f' % ('Tip Cell, Stalk Cell density at t=',set['t']))
    x_main_axis = numpy.arange(set['Hh'], coef['X'], set['h'])
    x_sub_axis = numpy.arange(0, coef['X']+set['Hh'], set['h'])
    plt.plot(x_main_axis, n_sol, x_main_axis, b_sol, x_sub_axis, c_sol)
    sol['stEC'] +=1  
    flag = 'N&S=%s' % str(sol['stEC']) 
    plt.savefig("%s.png" % flag)
    plt.close()
    
    return