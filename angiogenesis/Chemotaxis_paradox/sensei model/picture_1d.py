import matplotlib.pyplot as plt 
import numpy
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D


def pic_1d(coef,set,sol):
    c_sol = numpy.zeros(set['Nx']/2+1) #to save values at time step k (we are calculating at time step k+1)
    n_sol = numpy.zeros(set['Nx']/2)
    vel_sol = numpy.zeros(set['Nx']/2)
    
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
    for ind, v in enumerate(sol['vel_n']):
        if ind % 2 != 0:
            vel_sol[id] = sol['vel_n'][ind]
            id += 1

    
#     if set['k'] == 0:
#         sol['n_0'] = n_sol
#         sol['c_0'] = c_sol
#             
#     if set['k'] == 2000:
#         sol['n_2'] = n_sol
#         sol['b_2'] = b_sol
#         sol['c_2'] = c_sol
#     
#         
#     if set['k'] == 4000:
#         sol['n_6'] = n_sol
#         sol['b_6'] = b_sol
#         sol['c_6'] = c_sol
#         if set['ki_dep'] == 6:
#             sol['n_00'] = numpy.zeros(set['Nx']/2)
#             sol['b_00'] = numpy.zeros(set['Nx']/2)
#             sol['n_00'] = n_sol
#             sol['b_00'] = b_sol
#         elif set['ki_dep'] == 5:
#             sol['n_22'] = numpy.zeros(set['Nx']/2)
#             sol['b_22'] = numpy.zeros(set['Nx']/2)
#             sol['n_22'] = n_sol
#             sol['b_22'] = b_sol
#         elif set['ki_dep'] == 4:
#             sol['n_44'] = numpy.zeros(set['Nx']/2)
#             sol['b_44'] = numpy.zeros(set['Nx']/2)
#             sol['n_44'] = n_sol
#             sol['b_44'] = b_sol
#         if set['ki_dep'] == 3:
#             sol['n_66'] = numpy.zeros(set['Nx']/2)
#             sol['b_66'] = numpy.zeros(set['Nx']/2)
#             sol['n_66'] = n_sol
#             sol['b_66'] = b_sol
#         elif set['ki_dep'] == 2:
#             sol['n_88'] = numpy.zeros(set['Nx']/2)
#             sol['b_88'] = numpy.zeros(set['Nx']/2)
#             sol['n_88'] = n_sol
#             sol['b_88'] = b_sol
#         elif set['ki_dep'] == 1:
#             sol['n_1010'] = numpy.zeros(set['Nx']/2)
#             sol['b_1010'] = numpy.zeros(set['Nx']/2)
#             sol['n_1010'] = n_sol
#             sol['b_1010'] = b_sol
#         
#     if set['k'] == 8000:
#         sol['n_8'] = n_sol
#         sol['b_8'] = b_sol
#         sol['c_8'] = c_sol       
#     


    plt.figure(1)
    axes = plt.gca()
#     axes.set_xlim([0,1])
#     axes.set_ylim([0,1.2])
    plt.title('%s%f' % ('t=',set['t']))
    x_main_axis = numpy.arange(set['Hh'], coef['X'], set['h'])
    x_sub_axis = numpy.arange(0, coef['X']+set['Hh'], set['h'])
    plt.plot(x_main_axis, n_sol, color = 'r', linewidth=3.0)#, label = 'Tip')
    plt.plot(x_sub_axis, c_sol, color = 'k', linewidth=3.0)#, label = 'VEGF')
    plt.plot(x_main_axis, vel_sol, color = 'b', linewidth=1.0)#, label = 'Par_of_grad')
    plt.xlim([0,1])
    plt.ylim([0,1.2])
    plt.legend()
    plt.xlabel('x (position)')
    plt.ylabel('density')
    flag = 'a=%s' % str(sol['stEC']) 
    plt.savefig("%s.png" % flag)
    plt.close()
    sol['stEC'] +=1 
        
        
    return