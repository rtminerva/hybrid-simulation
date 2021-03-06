from collections import OrderedDict
import math as m

def declare_coef():
    '''Coefficients'''
    #to store coefficients
    coef = {}
    set = {}
    sol = {}
    
    ##Cell (n)
    coef['D_n'] = 0.00035
    coef['xi'] = 0.00001
#     coef['A_n'] = 0.4 #amplitude of n    
#     coef['Xi_n'] = 1
    coef['alpha'] =1#20 #first velocity 
    coef['beta'] = 1 #adaptation velocity
    
    ##VEGF (c)
    coef['vel'] = 15#10 #velocity of wave
    coef['perio'] = 4 #period of wave
    coef['A_c'] = 0.5#0.5#0.8 #amplitude of wave
    coef['vari'] = 0.08#0.1#0.3#0.05 #variance of wave
    
    '''Rotation'''
    coef['r'] = 1
    coef['teta'] = 1
    set['T_c'] = m.pi*100
    set['dt_c'] = m.pi*2/100
 
    '''Branching & Mitosis'''
    coef['T_branch'] = 0.25
    
    '''Spatial and Temporal Meshes Number'''
    ##set dictionaries tidak pernah berubah
    set['T'] = 2.002
    set['Nt'] = 100000
#     set['rad'] = 0.12
    set['h'] = 0.005 #0.01
    set['dt'] = 0.001
    coef['X'] = 1
    coef['Y'] = 1
    set['Hh'] = set['h']/2
    set['Nx'] = int(coef['X']/set['Hh'])
    set['Ny'] = int(coef['Y']/set['Hh'])
    
    '''Initial Setting'''
    set['t'] = 0
    set['t_c'] = 0
    set['k'] = 0
       
    '''To store solutions'''
    ##sol dictionaries dapat berubah
    sol['stEC'] = 0
    sol['Merge_cn'] = 0
    sol['Merge_cnd'] = 0
    sol['Merge_fn'] = 0
#     sol['VEGF'] = 0
#     sol['VEGF1'] = 0
#     sol['ECM'] = 0
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