import numpy

def rec_1_tip(coef,set,sol,z):
    x = int(set['Nx']/12)
    x3 = 3*x
    if x3 % 2 == 0:
        x3 += 1
    y3 = -2*x3 + 1
    if y3 % 2 == 0:
        y3 += 1
    sol['matrix_tip'].append([(x3,y3,z)])
    sol['n'][x3,y3,z] = 1
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    return sol

def rec_5_tip(coef,set,sol,z):
    '''Tip 0'''
    x = int(set['Nx']/12)
    if x % 2 == 0:
        x += 1
    y = -2*x + set['Nx']  
    if y % 2 == 0:
        y += 1
    sol['matrix_tip'].append([(x,y,z)])
    sol['n'][x,y,z] = 1
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    
    '''TIP 1'''
    x1 = 2*x
    if x1 % 2 == 0:
        x1 += 1
    y1 = -2*x1 + set['Nx']
    if y1 % 2 == 0:
        y1 += 1
    sol['matrix_tip'].append([(x1,y1,z)])
    sol['n'][x1,y1,z] = 1
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    
    '''TIP 2'''
    x2 = 3*x
    if x2 % 2 == 0:
        x2 += 1
    y2 = -2*x2 + set['Nx']
    if y2 % 2 == 0:
        y2 += 1
    sol['matrix_tip'].append([(x2,y2,z)])
    sol['n'][x2,y2,z] = 1
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    
    '''TIP 3'''
    x3 = 4*x
    if x3 % 2 == 0:
        x3 += 1
    y3 = -2*x3 + set['Nx']
    if y3 % 2 == 0:
        y3 += 1
    sol['matrix_tip'].append([(x3,y3,z)])
    sol['n'][x3,y3,z] = 1
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    
    '''TIP 4'''
    x4 = 5*x
    if x4 % 2 == 0:
        x4 += 1
    y4 = -2*x4 + set['Nx']
    if y4 % 2 == 0:
        y4 += 1
    sol['matrix_tip'].append([(x4,y4,z)])
    sol['n'][x4,y4,z] = 1
    sol['list_tip_movement'].append('start') #movement tip
    sol['life_time_tip'].append(0) #lifetime
    return sol

def rec_5_tip_ar(coef,set,sol,z):
    '''Tip 0'''
    x = int(set['Nx']/12)
    x0 = int(set['Nx']/2)+x
    if x0 % 2 == 0:
        x0 += 1
    y = -2*x0 + 2*set['Nx']
    if y % 2 == 0:
        y += 1
    sol['matrix_tip_2'].append([(x0,y,z)])
    sol['n'][x0,y,z] = 1
    sol['list_tip_movement_2'].append('start') #movement tip
    sol['life_time_tip_2'].append(0) #lifetime
    
    '''TIP 1'''
    x1 = int(set['Nx']/2)+2*x
    if x1 % 2 == 0:
        x1 += 1
    y1 = -2*x1 + 2*set['Nx']
    if y1 % 2 == 0:
        y1 += 1
    sol['matrix_tip_2'].append([(x1,y1,z)])
    sol['n'][x1,y1,z] = 1
    sol['list_tip_movement_2'].append('start') #movement tip
    sol['life_time_tip_2'].append(0) #lifetime
    
    '''TIP 2'''
    x2 = int(set['Nx']/2)+3*x
    if x2 % 2 == 0:
        x2 += 1
    y2 = -2*x2 + 2*set['Nx']
    if y2 % 2 == 0:
        y2 += 1
    sol['matrix_tip_2'].append([(x2,y2,z)])
    sol['n'][x2,y2,z] = 1
    sol['list_tip_movement_2'].append('start') #movement tip
    sol['life_time_tip_2'].append(0) #lifetime
    
    '''TIP 3'''
    x3 = int(set['Nx']/2)+4*x
    if x3 % 2 == 0:
        x3 += 1
    y3 = -2*x3 + 2*set['Nx']
    if y3 % 2 == 0:
        y3 += 1
    sol['matrix_tip_2'].append([(x3,y3,z)])
    sol['n'][x3,y3,z] = 1
    sol['list_tip_movement_2'].append('start') #movement tip
    sol['life_time_tip_2'].append(0) #lifetime
    
    '''TIP 4'''
    x4 = int(set['Nx']/2)+5*x
    if x4 % 2 == 0:
        x4 += 1
    y4 = -2*x4 + 2*set['Nx']
    if y4 % 2 == 0:
        y4 += 1
    sol['matrix_tip_2'].append([(x4,y4,z)])
    sol['n'][x4,y4,z] = 1
    sol['list_tip_movement_2'].append('start') #movement tip
    sol['life_time_tip_2'].append(0) #lifetime
    return sol

def rec_tip_two_parent(coef,set,sol,z):
    '''Vein'''
    sol = rec_5_tip(coef,set,sol,z)
    '''Artery'''
    sol = rec_5_tip_ar(coef,set,sol,z)
    return sol

def init_tip_3d_n_(coef,set,sol):
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
        z = 1
        sol = rec_tip_two_parent(coef,set,sol,z)
        '''Identifying Tip Cell'''
        for e,ti in enumerate(sol['matrix_tip']):
            sol['tip_cell'].append([sol['matrix_tip'][e][-1][0], sol['matrix_tip'][e][-1][1],sol['matrix_tip'][e][-1][2]])
        '''Identifying Tip Cell 2'''
        for e,ti in enumerate(sol['matrix_tip_2']):
            sol['tip_cell_2'].append([sol['matrix_tip_2'][e][-1][0],sol['matrix_tip_2'][e][-1][1],sol['matrix_tip_2'][e][-1][2]])
    else:
        z = 1
        if set['initial_prof'] == 'rectangular_1_tip':
            sol = rec_1_tip(coef,set,sol,z)
        elif set['initial_prof'] == 'rectangular_tip':
            sol = rec_5_tip(coef,set,sol,z)
        '''Identifying Tip Cell'''
        for e,ti in enumerate(sol['matrix_tip']):
            sol['tip_cell'].append([sol['matrix_tip'][e][-1][0],sol['matrix_tip'][e][-1][1],sol['matrix_tip'][e][-1][2]])
    return sol