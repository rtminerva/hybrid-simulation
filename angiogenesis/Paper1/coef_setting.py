from collections import OrderedDict

def declare_coef():
    '''Coefficients'''
    #to store coefficients
    coef = {}
    set = {}
    sol = {}
    
    set['initial_prof'] = 'rectangular_1_tip'
    #set['initial_prof'] = 'rectangular_tip'
    
#     set['c_prof'] = 'C1'
    set['c_prof'] = 'C2'
    
    '''measurement'''
    x = 0.07 #cm start from surface of spheroid
    y = 0.07
    T_1 = 86400 #s
    
    ''''Tip (n)'''
    #diffusion
    d_n = 10**(-10) #cm^2s^(-1)  
    coef['D_n'] = d_n*T_1/(x**2+y**2)
#     coef['D_n'] = 1.8*10**(-4) #aubert 
    #chemotaxis
#     ki_n = 2600-750 #cm^2 s^(-1) M^(-1) #stokes 1990
    ki_n = 650 #cm^2 s^(-1) M^(-1) #aubert estimation 650 - 750
    c_o = 10**(-10) #M
    coef['Ki_n'] = ki_n*T_1*c_o/(x**2+y**2)
#     coef['Ki_n'] = 0.133 #aubert
    coef['Ro_n'] = coef['D_n'] #Gaffney 0.003 #
    coef['Al_n'] = 0#.6

    '''VEGF (c)'''
    #diffusion
#     d_c = 2.9*10**(-7) #cm^2s^(-1) #Anderson and Chaplain, Bray
    d_c = 5.6*10**(-11) #aubert estimation 5.6*10**(-9) - 1.4*10**(-8)
#     d_c = 2.8*10**(-8) #miura 2009
    coef['D_c'] = d_c*T_1/(x**2+y**2)
#     coef['D_c'] = 0.01 #aubert
    coef['Nu'] = 0.5#1
    coef['lam'] = 0.5#1
 
    '''Branching & Mitosis'''
    coef['T_branch'] = 0.25
#     coef['T_mitosis'] = 1000#0.5
    
    '''Spatial and Temporal Meshes Number'''
    ##set dictionaries tidak pernah berubah
    coef['X'] = 1
    coef['Y'] = 1
    set['T'] = 5.002
    set['Nt'] = 100000
    set['theta'] = 0.5
    set['rad'] = 0.01/x
    
    set['h'] = 0.005 #0.01#
    set['dt'] = 0.001
    
    set['Hh'] = set['h']/2
    set['Nx'] = int(coef['X']/set['Hh'])
    set['Ny'] = int(coef['Y']/set['Hh'])
    
    '''Initial Setting'''
    set['t'] = 0
    set['k'] = 0
       
    '''To store solutions'''
    ##sol dictionaries dapat berubah
    sol['stEC'] = 0
    sol['Merge_cn'] = 0
    sol['Merge_cnd'] = 0
    sol['Merge_fn'] = 0
    sol['VEGF'] = 0
    sol['VEGF1'] = 0
    sol['ECM'] = 0
    sol['stop_iter'] = 0
    '''For Anastomosis'''
#     sol['pp'] = {}
#     sol['PP'] = [] 
    sol['backward'] = {}
    sol['backward_count'] = []
    sol['backward_list'] = []
    sol['tip_tip_anas'] = []
    sol['cause'] = {}

    return coef, set, sol