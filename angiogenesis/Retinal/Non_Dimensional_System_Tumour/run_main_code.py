import main_code as main
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
    sol = main.boolean_1_iter(coef, set, sol)                   
    start2 = timer()
    
    if sol['stop_iter'] >=100000:
        set['k'] = sol['stop_iter']
    
    '''PRINTING RESULT AS CONTROL'''  
    print 'at Time', set['t']
    print 'Total Tips:', len(sol['matrix_tip'])
    print 'Total Stop Tips:', len(sol['sp_stop'])
    print 'NILAI C MAX', sol['c'].max()
    print 'NILAI C MIN', sol['c'].min()
    print sol['tip_cell']
       
    print 'process time of Hybrid:', start2-start1

    '''SAVING PICTURES'''    
    if set['k'] % 1 == 0:
        
        if set['layout'] == '2D':
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
                globals()['plo%s' % i] = ax.plot(x_p, y_p, 'c', color ='r')
            x_p = []
            y_p = []
            for tip in sol['tip_cell']:
                x_p.append(tip[0]*set['Hh'])
                y_p.append(tip[1]*set['Hh'])
            ax.scatter(x_p, y_p, marker = 'o', s = 1.5, color ='b')
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
            
            
    '''Recording Time'''         
    ttime = time.clock()
    if ttime >= 3600: #jam
        jam = int(ttime/3600)
        sisa = ttime - jam*3600
        if sisa == 0:
            print 'total time of processing:', jam, 'hours', 0, 'minutes', 0, 'seconds'
        elif sisa > 60:
            menit = int(sisa/60)
            detik = sisa - menit*60
            if detik == 0:
                print 'total time of processing:', jam, 'hours', menit, 'minutes', 0, 'seconds'
            else:
                print 'total time of processing:', jam, 'hours', menit, 'minutes', detik, 'seconds'
        else:
            print 'total time of processing:', jam, 'hours', 0, 'minutes', sisa, 'seconds'
    elif ttime >= 60: #menit
        menit = int(ttime/60)
        detik = ttime - menit*60
        print 'total time of processing:', 0, 'hours', menit, 'minutes', detik, 'seconds'
    else:
        print 'total time of processing:', 0, 'hours', 0, 'minutes', ttime, 'seconds'
            
        
            
    #print 'total time of processing:', time.clock()
    print '***************************************************'
    print     
        
    set['t'] += set['dt']
    set['k'] += 1
     
print '*************DONE*****************'
print '''All coefficients:'''
print coef
raw_input()
# plt.show(block=True)

