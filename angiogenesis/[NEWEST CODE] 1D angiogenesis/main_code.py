from initial_conditions import initial_prof #2.1
from solve_system_1d import system_1d #2.3
from solve_system_2d import system_2d #2.3
from timeit import default_timer as timer

# def vn_conv_max(set, sol, coef):
#     Vn_conv_max = 0
#     v_conv = 0
#     for x in range(1,set['Nx'],2):
#         c_mean = (sol['c'][x+1]+sol['c'][x-1])/2
#         c_grad = (sol['c'][x+1]-sol['c'][x-1])/(set['h'])
#         v_conv = (coef['alpha'] - (coef['beta']*coef['vel']*c_grad/((c_grad)**2+coef['xi'])))*c_grad
#         if v_conv < 0:
#             v_conv *= -1
#         if v_conv > V_conv_max:
#             Vn_conv_max = v_conv  
#             
#     return Vn_conv_max

def boolean_1_iter(coef, set, sol): #2                      
    if set['k'] == 0:
        '''Initial Profile'''
        sol = initial_prof(coef, set, sol) #2.1
    else:                             
        '''2. Solvng System''' 
        start1 = timer()  
#         '''calculate dt'''
#         Vn_conv = vn_conv_max(set, sol, coef)
#         Vb_conv = vb_conv_max(set, sol, coef)
#         print 'V_max', V_conv
#         dt_conv_n = set['h']/(2*Vn_conv)
#         dt_conv_b = set['h']/(2*Vb_conv)
#         dt_diff_n = (set['h'])**2/(2*coef['D_n'])
#         dt_diff_b = (set['h'])**2/(2*coef['D_b'])
#         dt_diff_c = (set['h'])**2/(2*coef['D_c'])
# #         set['dt'] = 0.001
#         set['dt'] = min(dt_diff_n, dt_diff_b, dt_diff_c , dt_conv_n, dt_conv_b)
#         set['t'] += set['dt']
#         sol['time'].append(set['t'])
#         print 'dt', set['dt']
        
        sol['age'] += set['dt']
        if set['Dimension'] == '1D':
            sol = system_1d(coef, set, sol) #2.3
        elif set['Dimension'] == '2D':
            sol = system_2d(coef, set, sol) #2.3
        start2 = timer()            
        print 'Solve system time', start2-start1  
    return sol