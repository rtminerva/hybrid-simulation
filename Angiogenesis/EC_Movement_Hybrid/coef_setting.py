from collections import OrderedDict

def declare_coef(): #1
    '''Coefficients'''
    #to store coefficients
    coef = {}
    set = {}
    sol = {}
    
    '''Grad h function'''
    coef['m1'] = (0.2-0.5)/(50-2)#(0.5-1)/(50-2)
    coef['m2'] = (1-0.2)/(100-50)#(2-0.5)/(100-50)
    coef['m3'] = (0-1)/(200-100)#(0-2)/(200-100)
       
    ''''Kinetic Coef'''
    coef['k_1'] = 0.1#0#.1
    #coef['k_2'] = 0.83#0.25
    #coef['k_3'] = 0.83#.83
    #coef['k_4'] = 0.85#.85
    #coef['k_5'] = 0.25#1#.25
    #coef['beta1'] = 9.29#1
    coef['beta2'] = 0#.3
    
    ''''Tip (n)'''
    coef['C_1'] = 0.00018#0.00035#0.00018 
    coef['C_2'] = 0.00018#0.0001#0.00018
    coef['Ki'] = 0.133#0.38#0.133 
    #coef['Al_n'] = 0
    
    ''''Stalk (b)'''
    #coef['vi'] = 1
    #coef['mu'] = 5
    #coef['prod'] = 0
    #coef['anas_tt'] = coef['k_5']*coef['k_3']
    #coef['anas_tb'] = coef['k_5']*coef['k_4']
    
    '''VEGF (c)'''
    coef['C_3'] = 0.00018#0.01#0#0.00018
    coef['Nu'] = 0.1
    coef['gama'] = 0.5#0#0.5

    '''Branching & Mitosis'''
    
    '''Spatial and Temporal Meshes Number'''
    ##set dictionaries (fixed: never change)
    coef['X'] = 1
    coef['Y'] = 1#
    set['T'] = 10.002
    set['Nt'] = 100000
    
    set['con'] = False
    set['rad'] = 0.1
    
    set['h'] = 0.005 #0.005 #0.01#
    set['dt'] = 0.001 #0.001
    
    set['Hh'] = set['h']/2
    set['Nx'] = int(coef['X']/set['Hh'])
    set['Ny'] = int(coef['Y']/set['Hh'])
       
    '''Initial Setting'''
    set['t'] = 0
    set['k'] = 0
       
    '''To store images'''
    ##sol dictionaries (can change)
    sol['stEC'] = 0
    sol['stVEGF'] = 0
    sol['stop_iter'] = 0
    sol['pp'] = {}

    return coef, set, sol