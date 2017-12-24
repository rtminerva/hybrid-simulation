from random import randint, sample, uniform
import numpy
import math as m
import random
from random import randint

def set_list_prob(dirr): #2.2.(1)
    line_1 = range(1,10001)
    if dirr[1] == 0:
        list_prob_1 = []
    else:
        list_prob_1 = random.sample(line_1, dirr[1])
        for i in list_prob_1:
            line_1.remove(i)
    if dirr[2] == 0:
        list_prob_2 = []
    else:
        list_prob_2 = random.sample(line_1, dirr[2])
        for i in list_prob_2:
            line_1.remove(i)
    list_prob_0 = line_1
    return list_prob_0,list_prob_1,list_prob_2

def c_(coef, set, sol, c_o):              
    '''Calculate c at sub lattice'''
    for x in range(0,set['Nx']+1,2):
#         sol['c'][x] = 0.5*(numpy.sin(2*m.pi/(coef['la'])*x*set['Hh']-2*m.pi/(coef['pe'])*set['dt']*set['k'])) 
#         if sol['c'][x] < 0:
#             sol['c'][x] *= 0
        sol['c'][x] = coef['A_c']*m.exp(-(x*set['Hh']+(-1.5)*set['rad']-coef['vel']*set['t'])**2/coef['vari'])
        for i in range(1,100):
            sol['c'][x] += coef['A_c']*m.exp(-(x*set['Hh']+(-1.5)*set['rad']+i*coef['perio']-coef['vel']*set['t'])**2/coef['vari'])        
    return sol

def system_1d(coef, set, sol): #2.3
    c_o = numpy.copy(sol['c']) #to save values at time step k (we are calculating at time step k+1)
    
    '''Calculate Velocity of cell at n_p'''
    n_p = sol['n'][-1]
    print 'Position cell now:', n_p
    c_mean = (c_o[n_p+1]+c_o[n_p-1])/2
    c_grad = (c_o[n_p+1]-c_o[n_p-1])/(set['h'])
    a_per_b = c_mean/()
#     if c_grad < 0:
#         coef['alpha']
#     elif c_grad > 0:
    '''Metode c_t = cn'''    
#     sol['vel_n'].append((coef['alpha'] - (coef['beta']*c_mean/((c_grad)**2+coef['xi'])))*c_grad) #SOL N_P = 1
#     sol['in_vel_n'].append((coef['alpha'] - (coef['beta']*c_mean/((c_grad)**2+coef['xi']))))
#     sol['a_per_b'].append(c_mean/((c_grad)**2+coef['xi']))
    
    '''Metode c_t = -w c_x'''
    sol['vel_n'].append((coef['alpha'] - (coef['beta']*coef['vel']*c_grad/((c_grad)**2+coef['xi'])))*c_grad)
    sol['in_vel_n'].append((coef['alpha'] - (coef['beta']*coef['vel']*c_grad/((c_grad)**2+coef['xi']))))
    sol['a_per_b'].append(coef['vel']*c_grad/((c_grad)**2+coef['xi']))    
        
    sol['c_x'].append(c_grad)
    sol['c_'].append(c_mean)
    

    print 'velocity_value', sol['vel_n'][-1]
    
    '''Diffusion term'''
    p_1 = coef['D_n']*set['dt']/(set['h']**2)
    p_2 = p_1
    
    '''Adaptive term'''
    if sol['vel_n'][-1] < 0:
        p_1 += set['dt']/(set['h'])*(-sol['vel_n'][-1])
    else:
        p_2 += set['dt']/(set['h'])*(sol['vel_n'][-1])
    p_0 = 1-(p_1+p_2)    
    print p_0,',', p_1, ',', p_2
    '''create integer number based on probability value'''
    P_1 = int(p_1*10000)
    P_2 = int(p_2*10000)
    
    '''boundary checking'''
    if n_p == 1:
        P_1 = 0
    elif n_p == set['Nx']-1:
        P_2 = 0
    P_0 = 10000-(P_1+P_2)
    
    '''Probability value'''
    dirr = [P_0, P_1, P_2]  
    print dirr  
    list_prob_0,list_prob_1,list_prob_2 = set_list_prob(dirr)  
    
    '''Decide movement''' 
    tes = randint(1,10000)
    if tes in list_prob_0:
        sol['n'].append(sol['n'][-1])
        print 'stay'
    elif tes in list_prob_1:
        sol['n'].append(sol['n'][-1]-2)
        print 'left'
    elif tes in list_prob_2:
        sol['n'].append(sol['n'][-1]+2)
        print 'right'

    sol = c_(coef, set, sol, c_o)
    
    
                     
    return sol