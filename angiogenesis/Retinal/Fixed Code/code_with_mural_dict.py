from solve_cfT import c_f_T
from initial_conditions import initial_prof
from initial_m import init_m
from hybrid import hybrid_tech_c
from hybrid2 import hybrid_tech_m

from timeit import default_timer as timer

#import continuous_run as cont
def second_largest(numbers):
    count = 0
    m1 = m2 = float('-inf')
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1            
            else:
                m2 = x
    return m2 if count >= 2 else None

def check_anastomosis(sol):
    #creating list of active tips to be checked if the tip meets
    sp_in = []
    '''Check Anastomosis'''
    for noms in range(0,len(sol['matrix_tip'])):         
        if not noms in sol['sp_stop']:
            sp_in.append(noms)
    for tip_o in sp_in:
        for tips in sp_in:
            if tips > tip_o:
                if sol['matrix_tip'][tip_o][-1] == sol['matrix_tip'][tips][-1]:
                    sol['sp_stop'].append(tip_o)
                    sol['list_tip_movement'][tip_o] = 'stop'
    
    '''TIP CELL'''
    sol['tip_cell'] = []          
    if len(sol['sp_stop']) > 0:               
        for e,tip in enumerate(sol['matrix_tip']):
            if not e in sol['sp_stop']:
                sol['tip_cell'].append([tip[-1][0],tip[-1][1]])
    else:
        for tip in sol['matrix_tip']:
            sol['tip_cell'].append([tip[-1][0],tip[-1][1]])
                
    return sol


def boolean_1_iter(coef, set, sol, check = 'out'):                       
    if set['k'] == 0:
        '''Initial Profile'''
        sol = initial_prof(coef, set, sol)  
    else:                             
        if len(sol['sp_stop']) == len(sol['matrix_tip']):
            sol['stop_iter'] = 100000 #sp_stop harus dicek di setiap movement and branching. karena sudah tidak bergerak lagi yang ada di list ini.
            print 'all looping itself or anastomosis'
            check = 'in'
        else:
            '''2. Branching and Movement''' 
            start1 = timer()  
            sol = hybrid_tech_c(coef, set, sol)
            start2 = timer()
            '''1. Anastomosis & Tip Cell'''
            sol = check_anastomosis(sol)
            start3 = timer()
            if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                #print set['tm'], set['t']
                if set['t'] > set['tm']:
                    #print sol['kk']
                    if sol['kk'] == 1:
                        sol = init_m(coef,set,sol)
                        sol['kk']+= 1
                    else:
                        sol['kk'] = 10
                        #print 'enter here'
                        sol = hybrid_tech_m(coef, set, sol)
                        start4 = timer()
                '''Solving c,f,T'''
                sol = c_f_T(coef, set, sol)
                start5 = timer()            
        if not check == 'in':
            print 'Check Anastomosis Time', start3-start2
            print 'Hybrid for n time', start2-start1
            if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                if sol['kk'] > 2:
                    print 'Hybrid for m time', start4-start3
                    print 'Solve c,f,T time', start5-start4
                else:
                    print 'Solve c,f,T time', start5-start3
            else:
                print 'Solve c,f,T time', start5-start3
                    
    return sol