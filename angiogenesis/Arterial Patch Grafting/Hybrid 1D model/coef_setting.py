from collections import OrderedDict

def declare_coef(): #1
    '''Coefficients''' #
    #to store coefficients
    coef = {}
    set = {}
    sol = {}

    ''''Cell (n)'''
    coef['D_n'] = 0.0005#0.00018 #AUBERT, anderson chaplain tip Diffusion OK
    coef['Ki_n'] = 0.33#133 #AUBERT, Stokes Chemotaxis coef (range max) OK
    coef['xi'] = 0.00001
    coef['A_n'] = 0.4 #amplitude of n    
    coef['Xi_n'] = 1
    coef['alpha'] =1#20 #first velocity 
    coef['beta'] = 5 #adaptation velocity
    
    '''VEGF (c)'''
    coef['vel'] = 15#10 #velocity of wave
    coef['perio'] = 1.5 #period of wave
    coef['A_c'] = 0.4#0.8 #amplitude of wave
    coef['vari'] = 0.03#0.3#0.05 #variance of wave
    
    '''Spatial and Temporal Meshes Number'''
    ##set dictionaries (fixed: never change)
    coef['X'] = 1
    coef['Y'] = 1
    set['T'] = 0.201 #
    set['Nt'] = 1000000
    set['h'] = 0.005 #0.005 #0.01#
    set['rad'] = 0.12
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
    sol['stEC_1'] = 0
    sol['stEC_2'] = 0
    sol['stEC_3'] = 0
    sol['stEC_4'] = 0
    sol['stEC_5'] = 0
    sol['stop_iter'] = 0
          
    return coef, set, sol