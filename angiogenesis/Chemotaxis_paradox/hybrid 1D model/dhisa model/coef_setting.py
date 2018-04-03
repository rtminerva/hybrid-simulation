from collections import OrderedDict

def declare_coef(): #1
    '''Coefficients''' #
    #to store coefficients
    coef = {}
    set = {}
    sol = {}
    
#     coef['LEGI'] = 'basic'
    coef['LEGI'] = 'ultrasensitive'

    coef['Time'] = 60
    coef['L'] = 50
    coef['l'] = 7.5

    ''''Cell (n)'''
    coef['D_n'] = 0.3#30
    coef['ki_o'] = 100
    
    #kinetics
    coef['k_a'] = 3.3
    coef['l_a'] = 0.2    
    coef['teta_a'] = 10**(-3)
    coef['k_i'] = 2.8
    coef['l_i'] = 0.1
    coef['teta_i'] = 10**(-3) 
    if coef['LEGI'] == 'basic':
        coef['k_A'] = 68
        coef['k_I'] = 160        
    elif coef['LEGI'] == 'ultrasensitive':
        coef['k_A'] = 3
        coef['k_I'] = 1.6
    coef['R_o'] = 2
    coef['K_I'] = 0.01 #specified
    coef['K_A'] = 0.44
    
    '''VEGF (c)'''
    coef['vel'] = -100#10#200*60 #s #velocity of wave
    coef['perio'] = 0#1.5 #period of wave
    coef['A_c'] = 1 #amplitude of wave
    coef['vari'] = 50#0.3#0.05 #variance of wave
    coef['w'] = 1 #number of wave
    coef['shifted'] = -45 #position of first wave coming
    
    '''Spatial and Temporal Meshes Number'''
    ##set dictionaries (fixed: never change)
    coef['X'] = coef['L']
    coef['Y'] = 1
    set['T'] = 0.5 + 0.001 #second
    set['Nt'] = 1000000
    set['h'] = 0.1#2*coef['l']
    set['dt'] = 0.001
    set['Hh'] = set['h']/2
    set['Nx'] = int(coef['X']/set['Hh'])
#     set['Ny'] = int(coef['Y']/set['Hh'])
       
    '''Initial Setting'''
    set['t'] = 0
    set['k'] = 0
       
    '''To store images'''
    ##sol dictionaries (can change)
    sol['p_1'] = 0
    sol['p_2'] = 0
    sol['p_3'] = 0
    sol['p_4'] = 0
    sol['p_5'] = 0
    sol['stop_iter'] = 0
          
    return coef, set, sol