import main_code as main
from coef_setting import declare_coef
import numpy

from timeit import default_timer as timer 
import time
import matplotlib.pyplot as plt 
from picture_2d import pic_2d
from picture_3d import pic_3d
#declare coefficients & initial settings
coef, set, sol = declare_coef()

#to plot interactively
plt.ion()

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
    print 'NILAI C, F MAX', sol['c'].max(),',', sol['f'].max()
    print 'NILAI C, F MIN', sol['c'].min(),',', sol['f'].min()
    #print sol['tip_cell']
       
    print 'process time of Hybrid:', start2-start1

    '''SAVING PICTURES'''    
    if set['k'] % 1 == 0:
        if set['layout'] == '2D':
            pic_2d(coef,set,sol)
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

