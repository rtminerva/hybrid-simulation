from initial_conditions import initial_prof #2.1
from hybrid import hybrid_tech_c #2.2
from solve_cfT import c_f_T #2.3
from timeit import default_timer as timer

def boolean_1_iter(coef, set, sol, check = 'out'): #2                      
    if set['k'] == 0:
        '''Initial Profile'''
        sol = initial_prof(coef, set, sol) #2.1
    else:                             
        if len(sol['sp_stop']) == len(sol['matrix_tip']):
            sol['stop_iter'] = 100000 #sp_stop harus dicek di setiap movement and branching. karena sudah tidak bergerak lagi yang ada di list ini.
            print 'all looping itself or anastomosis'
            check = 'in'
        else:
            '''2. Branching and Movement''' 
            start1 = timer()  
            sol, n_o = hybrid_tech_c(coef, set, sol) #2.2
            start2 = timer()
            '''Solving c,f,T'''
            sol = c_f_T(coef, set, sol, n_o) #2.3
            start3 = timer()            
        if not check == 'in':
            print 'Hybrid for n time', start2-start1
            print 'Solve c,f,T time', start3-start2
                    
    return sol