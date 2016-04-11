import code_with_mural_dict as disc
from coef_setting import declare_coef
import numpy

from timeit import default_timer as timer 
import time

import matplotlib.pyplot as plt 
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
#from mpmath.functions.rszeta import coef
#import discrete_run as disc
'''Untuk Plot
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D


plt.ion() #interactively
plt.show()
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_zlim(-0.1, 1.2)
Untuk Plot'''

#declare coefficients & initial settings
coef, set, sol = declare_coef()
#to plot interactively
plt.ion()

#hybrid part
while set['t'] <= set['T'] and set['k'] < set['Nt']:
    start1 = timer()
    sol = disc.boolean_1_iter(coef, set, sol)                   
    start2 = timer()
    
    if sol['stop_iter'] >=100000:
        set['k'] = sol['stop_iter']
        
    print 'at Time', set['t']
    set['t'] += set['dt']
    set['k'] += 1
    
    #to print as control
    print 'Total Tips:', len(sol['matrix_tip'])
    print 'Total Stop Tips:', len(sol['sp_stop'])
    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
        print 'NILAI C, F, P MAX', sol['c'].max(), ',', sol['f'].max(), ',', sol['p'].max()
        print 'NILAI C, F, P MIN', sol['c'].min(), ',', sol['f'].min(), ',', sol['p'].min()
    else:
        print 'NILAI C, F MAX', sol['c'].max(), ',', sol['f'].max()
        print 'NILAI C, F MIN', sol['c'].min(), ',', sol['f'].min()
    print 'process time of Hybrid:', start2-start1
    print 'total time of processing:', time.clock()
    print '***************************************************'
    print
#     for i, tip in enumerate(sol['matrix_tip']):
#         print 'TIP', i,':',tip    
     
    if not coef['Kappa'] == 0 or not coef['Mic'] == 0:
        if set['k'] == 500 or set['k'] == 1000 or set['k'] == 1500 or set['k'] == 2000 or set['k'] == 2500 or set['k'] == 3000 or set['k'] == 3500 or set['k'] == 4000:
            fig = plt.figure()
            plt.xlim(set['Hh'],coef['X']-set['Hh'])
            plt.ylim(set['Hh'],coef['Y']-set['Hh'])
            #plt.xlim(set['Hh']*100,coef['X']-set['Hh']*300)
            #plt.ylim(set['Hh']*100,coef['Y']-set['Hh']*300)
            ax = fig.add_subplot(111)
            for i in range(0,len(sol['matrix_tip'])):
                x_p = []
                y_p = []
                for j in range(0,len(sol['matrix_tip'][i])):
                    x_p.append(sol['matrix_tip'][i][j][0]*set['Hh'])
                    y_p.append(sol['matrix_tip'][i][j][1]*set['Hh'])
                globals()['plo%s' % i] = ax.plot(x_p, y_p, 'b')
            plt.draw()
             
            plt.figure()
            plt.xlim(set['Hh'],coef['X']-set['Hh'])
            plt.ylim(set['Hh'],coef['Y']-set['Hh'])
            x_p = []
            y_p = []
            for y in range(1,ny,2):
                for x in range(1,nx,2):
                    if sol['m'][x,y] == 1:
                        x_p.append(x*set['Hh'])
                        y_p.append(y*set['Hh'])
            '''
            for i in range(0,len(sol['m'])):
                x_p.append(sol['m'][i][0]*set['Hh'])
                y_p.append(sol['m'][i][1]*set['Hh'])
            '''
            plt.scatter(x_p, y_p, marker = 'o', s = 0.5, color ='green')
            plt.draw()  
             
            plt.figure()
            plt.xlim(set['Hh'],coef['X']-set['Hh'])
            plt.ylim(set['Hh'],coef['Y']-set['Hh'])
            #plt.xlim(set['Hh']*100,coef['X']-set['Hh']*100)
            #plt.ylim(set['Hh']*100,coef['Y']-set['Hh']*100)
            x_p = []
            y_p = []
            for i in range(0,len(sol['index_mn'])):
                x_p.append(sol['index_mn'][i][0]*set['Hh'])
                y_p.append(sol['index_mn'][i][1]*set['Hh'])
            plt.scatter(x_p, y_p, marker = 'o', s = 0.5, color ='red')
            plt.draw()
             
            '''
            fig1 = plt.figure(1)
            ax = fig1.gca(projection='3d')
            ax.set_zlim(-0.1, 1)
            ax.zaxis.set_major_locator(LinearLocator(10))
            ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
             
            x_sub_axis = numpy.arange(0, coef['X']+set['Hh'], h)
            y_sub_axis = numpy.arange(0, coef['Y']+set['Hh'], h)
            x_sub_axis, y_sub_axis = numpy.meshgrid(x_sub_axis, y_sub_axis)
             
            p_sol = numpy.zeros((nx/2+1, ny/2+1))
            for j, y in enumerate(range(0,ny+1,2)):
                for i, x in enumerate(range(0,nx+1,2)):
                    p_sol[i,j] = g[9][x,y]
            surf = ax.plot_surface(x_sub_axis, y_sub_axis, p_sol, rstride=1, cstride=1, cmap=cm.coolwarm,
                    linewidth=0, antialiased=False)
            fig1.colorbar(surf, shrink=0.5, aspect=5)
            plt.draw()
            '''
             
            del x_p
            del y_p
    else:
        '''
        if  == 1:
            fig = plt.figure()
            plt.xlim(set['Hh']*170,coef['X']-set['Hh']*170)
            plt.ylim(set['Hh']*170,coef['Y']-set['Hh']*170)
            x_p = []
            y_p = []
            for i in range(0,len(sol['matrix_tip'])):
                x_p.append(sol['matrix_tip'][i][0][0]*set['Hh'])
                y_p.append(sol['matrix_tip'][i][0][1]*set['Hh'])
            plt.scatter(x_p, y_p, marker = 'o', s = 10, color ='blue')
            plt.draw()
            del x_p
            del y_p 
        '''  
        if set['k'] == 500 or set['k'] == 1000 or set['k'] == 1500 or set['k'] == 2000 or set['k'] == 2500 or set['k'] == 3000 or set['k'] == 3500 or set['k'] == 4000:
            fig = plt.figure()
            plt.xlim(set['Hh'],coef['X']-set['Hh'])
            plt.ylim(set['Hh'],coef['Y']-set['Hh'])
            ax = fig.add_subplot(111)
            for i in range(0,len(sol['matrix_tip'])):
                x_p = []
                y_p = []
                for j in range(0,len(sol['matrix_tip'][i])):
                    x_p.append(sol['matrix_tip'][i][j][0]*set['Hh'])
                    y_p.append(sol['matrix_tip'][i][j][1]*set['Hh'])
                globals()['plo%s' % i] = ax.plot(x_p, y_p, 'b')
            plt.draw()
            del x_p
            del y_p          
         
        '''
        fig = plt.figure()
        plt.xlim(set['Hh'],coef['X']-set['Hh'])#coef['X']-hh
        plt.ylim(set['Hh'],coef['Y']-set['Hh'])#
        ax = fig.add_subplot(111)
        for i in range(0,len(sol['matrix_tip'])):
            x_p = []
            y_p = []
            for j in range(0,len(sol['matrix_tip'][i])):
                x_p.append(sol['matrix_tip'][i][j][0]*set['Hh'])
                y_p.append(sol['matrix_tip'][i][j][1]*set['Hh'])
            globals()['plo%s' % i] = ax.plot(x_p, y_p, 'b')  
        plt.draw() 
         
        if not Kappa == 0 or not Mic == 0:
            plt.figure()
            plt.xlim(set['Hh'],coef['X']-set['Hh'])#coef['X']-hh
            plt.ylim(set['Hh'],coef['Y']-set['Hh'])#
            x_p = []
            y_p = []
            for i in range(0,len(g[11])):
                x_p.append(g[11][i][0]*set['Hh'])
                y_p.append(g[11][i][1]*set['Hh'])
            plt.scatter(x_p, y_p, marker = 'o', s = 0.5)
            plt.draw() 
        '''
     
    
print '*************DONE*****************'

'''Plot Continuous
fig1 = plt.figure(1)
ax = fig1.gca(projection='3d')
ax.set_zlim(-0.1, 1)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

x_main_axis = numpy.arange(0, coef['X']+Hh, h)
y_main_axis = numpy.arange(0, Y+Hh, h)
x_main_axis, y_main_axis = numpy.meshgrid(x_main_axis, y_main_axis)

c_sol = numpy.zeros((nx/2+1, ny/2+1))
for j, y in enumerate(range(0,ny+1,2)):
    for i, x in enumerate(range(0,nx+1,2)):
        c_sol[i,j] = g[8][x,y]
surf = ax.plot_surface(x_main_axis, y_main_axis, c_sol, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
fig1.colorbar(surf, shrink=0.5, aspect=5)
plt.draw()
Plot Continuous'''


'''Plot Hybrid
fig2 = plt.figure(2)
plt.xlim(Hh,X-Hh)#X-hh
plt.ylim(Hh,Y-Hh)#
ax = fig2.add_subplot(111)
for i in range(0,len(sol['matrix_tip'])):
    x_p = []
    y_p = []
    for j in range(0,len(g[9][i])):
        x_p.append(g[9][i][j][0]*Hh)
        y_p.append(g[9][i][j][1]*Hh)
    globals()['plo%s' % i] = ax.plot(x_p, y_p, 'b')
fig2.show()
'''  

'''
fig3 = plt.figure(3)
plt.xlim(Hh,X-Hh)#X-hh
plt.ylim(Hh,Y-Hh)#
ax = fig3.add_subplot(111)
x_p = []
y_p = []
for i in range(0,len(g[11])):
    x_p.append(g[11][i][0]*Hh)
    y_p.append(g[11][i][1]*Hh)
scat = ax.scatter(x_p, y_p, marker = 'o')
fig3.show()   
'''


raw_input()
# plt.show(block=True)

