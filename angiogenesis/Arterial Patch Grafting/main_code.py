from initial_conditions import initial_prof #2.1
from hybrid import hybrid_tech #2.2
from solve_con_fast import system_3d #2.3
from timeit import default_timer as timer

def boolean_1_iter(coef, set, sol): #2                      
    if set['k'] == 0:
        '''Initial Profile'''
        sol = initial_prof(coef, set, sol) #2.1
    else:                             
        '''Solving c,f,T''' 
        start1 = timer()  
        sol = system_3d(coef, set, sol) #2.3
        start2 = timer()
        '''2. Branching and Movement'''
        sol = hybrid_tech(coef, set, sol) #2.2
        start3 = timer()            
        print 'Solve c,f,T time', start2-start1
        print 'Hybrid for n time', start3-start2              
    return sol