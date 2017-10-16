from collections import OrderedDict

def declare_coef(): #1
    '''Coefficients'''
    #to store coefficients
    coef = {}
    set = {}
    sol = {}
    

    set['Model'] = 'normal'
    set['Dimension'] = '1D'
#     set['Dimension'] = '2D'
    
#     set['vegf_dep'] = 6
#     set['c_init'] = 0

    set['vegf_dep'] = 1
    set['c_init'] = 0.5
    set['ki_dep'] = 1
    
#     set['c_prof'] = 'C1'
#     set['c_prof'] = 'C2'

    '''Chem sensitivity (Alpha)'''
    coef['A'] = 0.01
    coef['m'] = 2
    coef['f_p'] = 0.5
    coef['f_n'] = 0.5
    
    ''''Tip (n)'''
    coef['D_n'] = 0.00018 #AUBERT, anderson chaplain tip Diffusion OK
    coef['Ki_n'] = 0.33#133 #AUBERT, Stokes Chemotaxis coef (range max) OK
    coef['Ro_n'] = 0.00018#0.0001#8 #AUBERT, Gaffney tip away from stalk OK
    coef['xi'] = 0.1
    
    coef['Xi_n'] = 1
    coef['alpha'] =0.5 #first velocity 
    coef['beta'] = 2 #adaptation velocity
    coef['vel'] = 2#3 #velocity of wave
    coef['perio'] = 0.7 #period of wave
    coef['A_c'] = 0.8 #amplitude of wave
    
    ##Kinetics
    coef['mu1'] = 0.83##AUBERT, Gaffney max tip branching OK
    coef['Lam_1'] = 0.83#5 #AUBERT in range tip-tip anastomosis OK
    coef['Lam_2'] = 0.85#5 #AUBERT in range tip-stalk anastomosis OK
    sol['age'] = 0
    
    ''''Stalk (b)'''
    coef['D_b'] = 0.00018#0.001 #1*10**(-3)#3*10**(-3) #NODATA Stalk diffusion
    coef['Ki_b'] = 0.01 #NODATA tip-taxis
    ##Kinetics
    coef['mu2'] = 7#1 #stalk proliferation 1 self
    coef['mu3'] = 3#03 #stalk-tip proliferation self
    coef['beta1'] = 9.29 #AUBERT, Dyson stalk-tip saturation point OK
    coef['Lam_3'] = 0.001 #Anastomosis should be small enough self
    
    '''VEGF (c)''' ##DONE
    coef['D_c'] = 0.01 #AUBERT diffusion OK
    coef['Lam_4'] = 0.1 #AUBERT, anderson chaplain digestion OK
    coef['mu4'] = 0.1 #AUBERT max proliferation OK
    coef['mu5'] = 0.5 #AUBERT, maggelasis and savakis decay OK
    coef['beta2'] = 0.3 #AUBERT stalk critical point

    '''Spatial and Temporal Meshes Number'''
    ##set dictionaries (fixed: never change)
    coef['X'] = 1
    coef['Y'] = 1
    set['T'] = 2.001 #
    set['Nt'] = 1000000
    set['rad'] = 0.12
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
    sol['stEC_1'] = 0
    sol['stEC_2'] = 0
    sol['stEC_3'] = 0
    sol['stEC_4'] = 0
    sol['stEC_5'] = 0
    sol['stop_iter'] = 0
          
    return coef, set, sol