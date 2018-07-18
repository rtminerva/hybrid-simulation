import matplotlib.pyplot as plt
import numpy
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D


def pic_1d(coef,set,sol):

    if set['k'] % 50 == 0:#set['t'] >= set['T']:  
        '''Chemotaxis velocity analysis'''        
        plt.figure(1)
        axes = plt.gca()
        plt.title('%s' % ('---'))
          
        plt.plot(sol['time'], sol['c'], 'g', linewidth=2.0, label = 'S')
        plt.plot(sol['time'], sol['A'], 'c', linewidth=2.0, label = 'A')
        plt.plot(sol['time'], sol['I'], 'm', linewidth=2.0, label = 'I')
        plt.plot(sol['time'], sol['Ki'], 'k', linewidth=2.0, label = 'R')
        plt.plot(sol['time'], sol['Q'], 'b', linewidth=2.0, label = 'Q')
        plt.legend(bbox_to_anchor=(0.85, 0.25), loc=0, borderaxespad=0.)
#         plt.xlim([0,0.2])
#         plt.ylim([-0.1,0.1])
        plt.ylabel('value')
        plt.xlabel('t (time)')
        flag = 'all_vel1=%s' % str(sol['p_3']) 
        plt.savefig("%s.png" % flag)
        plt.close()
        
        plt.figure(2)
        axes = plt.gca()
        plt.title('%s' % ('S'))
          
        plt.plot(sol['time'], sol['c'], 'g', linewidth=2.0, label = 'S')
        plt.legend(bbox_to_anchor=(0.85, 0.25), loc=2, borderaxespad=0.)
#         plt.xlim([0,0.2])
#         plt.ylim([-0.1,0.1])
        plt.ylabel('value')
        plt.xlabel('t (time)')
        flag = 'S_vel1=%s' % str(sol['p_3']) 
        plt.savefig("%s.png" % flag)
        plt.close()
        
        plt.figure(3)
        axes = plt.gca()
        plt.title('%s' % ('R'))
          
        plt.plot(sol['time'], sol['Ki'], 'k', linewidth=2.0, label = 'R')
        plt.legend(bbox_to_anchor=(0.85, 0.25), loc=2, borderaxespad=0.)
#         plt.xlim([0,0.2])
#         plt.ylim([-0.1,0.1])
        plt.ylabel('value')
        plt.xlabel('t (time)')
        flag = 'R_vel20=%s' % str(sol['p_3']) 
        plt.savefig("%s.png" % flag)
        plt.close()
        
        plt.figure(4)
        axes = plt.gca()
        plt.title('%s' % ('A & I'))
          
        plt.plot(sol['time'], sol['A'], 'c', linewidth=2.0, label = 'A')
        plt.plot(sol['time'], sol['I'], 'm', linewidth=2.0, label = 'I')
        plt.legend(bbox_to_anchor=(0.85, 0.25), loc=0, borderaxespad=0.)
#         plt.xlim([0,0.2])
#         plt.ylim([-0.1,0.1])
        plt.ylabel('value')
        plt.xlabel('t (time)')
        flag = 'AI_vel1=%s' % str(sol['p_3']) 
        plt.savefig("%s.png" % flag)
        plt.close()
        
        plt.figure(5)
        axes = plt.gca()
        plt.title('%s' % ('S & R'))
          
        plt.plot(sol['time'], sol['c'], 'g', linewidth=2.0, label = 'S')
        plt.plot(sol['time'], sol['Ki'], 'k', linewidth=2.0, label = 'R')
        plt.legend(bbox_to_anchor=(0.85, 0.25), loc=0, borderaxespad=0.)
#         plt.xlim([0,0.2])
#         plt.ylim([-0.1,0.1])
        plt.ylabel('value')
        plt.xlabel('t (time)')
        flag = 'SR_vel1=%s' % str(sol['p_3']) 
        plt.savefig("%s.png" % flag)
        plt.close()
        
        plt.figure(6)
        axes = plt.gca()
        plt.title('%s' % ('Q'))
          
        plt.plot(sol['time'], sol['Q'], 'b', linewidth=2.0, label = 'Q')
        plt.legend(bbox_to_anchor=(0.85, 0.25), loc=2, borderaxespad=0.)
#         plt.xlim([0,0.2])
#         plt.ylim([-0.1,0.1])
        plt.ylabel('value')
        plt.xlabel('t (time)')
        flag = 'Q_vel1=%s' % str(sol['p_3']) 
        plt.savefig("%s.png" % flag)
        plt.close()
        
        plt.figure(7)
        axes = plt.gca()
        plt.title('%s' % ('Q & R'))
          
        plt.plot(sol['time'], sol['Q'], 'b', linewidth=2.0, label = 'Q')
        plt.plot(sol['time'], sol['Ki'], 'k', linewidth=2.0, label = 'R')
        plt.legend(bbox_to_anchor=(0.85, 0.25), loc=0, borderaxespad=0.)
#         plt.xlim([0,0.2])
#         plt.ylim([-0.1,0.1])
        plt.ylabel('value')
        plt.xlabel('t (time)')
        flag = 'QR_vel1=%s' % str(sol['p_3']) 
        plt.savefig("%s.png" % flag)
        plt.close()



        
    return