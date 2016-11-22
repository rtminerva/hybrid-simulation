from initial_conditions import initial_prof #2.1
from hybrid import hybrid_tech_c #2.2
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
        if set['layout'] == '2D':
            start1 = timer()
            sol = c_f_T(coef, set, sol) #2.3
            start2 = timer()
        print 'Solve X1,X2,X3 time', start2-start1
    return sol

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
            if set['layout'] == '2D':
                sol, n_o = hybrid_tech_c(coef, set, sol) #2.2
            if set['layout'] == '3D':
                sol = hybrid_tech_c_3d(coef, set, sol)
            start2 = timer()
            '''1. Anastomosis & Tip Cell'''
            #sol = check_anastomosis(sol)
            start3 = timer()
            '''Solving c,f,T'''
            if set['layout'] == '2D':
                sol = c_f_T(coef, set, sol, n_o) #2.3
            if set['layout'] == '3D':
                sol = c_f_T_3d(coef, set, sol)
            start4 = timer()            
        if not check == 'in':
            print 'Check Anastomosis Time', start3-start2
            print 'Hybrid for n time', start2-start1
            print 'Solve c,f,T time', start4-start3
                    
    return sol