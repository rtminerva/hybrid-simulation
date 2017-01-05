import matplotlib.pyplot as plt 
import numpy
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

def pic_2d(coef,set,sol):
    '''Blood Vessel Growth (TIP and STALK)'''
    fig = plt.figure()
    plt.title('%s%f' % ('Blood Vessel Growth at t=',set['t']))
    plt.xlim(set['Hh'],coef['X']-set['Hh'])
    plt.ylim(set['Hh'],coef['Y']-set['Hh'])
    ax = fig.add_subplot(111)
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
    b_sol = numpy.ma.masked_array(b_sol, b_sol < 0.0001)#-.5)
    cmap = plt.cm.Reds
    plt.pcolormesh(y_main_axis, x_main_axis, b_sol, cmap="winter")
    sol['stEC'] +=1  
    flag = 'zVessel=%s' % str(sol['stEC']) 
    plt.colorbar()
    plt.savefig("%s.png" % flag)
    plt.close()
    
    '''Continuous Plot VEGF'''
    fig1 = plt.figure(1)
    plt.title('%s%f' % ('VEGF Distribution at t=',set['t']))
    plt.xlabel('X')
    plt.ylabel('Y')
     
    x_sub_axis = numpy.arange(0, coef['X']+set['Hh'], set['h'])
    y_sub_axis = numpy.arange(0, coef['Y']+set['Hh'], set['h'])
    x_sub_axis, y_sub_axis = numpy.meshgrid(x_sub_axis, y_sub_axis)
     
    c_sol = numpy.zeros((set['Nx']/2+1, set['Ny']/2+1))
    for j, y in enumerate(range(0,set['Ny']+1,2)):
        for i, x in enumerate(range(0,set['Nx']+1,2)):
            c_sol[i,j] = sol['c'][x,y]
    plt.pcolormesh(y_sub_axis, x_sub_axis, c_sol)
    sol['stVEGF'] +=1  
    flag = 'zVEGF=%s' % str(sol['stVEGF']) 
    plt.colorbar()
    plt.savefig("%s.png" % flag)
    plt.close()
    
    return