from initial_conditions import initial_prof #2.1
from solve_system_1d import system_1d #2.3
from timeit import default_timer as timer
import math as m

# def v_2_max(set, sol, coef):
#     V_2_max = 0
#     for x in range(1,set['Nx'],2):
#         a1 = (sol['c'][x+1]-sol['c'][x-1])/(set['h'])
#         a2 = a1**2
#         A = (sol['c'][x+1]+sol['c'][x-1])/2*a1/(a2+coef['xi'])#*sol['n'][x]
#         
#         if A < 0:
#             A *= -1
#         if A > V_2_max:
#             V_2_max = A
#     return V_2_max

def v_conv_max(set, sol, coef):
    V_conv_max = 0
    v_conv = 0
    n_p = sol['n'][-1]
      
#     '''Method c_t = cn'''
#     n_bool = 0
#     for x in range(1,set['Nx'],2):
#         if x == n_p:
#             n_bool = 1
#         c_mean = (sol['c'][x+1]+sol['c'][x-1])/2
#         c_grad = (sol['c'][x+1]-sol['c'][x-1])/(set['h'])
#         v_conv = (coef['alpha'] - (coef['beta']*n_bool*c_mean/((c_grad)**2+coef['xi'])))*c_grad
#         if v_conv < 0:
#             v_conv *= -1
#         if v_conv > V_conv_max:
#             V_conv_max = v_conv
    
    '''Method c_t = -w c_x'''
    for x in range(1,set['Nx'],2):
        c_mean = (sol['c'][x+1]+sol['c'][x-1])/2
        c_grad = (sol['c'][x+1]-sol['c'][x-1])/(set['h'])
        v_conv = (coef['alpha'] - (coef['beta']*coef['vel']*c_grad/((c_grad)**2+coef['xi'])))*c_grad
        if v_conv < 0:
            v_conv *= -1
        if v_conv > V_conv_max:
            V_conv_max = v_conv  
             
#     '''Method c_t = f_derivative'''  
#     for x in range(1,set['Nx'],2):
#         c_t_f = 0
#         c_grad = (sol['c'][x+1]-sol['c'][x-1])/(set['h'])
#         for i in range(0,100):
#             c_t_f += 2*coef['A_c']*(x*set['Hh']+i*coef['perio']-coef['vel']*set['t'])/coef['vari']*m.exp(-(x*set['Hh']+i*coef['perio']-coef['vel']*set['t'])**2/coef['vari'])
#         v_conv = (coef['alpha']-coef['beta']*c_t_f/((c_grad)**2+coef['xi']))*c_grad  
#         if v_conv < 0:
#             v_conv *= -1
#         if v_conv > V_conv_max:
#             V_conv_max = v_conv 
    
#     print V_conv_max
    return V_conv_max

def boolean_1_iter(coef, set, sol): #2                      
    if set['k'] == 0:
        '''Initial Profile'''
        sol = initial_prof(coef, set, sol) #2.1
        sol['time'] = [0]
    else:                             
        start1 = timer()  
        set['t'] += set['dt']
        sol['time'].append(set['t'])
        print 'time', set['t']
        
        '''Solve system'''
        sol = system_1d(coef, set, sol) #2.3
        start2 = timer()            
        print 'Solve system time', start2-start1  
    return sol