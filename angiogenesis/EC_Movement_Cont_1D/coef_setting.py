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
    
#     set['Dimension'] = '1D'
    set['Dimension'] = '2D'
    
    set['c_prof'] = 'C1'
#     set['c_prof'] = 'C2'
    
    ''''Tip (n)'''
    coef['D_n'] = 0.00018 #AUBERT tip Diffusion
    coef['Ki_n'] = 0.133 #AUBERT Chemotaxis coef (range)
    coef['Ro_n'] = 0.00018 #AUBERT tip away from stalk
    ##Kinetics
    coef['mu1'] = 0.2 # tip branching
    coef['Lam_1'] = 0.001 # tip-tip anastomosis 
    coef['Lam_2'] = 0.001 # tip-stalk anastomosis
    
    ''''Stalk (b)'''
    coef['D_b'] = 0#3*10**(-3) #NODATA Stalk diffusion
    coef['Ki_b'] = 0.02 #NODATA tip-taxis
    ##Kinetics
    coef['mu2'] = 1 #stalk proliferation 1
    coef['mu3'] = 1 #stalk-tip proliferation
    coef['beta1'] = 1 #stalk-tip saturation point
    coef['Lam_3'] = 0.001 #Anastomosis should be small enough
    
    '''VEGF (c)''' ##DONE
    coef['D_c'] = 0.005 #vegf diffusion (range)
    coef['Lam_4'] = 0.1 #AUBERT digestion
    coef['mu4'] = 0.05 #proliferation
    coef['mu5'] = 0.2 #decay
    coef['beta2'] = 0.3 #AUBERT stalk critical point

    '''Spatial and Temporal Meshes Number'''
    ##set dictionaries (fixed: never change)
    coef['X'] = 1
    coef['Y'] = 1
    set['T'] = 10.002
    set['Nt'] = 100000
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
    sol['stVEGF'] = 0
    sol['stop_iter'] = 0

    return coef, set, sol