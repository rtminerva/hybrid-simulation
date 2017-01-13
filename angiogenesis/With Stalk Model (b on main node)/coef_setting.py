from collections import OrderedDict

def declare_coef(): #1
    '''Coefficients'''
    #to store coefficients
    coef = {}
    set = {}
    sol = {}
    
    set['layout'] = '2D'
    set['initial_prof'] = 'rectangular_tip'
    
    set['con_sep'] = True
    
    set['c_prof'] = 'C1'
    set['parent'] = 'one'   
    
    ##Kinetic Coef
    coef['k_1'] = 0.1#0#.1
    coef['k_2'] = 0.83#0.25
    coef['k_3'] = 0.83#.83
    coef['k_4'] = 0.85#.85
    coef['k_5'] = 0.25#1#.25
    coef['beta1'] = 9.29#1
    coef['beta2'] = 0#.3
    
    ##Tip (n)
    coef['C_1'] = 0.00018#0.00035#0.00018 
    coef['C_2'] = 0.00018#0.0001#0.00018
    coef['Ki'] = 0.133#0.38#0.133 
    coef['Al_n'] = 0
    
    ##Stalk (b)
    coef['vi'] = 1
    coef['mu'] = 5
    coef['prod'] = 0
    coef['anas_tt'] = coef['k_5']*coef['k_3']
    coef['anas_tb'] = coef['k_5']*coef['k_4']
    
    ##VEGF (c)
    coef['C_3'] = 0.00018#0.01#0#0.00018
    coef['Nu'] = 0.1
    coef['gama'] = 0.5#0#0.5

 
    '''Branching & Mitosis'''
    coef['T_branch'] = coef['k_2']#0.25
    #coef['T_mitosis'] = 1000#0.5
    
    '''Spatial and Temporal Meshes Number'''
    ##set dictionaries tidak pernah berubah
    coef['X'] = 1
    coef['Y'] = 1
    set['T'] = 5.002
    set['Nt'] = 100000
    
    set['con'] = False
    #set['theta'] = 0.5
    set['rad'] = 0.1
    
    set['h'] = 0.005 #0.005 #0.01#
    set['dt'] = 0.001 #0.001
    
    set['Hh'] = set['h']/2
    set['Nx'] = int(coef['X']/set['Hh'])
    set['Ny'] = int(coef['Y']/set['Hh'])
    
    if set['layout'] == '3D':
        coef['Z'] = 1
        set['Nz'] = int(coef['Z']/set['Hh'])
    
    '''Initial Setting'''
    set['t'] = 0
    set['k'] = 0
       
    '''To store images'''
    ##sol dictionaries dapat berubah
    sol['stEC'] = 0
    sol['stEC1'] = 0
    sol['stStalk'] = 0
    sol['stVEGF'] = 0
    sol['stVEGF1'] = 0
    #sol['stFb'] = 0
    #sol['matrix_tip'] = 0
    #sol['list_tip_movement'] = 0
    #sol['life_time_tip'] = 0
    sol['stop_iter'] = 0
    #sol['sp_stop'] = 0
    if set['parent'] == 'two':
        #sol['matrix_tip_2'] = 0
        #sol['list_tip_movement_2'] = 0
        #sol['life_time_tip_2'] = 0
        #sol['sp_stop_2'] = 0
        #sol['tip_cell_2'] = 0
        sol['pp_2'] = {}
    #sol['tip_cell'] = 0
    sol['pp'] = {}

    return coef, set, sol