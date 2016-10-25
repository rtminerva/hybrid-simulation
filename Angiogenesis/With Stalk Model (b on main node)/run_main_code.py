from coef_setting import declare_coef #1
import main_code as main #2
#import main_code_con as main2
import picture_2d as pic #3
#from picture_2d_con import pic_2d
#from picture_3d import pic_3d

import numpy
from timeit import default_timer as timer 
import time
import matplotlib.pyplot as plt 

#declare coefficients & initial settings
coef, set, sol = declare_coef() #1

#to plot interactively
plt.ion()

while set['t'] <= set['T'] and set['k'] < set['Nt']:
    if set['con'] == True:
        sol = main.continuous_iter(coef, set, sol)
        '''PRINTING RESULT AS CONTROL'''
        print 'at Time', set['t']
        if not coef['Si'] == 0:
            print 'NILAI C, b MAX', sol['c'].max(),',', sol['b'].max()
            print 'NILAI C, b MIN', sol['c'].min(),',', sol['b'].min()
    else:
        sol = main.boolean_1_iter(coef, set, sol) #2                 
        
        if sol['stop_iter'] >=100000:
            set['k'] = sol['stop_iter']
        '''PRINTING RESULT AS CONTROL'''  
        print 'at Time', set['t']
        print 'Total Tips:', len(sol['matrix_tip'])
        print 'Total Stop Tips:', len(sol['sp_stop'])
        if not coef['Si'] == 0:
            print 'NILAI C, b MAX', sol['c'].max(),',', sol['b'].max()
            print 'NILAI C, b MIN', sol['c'].min(),',', sol['b'].min()
        else:
            print 'NILAI C MAX', sol['c'].max()
            print 'NILAI C MIN', sol['c'].min()
        #print sol['tip_cell']
    
    if set['con'] == True:
        #SAVING PICTURES   
        if set['k'] % 10 == 0:
            if set['layout'] == '2D':
                pic.pic_2d_con(coef,set,sol)
    else:
        #SAVING PICTURES    
        if set['k'] % 50 == 0:
            if set['layout'] == '2D':
                pic.pic_2d(coef,set,sol) #3
            if set['layout'] == '3D':
                pic_3d(coef,set,sol)
    
        
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
print '''All Coefficients:'''
print coef
print '''All Set'''
print set
raw_input()
# plt.show(block=True)

