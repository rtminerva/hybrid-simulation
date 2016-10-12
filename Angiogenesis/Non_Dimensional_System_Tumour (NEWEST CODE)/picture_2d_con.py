import matplotlib.pyplot as plt 
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D



import numpy

def pic_2d_con(coef,set,sol):
    '''Continuous Plot'''
    fig1 = plt.figure(1)
    plt.title('%s%f' % ('EC at t=',set['t']))  
    plt.xlabel('X')
    plt.ylabel('Y')
     
    x_sub_axis = numpy.arange(0, coef['X']+set['Hh'], set['h'])
    y_sub_axis = numpy.arange(0, coef['Y']+set['Hh'], set['h'])
    x_sub_axis, y_sub_axis = numpy.meshgrid(x_sub_axis, y_sub_axis)
     
    n_sol = numpy.zeros((set['Nx']/2+1, set['Ny']/2+1))
    for j, y in enumerate(range(0,set['Ny']+1,2)):
        for i, x in enumerate(range(0,set['Nx']+1,2)):
            n_sol[i,j] = sol['n'][x,y]
    #surf = ax.plot_surface(x_sub_axis, y_sub_axis, n_sol, rstride=1, cstride=1, cmap=cm.coolwarm,
    #        linewidth=0, antialiased=False)
    #fig1.colorbar(surf, shrink=0.5, aspect=5)
    plt.pcolormesh(y_sub_axis, x_sub_axis, c_sol)
    sol['stEC'] +=1  
    flag = 'EC=%s' % str(sol['stEC']) 
    plt.savefig("%s.png" % flag)
    plt.close()
    
    return