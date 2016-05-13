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

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D


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
    
    '''PRINTING RESULT AS CONTROL'''  
    print 'at Time', set['t']
    print 'Total Tips:', len(sol['matrix_tip'])
    print 'Total Stop Tips:', len(sol['sp_stop'])
    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
        print 'NILAI C, F, P MAX', sol['c'].max(), ',', sol['f'].max(), ',', sol['p'].max()
        print 'NILAI C, F, P MIN', sol['c'].min(), ',', sol['f'].min(), ',', sol['p'].min()
        print '# of MC', len(sol['index_mn'])
        print '# of EC', sol['number_ec']
        gg = len(sol['index_mn'])*100/(sol['number_ec'])
        print gg, '%'
    else:
        print 'NILAI C, F MAX', sol['c'].max(), ',', sol['f'].max()
        print 'NILAI C, F MIN', sol['c'].min(), ',', sol['f'].min()
    print 'process time of Hybrid:', start2-start1
    print 'total time of processing:', time.clock()
    print '***************************************************'
    print
#     for i, tip in enumerate(sol['matrix_tip']):
#         print 'TIP', i,':',tip
    '''SAVING PICTURES'''    
    if not coef['Kappa'] == 0 or not coef['Mic'] == 0:   
        if set['k'] % 100 == 0:
            sol['MC_per_EC'][set['k']] = gg        
        if set['k'] % 500 == 0: #and not set['k'] == 0 :    
            '''EC & MC'''           
            fig = plt.figure()
            plt.title('%s%f' % ('EC & MC at t=',set['t']))
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
            x_p = []
            y_p = []
            for i in range(0,len(sol['index_mn'])):
                x_p.append(sol['index_mn'][i][0]*set['Hh'])
                y_p.append(sol['index_mn'][i][1]*set['Hh'])
            plt.scatter(x_p, y_p, marker = 'o', s = 0.5, color ='red')
            sol['st'] +=1  
            flag = 'x=%s' % str(sol['st']) 
            plt.savefig("%s.png" % flag)
            plt.close()
            #plt.draw()
            
            '''EC'''
            fig = plt.figure()
            plt.title('%s%f' % ('EC at t=',set['t']))
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
            sol['st'] +=1  
            flag = 'x=%s' % str(sol['st']) 
            plt.savefig("%s.png" % flag)
            plt.close()
            #plt.draw()
            
            '''MC'''
            plt.figure()
            plt.title('%s%f' % ('MC at t=',set['t']))
            plt.xlim(set['Hh'],coef['X']-set['Hh'])
            plt.ylim(set['Hh'],coef['Y']-set['Hh'])
            x_p = []
            y_p = []
            for y in range(1,set['Ny'],2):
                for x in range(1,set['Nx'],2):
                    if sol['m'][x,y] == 1:
                        x_p.append(x*set['Hh'])
                        y_p.append(y*set['Hh'])
            '''
            for i in range(0,len(sol['m'])):
                x_p.append(sol['m'][i][0]*set['Hh'])
                y_p.append(sol['m'][i][1]*set['Hh'])
            '''
            plt.scatter(x_p, y_p, marker = 'o', s = 0.5, color ='green')
            sol['st'] +=1  
            flag = 'x=%s' % str(sol['st']) 
            plt.savefig("%s.png" % flag)
            plt.close()
            #plt.draw()  
            
            '''MC on EC''' 
            plt.figure()
            plt.title('%s%f' % ('MC on EC at t=',set['t']))
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
            sol['st'] +=1  
            flag = 'x=%s' % str(sol['st']) 
            plt.savefig("%s.png" % flag)
            plt.close()
            #plt.draw()
             
            del x_p
            del y_p
        print 'Percentage of MC on EC:', sol['MC_per_EC']
    else: 
        if set['k'] % 50 == 0: 
            fig = plt.figure()
            plt.title('%s%f' % ('EC at t=',set['t']))
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
            sol['st'] +=1  
            flag = 'x=%s' % str(sol['st']) 
            plt.savefig("%s.png" % flag)
            plt.close()
            #plt.draw()
            
            fig1 = plt.figure(1)
            plt.title('%s%f' % ('TAF at t=',set['t']))
            ax = fig1.gca(projection='3d')
            ax.set_zlim(-0.1, 1)
            ax.zaxis.set_major_locator(LinearLocator(10))
            ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
             
            x_sub_axis = numpy.arange(0, coef['X']+set['Hh'], set['h'])
            y_sub_axis = numpy.arange(0, coef['Y']+set['Hh'], set['h'])
            x_sub_axis, y_sub_axis = numpy.meshgrid(x_sub_axis, y_sub_axis)
             
            c_sol = numpy.zeros((set['Nx']/2+1, set['Ny']/2+1))
            for j, y in enumerate(range(0,set['Ny']+1,2)):
                for i, x in enumerate(range(0,set['Nx']+1,2)):
                    c_sol[i,j] = sol['c'][x,y]
            surf = ax.plot_surface(x_sub_axis, y_sub_axis, c_sol, rstride=1, cstride=1, cmap=cm.coolwarm,
                    linewidth=0, antialiased=False)
            fig1.colorbar(surf, shrink=0.5, aspect=5)
            sol['st'] +=1  
            flag = 'x=%s' % str(sol['st']) 
            plt.savefig("%s.png" % flag)
            plt.close()
            
            
            fig2 = plt.figure(2)
            plt.title('%s%f' % ('Fibronectin at t=',set['t']))
            ax = fig2.gca(projection='3d')
            ax.set_zlim(-0.1, 1)
            ax.zaxis.set_major_locator(LinearLocator(10))
            ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
            
            f_sol = numpy.zeros((set['Nx']/2+1, set['Ny']/2+1))
            for j, y in enumerate(range(0,set['Ny']+1,2)):
                for i, x in enumerate(range(0,set['Nx']+1,2)):
                    f_sol[i,j] = sol['f'][x,y]
            surf = ax.plot_surface(x_sub_axis, y_sub_axis, f_sol, rstride=1, cstride=1, cmap=cm.coolwarm,
                    linewidth=0, antialiased=False)
            fig2.colorbar(surf, shrink=0.5, aspect=5)
            sol['st'] +=1  
            flag = 'x=%s' % str(sol['st']) 
            plt.savefig("%s.png" % flag)
            plt.close()          
             
            del x_p
            del y_p          
         
        
    set['t'] += set['dt']
    set['k'] += 1
     
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

c_sol = numpy.zeros((set['Nx']/2+1, set['Ny']/2+1))
for j, y in enumerate(range(0,set['Ny']+1,2)):
    for i, x in enumerate(range(0,set['Nx']+1,2)):
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

