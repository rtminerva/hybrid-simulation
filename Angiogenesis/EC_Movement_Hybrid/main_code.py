from initial_conditions import initial_prof #2.1
from hybrid import hybrid_tech #2.2
from solve_cfT import c_f_T #2.3
from timeit import default_timer as timer

def boolean_1_iter(coef, set, sol): #2                      
    if set['k'] == 0:
        '''Initial Profile'''
        sol = initial_prof(coef, set, sol) #2.1
    else:                             
        '''2. Branching and Movement''' 
        start1 = timer()  
        sol= hybrid_tech(coef, set, sol) #2.2
        start2 = timer()
        '''Solving c,f,T'''
        sol = c_f_T(coef, set, sol) #2.3
        start3 = timer()            
        print 'Hybrid for n time', start2-start1
        print 'Solve c,f,T time', start3-start2
                    
    return sol