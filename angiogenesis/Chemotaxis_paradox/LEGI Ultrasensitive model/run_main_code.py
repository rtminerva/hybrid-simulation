from coef_setting import declare_coef #1
import main_code as main #2
import picture_1d as pic_1d #3

import numpy
from timeit import default_timer as timer 
import time
import matplotlib.pyplot as plt 
# from mpmath.functions.rszeta import coef

#declare coefficients & initial settings
coef, set, sol = declare_coef() #1 

#test
#to plot interactively
plt.ion()

while set['t'] <= set['T'] and set['k'] < set['Nt']:
    sol = main.boolean_1_iter(coef, set, sol) #2                 
    if sol['stop_iter'] >=100000:
        set['k'] = sol['stop_iter']
    '''PRINTING RESULT AS CONTROL'''  
    print 'at Time', set['t']
    print 'S', sol['c'][-1]
    print 'A,I,Q', sol['A'][-1],sol['I'][-1],sol['Q'][-1]
    print 'F,G', sol['F_Ki'][-1], sol['G_Ki'][-1]
    print 'R', sol['Ki'][-1]
    print 'Q(R)', sol['Qr'][-1]
        
    '''Picture'''
    gg = int((set['T'] - 0.001)/set['dt'])
    if set['k'] % gg == 0:
        pic_1d.pic_1d(coef,set,sol) #3

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

    if set['k'] % 100 == 0:
        print set
        print coef
    #print 'total time of processing:', time.clock()
    print '***************************************************'
    print     
    set['k'] += 1
     
print '*************DONE*****************'
print '''All Coefficients:'''
print coef
print '''All Set'''
print set
raw_input()
# plt.show(block=True)

