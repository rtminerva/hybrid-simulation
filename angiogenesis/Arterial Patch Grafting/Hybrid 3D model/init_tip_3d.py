import numpy
import math as m
from collections import OrderedDict

def rec_5_tip(coef,set,sol,z):
    '''Tip 0'''
    y = set['Ny']/6
    if y % 2 == 0:
        y += 1
    sol['matrix_tip'].append([(1,y,z)])
    sol['n'][1,y,z] = 1
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    
    '''TIP 1'''
    y1 = 2*y
    if y1 % 2 == 0:
        y1 += 1
    sol['matrix_tip'].append([(1,y1,z)])
    sol['n'][1,y1,z] = 1
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    
    '''TIP 2'''
    y2 = 3*y
    if y2 % 2 == 0:
        y2 += 1
    sol['matrix_tip'].append([(1,y2,z)])
    sol['n'][1,y2,z] = 1
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    
    '''TIP 3'''
    y2 = 4*y
    if y2 % 2 == 0:
        y2 += 1
    sol['matrix_tip'].append([(1,y2,z)])
    sol['n'][1,y2,z] = 1
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    
    '''TIP 4'''
    y2 = 5*y
    if y2 % 2 == 0:
        y2 += 1
    sol['matrix_tip'].append([(1,y2,z)])
    sol['n'][1,y2,z] = 1
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    return sol

def init_tip_3d_(coef,set,sol):
    sol['n'] = numpy.zeros((set['Nx']+1,set['Ny']+1,set['Nz']+1))   
    sol['cn'] = numpy.zeros((set['Nx']+1,set['Ny']+1,set['Nz']+1)) 
    sol['stalk'] = numpy.zeros((set['Nx']+1,set['Ny']+1,set['Nz']+1))
    sol['matrix_tip'] = []
    sol['list_tip_movement'] = []
    sol['life_time_tip'] = []
    sol['sp_stop'] = []
    sol['tip_cell'] = []
    
    z = set['Nz']/2 
    if z % 2 == 0:
        z += 1
    sol = rec_5_tip(coef,set,sol,z)
        
    '''Identifying Tip Cell'''
    for e,ti in enumerate(sol['matrix_tip']):
        sol['tip_cell'].append([sol['matrix_tip'][e][-1][0],sol['matrix_tip'][e][-1][1],sol['matrix_tip'][e][-1][2]])
    for i in sol['tip_cell']:
        sol['cn'][i[0]-1,i[1]-1,i[2]-1] = sol['c'][i[0]-1,i[1]-1,i[2]-1]
        sol['cn'][i[0]+1,i[1]-1,i[2]-1] = sol['c'][i[0]+1,i[1]-1,i[2]-1]
        sol['cn'][i[0]+1,i[1]+1,i[2]-1] = sol['c'][i[0]+1,i[1]+1,i[2]-1]
        sol['cn'][i[0]-1,i[1]+1,i[2]-1] = sol['c'][i[0]-1,i[1]+1,i[2]-1]
        sol['cn'][i[0]-1,i[1]-1,i[2]+1] = sol['c'][i[0]-1,i[1]-1,i[2]+1]
        sol['cn'][i[0]+1,i[1]-1,i[2]+1] = sol['c'][i[0]+1,i[1]-1,i[2]+1]
        sol['cn'][i[0]+1,i[1]+1,i[2]+1] = sol['c'][i[0]+1,i[1]+1,i[2]+1]
        sol['cn'][i[0]-1,i[1]+1,i[2]+1] = sol['c'][i[0]-1,i[1]+1,i[2]+1]
    return sol