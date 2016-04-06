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
    for noms in range(0,len(sol['matrix_tip'])):         
        if not noms in sol['sp_stop']:
            sp_in.append(noms)
    for tip_o in sp_in:
        for tips in sp_in:
            if tips > tip_o:
                if sol['matrix_tip'][tip_o][-1] == sol['matrix_tip'][tips][-1]:
                    sol['sp_stop'].append(tip_o)
                    sol['list_tip_movement'][tip_o] = 'stop'
    return sol['sp_stop'], sol['list_tip_movement']


def boolean_1_iter(coef, set, sol):
#     iter = 0, hh = 0, Nx = 0, Ny = 0,
#                     r_min = 0, r_max = 0,
#                     ro = 0, d_n = 0, ki_n = 0, al_n = 0,
#                     kappa = 0, mic = 0,
#                     d_c = 0, nu = 0,
#                     be = 0, ga = 0,
#                     d_m = 0, ki_m = 0, al_m = 0, #ro_m = 0,
#                     a_p = 0, b_p = 0, dl = 0,
#                     matrix_tip = 0,
#                     list_tip_movement = 0, life_time_tip = 0,
#                     stop_iter = 0, sp_stop = 0,
#                     n = 0, c = 0, f = 0, tp = 0, m = 0, p = 0, #index_m = 0,
#                     t_branch = 0,
#                     Error = 0, Rec = 0, index_mn = 0
#                     
    h2 = 2*set['Hh']
    O_x = set['Nx']/2*set['Hh']
    O_y = set['Ny']/2*set['Hh']
    
    if set['k'] == 0:
        '''Initial Profile'''
        sol = initial_prof(coef, set, sol, h2, O_x, O_y)  #done
    else:                      
        '''Solving c,f,T'''
        sol = c_f_T(coef, set, sol, h2, O_x, O_y)
        
        '''1. Anastomosis'''
        sol['sp_stop'], sol['list_tip_movement'] = check_anastomosis(sol)
               
        '''2. Branching and Movement'''        
        if len(sol['sp_stop']) == len(sol['matrix_tip']):
            sol['stop_iter'] = 100000 #sp_stop harus dicek di setiap movement and branching. karena sudah tidak bergerak lagi yang ada di list ini.
            print 'all looping itself or anastomosis'
        else:
            sol = hybrid_tech_c(coef, set, sol, h2)
            if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                sol = hybrid_tech_m(coef, set, sol, h2)
        
        print 'Total Tips:', len(sol['matrix_tip'])
        print 'Total Stop Tips:', len(sol['sp_stop'])
        
            
    return sol
    