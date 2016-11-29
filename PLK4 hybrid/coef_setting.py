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
    #set['initial_prof'] = 'rectangular_tip'
    
    #set['c_prof'] = 'C1'
    #set['c_prof'] = 'C2'
    
    #set['f_prof'] = 'F1'
    #set['f_prof'] = 'F2'
    
    #set['parent'] = 'one'   
    #set['parent'] = 'two' 
    
    ##Reaction rate coef
    coef['k_1'] = 0.1
    coef['k_2'] = 0.1
    coef['l_1'] = 0.1
    coef['l_2'] = 0
    
    ##X4
    coef['D4'] = 0.0035
    
    ##X1
    coef['D1'] = 0.0035
    
    ##X2
    coef['D2'] = 0.0035
    
    ##X3
    coef['D3'] = 0.0035
    
    '''Spatial and Temporal Meshes Number'''
    ##set dictionaries tidak pernah berubah
    coef['X'] = 1
    coef['Y'] = 1
    set['T'] = 5.002
    set['Nt'] = 100000
    
    set['con'] = False
    #set['theta'] = 0.5
    #set['rad'] = 0.1
    
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
       
    '''To store solutions'''
    ##sol dictionaries dapat berubah
    sol['num_of_absorbed'] = 0
    sol['tX1'] = 0
    sol['tX2'] = 0
    sol['tX3'] = 0
    sol['tX4'] = 0
    sol['matrix_tip'] = []
    sol['matrix_tip_die'] = []
    #sol['list_tip_movement'] = 0
    #sol['life_time_tip'] = 0
    sol['stop_iter'] = 0
    #sol['sp_stop'] = 0
    #if set['parent'] == 'two':
        #sol['matrix_tip_2'] = 0
        #sol['list_tip_movement_2'] = 0
        #sol['life_time_tip_2'] = 0
        #sol['sp_stop_2'] = 0
        #sol['tip_cell_2'] = 0
        #sol['pp_2'] = {}
    sol['tip_cell'] = []
    sol['pp'] = {}

    return coef, set, sol