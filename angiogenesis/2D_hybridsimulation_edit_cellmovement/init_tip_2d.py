import numpy
import math as m
from collections import OrderedDict
import random
from random import randint

 
# def rec_5_tip(coef,set,sol): 
#     x = int(set['rad']/set['Hh'])
#     if x % 2 == 0:
#         x += 1
#     '''Tip 0'''
#     y = set['Ny']/6
#     if y % 2 == 0:
#         y += 1
#     sol['matrix_tip'].append([[x,y-24]])
#     sol['n'][1,y-24] = 1
#     sol['list_tip_movement'].append('start') #movement tip
#     sol['life_time_tip'].append(0) #lifetime
#     
#     '''TIP 1'''
#     y1 = 2*y
#     if y1 % 2 == 0:
#         y1 += 1
#     sol['matrix_tip'].append([[x,y1-14]])
#     sol['n'][1,y1-14] = 1
#     sol['list_tip_movement'].append('start') #movement tip
#     sol['life_time_tip'].append(0) #lifetime
#     
#     '''TIP 2'''
#     y2 = 3*y
#     if y2 % 2 == 0:
#         y2 += 1
#     sol['matrix_tip'].append([[x,y2]])
#     sol['n'][1,y2] = 1
#     sol['list_tip_movement'].append('start') #movement tip
#     sol['life_time_tip'].append(0) #lifetime
#     
#     '''TIP 3'''
#     y2 = 4*y
#     if y2 % 2 == 0:
#         y2 += 1
#     sol['matrix_tip'].append([[x,y2+14]])
#     sol['n'][1,y2+14] = 1
#     sol['list_tip_movement'].append('start') #movement tip
#     sol['life_time_tip'].append(0) #lifetime
#     
#     '''TIP 4'''
#     y2 = 5*y
#     if y2 % 2 == 0:
#         y2 += 1
#     sol['matrix_tip'].append([[x,y2+24]])
#     sol['n'][1,y2+24] = 1
#     sol['list_tip_movement'].append('start') #movement tip
#     sol['life_time_tip'].append(0) #lifetime
#     
#     return sol

def random_tip(coef,set,sol): #Ref.2.2.1
    line = range(1,set['Ny'],2)
    x = 1#int(coef['X']/set['Hh']) #set the initial tip cell at the left boundary
    if x % 2 == 0:
        x -= 1    
    for i in range(0,10):
        y = random.choice(line)
        sol['n'][x,y] = 1
        sol['matrix_tip'].append([[x,y]])
        sol['list_tip_movement'].append('start') #movement tip
        sol['life_time_tip'].append(0) #lifetime
        line.remove(y)
    return sol

def rec_1_tip(coef,set,sol): #Ref.2.2.1
    y = set['Ny']/2 
    if y % 2 == 0:
        y += 1  
    sol['n'][1,y] = 1
    sol['matrix_tip'].append([[1,y]])
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    return sol

def init_tip_2d_(coef,set,sol): #Ref.2.2
    '''Create new variable to store solutions'''
    sol['n'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['stalk'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    
    sol['matrix_tip'] = [] #record of tip pathway
    sol['list_tip_movement'] = [] #record of tip cell movement
    sol['life_time_tip'] = [] #record of life time of each tip cell
    
    #for anastomosis tip-tip
    sol['pair_tiptotip1'] = []
    sol['new_ves_pair'] = []
    
    sol['tip_cell'] = [] #record of tip cell position
    sol['sp_stop'] = []
    
    '''Define tip cell'''
    sol = rec_1_tip(coef,set,sol) #Ref.2.2.1
#     sol = rec_5_tip(coef,set,sol) #2.1.2.(2)
#     sol = random_tip(coef,set,sol) #Ref.2.2.1
    
    '''TIP CELL'''
    for ind_i, i in enumerate(sol['matrix_tip']):
        sol['tip_cell'].append(i[-1])
    
    return sol