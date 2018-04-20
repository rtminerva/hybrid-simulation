from collections import OrderedDict

def declare_coef(): #1
    '''Coefficients'''
    #to store coefficients
    coef = {}
    set = {}
    sol = {}
    
    set['Model'] = 'normal'
#     set['Model'] = 'extension'
    set['Dimension'] = '1D'
#     set['Dimension'] = '2D'

    set['vegf_dep'] = 1
    set['c_init'] = 1
#     set['c_prof'] = 'C1'
#     set['c_prof'] = 'C2'
    
    set['ki_dep'] = 1
    
    '''measurement'''
    r = 0.07 #cm start from surface of spheroid
    T_1 = 86400 #s
    
    ''''Tip (n)'''
    #diffusion
    d_n = 10**(-10) #cm^2s^(-1)  
    coef['D_n'] = d_n*T_1/r**2
#     coef['D_n'] = 1.8*10**(-4) #aubert 
    #chemotaxis
#     ki_n = 2600-750 #cm^2 s^(-1) M^(-1) #stokes 1990
    ki_n = 2600-750 #750 #cm^2 s^(-1) M^(-1) #aubert estimation 650 - 750
    c_o = 10**(-10) #M
    coef['Ki_n'] = ki_n*T_1*c_o/r**2
#     coef['Ki_n'] = 0.133 #aubert
    coef['Ro_n'] = 0#coef['D_n'] #Gaffney
#     coef['Ro_n'] = 0.001

    ##Kinetics
    coef['k_2'] = 0#.83#0.9#7##Gaffney max tip branching OK
    coef['k_3'] = 0#.85#5 #Aubert 0.83 in range tip-tip anastomosis OK
    coef['k_4'] = 0#.85#9#7 #Dyson 0.85 in range tip-stalk anastomosis OK
    
    sol['age'] = 0.25 #Anderson and Chaplain
    coef['C_branc'] = 0.25 #Anderson and Chaplain
    
    ''''Stalk (s)'''
    #diffusion
    d_s = 1.5*10**(-10) #cm^2s^(-1) #nishiyama cell rep murine : stalk > tip (motility)
    coef['D_b'] = d_s*T_1/r**2 
    #tiptaxis
    coef['Ki_b'] = 0.03 #tip-taxis #will be estimated
    
    ##Kinetics
    coef['nu'] = 0.7 #stalk proliferation #1 aubert
    coef['omega'] = 0.7 #stalk-tip proliferation #5 aubert
    coef['beta'] = 9.29 #Dyson stalk-tip saturation point
    coef['k_5'] = 0.01 #0.01 #Anastomosis should be small enough (provide stalk proliferation)
    
    '''VEGF (c)'''
    #diffusion
#     d_c = 2.9*10**(-7) #cm^2s^(-1) #Anderson and Chaplain, Bray
    d_c = 5.6*10**(-10) #aubert estimation 5.6*10**(-9) - 1.4*10**(-8)
#     d_c = 2.8*10**(-8) #miura 2009
    coef['D_c'] = 0#d_c*T_1/r**2
#     coef['D_c'] = 0.01 #aubert
    
    ##Kinetics
    coef['Lam_4'] = 0.1#1.3 #Anderson and Chaplain digestion
    coef['mu5'] = 0.1#0.03 #Maggelasis and Savakis decay #0.5

    '''Spatial and Temporal Meshes Number'''
    ##set dictionaries (fixed: never change)
    coef['X'] = 1
    coef['Y'] = 1
    set['T'] = 5.001
    set['Nt'] = 1000000
    set['rad'] = 0.01/r
    set['h'] = 0.005
    set['dt'] = 0.001
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

    '''For Model Extension'''
    if set['Model'] == 'extension':
        '''Coefficients'''
        '''PDGF-B (p)'''
        coef['D_p'] = 0.008 #Xue diffusion
        coef['mu6'] = 0.5 #NODATA di Xue ngaco? Prolif
        coef['mu7'] = 0.1 #2.4 #Xue decay
        coef['Lam_5'] = 0.1 #NODATAuptake
        
        '''Tie2 (e)'''
        coef['D_e'] = 0.82*10**(-4) #0.82*10**(-2) #NODATA diffusion
        coef['mu8'] = 0.05 #NODATA prolif
        coef['mu9'] = 0.3 #NODATA decay
    
        '''Ang1 (a1)'''
        coef['D_a1'] = 0.82*10**(-4) #Xue diffusion
        coef['mu10'] = 0.06 #Xue43 prolif (Salah anda di paper?)
        coef['mu11'] = 0.48 #Xue decay
        
        '''Ang2 (a2)'''
        coef['D_a2'] = 0.82*10**(-4) #0.82*10**(-2) #Xue16 diffusion
        coef['mu12'] = 0.07#3.744 #Xue43 prolif
        coef['mu13'] = 0.5#0.96 #Xue43 decay
        coef['beta3'] = 0.2 #VEGF critical
        
        '''Kinetic Rate of Tie2, Ang1, Ang2'''
        coef['k1'] = 1 #Xue57/10
        coef['k_1'] = 1.2 #modif #3#Xue57/10
        coef['k2'] = 0.7 #Xue57/10
        coef['k_2'] = 1.2 #Xue57/10
        
        '''Mural (m)'''
        coef['D_m'] = 0.82*10**(-4) #0.008 #Xue
        coef['Ki_m'] = 0.048 #0.0048 #Xue
        coef['mu14'] = 0.3#3 #Xue prolif
        coef['mu15'] = 0.01#1.13 #Xue decay
        
        '''Attached Mural (ma)'''
        coef['Gam'] = 3.5#2.5 #Xue94,115
        coef['mu16'] = 0.5 #0.1 #Xue
        coef['mu17'] = 0.7 #0.3 #Xue

        '''To store Images need???'''
          
    return coef, set, sol