from initial_conditions import initial_prof #2.1
from solve_system_1d import system_1d #2.3
from solve_system_2d import system_2d #2.3
from timeit import default_timer as timer

def boolean_1_iter(coef, set, sol): #2                      
    if set['k'] == 0:
        '''Initial Profile'''
        sol = initial_prof(coef, set, sol) #2.1
    else:                             
        '''2. Solvng System''' 
        start1 = timer()  
        sol['age'] += set['dt']
        if set['Dimension'] == '1D':
            sol = system_1d(coef, set, sol) #2.3
        elif set['Dimension'] == '2D':
            sol = system_2d(coef, set, sol) #2.3
        start2 = timer()            
        print 'Solve system time', start2-start1  
    return sol