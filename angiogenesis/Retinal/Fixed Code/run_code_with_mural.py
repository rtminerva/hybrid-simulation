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
        print '# of MC on EC', len(sol['index_mn'])
        print '# of EC', numpy.count_nonzero(sol['n'])
        gg = len(sol['index_mn'])*100/(numpy.count_nonzero(sol['n']))
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
        if set['k'] % 50 == 0:
            sol['MC_per_EC'][set['k']] = gg
            if set['t'] > set['tm']:
                if set['initial_prof'] == 'test_1_tip':
                    '''EC & MC_dist'''
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
                        globals()['plo%s' % i] = ax.plot(x_p, y_p, 'y')
                    x_p = []
                    y_p = []
                    for y in range(1,set['Ny'],2):
                        for x in range(1,set['Nx'],2):
                            if sol['m'][x,y] == 1:
                                x_p.append(x*set['Hh'])
                                y_p.append(y*set['Hh'])
                    plt.scatter(x_p, y_p, marker = 'o', s = 1, color ='k')
                    sol['stEC_MC_dist'] +=1  
                    flag = 'EC_MC_dist=%s' % str(sol['stEC_MC_dist']) 
                    plt.savefig("%s.png" % flag)
                    plt.close()
                    
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
                    plt.scatter(x_p, y_p, marker = 'o', s = 1, color ='k')
                    sol['stMC'] +=1  
                    flag = 'MC=%s' % str(sol['stMC']) 
                    plt.savefig("%s.png" % flag)
                    plt.close()
                elif set['initial_prof'] == 'retina_tip':                       
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
                        globals()['plo%s' % i] = ax.plot(x_p, y_p, 'y')
                    x_p = []
                    y_p = []
                    for i in range(0,len(sol['index_mn'])):
                        x_p.append(sol['index_mn'][i][0]*set['Hh'])
                        y_p.append(sol['index_mn'][i][1]*set['Hh'])
                    plt.scatter(x_p, y_p, marker = 'o', s = 1, color ='k')
                    sol['stEC_MC'] +=1  
                    flag = 'EC_MC=%s' % str(sol['stEC_MC']) 
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
                    plt.scatter(x_p, y_p, marker = 'o', s = 1, color ='k')
                    sol['stMC'] +=1  
                    flag = 'MC=%s' % str(sol['stMC']) 
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
                    plt.scatter(x_p, y_p, marker = 'o', s = 1, color ='k')
                    sol['stMC_on_EC'] +=1  
                    flag = 'MC_on_EC=%s' % str(sol['stMC_on_EC']) 
                    plt.savefig("%s.png" % flag)
                    plt.close()
                    
                    fig3 = plt.figure(3)
                    plt.title('%s%f' % ('Tie2 at t=',set['t']))
                    ax = fig3.gca(projection='3d')
                    ax.set_zlim(-0.1, 1)
                    ax.zaxis.set_major_locator(LinearLocator(10))
                    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
                    
                    p_sol = numpy.zeros((set['Nx']/2+1, set['Ny']/2+1))
                    for j, y in enumerate(range(0,set['Ny']+1,2)):
                        for i, x in enumerate(range(0,set['Nx']+1,2)):
                            p_sol[i,j] = sol['p'][x,y]
                    surf = ax.plot_surface(x_sub_axis, y_sub_axis, p_sol, rstride=1, cstride=1, cmap=cm.coolwarm,
                            linewidth=0, antialiased=False)
                    fig3.colorbar(surf, shrink=0.5, aspect=5)
                    sol['stTie2'] +=1  
                    flag = 'Tie2=%s' % str(sol['stTie2']) 
                    plt.savefig("%s.png" % flag)
                    plt.close()
            
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
            sol['stEC'] +=1  
            flag = 'EC=%s' % str(sol['stEC']) 
            plt.savefig("%s.png" % flag)
            plt.close()
            #plt.draw()
            
            '''Continuous Plot'''
            fig1 = plt.figure(1)
            plt.title('%s%f' % ('VEGF at t=',set['t']))
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
            sol['stVEGF'] +=1  
            flag = 'VEGF=%s' % str(sol['stVEGF']) 
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
            sol['stFb'] +=1  
            flag = 'Fb=%s' % str(sol['stFb']) 
            plt.savefig("%s.png" % flag)
            plt.close()
            
            fig3 = plt.figure(3)
            plt.title('%s%f' % ('Tie2 at t=',set['t']))
            ax = fig3.gca(projection='3d')
            ax.set_zlim(-0.1, 1)
            ax.zaxis.set_major_locator(LinearLocator(10))
            ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
            
            p_sol = numpy.zeros((set['Nx']/2+1, set['Ny']/2+1))
            for j, y in enumerate(range(0,set['Ny']+1,2)):
                for i, x in enumerate(range(0,set['Nx']+1,2)):
                    p_sol[i,j] = sol['p'][x,y]
            surf = ax.plot_surface(x_sub_axis, y_sub_axis, p_sol, rstride=1, cstride=1, cmap=cm.coolwarm,
                    linewidth=0, antialiased=False)
            fig3.colorbar(surf, shrink=0.5, aspect=5)
            sol['stTie2'] +=1  
            flag = 'Tie2=%s' % str(sol['stTie2']) 
            plt.savefig("%s.png" % flag)
            plt.close()
                     
            del x_p
            del y_p
        if not set['initial_prof'] == 'test_1_tip':
            if set['k'] % 50 == 0 and not set['k'] == 0:
                print 'Percentage of MC on EC:', sol['MC_per_EC']
                '''Percentage MC on EC'''
                t1 = numpy.arange(0.0, set['T'], 0.1)
                MC_per_EC_p=[0]*len(t1)
                for e,ti in enumerate(range(0,set['k']+1,50)):
                    MC_per_EC_p[e] = sol['MC_per_EC'][ti]
                plt.figure(10)
                plt.title('%s%f' % ('Percentage of MC on EC at t=',set['t']))
                plt.xlim(0,set['T'])
                plt.ylim(0,100)
                plt.subplot(211)
                plt.plot(t1, MC_per_EC_p, 'bo', t1, MC_per_EC_p, 'k')
                sol['stPercentage_MC_on_EC'] +=1  
                flag = 'Percentage_MC_on_EC=%s' % str(sol['stPercentage_MC_on_EC']) 
                plt.savefig("%s.png" % flag)
                plt.close()
        
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
            sol['stT'] +=1  
            flag = 'T=%s' % str(sol['stT']) 
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
            sol['stU'] +=1  
            flag = 'U=%s' % str(sol['stU']) 
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
            sol['stV'] +=1  
            flag = 'V=%s' % str(sol['stV']) 
            plt.savefig("%s.png" % flag)
            plt.close()          
             
            del x_p
            del y_p          
         
        
    set['t'] += set['dt']
    set['k'] += 1
     
print '*************DONE*****************'
print '''All coefficients:'''
print coef
#if not coef['Kappa'] == 0 or not coef['Mic'] == 0:
#    print 'Percentage of MC on EC:', sol['MC_per_EC']
#    '''Percentage MC on EC'''
#    t1 = numpy.arange(0.0, 10.1, 0.1)
#    MC_per_EC_p=[]
#    for ti in range(0,set['k']+1,50):
#        MC_per_EC_p.append(sol['MC_per_EC'][ti])
#    plt.figure(10)
#    plt.title('%s%f' % ('Percentage of MC on EC at t=',set['t']))
#    plt.subplot(211)
#    plt.plot(t1, MC_per_EC_p, 'bo', t1, MC_per_EC_p, 'k')
#    sol['stZZ'] +=1  
#    flag = 'ZZ=%s' % str(sol['stZZ']) 
#    plt.savefig("%s.png" % flag)
#    plt.close()
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

