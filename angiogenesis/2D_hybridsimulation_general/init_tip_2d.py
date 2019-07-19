import numpy
import math as m
from collections import OrderedDict
import random
from random import randint

def rec_1_tip(coef,set,sol): #2.1.2.(1)
    y = set['Ny']/2 
    if y % 2 == 0:
        y += 1
    sol['matrix_tip'].append([[1,y]]) #should be on main-lattice (odd numbers)
    sol['n'][1,y] = 1
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    return sol

def random_tip(coef,set,sol): #2.1.2.(2)
    line = range(1,set['Ny'],2)
#     x = int(set['rad']/set['Hh'])
    x = int(coef['X']/set['Hh'])
    if x % 2 == 0:
        x -= 1
    
#     y = set['Ny']/2
#     if y % 2 == 0:
#         y += 1
#         
#     sol['matrix_tip'].append([[x,y]])
#     sol['n'][x,y] = 1
#     sol['list_tip_movement'].append('start') #movement tip
#     sol['life_time_tip'].append(0) #lifetime
    
    for i in range(0,20):
        y = random.choice(line)
        sol['matrix_tip'].append([[x,y]])
        sol['n'][x,y] = 1
        sol['list_tip_movement'].append('start') #movement tip
        sol['life_time_tip'].append(0) #lifetime
        line.remove(y)
    return sol

def rec_5_tip(coef,set,sol): #2.1.2.(2)
    x = int(set['rad']/set['Hh'])
    if x % 2 == 0:
        x += 1
    '''Tip 0'''
    y = set['Ny']/6
    if y % 2 == 0:
        y += 1
    sol['matrix_tip'].append([[x,y-24]])
    sol['n'][1,y-24] = 1
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    
    '''TIP 1'''
    y1 = 2*y
    if y1 % 2 == 0:
        y1 += 1
    sol['matrix_tip'].append([[x,y1-14]])
    sol['n'][1,y1-14] = 1
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    
    '''TIP 2'''
    y2 = 3*y
    if y2 % 2 == 0:
        y2 += 1
    sol['matrix_tip'].append([[x,y2]])
    sol['n'][1,y2] = 1
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    
    '''TIP 3'''
    y2 = 4*y
    if y2 % 2 == 0:
        y2 += 1
    sol['matrix_tip'].append([[x,y2+14]])
    sol['n'][1,y2+14] = 1
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    
    '''TIP 4'''
    y2 = 5*y
    if y2 % 2 == 0:
        y2 += 1
    sol['matrix_tip'].append([[x,y2+24]])
    sol['n'][1,y2+24] = 1
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    
    return sol

def init_tip_2d_(coef,set,sol):
    '''Create new variable to store solutions'''
    sol['n'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['stalk'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    
    sol['pair_tiptotip1'] = []
    sol['new_ves_pair'] = []
    sol['matrix_tip'] = []
    sol['list_tip_movement'] = []
    sol['life_time_tip'] = []
    sol['sp_stop'] = []
    sol['tip_cell'] = []
    
    '''Define tip cell'''
#     sol = rec_1_tip(coef,set,sol) #2.1.2.(1)
#     sol = rec_5_tip(coef,set,sol) #2.1.2.(2)
    sol = random_tip(coef,set,sol)
    
    '''TIP CELL'''
    for ind_i, i in enumerate(sol['matrix_tip']):
        if len(i) > 1:
            if isinstance(i[-1], int) == True: #sprout yang masih hidup
                sol['tip_cell'].append(i[-2])
            else:
                sol['tip_cell'].append(i[-1])
        else:
            sol['tip_cell'].append(i[-1])
    return sol