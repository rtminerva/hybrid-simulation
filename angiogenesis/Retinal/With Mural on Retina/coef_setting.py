from collections import OrderedDict

def declare_coef():
    '''Coefficients'''
    #to store coefficients
    coef = {}
    set = {}
    sol = {}
    
    '''measurement'''
    ra = 0.07
    x = ra*2 #cm start from surface of spheroid
    y = ra*2
    T_1 = 86400 #s
    
    ##tip cell (n)
    #diffusion
    d_n = 10**(-10) #cm^2s^(-1)  
    coef['D_n'] = d_n*T_1/(ra**2+ra**2)
    #chemotaxis
#     ki_n = 2600-750 #cm^2 s^(-1) M^(-1) #stokes 1990
    ki_n = 650 #cm^2 s^(-1) M^(-1) #aubert estimation 650 - 750
    c_o = 10**(-10) #M
    coef['Ki_n'] = ki_n*T_1*c_o/(ra**2+ra**2)
#     coef['Ki_n'] = 0.133 #aubert
    coef['Al_n'] = 0#.6
    
    ##VEGF (c)
    #diffusion
#     d_c = 2.9*10**(-7) #cm^2s^(-1) #Anderson and Chaplain, Bray
    d_c = 5.6*10**(-10) #aubert estimation 5.6*10**(-9) - 1.4*10**(-8)
#     d_c = 2.8*10**(-8) #miura 2009
    coef['D_c'] = d_c*T_1/(ra**2+ra**2)
#     coef['D_c'] = 0.01 #aubert

    coef['Nu'] = 1#1
    coef['lam'] = 0.05#1
    
    ##Chemotaxis inhibition & Haptotaxis Activation
    coef['Kappa'] = 0#.4
    coef['Mic'] = 0#.4
    
    if not coef['Kappa'] == 0 or not coef['Mic'] == 0:
        ##With Ang2
        coef['Ang2'] = False
        
        ##Mural Cell (m)
        coef['D_m'] = 0.00018 #0.009
        coef['Ki_m'] = 0.6
        coef['Al_m'] = 0#.4
        
        ##Tie2 with Angiopoietin (T), Ang1 & Ang2
        coef['A_p'] = 0.03#0.3
        coef['B_p'] = 0.03
        coef['Dl'] = 0.2 #0.5

    '''Branching & Mitosis'''
    coef['T_branch'] = 0.25 #0.078#
    #coef['T_mitosis'] = 0.709
    
    '''Setting layout1''' #==> changes initial prof of m
    set['layout'] = 'retina'
    
    '''Setting layout2''' ##==> changes initial prof of m
#     set['layout'] = 'rectangular'
    

    '''Spatial and Temporal Meshes Number'''
    ##set dictionaries tidak pernah berubah
    set['T'] = 5.002
    set['Nt'] = 100000
    
    if set['layout'] == 'retina':
        coef['X'] = 2
        coef['Y'] = 2
        set['h'] = 0.005
        set['R_min'] = 0.01/ra
        set['error'] = 0.005
        set['dt'] = 0.001
        set['O_x'] = set['Nx']/2*set['Hh']
        set['O_y'] = set['Ny']/2*set['Hh']
        set['initial_prof'] = 'retina_tip'
#         set['initial_prof'] = 'retina_1_tip'
            
    if set['layout'] == 'rectangular':
        coef['X'] = 1
        coef['Y'] = 1
        set['h'] = 0.01
        set['dt'] = 0.001
        set['initial_prof'] = 'rectangular_tip'
#         set['initial_prof'] = 'rectangular_1_tip'
    
    set['Hh'] = set['h']/2
    set['Nx'] = int(coef['X']/set['Hh'])
    set['Ny'] = int(coef['Y']/set['Hh'])
    
    '''Initial Setting'''
    set['t'] = 0
    set['k'] = 0
    set['tm'] = 0 #munculnya m cells
       
    '''To store solutions'''
    ##sol dictionaries dapat berubah
    sol['stEC'] = 0
    sol['stVEGF'] = 0
#     sol['stFb'] = 0
    sol['tp'] = set['dt']
    sol['inner_bound_tip'] = 0
    sol['matrix_tip'] = 0
    sol['list_tip_movement'] = 0
    sol['life_time_tip'] = 0
    sol['stop_iter'] = 0
    sol['sp_stop'] = 0
    sol['n'] = 0
    sol['c'] = 0
#     sol['f'] = 0
    sol['tip_cell'] = 0
    if not coef['Kappa'] == 0 or not coef['Mic'] == 0:
        #set['initial_m'] = 'retina_tip'
        #set['initial_m'] = 'retina__1_tip'
        set['initial_m'] = 'rectangular_tip'
        #set['initial_m'] = 'rectangular_1_tip'
        
        if set['initial_prof'] == 'retina_1_tip' or set['initial_prof'] == 'rectangular_1_tip':
            sol['stEC_MC_dist'] = 0
        sol['stEC_MC'] = 0
        sol['stEC_MC_full'] = 0
        sol['stMC'] = 0
        sol['stMC_on_EC'] = 0
        sol['stTie2'] = 0
        sol['stPercentage_MC_on_EC'] = 0
        sol['p'] = 0
        sol['m'] = 0
        sol['kk'] = 1
        sol['index_mn'] = 0
        sol['MC_per_EC'] = OrderedDict()
    return coef, set, sol