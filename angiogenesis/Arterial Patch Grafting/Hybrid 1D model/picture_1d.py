import matplotlib.pyplot as plt
import numpy
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D


def pic_1d(coef,set,sol):
    c_sol = numpy.zeros(set['Nx']/2+1) #to save values at time step k (we are calculating at time step k+1)
    n_sol = [set['Hh'] * sol['n'][-1]]
    cell = numpy.zeros(len(sol['n']))
    cell_2 = numpy.zeros(len(sol['n']))
#     t2 = numpy.arange(0, 1, 1000)
    id = 0
    for ind in sol['n']:
        cell[id] = ind*set['Hh']
        id += 1
        
    id = 0
    for ind in cell:
        cell_2[id] = ind * 8 -4
        id += 1
         
    x_main_axis = numpy.arange(set['Hh'], coef['X'], set['h'])
    x_sub_axis = numpy.arange(0, coef['X']+set['Hh'], set['h'])
    
    id = 0
    for ind, v in enumerate(sol['c']):
        if ind % 2 == 0:
            c_sol[id] = sol['c'][ind]
            id += 1
    if set['k'] % 10 == 0:
        plt.figure(1)
        axes = plt.gca()
        plt.title('%s%f' % ('t=',set['t']))
        plt.scatter(n_sol, 0+0.05, s=500, label = 'Cell')#, 0, color = 'r', 'o')#, label = 'Tip')
        plt.plot(x_sub_axis, c_sol, color = 'k', linewidth=3.0, label = 'VEGF')#, label = 'VEGF')
        plt.xlim([0,1])
        plt.ylim([0,1.2])
        plt.legend()
        plt.xlabel('x (position)')
        plt.ylabel('density')
        flag = 'z=%s' % str(sol['stEC']) 
        plt.savefig("%s.png" % flag)
        plt.close()
        sol['stEC'] +=1 
    
    if set['t'] >= set['T']:  
#         fig, ax1 = plt.subplot()  
#         plt.title('%s%f' % ('Cell position and VEGF concentration after t=',set['t']))
#         ax1.plot(cell, t1, 'b', linewidth=2.0)
#         ax1.set_xlabel('x (position)')
#         ax1.set_xlabel('time iteration no.', color='b')
#         ax1.tick_params('y', colors='b')  
#         ax1.ylim([0,1000])
#         ax2 = ax1.twinx()
#         ax2.plot(x_sub_axis, c_sol, color = 'k', linewidth=3.0, label = 'VEGF')
#         ax1.set_xlabel('VEGF', color='k')
#         ax1.tick_params('y', colors='k')  
#         ax1.ylim([0,1.2])
#         fig.tight_layout()        
#         flag = 'b=%s' % str(sol['stEC_1']) 
#         fig.savefig("%s.png" % flag)
#         fig.close()
#         sol['stEC_1'] +=1
#         plt.show 
        '''Cell movement path'''
        plt.figure(2)
        axes = plt.gca()
        plt.title('%s%f' % ('Cell movement path t=',set['t']))  
        plt.plot(cell, sol['time'], 'k', linewidth=2.0)
        plt.xlim([0,1])
        plt.ylim([0,1])
        plt.xlabel('x (position)')
        plt.ylabel('t (time)')
        flag = 'a=%s' % str(sol['stEC_1']) 
        plt.savefig("%s.png" % flag)
        plt.close()
        sol['stEC_1'] +=1 
        
        '''Chemotaxis velocity analysis'''        
        plt.figure(3)
        axes = plt.gca()
        plt.title('%s' % ('---'))
          
#         plt.plot(sol['time'], sol['a_per_b_coef'], 'c', linewidth=2.0, label = 'a\b')
#         plt.plot(sol['time'], sol['a_per_b_left'], 'm', linewidth=2.0, label = 'v_sen')
#         plt.plot(sol['time'], sol['c_'], 'g', linewidth=2.0, label = 'c')
#         plt.plot(sol['time'], sol['c_x'], 'b', linewidth=2.0, label = 'c_x')
        plt.plot(sol['time'], sol['c_t'], 'c', linewidth=2.0, label = 'c_t')
#         plt.plot(sol['time'], sol['vel_n'], 'k', linewidth=2.0, label = 'v')
        plt.legend(bbox_to_anchor=(0.85, 0.25), loc=2, borderaxespad=0.)
#         plt.xlim([0,0.2])
#         plt.ylim([-0.1,0.1])
        plt.ylabel('value (non-dimensional) / position (x=0~1)')
        plt.xlabel('t (time)')
        flag = 'b=%s' % str(sol['stEC_2']) 
        plt.savefig("%s.png" % flag)
        plt.close()
        sol['stEC_2'] +=1 
        
        plt.figure(6)
        axes = plt.gca()
        plt.title('%s' % ('---2'))  
#         plt.plot(sol['time'], sol['a_per_b_coef'], 'c', linewidth=2.0, label = 'a\b')
#         plt.plot(sol['time'], sol['a_per_b_left'], 'm', linewidth=2.0, label = 'v_sen')
#         plt.plot(sol['time'], sol['c_'], 'g', linewidth=2.0, label = 'c')
#         plt.plot(sol['time'], sol['c_x'], 'b', linewidth=2.0, label = 'c_x')
#         plt.plot(sol['time'], sol['c_t'], 'w', linewidth=2.0, label = 'c_t')
        plt.plot(sol['time'], sol['c_t_f'], 'y', linewidth=2.0, label = 'c_t_f')
#         plt.plot(sol['time'], sol['vel_n'], 'k', linewidth=2.0, label = 'v')
#         plt.plot(sol['time'], sol['in_vel_n'], 'y', linewidth=2.0, label = 'v/c_x')
#         plt.plot(sol['time'], cell_2, 'r', linewidth=2.0, label = 'cell pos')
        plt.legend(bbox_to_anchor=(0.85, 0.25), loc=2, borderaxespad=0.)
#         plt.xlim([0,0.2])
#         plt.ylim([-0.1,0.1])
        plt.ylabel('value (non-dimensional) / position (x=0~1)')
        plt.xlabel('t (time)')
        flag = 'c=%s' % str(sol['stEC_3']) 
        plt.savefig("%s.png" % flag)
        plt.close()
        sol['stEC_3'] +=1
        
        plt.figure(4)
        axes = plt.gca()
        plt.title('%s' % ('---3'))  
#         plt.plot(sol['time'], sol['a_per_b_coef'], 'c', linewidth=2.0, label = 'a\b')
#         plt.plot(sol['time'], sol['a_per_b_left'], 'm', linewidth=2.0, label = 'v_sen')
#         plt.plot(sol['time'], sol['c_'], 'g', linewidth=2.0, label = 'c')
#         plt.plot(sol['time'], sol['c_x'], 'b', linewidth=2.0, label = 'c_x')
        plt.plot(sol['time'], sol['c_t'], 'c', linewidth=2.0, label = 'c_t')
        plt.plot(sol['time'], sol['c_t_f'], 'y', linewidth=2.0, label = 'c_t_f')
#         plt.plot(sol['time'], sol['vel_n'], 'k', linewidth=2.0, label = 'v')
        plt.legend(bbox_to_anchor=(0.85, 0.25), loc=2, borderaxespad=0.)
#         plt.xlim([0,0.5])
#         plt.ylim([-0.1,0.1])
        plt.ylabel('value (non-dimensional) / position (x=0~1)')
        plt.xlabel('t (time)')
        flag = 'd=%s' % str(sol['stEC_4']) 
        plt.savefig("%s.png" % flag)
        plt.close()
        sol['stEC_4'] +=1
        
        plt.figure(5)
        axes = plt.gca()
        plt.title('%s' % ('---4'))  
#         plt.plot(sol['time'], sol['a_per_b_coef'], 'c', linewidth=2.0, label = 'a\b')
#         plt.plot(sol['time'], sol['a_per_b_left'], 'm', linewidth=2.0, label = 'v_sen')
        plt.plot(sol['time'], sol['c_'], 'g', linewidth=2.0, label = 'c')
        plt.plot(sol['time'], sol['c_x'], 'b', linewidth=2.0, label = 'c_x')
        plt.plot(sol['time'], sol['c_t'], 'c', linewidth=2.0, label = 'c_t')
        plt.plot(sol['time'], sol['c_t_f'], 'y', linewidth=2.0, label = 'c_t_f')
        plt.plot(sol['time'], sol['vel_n'], 'k', linewidth=2.0, label = 'v')
#         plt.plot(sol['time'], sol['in_vel_n'], 'y', linewidth=2.0, label = 'v/c_x')
        plt.plot(sol['time'], cell_2, 'r', linewidth=2.0, label = 'cell pos')
        plt.legend(bbox_to_anchor=(0.85, 0.25), loc=2, borderaxespad=0.)
#         plt.xlim([0,0.5])
#         plt.ylim([-20,20])
        plt.ylabel('value (non-dimensional) / position (x=0~1)')
        plt.xlabel('t (time)')
        flag = 'e=%s' % str(sol['stEC_5']) 
        plt.savefig("%s.png" % flag)
        plt.close()
        sol['stEC_5'] +=1 
        
    return