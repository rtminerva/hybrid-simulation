from coef_setting import declare_coef #1
import main_code as main #2
import picture_1d as pic_1d #3
import picture_2d as pic_2d

import numpy
from timeit import default_timer as timer 
import time
import matplotlib.pyplot as plt 
# from mpmath.functions.rszeta import coef

#declare coefficients & initial settings
coef, set, sol = declare_coef() #1 

#to plot interactively
plt.ion()


while set['vegf_dep'] > 0:
    while set['t'] <= set['T'] and set['k'] < set['Nt']:
        sol = main.boolean_1_iter(coef, set, sol) #2                 
        if sol['stop_iter'] >=100000:
            set['k'] = sol['stop_iter']
        '''PRINTING RESULT AS CONTROL'''  
        print 'at Time', set['t']
    #     print 'Total Tips:', len(sol['matrix_tip'])
    #     print 'Total Stop Tips:', len(sol['sp_stop'])
        '''Model extension'''
        if set['Model'] == 'extension':
            print 'Max Value of c, b, n', sol['c'].max(),',', sol['b'].max(),',', sol['n'].max()
            print 'Min Value of c, b, n', sol['c'].min(),',', sol['b'].min(),',', sol['n'].min()
            print '******======******'
            print 'Max Value of p, e, a1, a2, r1, r2, m, ma', sol['p'].max(),',', sol['e'].max(),',', sol['a1'].max(),',', sol['a2'].max(),',', sol['r1'].max(),',', sol['r2'].max(),',', sol['m'].max(),',', sol['ma'].max()
            print 'Min Value of p, e, a1, a2, r1, r2, m, ma', sol['p'].min(),',', sol['e'].min(),',', sol['a1'].min(),',', sol['a2'].min(),',', sol['r1'].min(),',', sol['r2'].min(),',', sol['m'].min(),',', sol['ma'].min()
        else:
            print 'c_init', set['c_init']
            print 'Max Value of c, b, n', sol['c'].max(),',', sol['b'].max(),',', sol['n'].max()
            print 'Min Value of c, b, n', sol['c'].min(),',', sol['b'].min(),',', sol['n'].min()
          
        if set['k'] % 100 == 0:
            if set['Dimension'] == '1D':
                pic_1d.pic_1d(coef,set,sol) #3
            elif set['Dimension'] == '2D':
                pic_2d.pic_2d(coef,set,sol) #3
    
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
    #     print sol['matrix_tip'][-1][-1], sol['tip_cell']
    #     print 'b sol not zero'
    #     for y in range(1,set['Ny'],2):
    #         for x in range(1,set['Nx'],2):
    #             if sol['b'][x,y] != 0:
    #                 print 'pos:[',x,',',y,']',',value:',sol['b'][x,y]
        if set['k'] % 100 == 0:
            print set
            print coef
        #print 'total time of processing:', time.clock()
        print '***************************************************'
        print     
            
        set['t'] += set['dt']
        set['k'] += 1
    set['vegf_dep'] -= 1
    set['c_init'] += 0.2
    set['t'] = 0
    set['k'] = 0
     
print '*************DONE*****************'
print '''All Coefficients:'''
print coef
print '''All Set'''
print set
raw_input()
# plt.show(block=True)

