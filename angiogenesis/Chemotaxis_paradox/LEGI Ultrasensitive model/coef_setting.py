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
    
    ff = 1
    
    #kinetics
    coef['k_a'] = ff*3.3
    coef['l_a'] = ff*0.2    
    coef['teta_a'] = ff*10**(-3)
    coef['k_i'] = ff*2.8
    coef['l_i'] = ff*0.1
    coef['teta_i'] = ff*10**(-3) 
    if coef['LEGI'] == 'basic':
        coef['k_A'] = 68
        coef['k_I'] = 160        
    elif coef['LEGI'] == 'ultrasensitive':
        coef['k_A'] = 3
        coef['k_I'] = 1.6
    coef['R_o'] = 2
    coef['K_I'] = ff*0.1 #specified
    coef['K_A'] = ff*0.44
    
    '''VEGF (c)'''
    coef['vel'] = 0.5#-115/60#10#200*60 #s #velocity of wave
    coef['perio'] = 0#1.5 #period of wave
    coef['A_c'] = 1 #amplitude of wave
    coef['vari'] = 1000#*15000#0.3#0.05 #variance of wave
    coef['w'] = 1 #number of wave
    coef['shifted'] = -1000 #position of first wave coming
    
    '''Spatial and Temporal Meshes Number'''
    ##set dictionaries (fixed: never change)
    set['T'] = 1500 + 0.001 #second
    set['delay'] = -300
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