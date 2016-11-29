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
#     if set['k'] == 0:
#         '''Vector Field'''
#         fig = plt.figure()
#         plt.title('Vector Field')
#         plt.xlim(set['Hh'],coef['X']-set['Hh'])
#         plt.ylim(set['Hh'],coef['Y']-set['Hh'])
#         
#         x_main_axis = numpy.arange(set['Hh'], coef['X'], set['h'])
#         y_main_axis = numpy.arange(set['Hh'], coef['Y'], set['h'])
#         x_main_axis, y_main_axis = numpy.meshgrid(x_main_axis, y_main_axis)
#         
#         G_sol_1 = numpy.zeros((set['Nx']/2+1, set['Ny']/2+1))
#         G_sol_2 = numpy.zeros((set['Nx']/2+1, set['Ny']/2+1))
#         for j, y in enumerate(range(1,set['Ny'],2)):
#             for i, x in enumerate(range(1,set['Nx'],2)):
#                 G_sol_1[i,j] = sol['G_vec_x'][x,y]
#                 G_sol_2[i,j] = sol['G_vec_y'][x,y]
#     
#         plt.streamplot(x_main_axis, y_main_axis, G_sol_1, G_sol_2,density=[0.5, 1],color='DarkRed',linewidth=2)
#         plt.colorbar()
#         plt.savefig("Vector Field.png")
#         plt.close()
        
    '''X4'''
    fig = plt.figure()
    plt.title('%s%f' % ('X4 Movement at t=',set['t']))
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
    ax.scatter(x_p, y_p, marker = 'o', s = 5, color ='r')
    sol['tX4'] +=1  
    flag = 'X4=%s' % str(sol['tX4']) 
    plt.savefig("%s.png" % flag)
    plt.close()
    
    '''X1'''
    plt.figure(2)
    plt.title('%s%f' % ('X1 Distribution at t=',set['t']))
    plt.xlabel('X')
    plt.ylabel('Y')
         
    x_main_axis = numpy.arange(set['Hh'], coef['X'], set['h'])
    y_main_axis = numpy.arange(set['Hh'], coef['Y'], set['h'])
    x_main_axis, y_main_axis = numpy.meshgrid(x_main_axis, y_main_axis)
    
    X1_sol = numpy.zeros((set['Nx']/2, set['Ny']/2))
    for j, y in enumerate(range(1,set['Ny'],2)):
        for i, x in enumerate(range(1,set['Nx'],2)):
            X1_sol[i,j] = sol['X1'][x,y]
    X1_sol = numpy.ma.masked_array(X1_sol, X1_sol < 0.0001)
    plt.pcolormesh(y_main_axis, x_main_axis, X1_sol, cmap="BuGn")
    plt.colorbar()
    
    sol['tX1'] +=1  
    flag = 'X1=%s' % str(sol['tX1']) 
    plt.savefig("%s.png" % flag)
    plt.close()
    
    '''X3'''
    plt.figure(2)
    plt.title('%s%f' % ('X3 Distribution at t=',set['t']))
    plt.xlabel('X')
    plt.ylabel('Y')
         
    x_main_axis = numpy.arange(set['Hh'], coef['X'], set['h'])
    y_main_axis = numpy.arange(set['Hh'], coef['Y'], set['h'])
    x_main_axis, y_main_axis = numpy.meshgrid(x_main_axis, y_main_axis)
    
    X3_sol = numpy.zeros((set['Nx']/2, set['Ny']/2))
    for j, y in enumerate(range(1,set['Ny'],2)):
        for i, x in enumerate(range(1,set['Nx'],2)):
            X3_sol[i,j] = sol['X3'][x,y]
    X3_sol = numpy.ma.masked_array(X3_sol, X3_sol < 0.0001)
    plt.pcolormesh(y_main_axis, x_main_axis, X3_sol, cmap="BuPu")
    plt.colorbar()
    
    sol['tX3'] +=1  
    flag = 'X3=%s' % str(sol['tX3']) 
    plt.savefig("%s.png" % flag)
    plt.close()
    
    return