from collections import OrderedDict

def declare_coef(): #1
    '''Coefficients'''
    #to store coefficients
    coef = {}
    set = {}
    sol = {}
    
#     '''Gradient of h function'''
#     #profile 1: \/\
#     coef['m1'] = (1.2-1.5)/(50-2)
#     coef['m2'] = (1.5-1.2)/(75-50)
#     coef['m3'] = (1-1.5)/(100-75)
#     
#     #profile 2: /
#     coef['M'] = (1-1.5)/(100-2)
    set['Model'] = 'normal'
#     set['Model'] = 'extension'
    set['Dimension'] = '1D'
#     set['Dimension'] = '2D'
    
#     set['vegf_dep'] = 6
#     set['c_init'] = 0

    set['vegf_dep'] = 1
    set['c_init'] = 0.5
    
    set['ki_dep'] = 1
    
#     set['c_prof'] = 'C1'
#     set['c_prof'] = 'C2'
    
    ''''Tip (n)'''
    coef['D_n'] = 0.00018 #AUBERT, anderson chaplain tip Diffusion OK
    coef['Ki_n'] = 0.33#133 #AUBERT, Stokes Chemotaxis coef (range max) OK
    coef['Ro_n'] = 0.00018#0.0001#8 #AUBERT, Gaffney tip away from stalk OK
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
    set['T'] = 4.001 #
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