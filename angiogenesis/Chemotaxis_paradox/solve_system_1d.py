from random import randint, sample, uniform
import numpy
import math as m

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
                if not set['Model'] == 'normal':
                    Ki_p = coef['Ki_n']*(sol['al'][x-1])**(coef['m'])/((coef['A'])**(coef['m'])+(sol['al'][x-1])**(coef['m']))
                cijx_p, cijx_n = max_min_c(set,sol,x,c_o) #2.3.(1).(1)
                if not set['Model'] == 'normal':
                    G_plus_1 = Ki_p*cijx_p
                else:
                    G_plus_1 = coef['Ki_n']*cijx_p
                
                if not set['Model'] == 'normal':
                    Ki_n = coef['Ki_n']*(sol['al'][x+1])**(coef['m'])/((coef['A'])**(coef['m'])+(sol['al'][x+1])**(coef['m']))
                cijx_p, cijx_n = max_min_c(set,sol,x+2,c_o) #2.3.(1).(1)
                if not set['Model'] == 'normal':
                    G_neg_1 = Ki_n*cijx_n
                else:
                    G_neg_1 = coef['Ki_n']*cijx_n
                
                F_sol_1[x] = -coef['D_n']/(set['h'])*(n_o[x+1]-n_o[x-1])+n_o[x-1]*G_plus_1-n_o[x+1]*G_neg_1
#                 if not F_sol_1[x] == 0:
#                     print 'F_sol', F_sol_1[x]
                
    return F_sol_1    

def H_vector_sol(coef,set,sol,n_o,b_o,c_o):
    H_sol_1 = numpy.zeros(set['Nx']+1)
    G_plus_1 = 0
    G_neg_1 = 0
    for x in range(0,set['Nx']+1,2):
        if not x == 0:
            if not x == set['Nx']:
                cijx_p, cijx_n = max_min_c(set,sol,x,c_o) #2.3.(1).(1)
                c_mean = (c_o[x]+c_o[x-2])/2
                G_plus_1 = coef['Xi_n']*cijx_p*c_mean/((cijx_p)**2+coef['xi'])
#                 if set['dt']*set['k'] > 0.1:
#                     if not cijx_p == 0:
#                         print 'p',cijx_p, c_mean, n_o[x-1], G_plus_1, (n_o[x-1])**2*G_plus_1
                
                cijx_p, cijx_n = max_min_c(set,sol,x+2,c_o) #2.3.(1).(1)
                c_mean = (c_o[x+2]+c_o[x])/2
                G_neg_1 = coef['Xi_n']*cijx_n*c_mean/((cijx_n)**2+coef['xi'])
#                 if set['dt']*set['k'] > 0.1:
#                     if not cijx_n == 0:
#                         print 'n',cijx_n, c_mean, n_o[x+1], G_neg_1, (n_o[x+1])**2*G_neg_1
                
                H_sol_1[x] = (n_o[x-1])**2*G_plus_1-(n_o[x+1])**2*G_neg_1
                
#                 if not H_sol_1[x] == 0:
#                     print 'H_sol', H_sol_1[x]
    return H_sol_1   
    
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

def n_b_c(coef, set, sol, n_o, b_o, c_o, al_o, branching_par = 0, branching = False):
    F_sol_1 = F_vector_sol(coef, set, sol, n_o, b_o, c_o)
    H_sol_1 = H_vector_sol(coef, set, sol, n_o, b_o, c_o)
     
    '''Solve b, n at main lattice'''    
    for x in range(1,set['Nx'],2):    
        if not set['Model'] == 'normal':  
            kinetic_al = - coef['f_p']*sol['al'][x] + coef['f_n']*(1-sol['al'][x])
            ##alpha
            F_mean = (F_sol_1[x+1] + F_sol_1 [x-1])/2
            vel_al = F_mean/(sol['n'][x]+0.001)
            vl_left = 0
            vl_right = 0
            if vel_al > 0:
                vl_left = vel_al
            if vel_al < 0:
                vl_right = vel_al*(-1)
        
        if x == 1:
            n_mean_i = n_mean_function(set,sol,x,n_o)
            n_mean_ip1 = n_mean_function(set,sol,x+2,n_o)
            move_n = set['dt']*(F_sol_1[x+1])/set['h']
            chemotaxis_n = set['dt']*(H_sol_1[x+1])/set['h']
            
            if not set['Model'] == 'normal':
                ##alpha
                move_al = set['dt']*(vl_right*(al_o[x+2]-al_o[x]))/set['h']
            
            ##Stalk Vel grad n
            move_b = set['dt']*coef['Ki_b']*((b_o[x]*max((n_mean_i[1]-n_mean_i[0])/set['h'],0)-b_o[x+2]*max(-(n_mean_ip1[1]-n_mean_ip1[0])/set['h'],0)))/set['h'] - coef['D_b']*set['dt']*(b_o[x+2]-b_o[x])/(set['h']**2)

        elif x == set['Nx']-1:
            n_mean_i = n_mean_function(set,sol,x,n_o)
            n_mean_in1 = n_mean_function(set,sol,x-2,n_o)
            move_n = set['dt']*(-F_sol_1[x-1])/set['h']
            chemotaxis_n = set['dt']*(-H_sol_1[x-1])/set['h']
            
            if not set['Model'] == 'normal':
                ##alpha
                move_al = set['dt']*(vl_left*(al_o[x]-al_o[x-2]))/set['h']
            
            ##Stalk Vel grad n
            move_b = set['dt']*coef['Ki_b']*(-(b_o[x-2]*max((n_mean_in1[1]-n_mean_in1[0])/set['h'],0)-b_o[x]*max(-(n_mean_i[1]-n_mean_i[0])/set['h'],0)))/set['h'] - coef['D_b']*set['dt']*(b_o[x-2]-b_o[x])/(set['h']**2)
            ##Stalk Vel positive grad c
#             move_b = set['dt']*coef['Ki_b']*(-(b_o[x-2]*max((c_o[x-1]-c_o[x-3])/set['h'],0)-b_o[x]*max(-(c_o[x+1]-c_o[x-1])/set['h'],0)))/set['h']
        else:
            n_mean_i = n_mean_function(set,sol,x,n_o)
            n_mean_ip1 = n_mean_function(set,sol,x+2,n_o)
            n_mean_in1 = n_mean_function(set,sol,x-2,n_o)
            move_n = set['dt']*(F_sol_1[x+1]-F_sol_1[x-1])/set['h']
            chemotaxis_n = set['dt']*(H_sol_1[x+1]-H_sol_1[x-1])/set['h']
            
            if not set['Model'] == 'normal':
                ##alpha
                move_al = set['dt']*(vl_left*(al_o[x]-al_o[x-2]) + vl_right*(al_o[x+2]-al_o[x]))/set['h']
            
            ##Stalk Vel grad n
            move_b = set['dt']*coef['Ki_b']*((b_o[x]*max((n_mean_i[1]-n_mean_i[0])/set['h'],0)-b_o[x+2]*max(-(n_mean_ip1[1]-n_mean_ip1[0])/set['h'],0))-(b_o[x-2]*max((n_mean_in1[1]-n_mean_in1[0])/set['h'],0)-b_o[x]*max(-(n_mean_i[1]-n_mean_i[0])/set['h'],0)))/set['h'] - coef['D_b']*set['dt']*(b_o[x-2]+b_o[x+2]-2*b_o[x])/(set['h']**2)
            ##Stalk Vel positive grad c
#             move_b = set['dt']*coef['Ki_b']*((b_o[x]*max((c_o[x+1]-c_o[x-1])/set['h'],0)-b_o[x+2]*max(-(c_o[x+3]-c_o[x+1])/set['h'],0))-(b_o[x-2]*max((c_o[x-1]-c_o[x-3])/set['h'],0)-b_o[x]*max(-(c_o[x+1]-c_o[x-1])/set['h'],0)))/set['h']
        sol['n'][x] = n_o[x] - move_n# + chemotaxis_n # + kinetic_n
        sol['b'][x] = b_o[x] - move_b# + kinetic_b
        if not set['Model'] == 'normal':
            sol['al'][x] = al_o[x] - move_al + kinetic_al
            sol['n'][x] = n_o[x] - move_n
        else:
            sol['n'][x] = n_o[x] - coef['alpha']*move_n + coef['beta']*chemotaxis_n
        if chemotaxis_n > 0.001:
            print 'chemo_n', chemotaxis_n, 'move', move_n
#         if not sol['n'][x] == 0:
#             if not sol['c'][x+1] == 0:
#                 print move_n, chemotaxis_n
#             if not sol['c'][x-1] == 0:
#                 print move_n, chemotaxis_n
                     
    '''Solve c at sub lattice'''
    for x in range(0,set['Nx']+1,2):
#         sol['c'][x] = 0.5*(numpy.sin(2*m.pi/(coef['la'])*x*set['Hh']-2*m.pi/(coef['pe'])*set['dt']*set['k'])) 
#         if sol['c'][x] < 0:
#             sol['c'][x] *= 0
        sol['c'][x] = 0.5*m.exp(-(x*set['Hh']-coef['vel']*set['dt']*set['k'])**2/0.02)
        for i in range(1,100):
            sol['c'][x] += 0.5*m.exp(-(x*set['Hh']+i*coef['perio']-coef['vel']*set['dt']*set['k'])**2/0.02)        
    return sol

def system_1d(coef, set, sol): #2.3
    c_o = numpy.copy(sol['c']) #to save values at time step k (we are calculating at time step k+1)
    n_o = numpy.copy(sol['n']) 
    b_o = numpy.copy(sol['b'])
    if not set['Model'] == 'normal':
        al_o = numpy.copy(sol['al'])
    else:
        al_o = 0
    sol = n_b_c(coef, set, sol, n_o, b_o, c_o, al_o)
                     
    return sol