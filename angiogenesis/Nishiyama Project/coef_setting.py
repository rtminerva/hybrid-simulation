from collections import OrderedDict

def declare_coef():
    '''Coefficients'''
    #to store coefficients
    coef = {}
    set = {}
    sol = {}
    
    set['initial_prof'] = 'rectangular_1_tip'
    #set['initial_prof'] = 'rectangular_tip'
    
    set['c_prof'] = 'C1'
    #set['c_prof'] = 'C2'
    
    set['f_prof'] = 'F1'
    #set['f_prof'] = 'F2'
    
    ##Tip (n)
    coef['D_n'] = 0.00035
    coef['Ki_n'] = 0.38
    coef['Al_n'] = 0.6
    coef['Ro'] = 0.3#0.34
    
    ##VEGF (c)
    coef['D_c'] = 0.00035
    coef['Nu'] = 0.1#1
    coef['Alp_c'] = 5#1
    
    ##ECM Fibronectin (f)
    coef['Beta'] = 0.05#7
    coef['Gama'] = 0.1
    coef['Alp_f'] = 5#1
 
    '''Branching & Mitosis'''
    coef['T_branch'] = 0.25
#     coef['T_mitosis'] = 1000#0.5
    
    '''Spatial and Temporal Meshes Number'''
    ##set dictionaries tidak pernah berubah
    coef['X'] = 1
    coef['Y'] = 1
    set['T'] = 10.002
    set['Nt'] = 100000
    set['theta'] = 0.5
    
    set['h'] = 0.005 #0.01#
    set['dt'] = 0.001
    
    set['Hh'] = set['h']/2
    set['Nx'] = int(coef['X']/set['Hh'])
    set['Ny'] = int(coef['Y']/set['Hh'])
    
    '''Initial Setting'''
    set['t'] = 0
    set['k'] = 0
       
    '''To store solutions'''
    ##sol dictionaries dapat berubah
    sol['stEC'] = 0
    sol['Merge_cn'] = 0
    sol['Merge_cnd'] = 0
    sol['Merge_fn'] = 0
    sol['VEGF'] = 0
    sol['VEGF1'] = 0
    sol['ECM'] = 0
    sol['stop_iter'] = 0
    '''For Anastomosis'''
#     sol['pp'] = {}
#     sol['PP'] = [] 
    sol['backward'] = {}

    return coef, set, sol