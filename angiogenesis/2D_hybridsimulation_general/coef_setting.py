from collections import OrderedDict

def declare_coef(): #Ref.1
    '''Create storages to store all coefficient, setting, and solution'''
    coef = {}
    set = {}
    sol = {}

    '''measurement'''
    ra = 2 #real distance on measurement (mm) 
    T_1 = 129600 #86400 #real time observations in 1.5 day (second)
    
    '''diffusion of Tip (n)'''
    coef['D_n'] = 3.5*10**(-4)
#     d_n = 10**(-14)#10**(-9) #mm^2s^(-1)
#     coef['D_n'] = d_n*T_1/ra**2

    '''v_m (vm_1) of Tip (n)'''
    coef['a_1'] = 0.38
#     ki_n = 0.26 #mm^2 s^(-1) M^(-1) #aubert estimation 650 - 750
#     c_o = 10**(-10) #M
#     coef['vm_1'] = ki_n*T_1*c_o/ra**2

    '''v_m (vm_2) of Tip (n)'''
    coef['a_2'] = 0#.003

    '''VEGF (c) correspond to vm_1'''
    coef['c_1'] = 0.1
    
    '''Fibronectin (f) correspond to vm_2'''
    coef['f_1'] = 0#.05
    
    '''Branching & Mitosis'''
    coef['T_branch'] = 0.25 #*1.5 day
#     coef['T_mitosis'] = 1000#0.5
    
    '''Spatial and Temporal Meshes Number'''
    ##'set' dictionary never changes during the iteration
    set['T'] = 10 + 0.002 #Set maximum time observation
    coef['X'] = 1
    coef['Y'] = 1
    
    set['h'] = 0.005 #0.01#
    #set['dtt'] = 0#0.01#0.005#005
    
    set['Hh'] = set['h']/2
    set['Nx'] = int(coef['X']/set['Hh'])
    set['Ny'] = int(coef['Y']/set['Hh'])
    
    '''Initial Setting'''
    set['t'] = 0
    set['k'] = 0
       
    '''To store solutions'''
    ##sol dictionaries dapat berubah
    #for pictures
    sol['ves'] = 0
    sol['Merge_cn'] = 0
    sol['Merge_cnt'] = 0
    sol['Merge_fn'] = 0
    sol['VEGF'] = 0
    sol['VEGF1'] = 0
    sol['ECM'] = 0
    
    #other
    sol['stop_iter'] = 0
#     sol['backward'] = {}
#     sol['backward_count'] = []
#     sol['backward_list'] = []
    sol['tip_tip_anas'] = []
    sol['cause'] = {}
    sol['tip_cell_pos_ave'] = [0]
#     '''For Anastomosis'''
#     sol['pp'] = {}
#     sol['PP'] = [] 

    return coef, set, sol