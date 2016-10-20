from collections import OrderedDict

def declare_coef(): #1
    '''Coefficients'''
    #to store coefficients
    coef = {}
    set = {}
    sol = {}
    
    set['layout'] = '2D'
    #set['layout'] = '3D'
    
    #set['initial_prof'] = 'rectangular_1_tip'
    set['initial_prof'] = 'rectangular_tip'
    
    set['c_prof'] = 'C1'
    #set['c_prof'] = 'C2'
    
    #set['f_prof'] = 'F1'
    #set['f_prof'] = 'F2'
    
    set['parent'] = 'one'   
    #set['parent'] = 'two' 
    
    ##Tip (n)
    coef['D_n'] = 0.00035
    coef['Ki_n'] = 0.38
    coef['Al_n'] = 0#0.6
    #coef['Ro'] = 0.3#0.34
    
    ##Stalk (b)
    coef['Si'] = 0.0001
    
    ##VEGF (c)
    #coef['D_c'] = 0.00035
    coef['Nu'] = 0.1
    
    ##ECM Fibronectin (f)
    #coef['Beta'] = 0#.05#7
    #coef['Gama'] = 0.1
 
    '''Branching & Mitosis'''
    coef['T_branch'] = 1000#0.25
    #coef['T_mitosis'] = 1000#0.5
    
    '''Spatial and Temporal Meshes Number'''
    ##set dictionaries tidak pernah berubah
    coef['X'] = 1
    coef['Y'] = 1
    set['T'] = 100.002
    set['Nt'] = 100000
    
    set['con'] = False
    set['theta'] = 0.5
    
    set['h'] = 0.005 #0.01#
    set['dt'] = 0.001
    
    set['Hh'] = set['h']/2
    set['Nx'] = int(coef['X']/set['Hh'])
    set['Ny'] = int(coef['Y']/set['Hh'])
    
    if set['layout'] == '3D':
        coef['Z'] = 1
        set['Nz'] = int(coef['Z']/set['Hh'])
    
    '''Initial Setting'''
    set['t'] = 0
    set['k'] = 0
       
    '''To store solutions'''
    ##sol dictionaries dapat berubah
    sol['stEC'] = 0
    sol['stStalk'] = 0
    sol['stVEGF'] = 0
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