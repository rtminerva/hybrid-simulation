from collections import OrderedDict

def declare_coef(): #1
    '''Coefficients''' #
    coef = {}
    set = {}
    sol = {}
    
#     coef['C_prof'] = 'exp'
    coef['C_prof'] = 'step'
#     coef['C_prof'] = 'tan'
    
#     coef['LEGI'] = 'basic'
    coef['LEGI'] = 'ultrasensitive'
    
    #kinetics
    ff = 1
    coef['k_a'] = ff*5#3.3 #5
    coef['l_a'] = ff*0.2 #0.2   
#     coef['teta_a'] = ff*10**(-3)
    coef['k_i'] = ff*2.8
    coef['l_i'] = ff*0.1 #0.1
#     coef['teta_i'] = ff*10**(-3) 
    if coef['LEGI'] == 'basic':
        coef['k_A'] = 3#3#68
        coef['k_I'] = 1.6#1.6#160        
    elif coef['LEGI'] == 'ultrasensitive':
        coef['k_A'] = 3
        coef['k_I'] = 1.6
    coef['R_o'] = 2
    coef['K_I'] = ff*0.01 #0.1#0.01 
    coef['K_A'] = ff*0.44
    
    '''VEGF (c)'''
    coef['vel'] = 1 #velocity of wave
    coef['A_c'] = 1 #amplitude of wave
    coef['vari'] = 1#1000 #1 #600 #variance of wave

    
    '''Spatial and Temporal Meshes Number'''
    ##set dictionaries (fixed: never change)
    set['T'] = 800 + 0.001 #second #100 #300 # 800
    set['delay1'] =200 #5 #90
    set['delay2'] =400
    set['Nt'] = 1000000
    set['dt'] = 0.01
       
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