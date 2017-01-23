from collections import OrderedDict

def declare_coef(): #1
    '''Coefficients'''
    #to store coefficients
    coef = {}
    set = {}
    sol = {}
    
    '''Gradient of h function'''
    #profile 1: \/\
    coef['m1'] = (0.5-1)/(10-2)
    coef['m2'] = (2-0.5)/(20-10)
    coef['m3'] = (0-2)/(40-20)
    
    #profile 2: /
    coef['M'] = (1-0)/(50-2)
       
    ''''Kinetic Coef'''
    coef['k_1'] = 0#.1
    #coef['k_2'] = 0.83#0.25
    #coef['k_3'] = 0.83#.83
    #coef['k_4'] = 0.85#.85
    #coef['k_5'] = 0.25#1#.25 #F
    #coef['beta1'] = 9.29#1
    coef['beta2'] = 0#.3
    
    ''''Tip (n)'''
    coef['C_1'] = 0.00018#0.00035#0.00018 
    coef['C_2'] = 0.00018#0.0001#0.00018
    coef['Ki'] = 0.133#0.38#0.133 
    #coef['Al_n'] = 0
    
    ''''Stalk (b)'''
    coef['vi'] = 0#10
    coef['C_4'] = 0.01
    #coef['mu'] = 5
    #coef['prod'] = 0
    
    '''VEGF (c)'''
    coef['C_3'] = 0#.00018#0.00035
    coef['Nu'] = 0.1
    coef['gama'] = 0#.5

    '''Branching & Mitosis'''
    
    '''Spatial and Temporal Meshes Number'''
    ##set dictionaries (fixed: never change)
    coef['X'] = 1
    set['T'] = 5.002
    set['Nt'] = 100000
    
    set['rad'] = 0.12
    
    set['h'] = 0.005 #0.005 #0.01#
    set['dt'] = 0.001 #0.001
    
    set['Hh'] = set['h']/2
    set['Nx'] = int(coef['X']/set['Hh'])
       
    '''Initial Setting'''
    set['t'] = 0
    set['k'] = 0
       
    '''To store images'''
    ##sol dictionaries (can change)
    sol['stEC'] = 0
    sol['stVEGF'] = 0
    sol['stop_iter'] = 0

    return coef, set, sol