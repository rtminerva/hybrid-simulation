from collections import OrderedDict

def declare_coef():
    '''Coefficients'''
    #to store coefficients
    coef = {}
    set = {}
    sol = {}
    
    set['layout'] = '2D'
    set['initial_prof'] = 'rectangular_1_tip'
    
    ##Tip (n)
    coef['D_n'] = 2.6*10**(-4)
    coef['Ki_n'] = 0.5616
    coef['Al_n'] = 0
    
    ##VEGF (c)
    coef['D_c'] = 2.6*10**(-4)
    coef['Nu'] = 0.1
    
    ##ECM Fibronectin (f)
    #coef['Beta'] = 0.05
    #coef['Gama'] = 0.085
 
    '''Branching & Mitosis'''
    coef['T_branch'] = 0.75
    
    '''Spatial and Temporal Meshes Number'''
    ##set dictionaries tidak pernah berubah
    coef['X'] = 1
    coef['Y'] = 1
    set['T'] = 10.002
    set['Nt'] = 100000
    
    set['h'] = 0.01
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
    sol['stVEGF'] = 0
    sol['matrix_tip'] = 0
    sol['list_tip_movement'] = 0
    sol['life_time_tip'] = 0
    sol['stop_iter'] = 0
    sol['sp_stop'] = 0
    sol['n'] = 0
    sol['c'] = 0
    sol['tip_cell'] = 0

    return coef, set, sol