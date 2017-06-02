from random import randint, sample, uniform
import numpy

def b_mean_function(set,sol,xb,b_o):
    if xb == 1:
        b_mean_r = (b_o[xb+2]+b_o[xb])/2
        b_mean_l = b_o[xb]/2
    elif xb == set['Nx']-1:
        b_mean_r = b_o[xb]/2
        b_mean_l = (b_o[xb-2]+b_o[xb])/2
    else:
        b_mean_r = (b_o[xb+2]+b_o[xb])/2
        b_mean_l = (b_o[xb-2]+b_o[xb])/2
    b_mean = [b_mean_r, b_mean_l]
    return b_mean

def n_mean_function(set,sol,xb,n_o):
    if xb == 1:
        n_mean_r = (n_o[xb+2]+n_o[xb])/2
        n_mean_l = n_o[xb]/2
    elif xb == set['Nx']-1:
        n_mean_r = n_o[xb]/2
        n_mean_l = (n_o[xb-2]+n_o[xb])/2
    else:
        n_mean_r = (n_o[xb+2]+n_o[xb])/2
        n_mean_l = (n_o[xb-2]+n_o[xb])/2
    n_mean = [n_mean_l, n_mean_r]
    return n_mean

def max_min_c(set,sol,x,c_o): #2.3.(1).(1)
    cijx = (c_o[x]-c_o[x-2])/(set['h'])
    cijx_p = max(0,cijx)
    cijx_n = max(0,-cijx)
    return cijx_p, cijx_n

def max_min_p(set,sol,x,p_o): #2.3.(1).(1)
    pijx = (p_o[x]-p_o[x-2])/(set['h'])
    pijx_p = max(0,pijx)
    pijx_n = max(0,-pijx)
    return pijx_p, pijx_n

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
                cijx_p, cijx_n = max_min_c(set,sol,x,c_o) #2.3.(1).(1)
                bijx_p, bijx_n = max_min_b(set,sol,x,b_o) #2.3.(1).(2)
                G_plus_1 = coef['Ki_n']*cijx_p-coef['Ro_n']*bijx_p
                
                cijx_p, cijx_n = max_min_c(set,sol,x+2,c_o) #2.3.(1).(1)
                bijx_p, bijx_n = max_min_b(set,sol,x+2,b_o) #2.3.(1).(2)
                G_neg_1 = coef['Ki_n']*cijx_n-coef['Ro_n']*bijx_n
                
                F_sol_1[x] = -coef['D_n']/(set['h'])*(n_o[x+1]-n_o[x-1])+n_o[x-1]*G_plus_1-n_o[x+1]*G_neg_1
                
    return F_sol_1    

def G_vector_sol(coef,set,sol,m_o,p_o): #2.3.(1)
    G_sol_1 = numpy.zeros(set['Nx']+1)
    G_plus_1 = 0
    G_neg_1 = 0
    for x in range(0,set['Nx']+1,2):
        if not x == 0:
            if not x == set['Nx']:
                pijx_p, pijx_n = max_min_p(set,sol,x,p_o) #2.3.(1).(2)
                G_plus_1 = coef['Ki_m']*pijx_p
                
                pijx_p, pijx_n = max_min_p(set,sol,x+2,p_o) #2.3.(1).(2)
                G_neg_1 = coef['Ki_m']*pijx_n
                
                G_sol_1[x] = m_o[x-1]*G_plus_1-m_o[x+1]*G_neg_1
                
    return G_sol_1     

def n_b_c(coef, set, sol, n_o, b_o, c_o, ma_o, branching_par = 0, branching = False):
    F_sol_1 = F_vector_sol(coef, set, sol, n_o, b_o, c_o)
    
    #check branching age
    if sol['age'] > 0.001:
        branching = True
    tip_cell_pos = numpy.argmax(n_o)
   
     
    '''Solve b, n at main lattice'''
    for x in range(1,set['Nx'],2):
#         kinetic_n = set['dt']*coef['mu1']*n_o[x] - set['dt']*coef['Lam_1']*(n_o[x])**2-set['dt']*coef['Lam_2']*n_o[x]*b_o[x]
       
        #branching is obtained by cell density and vegf level
        if branching == True:# and x == tip_cell_pos:
            #branching due to cell density and VEGF
            branch_dec = (b_o[x] - 1/2*n_o[x]) * ((c_o[x+1]+c_o[x-1])/(2*0.1) - 1)
            
            if branch_dec > 0:
                branching_par = coef['mu1']
#                 print 'branching'
#                 print x
#                 print branch_dec
                sol['age'] = 0
        
        kinetic_n = set['dt']*branching_par*n_o[x] - set['dt']*coef['Lam_1']*(n_o[x])**2-set['dt']*coef['Lam_2']*n_o[x]*b_o[x]
        
        
        '''Model Extension''' 
        if set['Model'] == 'extensions':  #SSSSSSS
            kinetic_b = set['dt']*coef['mu2']*(1/(1+ma_o[x]))*b_o[x]*(1-b_o[x]) + set['dt']*coef['mu3']*(1/(1+ma_o[x]))*n_o[x]*b_o[x]*(1-(b_o[x])/(coef['beta1'])) + set['dt']*coef['Lam_3']*(coef['Lam_1']*(n_o[x])**2+coef['Lam_2']*n_o[x]*b_o[x])
        else:
            kinetic_b = set['dt']*coef['mu2']*b_o[x]*(1-b_o[x]) + set['dt']*coef['mu3']*n_o[x]*b_o[x]*(1-(b_o[x])/(coef['beta1'])) + set['dt']*coef['Lam_3']*(coef['Lam_1']*(n_o[x])**2+coef['Lam_2']*n_o[x]*b_o[x])
            
        ##Pettet & Balding
#         kinetic_b = - 0.1*set['dt']*coef['C_1']*(n_mean[0]-n_mean[1])/(set['h']) #+ set['dt']*coef['Ki']*(c_o[x+1]-c_o[x-1])/(set['h'])
        #we put the convection term as move variable
        if x == 1:
            n_mean_i = n_mean_function(set,sol,x,n_o)
            n_mean_ip1 = n_mean_function(set,sol,x+2,n_o)
            move_n = set['dt']*(F_sol_1[x+1])/set['h']
            ##New Model
#             move_b = set['dt']*coef['Ki_b']*((b_o[x]*max(sol['Vb_x'][x],0)-b_o[x+2]*max(-sol['Vb_x'][x+2],0)))/set['h']

            ##Stalk Vel grad n
            move_b = set['dt']*coef['Ki_b']*((b_o[x]*max((n_mean_i[1]-n_mean_i[0])/set['h'],0)-b_o[x+2]*max(-(n_mean_ip1[1]-n_mean_ip1[0])/set['h'],0)))/set['h'] - coef['D_b']*set['dt']*(b_o[x+2]-b_o[x])/(set['h']**2)
            ##Stalk Vel positive grad c
#             move_b = set['dt']*coef['Ki_b']*((b_o[x]*max((c_o[x+1]-c_o[x-1])/set['h'],0)-b_o[x+2]*max(-(c_o[x+3]-c_o[x+1])/set['h'],0)))/set['h']
        elif x == set['Nx']-1:
            n_mean_i = n_mean_function(set,sol,x,n_o)
            n_mean_in1 = n_mean_function(set,sol,x-2,n_o)
            move_n = set['dt']*(-F_sol_1[x-1])/set['h']
            ##New Model
#             move_b = set['dt']*coef['Ki_b']*(-(b_o[x-2]*max(sol['Vb_x'][x-2],0)-b_o[x]*max(-sol['Vb_x'][x],0)))/set['h']

            ##Stalk Vel grad n
            move_b = set['dt']*coef['Ki_b']*(-(b_o[x-2]*max((n_mean_in1[1]-n_mean_in1[0])/set['h'],0)-b_o[x]*max(-(n_mean_i[1]-n_mean_i[0])/set['h'],0)))/set['h'] - coef['D_b']*set['dt']*(b_o[x-2]-b_o[x])/(set['h']**2)
            ##Stalk Vel positive grad c
#             move_b = set['dt']*coef['Ki_b']*(-(b_o[x-2]*max((c_o[x-1]-c_o[x-3])/set['h'],0)-b_o[x]*max(-(c_o[x+1]-c_o[x-1])/set['h'],0)))/set['h']
        else:
            n_mean_i = n_mean_function(set,sol,x,n_o)
            n_mean_ip1 = n_mean_function(set,sol,x+2,n_o)
            n_mean_in1 = n_mean_function(set,sol,x-2,n_o)
            move_n = set['dt']*(F_sol_1[x+1]-F_sol_1[x-1])/set['h']
            ##New Model
#             move_b = set['dt']*coef['Ki_b']*((b_o[x]*max(sol['Vb_x'][x],0)-b_o[x+2]*max(-sol['Vb_x'][x+2],0))-(b_o[x-2]*max(sol['Vb_x'][x-2],0)-b_o[x]*max(-sol['Vb_x'][x],0)))/set['h'] 
            
            ##Stalk Vel grad n
            move_b = set['dt']*coef['Ki_b']*((b_o[x]*max((n_mean_i[1]-n_mean_i[0])/set['h'],0)-b_o[x+2]*max(-(n_mean_ip1[1]-n_mean_ip1[0])/set['h'],0))-(b_o[x-2]*max((n_mean_in1[1]-n_mean_in1[0])/set['h'],0)-b_o[x]*max(-(n_mean_i[1]-n_mean_i[0])/set['h'],0)))/set['h'] - coef['D_b']*set['dt']*(b_o[x-2]+b_o[x+2]-2*b_o[x])/(set['h']**2)
            ##Stalk Vel positive grad c
#             move_b = set['dt']*coef['Ki_b']*((b_o[x]*max((c_o[x+1]-c_o[x-1])/set['h'],0)-b_o[x+2]*max(-(c_o[x+3]-c_o[x+1])/set['h'],0))-(b_o[x-2]*max((c_o[x-1]-c_o[x-3])/set['h'],0)-b_o[x]*max(-(c_o[x+1]-c_o[x-1])/set['h'],0)))/set['h']
        sol['n'][x] = n_o[x] - move_n# + kinetic_n
        sol['b'][x] = b_o[x] - move_b# + kinetic_b
        
#         sol['b'][1] =1
#         #Keeping Source of Stalk
#         if x*set['Hh'] < set['rad']-0.06:
#             sol['b'][x] =1
#             sol['b'][x] = 0.5 + 0.5*m.tanh(((set['rad'])-x*set['Hh'])/0.01)

#         if b_o[x] != 0:
#             print 'Value of proliferation:', kinetic_b
#             print 'Value of degradation by movement:', move_b    
                     
    '''Solve c at sub lattice'''
    for x in range(0,set['Nx']+1,2):
        if x == 0:
            mean_b = b_o[x+1]/2
            mean_n = n_o[x+1]/2
            if mean_b < coef['beta2']:
                S = 1- (mean_b/coef['beta2'])
            else:
                S = 0
            move_c = coef['D_c']*set['dt']*(c_o[x+2]+c_o[x]-2*c_o[x])/(set['h']**2)                 
        elif x == set['Nx']:
            mean_b = b_o[x-1]/2
            mean_n = n_o[x-1]/2
            if mean_b < coef['beta2']:
                S = 1- (mean_b/coef['beta2'])
            else:
                S = 0
            move_c = coef['D_c']*set['dt']*(c_o[x-2]+c_o[x]-2*c_o[x])/(set['h']**2)
        else:
            mean_b = (b_o[x-1] + b_o[x+1])/2
            mean_n = (n_o[x-1] + n_o[x+1])/2
            if mean_b < coef['beta2']:
                S = 1- (mean_b/coef['beta2'])
            else:
                S = 0   
            move_c = coef['D_c']*set['dt']*(c_o[x+2]+c_o[x-2]-2*c_o[x])/(set['h']**2)               
        prolifer_c = set['dt']*coef['mu4']*S
        digestion_c = set['dt']*coef['Lam_4']*c_o[x]*mean_n
        degradation_c = set['dt']*coef['mu5']*c_o[x] 
        
        sol['c'][x] = c_o[x] + move_c + prolifer_c - digestion_c - degradation_c
        
#     for y in range(1,set['Ny'],2):
#         for x in range(1,set['Nx'],2):
#             if sol['b'][x,y] != 0:
#                 print 'Stalk cell position:[',x,',',y,'], With value:',sol['b'][x,y]
    return sol

def n_b_c_stop(coef, set, sol, n_o, b_o, c_o, ma_o):
    for x in range(1,set['Nx'],2):
        '''Model Extension''' 
        if set['Model'] == 'extension': 
            kinetic_b = set['dt']*coef['mu2']*(1/(1+ma_o[x]))*b_o[x]*(1-b_o[x]) + set['dt']*coef['mu3']*(1/(1+ma_o[x]))*n_o[x]*b_o[x]*(1-(b_o[x])/(coef['beta1']))
            sol['b'][x] = b_o[x] + kinetic_b
    return sol

def system_1d(coef, set, sol): #2.3
    c_o = numpy.copy(sol['c']) #to save values at time step k (we are calculating at time step k+1)
    n_o = numpy.copy(sol['n']) 
    b_o = numpy.copy(sol['b'])
    ma_o = numpy.copy(sol['ma']) 
    
    '''Model Extension'''    
    if set['Model'] == 'extension':
        p_o = numpy.copy(sol['p']) #to save values at time step k (we are calculating at time step k+1)
        e_o = numpy.copy(sol['e']) 
        a1_o = numpy.copy(sol['a1']) 
        a2_o = numpy.copy(sol['a2']) 
        r1_o = numpy.copy(sol['a1']) 
        r2_o = numpy.copy(sol['a2']) 
        m_o = numpy.copy(sol['m']) 
        ma_o = numpy.copy(sol['ma']) 

        G_sol_1 = G_vector_sol(coef, set, sol, m_o, p_o)
        '''Solve p at sub lattice'''
        for x in range(0,set['Nx']+1,2):
            if x == 0:
                mean_m = m_o[x+1]/2
                mean_n = n_o[x+1]/2
                move_p = coef['D_p']*set['dt']*(p_o[x+2]+p_o[x]-2*p_o[x])/(set['h']**2)                 
            elif x == set['Nx']:
                mean_m = m_o[x-1]/2
                mean_n = n_o[x-1]/2
                move_p = coef['D_p']*set['dt']*(p_o[x-2]+p_o[x]-2*p_o[x])/(set['h']**2)
            else:
                mean_m = (m_o[x-1] + m_o[x+1])/2
                mean_n = (n_o[x-1] + n_o[x+1])/2
                move_p = coef['D_p']*set['dt']*(p_o[x+2]+p_o[x-2]-2*p_o[x])/(set['h']**2)               
            prolifer_p = set['dt']*coef['mu6']*mean_n*(1-p_o[x])
            degradation_p = set['dt']*coef['mu7']*p_o[x]
            uptake_p = set['dt']*coef['Lam_5']*p_o[x]*mean_m 
            
            sol['p'][x] = p_o[x] + prolifer_p - uptake_p - degradation_p + move_p
            
        '''Solve e,a1,a2,m,ma at main'''
        for x in range(1,set['Nx'],2):
            if x == 1:
                move_e = coef['D_e']*set['dt']*(e_o[x+2]-e_o[x])/(set['h']**2)
                move_a1 = coef['D_a1']*set['dt']*(a1_o[x+2]-a1_o[x])/(set['h']**2)
                move_a2 = coef['D_a2']*set['dt']*(a2_o[x+2]-a2_o[x])/(set['h']**2)
                move_m =  set['dt']*(G_sol_1[x+1])/set['h'] - coef['D_m']*set['dt']*(m_o[x+2]-m_o[x])/(set['h']**2)
        
            elif x == set['Nx']-1:
                move_e = coef['D_e']*set['dt']*(e_o[x-2]-e_o[x])/(set['h']**2)
                move_a1 = coef['D_a1']*set['dt']*(a1_o[x-2]-a1_o[x])/(set['h']**2)
                move_a2 = coef['D_a2']*set['dt']*(a2_o[x-2]-a2_o[x])/(set['h']**2)
                move_m = set['dt']*(-G_sol_1[x-1])/set['h'] - coef['D_m']*set['dt']*(m_o[x-2]-m_o[x])/(set['h']**2)
                
            else:
                move_e = coef['D_e']*set['dt']*(e_o[x-2]-e_o[x])/(set['h']**2)
                move_a1 = coef['D_a1']*set['dt']*(a1_o[x-2]-a1_o[x])/(set['h']**2)
                move_a2 = coef['D_a2']*set['dt']*(a2_o[x-2]-a2_o[x])/(set['h']**2)
                move_m = set['dt']*(G_sol_1[x+1]-G_sol_1[x-1])/set['h'] - coef['D_m']*set['dt']*(m_o[x-2]-m_o[x])/(set['h']**2)
            
            kinetic_e = set['dt']*coef['mu8']*b_o[x]*(1-e_o[x]) - set['dt']*coef['mu9']*e_o[x] + set['dt']*(-coef['k1']*a1_o[x]*e_o[x]+coef['k_1']*r1_o[x]-coef['k2']*a2_o[x]*e_o[x]+coef['k_2']*r2_o[x])
            kinetic_a1 = set['dt']*coef['mu10']*m_o[x]*(1-a1_o[x]) - set['dt']*coef['mu11']*a1_o[x] + set['dt']*(-coef['k1']*a1_o[x]*e_o[x]+coef['k_1']*r1_o[x])
            AD = 0
            mean_c = (sol['c'][x-1] + sol['c'][x+1])/2
            if mean_c > coef['beta3']:
                AD = set['dt']*coef['mu12']*b_o[x]*(1-a2_o[x])
            kinetic_a2 = AD - set['dt']*coef['mu13']*a2_o[x] + set['dt']*(-coef['k2']*a2_o[x]*e_o[x]+coef['k_2']*r2_o[x])
            kinetic_m = set['dt']*coef['mu14']*m_o[x]*(0.8-m_o[x]) - set['dt']*coef['mu15']*m_o[x]
            kinetic_ma = set['dt']*coef['mu16']*(m_o[x]-ma_o[x])*max((r1_o[x]-(r2_o[x])/coef['Gam']),0) - set['dt']*coef['mu17']*ma_o[x]*max((r2_o[x]-r1_o[x]*coef['Gam']),0)
            kinetic_r1 = set['dt']*(coef['k1']*a1_o[x]*e_o[x]-coef['k_1']*r1_o[x])
            kinetic_r2 = set['dt']*(coef['k2']*a2_o[x]*e_o[x]-coef['k_2']*r2_o[x])
            
            sol['e'][x] = e_o[x] + move_e + kinetic_e
            sol['a1'][x] = a1_o[x] + move_a1 + kinetic_a1
            sol['a2'][x] = a2_o[x] + move_a2 + kinetic_a2
            sol['m'][x] = m_o[x] - move_m + kinetic_m
            sol['ma'][x] = ma_o[x] + kinetic_ma
            sol['r1'][x] = r1_o[x] + kinetic_r1
            sol['r2'][x] = r2_o[x] + kinetic_r2
            
            if x*set['Hh'] < set['rad']-0.1:
                sol['m'][x] = 0.8
    
    '''Defining Vb at main latice'''
#     ##Finding index of n max
#     Ind_max_n = numpy.argmax(n_o)
        
    #profile 1: \/\
#     for x in range(1,set['Nx'],2):
#         s = Ind_max_n-x
#         if s <= 2:
#             h_s = 0
#         elif s <= 50:
#             h_s = 1.2 + coef['m1']*(s-50)
#         elif s <= 75:
#             h_s = 1.5 + coef['m2']*(s-75)
#         elif s <= 100:
#             h_s = 1 + coef['m3']*(s-100)
#         else:
#             h_s = 1
#         if s != 0:
#             sol['Vb_x'][x] = (Ind_max_n-x)*h_s/s #unit vector
        
    #profile 2: /
#     for x in range(1,set['Nx'],2):
#         s = Ind_max_n-x
#         if s <= 2:
#             h_s = 0
#         elif s <= 100:
#             h_s = 1 + coef['M']*(s-100)
#         else:
#             h_s = 1
#         if s != 0:
#             sol['Vb_x'][x] = (Ind_max_n-x)*h_s/s #unit vector
    '''Model Extension'''    
    if set['Model'] == 'extension':
        if set['t'] < 8:
            sol = n_b_c(coef, set, sol, n_o, b_o, c_o, ma_o)
#         else:
#             sol = n_b_c_stop(coef, set, sol, n_o, b_o, c_o, ma_o)
    else:
        sol = n_b_c(coef, set, sol, n_o, b_o, c_o, ma_o)
                     
    return sol