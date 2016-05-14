from collections import OrderedDict

def declare_coef():
    '''Coefficients'''
    #to store coefficients
    coef = {}
    set = {}
    
    ##With Ang2
    coef['Ang2'] = True
      
    ##Endothelial (n)
    coef['Ro'] = 0.16
    coef['D_n'] = 0.00018
    coef['Ki_n'] = 0.4
    coef['Al_n'] = 0.6
    
    ##VEGF (c)
    coef['D_c'] = 0.005
    coef['Nu'] = 0.1
    
    ##Fibronectin (f)
    coef['Beta'] = 0.05
    coef['Gama'] = 0.1 #/5
    
    ##Mural Cell (m)
    coef['D_m'] = 0.009 #0.00018
    coef['Ki_m'] = 0.6
    coef['Al_m'] = 0.4
    
    ##Tie2 with Angiopoietin (T), Ang1 & Ang2
    coef['A_p'] = 0.3#0.3
    coef['B_p'] = 0.3
    coef['Dl'] = 0.2 #0.5
    
    ##Chemotaxis inhibition & Haptotaxis Activation
    coef['Kappa'] = 0.4#0.4#0.4
    coef['Mic'] = 0.4#0.4#0.4

    '''Branching & Mitosis'''
    coef['T_branch'] = 0.078#0.25#
    coef['T_mitosis'] = 0.709
    
    '''Spatial and Temporal Meshes Number'''
    ##set dictionaries tidak pernah berubah
    set['T'] = 10.002
    coef['X'] = 4.4
    coef['Y'] = 4.4
    set['Nt'] = 100000
    set['h'] = 0.02
    
    set['Hh'] = set['h']/2
    set['Nx'] = int(coef['X']/set['Hh'])
    set['Ny'] = int(coef['Y']/set['Hh'])
    set['R_min'] = 0.52/2
    set['R_max'] = coef['X']/2
    
    set['O_x'] = set['Nx']/2*set['Hh']
    set['O_y'] = set['Ny']/2*set['Hh']
    
    '''Initial Setting'''
    set['t'] = 0
    set['k'] = 0
    set['dt'] = 0.002
    set['error'] = 0.02
       
    '''To store solutions'''
    ##sol dictionaries dapat berubah
    sol = {}
    sol['st'] = 0
    sol['tp'] = set['dt']
    sol['matrix_tip'] = 0
    sol['list_tip_movement'] = 0
    sol['life_time_tip'] = 0
    sol['stop_iter'] = 0
    sol['sp_stop'] = 0
    sol['n'] = 0
    sol['c'] = 0
    sol['f'] = 0
    sol['p'] = 0
    sol['m'] = 0
    sol['index_mn'] = 0
    sol['tip_cell'] = 0
    sol['number_ec'] = 0
    sol['MC_per_EC'] = OrderedDict()
    return coef, set, sol