from solve_cfT import c_f_T
from initial_conditions import initial_prof
from continuous_n import continuous_n_
from timeit import default_timer as timer

def con_(coef, set, sol, check = 'out'):                       
    if set['k'] == 0:
        '''Initial Profile'''
        sol = initial_prof(coef, set, sol)  
    else:
        '''Solving n'''
        sol = continuous_n_(coef, set, sol)
              
        '''Solving c,f,T'''
        if set['layout'] == '2D':
            sol = c_f_T(coef, set, sol)
        if set['layout'] == '3D':
            sol = c_f_T_3d(coef, set, sol)
                    
    return sol