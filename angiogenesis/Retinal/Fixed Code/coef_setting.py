def declare_coef():
    '''Coefficients'''
    #to store coefficients
    coef = {}
    set = {}
    
    ##With Ang2
    coef['Ang2'] == False
      
    ##Endothelial (n)
    Ro = 0.16
    coef['Ro'] = 0.16
    D_n = 0.00018
    coef['D_n'] = 0.00018
    Ki_n = 0.4
    coef['Ki_n'] = 0.4
    Al_n = 0.6
    coef['Al_n'] = 0.6
    
    ##VEGF (c)
    D_c = 0.005
    coef['D_c'] = 0.005
    Nu = 0.1
    coef['Nu'] = 0.1
    
    ##Fibronectin (f)
    Beta = 0.05
    coef['Beta'] = 0.05
    Gama = 0.1
    coef['Gama'] = 0.1
    
    ##Mural Cell (m)
    D_m = 0.009 #0.00018 #
    coef['D_m'] = 0.009
    Ki_m = 0.6 #
    coef['Ki_m'] = 0.6
    Al_m = 0.4 #
    coef['Al_m'] = 0.4
    
    ##Tie2 with Angiopoietin (T), Ang1 & Ang2
    A_p = 0.3 #0.2 #
    coef['A_p'] = 0.3
    B_p = 0.3 #0.2 #
    coef['B_p'] = 0.3
    Dl = 0.05 #
    coef['Dl'] = 0.05
    
    ##Chemotaxis inhibition & Haptotaxis Activation
    Kappa = 0#0.4
    coef['Kappa'] = 0#0.4
    Mic = 0#0.4
    coef['Mic'] = 0#0.4

    '''Branching & Mitosis'''
    T_branch = 0.078 #
    coef['T_branch'] = 0.078
    T_mitosis = 0.709
    coef['T_mitosis'] = 0.709
    
    '''Spatial and Temporal Meshes Number'''
    ##set dictionaries tidak pernah berubah
    T = 0.004
    set['T'] = 0.004
    X = 4.4
    Y = 4.4
    Nt = 100000
    set['Nt'] = 100000
    h = 0.02
    set['h'] = h
    
    Hh = h/2
    set['Hh'] = h/2
    nx = int(X/Hh)
    set['Nx'] = int(X/set['Hh'])
    ny = int(Y/Hh)
    set['Ny'] = int(Y/set['Hh'])
    R_min = 0.52/2
    set['R_min'] = 0.52/2
    R_max = X/2
    set['R_max'] = X/2
    
    O_x = set['Nx']/2*set['Hh']
    O_y = set['Ny']/2*set['Hh']
    set['O_x'] = O_x
    set['O_y'] = O_y
    
    '''Initial Setting'''
    t = 0
    set['t'] = 0
    k = 0
    set['k'] = 0
    dt = 0.002
    set['dt'] = 0.002
    sol['tp'] = dt
    error = 0.01
    set['error'] = 0.01
       
    '''To store solutions'''
    ##sol dictionaries dapat berubah
    sol = {}
    sol['matrix_tip'] = 0
    sol['list_tip_movement'] = 0
    sol['life_time_tip'] = 0
    sol['stop_iter'] = 0
    sol['sp_stop'] = 0
    sol['n'] = 0
    sol['c'] = 0
    sol['f'] = 0
    sol['p'] = 0
    sol['m'] = 0
    sol['index_mn'] = 0
    sol['tip_cell'] = 0
    #g = [0, 0, 0, 0, 0, 0, 0, 0, dt, 0, 0, 0]
    return coef, set, sol