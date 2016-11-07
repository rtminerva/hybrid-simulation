import numpy
import math as m
from collections import OrderedDict

def rec_1_tip(coef,set,sol): #2.1.2.(1)
    y = set['Ny']/2 
    if y % 2 == 0:
        y += 1
    sol['matrix_tip'].append([(11,y)])
    sol['n'][11,y] = 1
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    return sol

def rec_5_tip(coef,set,sol): #2.1.2.(2)
    '''Tip 0'''
    y = set['Ny']/6
    if y % 2 == 0:
        y += 1
    sol['matrix_tip'].append([(11,y-24)])
    sol['n'][11,y-24] = 1
    for x in range(1,10,2):
        sol['b'][x,y-18] = 0.7
        sol['b'][x,y-20] = 0.8
        sol['b'][x,y-22] = 0.9
        sol['b'][x,y-24] = 1
        sol['b'][x,y-26] = 0.9
        sol['b'][x,y-28] = 0.8
        sol['b'][x,y-30] = 0.7

    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    sol['life_mit'].append(0)
    
    '''TIP 1'''
    y1 = 2*y
    if y1 % 2 == 0:
        y1 += 1
    sol['matrix_tip'].append([(11,y1-14)])
    sol['n'][11,y1-14] = 1
    for x in range(1,10,2):
        sol['b'][x,y1-8] = 0.7
        sol['b'][x,y1-10] = 0.8
        sol['b'][x,y1-12] = 0.9
        sol['b'][x,y1-14] = 1
        sol['b'][x,y1-16] = 0.9
        sol['b'][x,y1-18] = 0.8
        sol['b'][x,y1-20] = 0.7
    
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    sol['life_mit'].append(0)
    
    '''TIP 2'''
    y2 = 3*y
    if y2 % 2 == 0:
        y2 += 1
    sol['matrix_tip'].append([(11,y2)])
    sol['n'][11,y2] = 1
    for x in range(1,10,2):
        sol['b'][x,y2-6] = 0.7
        sol['b'][x,y2-4] = 0.8
        sol['b'][x,y2-2] = 0.9
        sol['b'][x,y2] = 1
        sol['b'][x,y2+2] = 0.9
        sol['b'][x,y2+4] = 0.8
        sol['b'][x,y2+6] = 0.7
        
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    sol['life_mit'].append(0)
    
    '''TIP 3'''
    y2 = 4*y
    if y2 % 2 == 0:
        y2 += 1
    sol['matrix_tip'].append([(11,y2+14)])
    sol['n'][11,y2+14] = 1
    for x in range(1,10,2):
        sol['b'][x,y2+8] = 0.7
        sol['b'][x,y2+10] = 0.8
        sol['b'][x,y2+12] = 0.9
        sol['b'][x,y2+14] = 1
        sol['b'][x,y2+16] = 0.9
        sol['b'][x,y2+18] = 0.8
        sol['b'][x,y2+20] = 0.7
    
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    sol['life_mit'].append(0)
    
    '''TIP 4'''
    y2 = 5*y
    if y2 % 2 == 0:
        y2 += 1
    sol['matrix_tip'].append([(11,y2+24)])
    sol['n'][11,y2+24] = 1
    for x in range(1,10,2):
        sol['b'][x,y2+18] = 0.7
        sol['b'][x,y2+20] = 0.8
        sol['b'][x,y2+22] = 0.9
        sol['b'][x,y2+24] = 1
        sol['b'][x,y2+26] = 0.9
        sol['b'][x,y2+28] = 0.8
        sol['b'][x,y2+30] = 0.7
    
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    sol['life_mit'].append(0)
    
    return sol

def init_tip_2d_(coef,set,sol):
    sol['n'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['b'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['matrix_tip'] = []
    sol['list_tip_movement'] = []
    sol['life_time_tip'] = []
    sol['life_mit'] = []
    sol['sp_stop'] = []
    sol['tip_cell'] = []
    sol['PP'] =[]
    sol['pp'] =OrderedDict()
    
    if set['initial_prof'] == 'rectangular_1_tip':
        sol = rec_1_tip(coef,set,sol) #2.1.2.(1)
    elif set['initial_prof'] == 'rectangular_tip':
        sol = rec_5_tip(coef,set,sol) #2.1.2.(2)
        tip = 5
        
    '''Identifying Tip Cell'''
    for e,ti in enumerate(sol['matrix_tip']):
        sol['tip_cell'].append([sol['matrix_tip'][e][-1][0],sol['matrix_tip'][e][-1][1]])
    return sol