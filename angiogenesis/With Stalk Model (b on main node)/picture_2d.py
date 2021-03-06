import matplotlib.pyplot as plt 
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D



import numpy

def pic_2d_con(coef,set,sol):
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
    plt.pcolormesh(y_main_axis, x_main_axis, n_sol, cmap="Reds")
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
    plt.pcolormesh(y_main_axis, x_main_axis, b_sol, cmap="BuGn")
    plt.colorbar()
    
    sol['stStalk'] +=1  
    flag = 'St=%s' % str(sol['stStalk']) 
    plt.savefig("%s.png" % flag)
    plt.close()
    return sol

def pic_2d(coef,set,sol):
    '''Blood Vessel Growth'''
    fig = plt.figure()
    plt.title('%s%f' % ('Blood Vessel Growth at t=',set['t']))
    plt.xlim(set['Hh'],coef['X']-set['Hh'])
    plt.ylim(set['Hh'],coef['Y']-set['Hh'])
    ax = fig.add_subplot(111)
#     for i in range(0,len(sol['matrix_tip'])):
#         x_p = []
#         y_p = []
#         for j in range(0,len(sol['matrix_tip'][i])):
#             x_p.append(sol['matrix_tip'][i][j][0]*set['Hh'])
#             y_p.append(sol['matrix_tip'][i][j][1]*set['Hh'])
#         globals()['plo%s' % i] = ax.plot(x_p, y_p, 'c', color ='r')
    x_p = []
    y_p = []
    for tip in sol['tip_cell']:
        x_p.append(tip[0]*set['Hh'])
        y_p.append(tip[1]*set['Hh'])
    ax.scatter(x_p, y_p, marker = 'o', s = 10, color ='r')
    
    x_main_axis = numpy.arange(set['Hh'], coef['X'], set['h'])
    y_main_axis = numpy.arange(set['Hh'], coef['Y'], set['h'])
    x_main_axis, y_main_axis = numpy.meshgrid(x_main_axis, y_main_axis)
     
    b_sol = numpy.zeros((set['Nx']/2, set['Ny']/2))
    for j, y in enumerate(range(1,set['Ny'],2)):
        for i, x in enumerate(range(1,set['Nx'],2)):
            b_sol[i,j] = sol['b'][x,y]
    #surf = ax.plot_surface(x_sub_axis, y_sub_axis, f_sol, rstride=1, cstride=1, cmap=cm.coolwarm,
    #        linewidth=0, antialiased=False)
    #fig1.colorbar(surf, shrink=0.5, aspect=5)
    b_sol = numpy.ma.masked_array(b_sol, b_sol < 0.0001)#-.5)
    cmap = plt.cm.Reds
    plt.pcolormesh(y_main_axis, x_main_axis, b_sol, cmap="winter")
    sol['stEC'] +=1  
    flag = 'zVessel=%s' % str(sol['stEC']) 
    plt.colorbar()
    plt.savefig("%s.png" % flag)
    plt.close()
    #plt.draw()
    
    '''Continuous Plot VEGF Hybrid'''
    fig1 = plt.figure(1)
    plt.title('%s%f' % ('VEGF (in Hybrid) at t=',set['t']))
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
    plt.pcolormesh(y_sub_axis, x_sub_axis, c_sol)
    sol['stVEGF'] +=1  
    flag = 'zVEGF=%s' % str(sol['stVEGF']) 
    plt.colorbar()
    plt.savefig("%s.png" % flag)
    plt.close()
    
    '''Continuous Plot VEGF Hybrid'''
    fig1 = plt.figure(1)
    plt.title('%s%f' % ('VEGF at t=',set['t']))
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
     
    c1_sol = numpy.zeros((set['Nx']/2+1, set['Ny']/2+1))
    for j, y in enumerate(range(0,set['Ny']+1,2)):
        for i, x in enumerate(range(0,set['Nx']+1,2)):
            c1_sol[i,j] = sol['c1'][x,y]
    #surf = ax.plot_surface(x_sub_axis, y_sub_axis, c_sol, rstride=1, cstride=1, cmap=cm.coolwarm,
    #        linewidth=0, antialiased=False)
    #fig1.colorbar(surf, shrink=0.5, aspect=5)
    plt.pcolormesh(y_sub_axis, x_sub_axis, c1_sol)
    sol['stVEGF1'] +=1  
    flag = 'zVEGF1=%s' % str(sol['stVEGF1']) 
    plt.colorbar()
    plt.savefig("%s.png" % flag)
    plt.close()
        
    
    '''Continuous Plot Tip'''
    fig1 = plt.figure(1)
    plt.title('%s%f' % ('Tip Distribution at t=',set['t']))
    #ax = fig1.gca(projection='3d')
    #ax.set_zlim(-0.1, 1)
    #ax.zaxis.set_major_locator(LinearLocator(10))
    #ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    #plt.set_xlabel('X')
    #plt.set_ylabel('Y')
    #plt.set_zlabel('Z')
    
    plt.xlabel('X')
    plt.ylabel('Y')
     
    x_main_axis = numpy.arange(set['Hh'], coef['X'], set['h'])
    y_main_axis = numpy.arange(set['Hh'], coef['Y'], set['h'])
    x_main_axis, y_main_axis = numpy.meshgrid(x_main_axis, y_main_axis)
     
    n1_sol = numpy.zeros((set['Nx']/2, set['Ny']/2))
    for j, y in enumerate(range(1,set['Ny'],2)):
        for i, x in enumerate(range(1,set['Nx'],2)):
            n1_sol[i,j] = sol['n1'][x,y]
    #surf = ax.plot_surface(x_sub_axis, y_sub_axis, c_sol, rstride=1, cstride=1, cmap=cm.coolwarm,
    #        linewidth=0, antialiased=False)
    #fig1.colorbar(surf, shrink=0.5, aspect=5)
    plt.pcolormesh(y_main_axis, x_main_axis, n1_sol, cmap="Reds")
    sol['stEC1'] +=1  
    flag = 'zEC1=%s' % str(sol['stEC1']) 
    plt.colorbar()
    plt.savefig("%s.png" % flag)
    plt.close()
    
    '''Continuous Plot Stalk'''
    fig2 = plt.figure(1)
    plt.title('%s%f' % ('Stalk Distribution at t=',set['t']))
    #ax = fig1.gca(projection='3d')
    #ax.set_zlim(-0.1, 1)
    #ax.zaxis.set_major_locator(LinearLocator(10))
    #ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    #plt.set_xlabel('X')
    #plt.set_ylabel('Y')
    #plt.set_zlabel('Z')
    
    plt.xlabel('X')
    plt.ylabel('Y')
     
    x_main_axis = numpy.arange(set['Hh'], coef['X'], set['h'])
    y_main_axis = numpy.arange(set['Hh'], coef['Y'], set['h'])
    x_main_axis, y_main_axis = numpy.meshgrid(x_main_axis, y_main_axis)
     
    b1_sol = numpy.zeros((set['Nx']/2, set['Ny']/2))
    for j, y in enumerate(range(1,set['Ny'],2)):
        for i, x in enumerate(range(1,set['Nx'],2)):
            b1_sol[i,j] = sol['b1'][x,y]
    #surf = ax.plot_surface(x_sub_axis, y_sub_axis, c_sol, rstride=1, cstride=1, cmap=cm.coolwarm,
    #        linewidth=0, antialiased=False)
    #fig1.colorbar(surf, shrink=0.5, aspect=5)
    b1_sol = numpy.ma.masked_array(b1_sol, b1_sol < 0.0001)#-.5)
    cmap = plt.cm.Reds
    plt.pcolormesh(y_main_axis, x_main_axis, b1_sol, cmap="winter")
    sol['stStalk'] +=1  
    flag = 'zStalk1=%s' % str(sol['stStalk']) 
    plt.colorbar()
    plt.savefig("%s.png" % flag)
    plt.close()

    
#     if set['k'] % 50 == 0:
#         ppp = 1
#         '''Continuous Plot
#         fig1 = plt.figure(1)
#         plt.title('%s%f' % ('VEGF at t=',set['t']))
#         #ax = fig1.gca(projection='3d')
#         #ax.set_zlim(-0.1, 1)
#         #ax.zaxis.set_major_locator(LinearLocator(10))
#         #ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# 
#         #plt.set_xlabel('X')
#         #plt.set_ylabel('Y')
#         #plt.set_zlabel('Z')
#         
#         plt.xlabel('X')
#         plt.ylabel('Y')
#          
#         x_sub_axis = numpy.arange(0, coef['X']+set['Hh'], set['h'])
#         y_sub_axis = numpy.arange(0, coef['Y']+set['Hh'], set['h'])
#         x_sub_axis, y_sub_axis = numpy.meshgrid(x_sub_axis, y_sub_axis)
#          
#         c_sol = numpy.zeros((set['Nx']/2+1, set['Ny']/2+1))
#         for j, y in enumerate(range(0,set['Ny']+1,2)):
#             for i, x in enumerate(range(0,set['Nx']+1,2)):
#                 c_sol[i,j] = sol['c'][x,y]
#         #surf = ax.plot_surface(x_sub_axis, y_sub_axis, c_sol, rstride=1, cstride=1, cmap=cm.coolwarm,
#         #        linewidth=0, antialiased=False)
#         #fig1.colorbar(surf, shrink=0.5, aspect=5)
#         plt.pcolormesh(y_sub_axis, x_sub_axis, c_sol)
#         sol['stVEGF'] +=1  
#         flag = 'VEGF=%s' % str(sol['stVEGF']) 
#         plt.savefig("%s.png" % flag)
#         plt.close()
#         '''
#         
#         '''Continuous Plot b
#         fig1 = plt.figure(1)
#         plt.title('%s%f' % ('Stalk Cell at t=',set['t']))
#         #ax = fig1.gca(projection='3d')
#         #ax.set_zlim(-0.1, 1)
#         #ax.zaxis.set_major_locator(LinearLocator(10))
#         #ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
#         
#         plt.xlabel('X')
#         plt.ylabel('Y')
#     
#         x_main_axis = numpy.arange(set['Hh'], coef['X'], set['h'])
#         y_main_axis = numpy.arange(set['Hh'], coef['Y'], set['h'])
#         x_main_axis, y_main_axis = numpy.meshgrid(x_main_axis, y_main_axis)
#          
#         b_sol = numpy.zeros((set['Nx']/2, set['Ny']/2))
#         for j, y in enumerate(range(1,set['Ny'],2)):
#             for i, x in enumerate(range(1,set['Nx'],2)):
#                 b_sol[i,j] = sol['b'][x,y]
#         #surf = ax.plot_surface(x_sub_axis, y_sub_axis, f_sol, rstride=1, cstride=1, cmap=cm.coolwarm,
#         #        linewidth=0, antialiased=False)
#         #fig1.colorbar(surf, shrink=0.5, aspect=5)
#         plt.pcolormesh(y_main_axis, x_main_axis, b_sol)
#         sol['stStalk'] +=1  
#         flag = 'St=%s' % str(sol['stStalk']) 
#         plt.savefig("%s.png" % flag)
#         plt.close()
#         '''
    
    return