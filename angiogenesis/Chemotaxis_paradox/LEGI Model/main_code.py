from initial_conditions import initial_prof #2.1
from solve_system_1d import system_1d #2.3
from timeit import default_timer as timer


def v_1_max(set, sol):
    V_1_max = 0
    for x in range(1,set['Nx'],2):
        cijx = sol['Ki'][x]*(sol['c'][x+1]-sol['c'][x-1])/(set['h'])
        if cijx < 0:
            cijx *= -1
        if cijx > V_1_max:
            V_1_max = cijx
    return V_1_max

def boolean_1_iter(coef, set, sol): #2                      
    if set['k'] == 0:
        '''Initial Profile'''
        sol = initial_prof(coef, set, sol) #2.1
    else:                             
        '''2. Solvng System''' 
        start1 = timer()  
        '''calculate dt'''
        V_1 = v_1_max(set, sol)
        dt_1 = set['h']/V_1
        dt_3 = (set['h'])**2/(2*coef['D_n'])
        
        set['dt'] = min(dt_1,dt_3)
        set['t'] += set['dt']
        print 'dt', set['dt']
        
        '''Solve system'''
        sol = system_1d(coef, set, sol) #2.3
        start2 = timer()            
        print 'Solve system time', start2-start1  
    return sol