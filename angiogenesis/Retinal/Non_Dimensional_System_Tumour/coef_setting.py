from collections import OrderedDict

def declare_coef():
    '''Coefficients'''
    #to store coefficients
    coef = {}
    set = {}
    sol = {}
    
    set['layout'] = '2D'
    #set['initial_prof'] = 'rectangular_1_tip'
    set['initial_prof'] = 'rectangular_tip'
    #set['c_prof'] = 'C1'
    set['c_prof'] = 'C2'
    
    ##Tip (n)
    coef['D_n'] = 0.00035
    coef['Ki_n'] = 0.38
    coef['Al_n'] = 0#.6
    
    ##VEGF (c)
    coef['D_c'] = 0.00035
    coef['Nu'] = 0.1
    
    ##ECM Fibronectin (f)
    #coef['Beta'] = 0.05
    #coef['Gama'] = 0.1
 
    '''Branching & Mitosis'''
    coef['T_branch'] = 0.25
    
    '''Spatial and Temporal Meshes Number'''
    ##set dictionaries tidak pernah berubah
    coef['X'] = 1
    coef['Y'] = 1
    set['T'] = 10.002
    set['Nt'] = 100000
    
    set['h'] = 0.005
    set['dt'] = 0.002
    
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
    sol['stVEGF'] = 0
    sol['matrix_tip'] = 0
    sol['list_tip_movement'] = 0
    sol['life_time_tip'] = 0
    sol['stop_iter'] = 0
    sol['sp_stop'] = 0
    sol['n'] = 0
    sol['c'] = 0
    sol['tip_cell'] = 0
    sol['pp'] = {}

    return coef, set, sol