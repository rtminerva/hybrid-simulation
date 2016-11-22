from initial_conditions import initial_prof #2.1
from hybrid import hybrid_tech #2.2
from solve_cfT import c_f_T #2.3

#from solve_cfT_3d import c_f_T_3d
#from hybrid_c_3d import hybrid_tech_c_3d
from timeit import default_timer as timer

def continuous_iter(coef, set, sol):
    if set['k'] == 0:
        '''Initial Profile'''
        sol = initial_prof(coef, set, sol) #2.1
    else:
        '''Solving X1,X2,X3,X4'''
        start1 = timer()
        sol = c_f_T(coef, set, sol) #2.3
        start2 = timer()
        print 'Solve X1,X2,X3,X4 time', start2-start1
    return sol

def boolean_1_iter(coef, set, sol, check = 'out'): #2                      
    if set['k'] == 0:
        '''Initial Profile'''
        sol = initial_prof(coef, set, sol) #2.1
    else:                             
        if len(sol['sp_stop']) == len(sol['matrix_tip']): #???
            sol['stop_iter'] = 100000 
            print 'all is absorbed'
            check == 'in'
        else:
            start1 = timer() 
            '''Solving X1,X2,X3,X4 continuously'''
            sol = c_f_T(coef, set, sol) #2.3
            start2 = timer()      
            
            '''Movement of X4''' 
            sol = hybrid_tech(coef, set, sol) #2.2
            start3 = timer()
                  
        if not check == 'in':
            print 'Hybrid for X4 time', start2-start1
            print 'Solve X1,X2,X3 time', start4-start3
                    
    return sol