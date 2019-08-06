import matplotlib.pyplot as plt 
import os
import numpy
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

def pic_2d(coef,set,sol): #Ref.5
    script_dir = os.path.dirname(__file__)
    results_dir0 = os.path.join(script_dir, 'cc/n/')
    results_dir1 = os.path.join(script_dir, 'cc/c/')
    results_dir2 = os.path.join(script_dir, 'cc/f/')
    
    if not os.path.isdir(results_dir0):
        os.makedirs(results_dir0)
    if not os.path.isdir(results_dir1):
        os.makedirs(results_dir1)
    if not os.path.isdir(results_dir2):
        os.makedirs(results_dir2)
      
    '''1. EC'''
    fig11 = plt.figure(1)
    plt.title('%s%f' % ('vessel growth t=',set['t']))
    ax = fig11.add_subplot(111)
    '''tip cell'''
    x_p = []
    y_p = []
    for tip in sol['tip_cell']:
        x_p.append(tip[0]*set['Hh'])
        y_p.append(tip[1]*set['Hh'])
    ax.scatter(x_p, y_p, marker = 'o', s = 5, color ='r')
    '''Vessel Growth'''
    for i in range(0,len(sol['matrix_tip'])):
        if isinstance(sol['matrix_tip'][i][-1], int) == False:
            x_p = []
            y_p = []
            for j in range(0,len(sol['matrix_tip'][i])):
                x_p.append(sol['matrix_tip'][i][j][0]*set['Hh'])
                y_p.append(sol['matrix_tip'][i][j][1]*set['Hh'])
            globals()['plo%s' % i] = ax.plot(x_p, y_p, 'c', color ='k')
        else:
            x_p = []
            y_p = []
            for j in range(0,len(sol['matrix_tip'][i])-1):
                x_p.append(sol['matrix_tip'][i][j][0]*set['Hh'])
                y_p.append(sol['matrix_tip'][i][j][1]*set['Hh'])
            globals()['plo%s' % i] = ax.plot(x_p, y_p, 'c', color ='k')
    plt.xlim((set['Hh'],coef['X']-set['Hh']))
    plt.ylim((set['Hh'],coef['Y']-set['Hh']))
    sol['ves'] +=1
    flag = 'ves=%s' % str(sol['ves']) 
    plt.savefig(results_dir0 + "%s.png" % flag)
    plt.close()
    
    '''Record for c, f'''
    x_sub_axis = numpy.arange(0, coef['X']+set['Hh'], set['h'])
    y_sub_axis = numpy.arange(0, coef['Y']+set['Hh'], set['h'])
    x_sub_axis, y_sub_axis = numpy.meshgrid(x_sub_axis, y_sub_axis)
      
    c_sol = numpy.zeros((set['Nx']/2+1, set['Ny']/2+1))
    for j, y in enumerate(range(0,set['Ny']+1,2)):
        for i, x in enumerate(range(0,set['Nx']+1,2)):
            c_sol[i,j] = sol['c'][x,y]
            
    f_sol = numpy.zeros((set['Nx']/2+1, set['Ny']/2+1))
    for j, y in enumerate(range(0,set['Ny']+1,2)):
        for i, x in enumerate(range(0,set['Nx']+1,2)):
            f_sol[i,j] = sol['f'][x,y]
       
       
#     '''2. Continuous Plot VEGF & ECM'''
# #     if set['k'] % 100 == 0:
#     '''Only VEGF'''
#     fig1 = plt.figure(2)
#     plt.title('%s%f' % ('VEGF Distribution at t=',set['t']))
#     plt.pcolormesh(y_sub_axis, x_sub_axis, c_sol, vmin = 0, vmax = 1, cmap="Wistia", shading = 'gouraud')
#     sol['VEGF'] +=1  
#     flag = 'VEGF=%s' % str(sol['VEGF']) 
#     plt.colorbar()
#     plt.savefig(results_dir + "%s.png" % flag)
#     plt.close()
      
      
    '''2. Continuous Plot VEGF & Fibronectin'''
#     if set['k'] % 1000 == 0:
    '''MERGE_cn'''
    fig13 = plt.figure(2)
    plt.title('%s%f' % ('VEGF (c) and vessel growth t=',set['t']))
    ax = fig13.add_subplot(111)
    '''vegf'''
#     c_sol = numpy.ma.masked_array(c_sol, c_sol < 0.0001)#-.5)
    im1 = ax.pcolormesh(y_sub_axis, x_sub_axis, c_sol, vmin = 0, vmax = 1, cmap="Wistia", shading = 'gouraud')
#     plt.colorbar(im1)
    '''tip cell'''
    x_p = []
    y_p = []
    for tip in sol['tip_cell']:
        x_p.append(tip[0]*set['Hh'])
        y_p.append(tip[1]*set['Hh'])
    ax.scatter(x_p, y_p, marker = 'o', s = 5, color ='r')
#     '''Backward Marker'''
#     if len(sol['backward_list']) > 0:
#         x_pp = []
#         y_pp = []
#         for tip in sol['backward_list']:
#             x_pp.append(tip[0]*set['Hh'])
#             y_pp.append(tip[1]*set['Hh'])
#         ax.scatter(x_pp, y_pp, marker = '^', s = 10, color ='c')
    '''Vessel Growth'''
    for i in range(0,len(sol['matrix_tip'])):
        if isinstance(sol['matrix_tip'][i][-1], int) == False:
            x_p = []
            y_p = []
            for j in range(0,len(sol['matrix_tip'][i])):
                x_p.append(sol['matrix_tip'][i][j][0]*set['Hh'])
                y_p.append(sol['matrix_tip'][i][j][1]*set['Hh'])
            globals()['plo%s' % i] = ax.plot(x_p, y_p, 'c', color ='k')
        else:
            x_p = []
            y_p = []
            for j in range(0,len(sol['matrix_tip'][i])-1):
                x_p.append(sol['matrix_tip'][i][j][0]*set['Hh'])
                y_p.append(sol['matrix_tip'][i][j][1]*set['Hh'])
            globals()['plo%s' % i] = ax.plot(x_p, y_p, 'c', color ='k')
    plt.xlim((set['Hh'],coef['X']-set['Hh']))
    plt.ylim((set['Hh'],coef['Y']-set['Hh']))
    sol['Merge_cn'] +=1
    flag = 'c_with_n=%s' % str(sol['Merge_cn']) 
    plt.savefig(results_dir1 + "%s.png" % flag)
    plt.close()
    
    
    '''3. Continuous Plot VEGF & ECM'''
#     if set['k'] % 1000 == 0:
    '''MERGE_c_n'''
    fig13 = plt.figure(3)
    plt.title('%s%f' % ('Fibronectin (f) and vessel growth t=',set['t']))
    ax = fig13.add_subplot(111)
    '''vegf'''
#     c_sol = numpy.ma.masked_array(c_sol, c_sol < 0.0001)#-.5)
    im2 = ax.pcolormesh(y_sub_axis, x_sub_axis, f_sol, vmin = 0, vmax = 1, cmap="cool", shading = 'gouraud')
#     plt.colorbar(im2)
    '''tip cell'''
    x_p = []
    y_p = []
    for tip in sol['tip_cell']:
        x_p.append(tip[0]*set['Hh'])
        y_p.append(tip[1]*set['Hh'])
    ax.scatter(x_p, y_p, marker = 'o', s = 5, color ='r')
#     '''Backward Marker'''
#     if len(sol['backward_list']) > 0:
#         x_pp = []
#         y_pp = []
#         for tip in sol['backward_list']:
#             x_pp.append(tip[0]*set['Hh'])
#             y_pp.append(tip[1]*set['Hh'])
#         ax.scatter(x_pp, y_pp, marker = '^', s = 10, color ='c')
    '''Vessel Growth'''
    for i in range(0,len(sol['matrix_tip'])):
        if isinstance(sol['matrix_tip'][i][-1], int) == False:
            x_p = []
            y_p = []
            for j in range(0,len(sol['matrix_tip'][i])):
                x_p.append(sol['matrix_tip'][i][j][0]*set['Hh'])
                y_p.append(sol['matrix_tip'][i][j][1]*set['Hh'])
            globals()['plo%s' % i] = ax.plot(x_p, y_p, 'c', color ='k')
        else:
            x_p = []
            y_p = []
            for j in range(0,len(sol['matrix_tip'][i])-1):
                x_p.append(sol['matrix_tip'][i][j][0]*set['Hh'])
                y_p.append(sol['matrix_tip'][i][j][1]*set['Hh'])
            globals()['plo%s' % i] = ax.plot(x_p, y_p, 'c', color ='k')
    plt.xlim((set['Hh'],coef['X']-set['Hh']))
    plt.ylim((set['Hh'],coef['Y']-set['Hh']))
    sol['Merge_cnt'] +=1
    flag = 'f_with_n=%s' % str(sol['Merge_cnt']) 
    plt.savefig(results_dir2 + "%s.png" % flag)
    plt.close()
    
    
#     if set['k'] % 1400 == 0 and set['k'] != 0:
#         plt.plot([0,1,2,3,4,5,6,7],sol['tip_cell_pos_ave'],'ro')
#         plt.savefig(results_dir + "gg.png")
#         plt.close()

    return