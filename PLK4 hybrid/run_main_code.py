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
    sol = main.boolean_1_iter(coef, set, sol) #2                 
    if sol['stop_iter'] >=100000:
        set['k'] = sol['stop_iter']
    '''PRINTING RESULT AS CONTROL'''  
    print 'at Time', set['t']
    print 'Total X4:', len(sol['matrix_tip'])
    print 'Total X4 die:', len(sol['matrix_tip_die'])
    print 'NILAI X1, X2, X3, X4 Max', sol['X1'].max(),',', sol['X2'].max(),',', sol['X3'].max(),',', sol['X4'].max()
    print 'NILAI X1, X2, X3, X4 Min', sol['X1'].min(),',', sol['X2'].min(),',', sol['X3'].min(),',', sol['X4'].min()
    
    if set['k'] % 10 == 0:
        pic.pic_2d(coef,set,sol) #3
    
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

