import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D



import numpy

def c_sol(set,sol):
    c_sol = numpy.zeros(set['Nx']/2+1, set['Ny']/2+1, set['Nz']/2+1)
    for k, z in enumerate(range(0,set['Nz']+1,2)):
        for j, y in enumerate(range(0,set['Ny']+1,2)):
            for i, x in enumerate(range(0,set['Nx']+1,2)):
                c_sol[i,j,k] = sol['c'][x,y,z]
    return c_sol

def f_sol(set,sol):
    f_sol = numpy.zeros(set['Nx']/2+1, set['Ny']/2+1, set['Nz']/2+1)
    for k, z in enumerate(range(0,set['Nz']+1,2)):
        for j, y in enumerate(range(0,set['Ny']+1,2)):
            for i, x in enumerate(range(0,set['Nx']+1,2)):
                f_sol[i,j,k] = sol['f'][x,y,z]
    return f_sol

def flow3d(coef,set,sol):
    #x, y, z = numpy.mgrid[coef['X']+set['Hh'], set['h'], coef['Y']+set['Hh'], set['h'], coef['Z']+set['Hh'], set['h']]
    may.xlabel('X')
    may.ylabel('Y')
    may.zlabel('Z')
    may.flow(c_sol(set,sol), f_sol(set,sol))
    plt.savefig("flow.png")
    plt.close()
    return

def c_contour3d(coef,set,sol):
    '''
    x_sub_axis = numpy.arange(0, coef['X']+set['Hh'], set['h'])
    y_sub_axis = numpy.arange(0, coef['Y']+set['Hh'], set['h'])
    x_sub_axis, y_sub_axis = numpy.meshgrid(x_sub_axis, y_sub_axis)
    x, y, z = numpy.mgrid[coef['X']+set['Hh'], set['h'], coef['Y']+set['Hh'], set['h'], coef['Z']+set['Hh'], set['h']]
    '''
    may.xlabel('X')
    may.ylabel('Y')
    may.zlabel('Z')
    
    may.contour3d(c_sol(set,sol), contours=4, transparent=True)
    sol['stVEGF'] +=1  
    flag = 'VEGF=%s' % str(sol['stVEGF']) 
    plt.savefig("%s.png" % flag)
    plt.close()
    return

def f_contour3d(coef,set,sol):
    #x, y, z = numpy.mgrid[coef['X']+set['Hh'], set['h'], coef['Y']+set['Hh'], set['h'], coef['Z']+set['Hh'], set['h']]
    may.xlabel('X')
    may.ylabel('Y')
    may.zlabel('Z')
    may.contour3d(f_sol(set,sol), contours=4, transparent=True)
    sol['stFb'] +=1  
    flag = 'Fb=%s' % str(sol['stFb']) 
    plt.savefig("%s.png" % flag)
    plt.close()
    return

def hybrid_one_parent(coef,set,sol):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.title('%s%f' % ('EC at t=',set['t']))
    ax.set_xlim(set['Hh'],coef['X']-set['Hh'])
    ax.set_ylim(set['Hh'],coef['Y']-set['Hh'])
    ax.set_zlim(set['Hh'],coef['Z']-set['Hh'])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    for i in range(0,len(sol['matrix_tip'])):
        x_p = []
        y_p = []
        z_p = []
        for j in range(0,len(sol['matrix_tip'][i])):
            x_p.append(sol['matrix_tip'][i][j][0]*set['Hh'])
            y_p.append(sol['matrix_tip'][i][j][1]*set['Hh'])
            z_p.append(sol['matrix_tip'][i][j][2]*set['Hh'])
        globals()['plo%s' % i] = ax.plot(x_p, y_p, z_p, 'c', color ='r')
    x_p = []
    y_p = []
    z_p = []
    for tip in sol['tip_cell']:
        x_p.append(tip[0]*set['Hh'])
        y_p.append(tip[1]*set['Hh'])
        z_p.append(tip[2]*set['Hh'])
    ax.scatter(x_p, y_p, z_p, marker = 'o', s = 2, color ='b')
    sol['stEC'] +=1  
    flag = 'EC=%s' % str(sol['stEC']) 
    plt.savefig("%s.png" % flag)
    plt.close()
    return

def hybrid_two_parent(coef,set,sol):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.title('%s%f' % ('EC at t=',set['t']))
    ax.set_xlim(set['Hh'],coef['X']-set['Hh'])
    ax.set_ylim(set['Hh'],coef['Y']-set['Hh'])
    ax.set_zlim(set['Hh'],coef['Z']-set['Hh'])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    '''Vein'''
    for i in range(0,len(sol['matrix_tip'])):
        x_p = []
        y_p = []
        z_p = []
        for j in range(0,len(sol['matrix_tip'][i])):
            x_p.append(sol['matrix_tip'][i][j][0]*set['Hh'])
            y_p.append(sol['matrix_tip'][i][j][1]*set['Hh'])
            z_p.append(sol['matrix_tip'][i][j][2]*set['Hh'])
        globals()['plo%s' % i] = ax.plot(x_p, y_p, z_p, 'c', color ='b')
    '''Artery'''
    x_p = []
    y_p = []
    z_p = []
    for i in range(0,len(sol['matrix_tip_2'])):
        x_p = []
        y_p = []
        z_p = []
        for j in range(0,len(sol['matrix_tip_2'][i])):
            x_p.append(sol['matrix_tip_2'][i][j][0]*set['Hh'])
            y_p.append(sol['matrix_tip_2'][i][j][1]*set['Hh'])
            z_p.append(sol['matrix_tip_2'][i][j][2]*set['Hh'])
        globals()['plo2%s' % i] = ax.plot(x_p, y_p, z_p, 'c', color ='r')
    x_p = []
    y_p = []
    z_p = []
    for tip in sol['tip_cell']:
        x_p.append(tip[0]*set['Hh'])
        y_p.append(tip[1]*set['Hh'])
        z_p.append(tip[2]*set['Hh'])
    ax.scatter(x_p, y_p, z_p, marker = 'o', s = 2, color ='g')
    x_p = []
    y_p = []
    z_p = []
    for tip in sol['tip_cell_2']:
        x_p.append(tip[0]*set['Hh'])
        y_p.append(tip[1]*set['Hh'])
        z_p.append(tip[2]*set['Hh'])
    ax.scatter(x_p, y_p, z_p, marker = 'o', s = 2, color ='c')
    sol['stEC'] +=1  
    flag = 'EC=%s' % str(sol['stEC']) 
    plt.savefig("%s.png" % flag)
    plt.close()
    return

def pic_3d(coef,set,sol):
#     if set['parent'] == 'two':
#         hybrid_two_parent(coef,set,sol)
#     else:
    hybrid_one_parent(coef,set,sol)
    '''Continuous Plot
    if set['k'] == 0:
        c_contour3d(coef,set,sol)
        f_contour3d(coef,set,sol)
        flow3d(coef,set,sol)   
    '''
    return