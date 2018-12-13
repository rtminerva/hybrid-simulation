from coef_setting import declare_coef #1
import main_code as main #2
import picture_2d as pic #3

import numpy
from timeit import default_timer as timer 
import time
import matplotlib.pyplot as plt 

#declare coefficients & initial settings
coef, set, sol = declare_coef() #1

#to plot interactively
plt.ion()

while set['t'] <= set['T']:
    sol = main.boolean_1_iter(coef, set, sol) #2                 
    '''PRINTING RESULT AS CONTROL start'''  
    print 'at Time', set['t']
    print 'Total Tips:', len(sol['matrix_tip'])
    print 'Total Stop Tips:', len(sol['sp_stop'])
    print 'Tip Stop:', sol['sp_stop']
    print 'Tip Cell Pos:', sol['tip_cell']
    print 'Max Value of c, n', sol['c'].max(),',', sol['n'].max()
    print 'Min Value of c, n', sol['c'].min(),',', sol['n'].min()
#     if set['k'] % 200 == 0:
#         print 'Tip Cell Pos_ave:', sol['tip_cell_pos_ave']
#     for e, i in enumerate(sol['matrix_tip']):
#         if e in sol['sp_stop']:
#             if len(i) > 1:
#                 print 'stop', e, ':',i[-2] , i[-1], ',', sol['cause'][e], ',', 'Length of sprout:', len(i)
#             else:
#                 print 'stop', e, ':',i[-1], ',', sol['cause'][e], ',', 'Length of sprout:', len(i)
#         else:
#             if len(i) > 1:
#                 print 'RUN', e, ':',i[-2] , i[-1], ',', 'Length of sprout:', len(i)
#             else:
#                 print 'RUN', e, ':',i[-1], ',', 'Length of sprout:', len(i)
#     print 'Backward at time step:', sol['backward_count']
    '''PRINTING RESULT AS CONTROL end'''
    
    '''Picture result start'''
    if set['k'] % 1 == 0:
        pic.pic_2d(coef,set,sol) #3
    '''Picture result end'''
        
    '''Recording Time & Coefficients start'''         
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
        print '''All Coefficients:'''
        print coef
        print '''All Set'''
        print set
    print 'total time of processing:', time.clock()
    print '***************************************************'
    print 
    
    '''Adaptive time step start'''    
    max_ct = 0
    for yb in range(1,set['Ny'],2):
        for xb in range(1,set['Nx'],2):
            cijx = (sol['c'][xb+1,yb+1]-sol['c'][xb-1,yb+1]+sol['c'][xb+1,yb-1]-sol['c'][xb-1,yb-1])/(2*set['h'])
            cijy = (sol['c'][xb+1,yb+1]-sol['c'][xb+1,yb-1]+sol['c'][xb-1,yb+1]-sol['c'][xb-1,yb-1])/(2*set['h'])
            
            ctijx = (sol['c_t'][xb+1,yb+1]-sol['c_t'][xb-1,yb+1]+sol['c_t'][xb+1,yb-1]-sol['c_t'][xb-1,yb-1])/(2*set['h'])
            ctijy = (sol['c_t'][xb+1,yb+1]-sol['c_t'][xb+1,yb-1]+sol['c_t'][xb-1,yb+1]-sol['c_t'][xb-1,yb-1])/(2*set['h'])
            
            ave_ct = (sol['c_t'][xb-1,yb-1] + sol['c_t'][xb+1,yb+1] + sol['c_t'][xb-1,yb+1] + sol['c_t'][xb+1,yb-1])/4
            if ave_ct > 0:
                vijx = coef['al_1']*cijx - coef['be_1']*ctijx
                vijy = coef['al_1']*cijy - coef['be_1']*ctijy
            else:
                vijx = coef['al_1']*cijx
                vijy = coef['al_1']*cijy
                
            if vijx <=0:
                vijx_m = max(0,-vijx)
            elif vijx >0:
                vijx_m = max(0,vijx)
                
            if vijy <=0:
                vijy_m = max(0,-vijy)
            elif vijy >0:
                vijy_m = max(0,vijy)   
            
            if vijx_m >= vijy_m:
                vv = vijx_m
            else:
                vv = vijy_m
            
            if vv > max_ct:
                max_ct = vv
    ddt = set['h']**2/(4*(coef['D_n']+set['h']*coef['be_1']*max_ct))
#     if ddt > set['dt']:
#         set['t'] += set['dt']
#     else:
    set['t'] += ddt
    set['k'] += 1
    print 'max_ct, ddt', max_ct, ddt
    '''Adaptive time step end'''
     
print '*************DONE*****************'
print '''All Coefficients:'''
print coef
print '''All Set'''
print set
raw_input()
# plt.show(block=True)

