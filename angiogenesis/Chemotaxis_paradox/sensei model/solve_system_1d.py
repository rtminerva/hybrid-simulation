from random import randint, sample, uniform
import numpy
import math as m

def max_min_c(set,sol,x,c_o): #2.3.(1).(1)
    cijx = (c_o[x]-c_o[x-2])/(set['h'])
    cijx_p = max(0,cijx)
    cijx_n = max(0,-cijx)
    return cijx_p, cijx_n

def F_vector_sol(coef,set,sol,n_o,c_o): #2.3.(1)
    F_sol_1 = numpy.zeros(set['Nx']+1)
    G_plus_1 = 0
    G_neg_1 = 0
    for x in range(0,set['Nx']+1,2):
        if not x == 0:
            if not x == set['Nx']:
                cijx_p, cijx_n = max_min_c(set,sol,x,c_o) #2.3.(1).(1)
                G_plus_1 = coef['Ki_n']*cijx_p
                
                cijx_p, cijx_n = max_min_c(set,sol,x+2,c_o) #2.3.(1).(1)
                G_neg_1 = coef['Ki_n']*cijx_n
                
                F_sol_1[x] = -coef['D_n']/(set['h'])*(n_o[x+1]-n_o[x-1])+n_o[x-1]*G_plus_1-n_o[x+1]*G_neg_1
                
    return F_sol_1    

def H_vector_sol(coef,set,sol,n_o,c_o):
    H_sol_1 = numpy.zeros(set['Nx']+1)
    G_plus_1 = 0
    G_neg_1 = 0
    for x in range(0,set['Nx']+1,2):
        if not x == 0:
            if not x == set['Nx']:
                cijx_p, cijx_n = max_min_c(set,sol,x,c_o) #2.3.(1).(1)
                c_mean = (c_o[x]+c_o[x-2])/2
                G_plus_1 = coef['Xi_n']*cijx_p*c_mean/((cijx_p)**2+coef['xi'])
                
                cijx_p, cijx_n = max_min_c(set,sol,x+2,c_o) #2.3.(1).(1)
                c_mean = (c_o[x+2]+c_o[x])/2
                G_neg_1 = coef['Xi_n']*cijx_n*c_mean/((cijx_n)**2+coef['xi'])

                H_sol_1[x] = (n_o[x-1])**2*G_plus_1-(n_o[x+1])**2*G_neg_1
                
    return H_sol_1      

def n_b_c(coef, set, sol, n_o, c_o):
    F_sol_1 = F_vector_sol(coef, set, sol, n_o, c_o)
    H_sol_1 = H_vector_sol(coef, set, sol, n_o, c_o)
     
    '''Solve n at main lattice'''    
    for x in range(1,set['Nx'],2):           
        if x == 1:
            move_n = set['dt']*(F_sol_1[x+1])/set['h']
            chemotaxis_n = set['dt']*(H_sol_1[x+1])/set['h']
        elif x == set['Nx']-1:
            move_n = set['dt']*(-F_sol_1[x-1])/set['h']
            chemotaxis_n = set['dt']*(-H_sol_1[x-1])/set['h']
        else:
            move_n = set['dt']*(F_sol_1[x+1]-F_sol_1[x-1])/set['h']
            chemotaxis_n = set['dt']*(H_sol_1[x+1]-H_sol_1[x-1])/set['h']
        sol['n'][x] = n_o[x] - coef['alpha']*move_n + coef['beta']*chemotaxis_n
        if chemotaxis_n > 0.001:
            print 'chemo_n', chemotaxis_n, 'move', move_n
                     
    '''Calculate c at sub lattice'''
    for x in range(0,set['Nx']+1,2):
#         sol['c'][x] = 0.5*(numpy.sin(2*m.pi/(coef['la'])*x*set['Hh']-2*m.pi/(coef['pe'])*set['dt']*set['k'])) 
#         if sol['c'][x] < 0:
#             sol['c'][x] *= 0
        sol['c'][x] = coef['A_c']*m.exp(-(x*set['Hh']-coef['vel']*set['dt']*set['k'])**2/0.02)
        for i in range(1,100):
            sol['c'][x] += coef['A_c']*m.exp(-(x*set['Hh']+i*coef['perio']-coef['vel']*set['dt']*set['k'])**2/0.02)        
    return sol

def system_1d(coef, set, sol): #2.3
    c_o = numpy.copy(sol['c']) #to save values at time step k (we are calculating at time step k+1)
    n_o = numpy.copy(sol['n']) 
    sol = n_b_c(coef, set, sol, n_o, c_o)
                     
    return sol