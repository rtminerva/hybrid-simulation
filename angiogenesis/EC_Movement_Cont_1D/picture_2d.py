import matplotlib.pyplot as plt 
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D



import numpy

def pic_2d(coef,set,sol):
    '''Tip'''
    plt.figure(1)
    plt.title('%s%f' % ('Tip Cell Distribution at t=',set['t']))
    plt.xlabel('X')
    plt.ylabel('Y')
         
    x_main_axis = numpy.arange(set['Hh'], coef['X'], set['h'])
    y_main_axis = numpy.arange(set['Hh'], coef['Y'], set['h'])
    x_main_axis, y_main_axis = numpy.meshgrid(x_main_axis, y_main_axis)
    
    n_sol = numpy.zeros((set['Nx']/2, set['Ny']/2))
    for j, y in enumerate(range(1,set['Ny'],2)):
        for i, x in enumerate(range(1,set['Nx'],2)):
            n_sol[i,j] = sol['n'][x,y]
    plt.pcolormesh(y_main_axis, x_main_axis, n_sol, cmap="Reds", vmin=0, vmax=1)
    plt.colorbar()
    
    sol['stEC'] +=1  
    flag = 'Tt=%s' % str(sol['stEC']) 
    plt.savefig("%s.png" % flag)
    plt.close()
   
    '''Stalk'''
    plt.figure(2)
    plt.title('%s%f' % ('Stalk Cell Distribution at t=',set['t']))
    plt.xlabel('X')
    plt.ylabel('Y')
         
    x_main_axis = numpy.arange(set['Hh'], coef['X'], set['h'])
    y_main_axis = numpy.arange(set['Hh'], coef['Y'], set['h'])
    x_main_axis, y_main_axis = numpy.meshgrid(x_main_axis, y_main_axis)
    
    b_sol = numpy.zeros((set['Nx']/2, set['Ny']/2))
    for j, y in enumerate(range(1,set['Ny'],2)):
        for i, x in enumerate(range(1,set['Nx'],2)):
            b_sol[i,j] = sol['b'][x,y]
    b_sol = numpy.ma.masked_array(b_sol, b_sol < 0.0001)
    plt.pcolormesh(y_main_axis, x_main_axis, b_sol, cmap="BuGn", vmin=0, vmax=1)
    plt.colorbar()
    
    sol['stEC_1'] +=1  
    flag = 'St=%s' % str(sol['stEC_1']) 
    plt.savefig("%s.png" % flag)
    plt.close()
    return sol
    
    '''Continuous Plot VEGF Hybrid'''
    fig1 = plt.figure(1)
    plt.title('%s%f' % ('VEGF Concentration at t=',set['t']))
    #ax = fig1.gca(projection='3d')
    #ax.set_zlim(-0.1, 1)
    #ax.zaxis.set_major_locator(LinearLocator(10))
    #ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    #plt.set_xlabel('X')
    #plt.set_ylabel('Y')
    #plt.set_zlabel('Z')
    
    plt.xlabel('X')
    plt.ylabel('Y')
     
    x_sub_axis = numpy.arange(0, coef['X']+set['Hh'], set['h'])
    y_sub_axis = numpy.arange(0, coef['Y']+set['Hh'], set['h'])
    x_sub_axis, y_sub_axis = numpy.meshgrid(x_sub_axis, y_sub_axis)
     
    c_sol = numpy.zeros((set['Nx']/2+1, set['Ny']/2+1))
    for j, y in enumerate(range(0,set['Ny']+1,2)):
        for i, x in enumerate(range(0,set['Nx']+1,2)):
            c_sol[i,j] = sol['c'][x,y]
    #surf = ax.plot_surface(x_sub_axis, y_sub_axis, c_sol, rstride=1, cstride=1, cmap=cm.coolwarm,
    #        linewidth=0, antialiased=False)
    #fig1.colorbar(surf, shrink=0.5, aspect=5)
    plt.pcolormesh(y_sub_axis, x_sub_axis, c_sol, vmin=0, vmax=1)
    sol['stVEGF'] +=1  
    flag = 'zVEGF=%s' % str(sol['stVEGF']) 
    plt.colorbar()
    plt.savefig("%s.png" % flag)
    plt.close()
    
    return