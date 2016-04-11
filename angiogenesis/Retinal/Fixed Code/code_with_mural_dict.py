from solve_cfT import c_f_T
from initial_conditions import initial_prof
from hybrid import hybrid_tech_c

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
    #creating list of tips to be checked if the tip meets
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
    if len(sol['sp_stop']) > 0:               
        for e,tip in enumerate(sol['matrix_tip']):
            if not e in sol['sp_stop']:
                sol['tip_cell'].append(tip[-1])
        
    return sol


def boolean_1_iter(coef, set, sol):                       
    if set['k'] == 0:
        '''Initial Profile'''
        sol = initial_prof(coef, set, sol)  #done
    else:
        '''1. Anastomosis & Tip Cell'''
        if set['k'] > 1:
            sol = check_anastomosis(sol)
                              
        '''Solving c,f,T'''
        sol = c_f_T(coef, set, sol)
                       
        '''2. Branching and Movement'''        
        if len(sol['sp_stop']) == len(sol['matrix_tip']):
            sol['stop_iter'] = 100000 #sp_stop harus dicek di setiap movement and branching. karena sudah tidak bergerak lagi yang ada di list ini.
            print 'all looping itself or anastomosis'
        else:
            sol = hybrid_tech_c(coef, set, sol)
            if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                sol = hybrid_tech_m(coef, set, sol)
        
        print 'Total Tips:', len(sol['matrix_tip'])
        print 'Total Stop Tips:', len(sol['sp_stop'])  
                    
    return sol