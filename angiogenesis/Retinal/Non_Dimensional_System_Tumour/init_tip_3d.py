import numpy

def rec_1_tip(coef,set,sol,z):
    y = set['Ny']/2 
    if y % 2 == 0:
        y += 1
    sol['matrix_tip'].append([(1,y,z)])
    sol['n'][1,y,z] = 1
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    return sol

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

def rec_5_tip_ar(coef,set,sol,z):
    '''Tip 0'''
    y = set['Ny']/6
    if y % 2 == 0:
        y += 1
    sol['matrix_tip_2'].append([(1,y,z)])
    sol['n'][1,y,z] = 1
    sol['list_tip_movement_2'].append('start') #movement tip
    sol['life_time_tip_2'].append(0) #lifetime
    
    '''TIP 1'''
    y1 = 2*y
    if y1 % 2 == 0:
        y1 += 1
    sol['matrix_tip_2'].append([(1,y1,z)])
    sol['n'][1,y1,z] = 1
    sol['list_tip_movement_2'].append('start') #movement tip
    sol['life_time_tip_2'].append(0) #lifetime
    
    '''TIP 2'''
    y2 = 3*y
    if y2 % 2 == 0:
        y2 += 1
    sol['matrix_tip_2'].append([(1,y2,z)])
    sol['n'][1,y2,z] = 1
    sol['list_tip_movement_2'].append('start') #movement tip
    sol['life_time_tip_2'].append(0) #lifetime
    
    '''TIP 3'''
    y2 = 4*y
    if y2 % 2 == 0:
        y2 += 1
    sol['matrix_tip_2'].append([(1,y2,z)])
    sol['n'][1,y2,z] = 1
    sol['list_tip_movement_2'].append('start') #movement tip
    sol['life_time_tip_2'].append(0) #lifetime
    
    '''TIP 4'''
    y2 = 5*y
    if y2 % 2 == 0:
        y2 += 1
    sol['matrix_tip_2'].append([(1,y2,z)])
    sol['n'][1,y2,z] = 1
    sol['list_tip_movement_2'].append('start') #movement tip
    sol['life_time_tip_2'].append(0) #lifetime
    return sol

def rec_tip_two_parent(coef,set,sol,z):
    '''Vein'''
    sol = rec_5_tip(coef,set,sol,z)
    '''Artery'''
    z *= 3
    sol = rec_5_tip_ar(coef,set,sol,z)
    return sol

def init_tip_3d_(coef,set,sol):
    sol['n'] = numpy.zeros((set['Nx']+1,set['Ny']+1,set['Nz']+1))
    sol['matrix_tip'] = []
    sol['list_tip_movement'] = []
    sol['life_time_tip'] = []
    sol['sp_stop'] = []
    sol['tip_cell'] = []
    
    if set['parent'] == 'two':
        sol['matrix_tip_2'] = []
        sol['list_tip_movement_2'] = []
        sol['life_time_tip_2'] = []
        sol['sp_stop_2'] = []
        sol['tip_cell_2'] = []
        z = set['Nz']/4 
        if z % 2 == 0:
            z += 1
        sol = rec_tip_two_parent(coef,set,sol,z)
        '''Identifying Tip Cell'''
        for e,ti in enumerate(sol['matrix_tip']):
            sol['tip_cell'].append([sol['matrix_tip'][e][-1][0],sol['matrix_tip'][e][-1][1]])
        '''Identifying Tip Cell 2'''
        for e,ti in enumerate(sol['matrix_tip_2']):
            sol['tip_cell_2'].append([sol['matrix_tip_2'][e][-1][0],sol['matrix_tip_2'][e][-1][1]])
    else:
        z = set['Nz']/2 
        if z % 2 == 0:
            z += 1
        if set['initial_prof'] == 'rectangular_1_tip':
            sol = rec_1_tip(coef,set,sol)
        elif set['initial_prof'] == 'rectangular_tip':
            sol = rec_5_tip(coef,set,sol)
        '''Identifying Tip Cell'''
        for e,ti in enumerate(sol['matrix_tip']):
            sol['tip_cell'].append([sol['matrix_tip'][e][-1][0],sol['matrix_tip'][e][-1][1]])
    return sol