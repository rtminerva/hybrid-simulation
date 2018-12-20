from collections import OrderedDict

def declare_coef():
    '''Coefficients'''
    #to store coefficients
    coef = {}
    set = {}
    sol = {}

    '''measurement'''
    ra = 0.5 #cm 
    T_1 = 86400 #s for 1 day
    
    '''Tip (n)'''
    #diffusion
    d_n = 10**(-9) #cm^2s^(-1)  10 
    coef['D_n'] = d_n*T_1/(ra**2+ra**2)
#     coef['D_n'] = 1.8*10**(-4) #aubert 
    
    #chemotaxis1
#     ki_n = 2600-750 #cm^2 s^(-1) M^(-1) #stokes 1990
#     coef['Ki_n'] = 0.133 #aubert
    ki_n = 650 #cm^2 s^(-1) M^(-1) #aubert estimation 650 - 750
    c_o = 10**(-10) #M
    coef['al_1'] = 0#ki_n*T_1*c_o/(ra**2+ra**2)

    #chemotaxis2
    coef['be_1'] = 0.35

    '''VEGF (c)'''
    set['ga_1'] = 1 #amplitude of vegf
    set['et_1'] = 0.26 #oscilation velocity of vegf
    set['alpha'] = 0.04
    set['u'] = 1 #area of patch
    
    '''Branching & Mitosis'''
    coef['T_branch'] = 0.75 #day Chaplain
#     coef['T_mitosis'] = 1000#0.5
    
    '''Spatial and Temporal Meshes Number'''
    ##set dictionaries tidak pernah berubah
    coef['X'] = 1
    coef['Y'] = 1
    set['T'] = 14.002
#     set['Nt'] = 100000
#     set['theta'] = 0.5
#     set['rad'] = 0.01/ra
    
    set['h'] = 0.005 #0.01#
    set['dt'] = 0.005#005
    
    set['Hh'] = set['h']/2
    set['Nx'] = int(coef['X']/set['Hh'])
    set['Ny'] = int(coef['Y']/set['Hh'])
    
#     set['O_x'] = set['Nx']/2*set['Hh']
#     set['O_y'] = set['Ny']/2*set['Hh']
    
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
    sol['tip_cell_pos_ave'] = [0]

    return coef, set, sol