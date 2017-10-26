import matplotlib.pyplot as plt 
import numpy
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D


def pic_1d(coef,set,sol):
    c_sol = numpy.zeros(set['Nx']/2+1) #to save values at time step k (we are calculating at time step k+1)
    n_sol = [set['Hh'] * sol['n'][-1]]
#     vel_sol = numpy.zeros(set['Nx']/2)
    
    id = 0
    for ind, v in enumerate(sol['c']):
        if ind % 2 == 0:
            c_sol[id] = sol['c'][ind]
            id += 1
            
#     id = 0
#     for ind, v in enumerate(sol['vel_n']):
#         if ind % 2 != 0:
#             vel_sol[id] = sol['vel_n'][ind]
#             id += 1

    plt.figure(1)
    axes = plt.gca()
    plt.title('%s%f' % ('t=',set['t']))
    x_main_axis = numpy.arange(set['Hh'], coef['X'], set['h'])
    x_sub_axis = numpy.arange(0, coef['X']+set['Hh'], set['h'])
    plt.scatter(n_sol, 0+0.05, s=500, label = 'Cell')#, 0, color = 'r', 'o')#, label = 'Tip')
    plt.plot(x_sub_axis, c_sol, color = 'k', linewidth=3.0, label = 'VEGF')#, label = 'VEGF')
    plt.xlim([0,1])
    plt.ylim([0,1.2])
#     plt.legend()
    plt.xlabel('x (position)')
    plt.ylabel('density')
    flag = 'a=%s' % str(sol['stEC']) 
    plt.savefig("%s.png" % flag)
    plt.close()
    sol['stEC'] +=1 
        
        
    return