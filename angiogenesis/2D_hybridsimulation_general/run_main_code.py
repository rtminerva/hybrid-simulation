'''Import all files. We run all the files through run_main_code.py'''
from coef_setting import declare_coef #Ref.1
from initial_conditions import initial_prof #Ref.2
import main_code as main #Ref.4
import picture_2d as pic #Ref.5


'''Import additional functions to support calculation and graphics'''
import numpy
from timeit import default_timer as timer 
import time
import matplotlib.pyplot as plt 
plt.ion() #to plot interactively

'''declare coefficients & initial settings'''
coef, set, sol = declare_coef() #Ref.1

'''Initialize functions for k=0 (first iteration), t=0 (initial time)'''
sol = initial_prof(coef, set, sol) #Ref.2
pic.pic_2d(coef,set,sol) #to generate the picture of initial condition #Ref.5
print '''All Coefficients:'''
print coef
print '''All Set'''
print set

'''PRINTING RESULT AS CONTROL'''  
print 'at Time', set['t']
print 'Total Tips:', len(sol['matrix_tip'])
print 'Total Stop Tips:', len(sol['sp_stop'])
print 'Tip Stop:', sol['sp_stop']
print 'Tip Cell Pos:', sol['tip_cell']
print 'Max Value of ct, c', sol['c_t'].max(),',', sol['c'].max()
print 'Min Value of ct, c', sol['c_t'].min(),',', sol['c'].min()

'''Main part of the Hybrid calculation'''
while set['t'] <= set['T']:
    '''Adaptive time step start here''' #Ref.3    
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
                vijx = coef['al_1']*cijx# - coef['be_1']*ctijx
                vijy = coef['al_1']*cijy# - coef['be_1']*ctijy
                
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
    ddt = set['h']**2/(4*(coef['D_n']+set['h']*max_ct))
#     if ddt < set['dtt']:
#         set['dt'] = ddt
#     else:
#         set['dt'] = set['dtt']
    set['dt'] = ddt
    set['t'] += set['dt']
    set['k'] += 1
    '''Adaptive time step end here'''    
    
    '''PRINTING RESULT AS CONTROL'''  
    print 'at Time', set['t']
    print 'max_ct, ddt', max_ct, ddt
    print 'Max Value of ct, c', sol['c_t'].max(),',', sol['c'].max()
    print 'Min Value of ct, c', sol['c_t'].min(),',', sol['c'].min()
    
    '''Solving Hybrid'''
    sol = main.boolean_1_iter(coef, set, sol) #Ref.4    
    
    '''PRINTING RESULT AS CONTROL'''
    print 'Total Tips:', len(sol['matrix_tip'])
    print 'Total Stop Tips:', len(sol['sp_stop'])
    print 'Tip Stop:', sol['sp_stop']
    print 'Tip Cell Pos:', sol['tip_cell']
    
    '''To check the reason of tip cell stopping'''
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
    
    '''Picture result start'''
    if set['k'] % 1 == 0:
        pic.pic_2d(coef,set,sol) #Ref.5
    '''Picture result end'''
        
    '''Recording Time & Coefficients start'''         
#     ttime = time.clock()
#     if ttime >= 3600: #jam
#         jam = int(ttime/3600)
#         sisa = ttime - jam*3600
#         if sisa == 0:
#             print 'total time of processing:', jam, 'hours', 0, 'minutes', 0, 'seconds'
#         elif sisa > 60:
#             menit = int(sisa/60)
#             detik = sisa - menit*60
#             if detik == 0:
#                 print 'total time of processing:', jam, 'hours', menit, 'minutes', 0, 'seconds'
#             else:
#                 print 'total time of processing:', jam, 'hours', menit, 'minutes', detik, 'seconds'
#         else:
#             print 'total time of processing:', jam, 'hours', 0, 'minutes', sisa, 'seconds'
#     elif ttime >= 60: #menit
#         menit = int(ttime/60)
#         detik = ttime - menit*60
#         print 'total time of processing:', 0, 'hours', menit, 'minutes', detik, 'seconds'
#     else:
#         print 'total time of processing:', 0, 'hours', 0, 'minutes', ttime, 'seconds'

    if set['k'] % 100 == 0:
        print '''All Coefficients:'''
        print coef
        print '''All Set'''
        print set
    print 'total time of processing:', time.clock()
    print '***************************************************'
    print 
       
print '*************DONE*****************'
print '''All Coefficients:'''
print coef
print '''All Set'''
print set
raw_input()
# plt.show(block=True)

