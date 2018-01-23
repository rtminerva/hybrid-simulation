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
# #         sol['c'][x] = 0.5*(numpy.sin(2*m.pi/(coef['la'])*x*set['Hh']-2*m.pi/(coef['pe'])*set['dt']*set['k'])) 
# #         if sol['c'][x] < 0:
# #             sol['c'][x] *= 0
        sol['c'][x] = coef['A_c']*m.exp(-(x*set['Hh']+(1)*set['rad']-coef['vel']*set['t'])**2/coef['vari'])
        for i in range(1,100):
            sol['c'][x] += coef['A_c']*m.exp(-(x*set['Hh']+(1)*set['rad']+i*coef['perio']-coef['vel']*set['t'])**2/coef['vari'])        
 
    
    
#     '''Different Var'''
#     dd = 0
#     x = 0
#     while dd == 0 and x <= set['Nx']:
#         if sol['c'][x] == coef['A_c']:
#             dd = 1
#         elif sol['c'][x] < coef['A_c']:
#             vari = 0.1
#             sol['c'][x] = coef['A_c']*m.exp(-(x*set['Hh']+(-3)*set['rad']-coef['vel']*set['t'])**2/vari)#0.05 set['dt']*set['k']
#             for i in range(1,100):
#                 sol['c'][x] += coef['A_c']*m.exp(-(x*set['Hh']+(-3)*set['rad']+i*coef['perio']-coef['vel']*set['t'])**2/vari)
#             x += 2
    
    return sol

def system_1d(coef, set, sol): #2.3
    c_o = numpy.copy(sol['c']) #to save values at time step k (we are calculating at time step k+1)
    sol = c_(coef, set, sol, c_o)
    
    '''Calculate Velocity of cell at n_p'''
    n_p = sol['n'][-1]
    print 'Position cell now:', n_p
    c_t_f = (sol['c'][n_p+1]-c_o[n_p+1])/set['dt']
    c_t_b = (sol['c'][n_p-1]-c_o[n_p-1])/set['dt']
    c_t_x = (c_t_f-c_t_b)/set['h']
    sol['vel_n'].append(c_t_x)  
    
    
    sol['c_x'].append(c_grad)
    sol['c_'].append(c_mean)
    
    print '-----------------'
    print 'c_x', c_grad
    print 'velocity_value', sol['vel_n'][-1]
    print '-----------------'
    
    '''Diffusion term'''
    p_1 = coef['D_n']*set['dt']/(set['h']**2)
    p_2 = p_1
    
    '''Adaptive term'''
    if sol['vel_n'][-1] < 0:
        p_1 += set['dt']/(set['h'])*(-sol['vel_n'][-1])
    else:
        p_2 += set['dt']/(set['h'])*(sol['vel_n'][-1])
    p_0 = 1-(p_1+p_2)    
    print 'prob', p_0,',', p_1, ',', p_2
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
#     print dirr  
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
    
    
                     
    return sol