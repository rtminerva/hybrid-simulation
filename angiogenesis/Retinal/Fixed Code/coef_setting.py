from collections import OrderedDict

def declare_coef():
    '''Coefficients'''
    #to store coefficients
    coef = {}
    set = {}
    sol = {}
    
    ##Endothelial (n)
    coef['Ro'] = 0.16
    coef['D_n'] = 0.00018
    coef['Ki_n'] = 0.4
    coef['Al_n'] = 0.6
    
    ##VEGF (c)
    coef['D_c'] = 0.005
    coef['Nu'] = 0.1
    
    ##Fibronectin (f)
    coef['Beta'] = 0.05#0.05
    coef['Gama'] = 0.085#07#0.1
    
    ##Chemotaxis inhibition & Haptotaxis Activation
    coef['Kappa'] = 0.4
    coef['Mic'] = 0.4
    
    if not coef['Kappa'] == 0 or not coef['Mic'] == 0:
        ##With Ang2
        coef['Ang2'] = True
        
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
    #set['layout'] = 'retina'
    #set['initial_prof'] = 'retina_tip'
    #set['initial_prof'] = 'retina_1_tip'
    
    '''Setting layout2''' ##==> changes initial prof of m
    set['layout'] = 'rectangular'
    #set['initial_prof'] = 'rectangular_tip'
    set['initial_prof'] = 'rectangular_1_tip'

    '''Spatial and Temporal Meshes Number'''
    ##set dictionaries tidak pernah berubah
    set['T'] = 10.002
    set['Nt'] = 100000
    
    if set['layout'] == 'retina':
        coef['X'] = 4.4
        coef['Y'] = 4.4
        set['h'] = 0.02
        set['R_min'] = 0.52/2
        set['R_max'] = coef['X']/2
        set['error'] = 0.02
        set['dt'] = 0.002
            
    if set['layout'] == 'rectangular':
        coef['X'] = 1
        coef['Y'] = 1
        set['h'] = 0.01
        set['dt'] = 0.001
    
    set['Hh'] = set['h']/2
    set['Nx'] = int(coef['X']/set['Hh'])
    set['Ny'] = int(coef['Y']/set['Hh'])
    
    if set['layout'] == 'retina':
        set['O_x'] = set['Nx']/2*set['Hh']
        set['O_y'] = set['Ny']/2*set['Hh']
    
    '''Initial Setting'''
    set['t'] = 0
    set['k'] = 0
    set['tm'] = 0 #munculnya m cells
       
    '''To store solutions'''
    ##sol dictionaries dapat berubah
    sol['stEC'] = 0
    sol['stVEGF'] = 0
    sol['stFb'] = 0
    sol['tp'] = set['dt']
    sol['inner_bound_tip'] = 0
    sol['matrix_tip'] = 0
    sol['list_tip_movement'] = 0
    sol['life_time_tip'] = 0
    sol['stop_iter'] = 0
    sol['sp_stop'] = 0
    sol['n'] = 0
    sol['c'] = 0
    sol['f'] = 0
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