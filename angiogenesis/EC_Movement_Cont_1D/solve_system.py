from random import randint, sample, uniform
import numpy

def b_mean_function(set,sol,xb,b_o):
    if xb == 1:
        b_mean_r = (b_o[xb+2]+b_o[xb])/2
        b_mean_l = b_o[xb]
    elif xb == set['Nx']-1:
        b_mean_r = b_o[xb]
        b_mean_l = (b_o[xb-2]+b_o[xb])/2
    else:
        b_mean_r = (b_o[xb+2]+b_o[xb])/2
        b_mean_l = (b_o[xb-2]+b_o[xb])/2
    b_mean = [b_mean_r, b_mean_l]
    return b_mean

def n_mean_function(set,sol,xb,n_o):
    if xb == 1:
        n_mean_r = (n_o[xb+2]+n_o[xb])/2
        n_mean_l = n_o[xb]
    elif xb == set['Nx']-1:
        n_mean_r = n_o[xb]
        n_mean_l = (n_o[xb-2]+n_o[xb])/2
    else:
        n_mean_r = (n_o[xb+2]+n_o[xb])/2
        n_mean_l = (n_o[xb-2]+n_o[xb])/2
    n_mean = [n_mean_r, n_mean_l]
    return n_mean

def max_min_c(set,sol,x,c_o): #2.3.(1).(1)
    cijx = (c_o[x]-c_o[x-2])/(set['h'])
    cijx_p = max(0,cijx)
    cijx_n = max(0,-cijx)
    return cijx_p, cijx_n

def max_min_b(set,sol,x,b_o): #2.3.(1).(2)
    xb = x-1
    
    b_mean = b_mean_function(set,sol,xb,b_o)
    
    bijx = (b_mean[0]-b_mean[1])/(set['h'])

    bijx_p = max(0,bijx)
    bijx_n = max(0,-bijx)
    return bijx_p, bijx_n

def F_vector_sol(coef,set,sol,n_o,b_o,c_o): #2.3.(1)
    F_sol_1 = numpy.zeros(set['Nx']+1)
    G_plus_1 = 0
    G_neg_1 = 0
    for x in range(0,set['Nx']+1,2):
        if not x == 0:
            if not x == set['Nx']:
                #chemo_coef = coef['Ki']/(1+coef['Al_n']*(c_o[x,y]+c_o[x-2,y]+c_o[x,y-2]+c_o[x-2,y-2])/4)
                cijx_p, cijx_n = max_min_c(set,sol,x,c_o) #2.3.(1).(1)
                bijx_p, bijx_n = max_min_b(set,sol,x,b_o) #2.3.(1).(2)
                G_plus_1 = coef['Ki']*cijx_p-coef['C_2']*bijx_p
                
                #chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(c_o[x,y]+c_o[x+2,y]+c_o[x,y-2]+c_o[x+2,y-2])/4)
                cijx_p, cijx_n = max_min_c(set,sol,x+2,c_o) #2.3.(1).(1)
                bijx_p, bijx_n = max_min_b(set,sol,x+2,b_o) #2.3.(1).(2)
                G_neg_1 = coef['Ki']*cijx_n-coef['C_2']*bijx_n
                
                F_sol_1[x] = -coef['C_1']/(set['h'])*(n_o[x+1]-n_o[x-1])+n_o[x-1]*G_plus_1-n_o[x+1]*G_neg_1
                
    return F_sol_1     

def system(coef, set, sol): #2.3
    c_o = numpy.copy(sol['c']) #to save values at time step k (we are calculating at time step k+1)
    n_o = numpy.copy(sol['n']) #to save values at time step k (we are calculating at time step k+1)
    b_o = numpy.copy(sol['b']) #to save values at time step k (we are calculating at time step k+1)
    
    '''Defining Vb at main latice'''
    ##Finding index of n max
    Ind_max_n = numpy.argmax(n_o)
        
    #profile 2: /
    for x in range(1,set['Nx'],2):
        s = Ind_max_n-x
        if s <= 2:
            h_s = 0
        elif s <= 50:
            h_s = 1 + coef['M']*(s-50)
        else:
            h_s = 1
        if s != 0:
            sol['Vb_x'][x] = (Ind_max_n-x)*h_s/s #unit vector

    F_sol_1 = F_vector_sol(coef, set, sol, n_o, b_o, c_o)
    
    '''Pettet Method'''
     #Mean of n on sub-lattice
     
    '''Solve b, n at main lattice'''
    for x in range(1,set['Nx'],2):
        kinetic_b = 0#set['dt']*coef['vi']*b_o[x]*(1-b_o[x]) + set['dt']*coef['k_5']*(coef['k_3']*(n_o[x])**2+coef['k_4']*n_o[x]*b_o[x])
        kinetic_n = 0#set['dt']*coef['k_2']*n_o[x] - set['dt']*coef['k_3']*(n_o[x])**2-set['dt']*coef['k_4']*n_o[x]*b_o[x]
        ##Pettet & Balding
#         kinetic_b = - 0.1*set['dt']*coef['C_1']*(n_mean[0]-n_mean[1])/(set['h']) #+ set['dt']*coef['Ki']*(c_o[x+1]-c_o[x-1])/(set['h'])
        #we put the convection term as move variable
        if x == 1:
            n_mean_i = n_mean_function(set,sol,x,n_o)
            n_mean_ip1 = n_mean_function(set,sol,x+2,n_o)
            move_n = set['dt']*(F_sol_1[x+1])/set['h']
#             move_b = set['dt']*coef['C_4']*((b_o[x]*max(sol['Vb_x'][x],0)-b_o[x+2]*max(-sol['Vb_x'][x+2],0)))/set['h']
            ##Stalk Vel positive grad n
            move_b = set['dt']*coef['C_4']*((b_o[x]*max((n_mean_i[1]-n_mean_i[0])/set['h'],0)-b_o[x+2]*max(-(n_mean_ip1[1]-n_mean_ip1[0])/set['h'],0)))/set['h']
            ##Stalk Vel positive grad c
#             move_b = set['dt']*coef['C_4']*((b_o[x]*max((c_o[x+1]-c_o[x-1])/set['h'],0)-b_o[x+2]*max(-(c_o[x+3]-c_o[x+1])/set['h'],0)))/set['h']
        elif x == set['Nx']-1:
            n_mean_i = n_mean_function(set,sol,x,n_o)
            n_mean_in1 = n_mean_function(set,sol,x-2,n_o)
            move_n = set['dt']*(-F_sol_1[x-1])/set['h']
#             move_b = set['dt']*coef['C_4']*(-(b_o[x-2]*max(sol['Vb_x'][x-2],0)-b_o[x]*max(-sol['Vb_x'][x],0)))/set['h']
            ##Stalk Vel positive grad n
            move_b = set['dt']*coef['C_4']*(-(b_o[x-2]*max((n_mean_in1[1]-n_mean_in1[0])/set['h'],0)-b_o[x]*max(-(n_mean_i[1]-n_mean_i[0])/set['h'],0)))/set['h']
            ##Stalk Vel positive grad c
#             move_b = set['dt']*coef['C_4']*(-(b_o[x-2]*max((c_o[x-1]-c_o[x-3])/set['h'],0)-b_o[x]*max(-(c_o[x+1]-c_o[x-1])/set['h'],0)))/set['h']
        else:
            n_mean_i = n_mean_function(set,sol,x,n_o)
            n_mean_ip1 = n_mean_function(set,sol,x+2,n_o)
            n_mean_in1 = n_mean_function(set,sol,x-2,n_o)
            move_n = set['dt']*(F_sol_1[x+1]-F_sol_1[x-1])/set['h']
#             move_b = set['dt']*coef['C_4']*((b_o[x]*max(sol['Vb_x'][x],0)-b_o[x+2]*max(-sol['Vb_x'][x+2],0))-(b_o[x-2]*max(sol['Vb_x'][x-2],0)-b_o[x]*max(-sol['Vb_x'][x],0)))/set['h']
            ##Stalk Vel positive grad n
            move_b = set['dt']*coef['C_4']*((b_o[x]*max((n_mean_i[1]-n_mean_i[0])/set['h'],0)-b_o[x+2]*max(-(n_mean_ip1[1]-n_mean_ip1[0])/set['h'],0))-(b_o[x-2]*max((n_mean_in1[1]-n_mean_in1[0])/set['h'],0)-b_o[x]*max(-(n_mean_i[1]-n_mean_i[0])/set['h'],0)))/set['h']
            ##Stalk Vel positive grad c
#             move_b = set['dt']*coef['C_4']*((b_o[x]*max((c_o[x+1]-c_o[x-1])/set['h'],0)-b_o[x+2]*max(-(c_o[x+3]-c_o[x+1])/set['h'],0))-(b_o[x-2]*max((c_o[x-1]-c_o[x-3])/set['h'],0)-b_o[x]*max(-(c_o[x+1]-c_o[x-1])/set['h'],0)))/set['h']
        sol['n'][x] = n_o[x] - move_n + kinetic_n
        sol['b'][x] = b_o[x] - move_b + kinetic_b

#         sol['b'][1] = 1 #the supply of stalk from pre-existing vessel
#             if b_o[x,y] != 0:
#                 print 'Value of proliferation:', prolifer_1
#                 print 'Value of degradation by movement:', move    
                     
    '''Solve c at sub lattice'''
    for x in range(0,set['Nx']+1,2):
        degradation_c = set['dt']*coef['gama']*c_o[x] 
        if x == 0:
            mean_b = b_o[x+1]
            mean_n = n_o[x+1]
            if mean_b < coef['beta2']:
                S = 1- (mean_b/coef['beta2'])
            else:
                S = 0
            move_c = coef['C_3']*set['dt']*(c_o[x+2]+c_o[x]-2*c_o[x])/(set['h']**2)                 
        elif x == set['Nx']:
            mean_b = b_o[x-1]
            mean_n = n_o[x-1]
            if mean_b < coef['beta2']:
                S = 1- (mean_b/coef['beta2'])
            else:
                S = 0
            move_c = coef['C_3']*set['dt']*(c_o[x-2]+c_o[x]-2*c_o[x])/(set['h']**2)
        else:
            mean_b = (b_o[x-1] + b_o[x+1])/2
            mean_n = (n_o[x-1] + n_o[x+1])/2
            if mean_b < coef['beta2']:
                S = 1- (mean_b/coef['beta2'])
            else:
                S = 0   
            move_c = coef['C_3']*set['dt']*(c_o[x+2]+c_o[x-2]+c_o[x]-3*c_o[x])/(set['h']**2)               
        prolifer_c = set['dt']*coef['k_1']*S
        digestion_c = set['dt']*coef['Nu']*c_o[x]*mean_n
        sol['c'][x] = c_o[x] + prolifer_c - digestion_c - degradation_c + move_c
        
#     for y in range(1,set['Ny'],2):
#         for x in range(1,set['Nx'],2):
#             if sol['b'][x,y] != 0:
#                 print 'Stalk cell position:[',x,',',y,'], With value:',sol['b'][x,y]                 
    return sol