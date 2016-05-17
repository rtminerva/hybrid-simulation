import numpy
import random
from random import randint
from sympy.polys.benchmarks.bench_solvers import sol_10x8


def initial_prof(coef, set, sol):
       
    '''Initial VEGF & Fibronectin'''
    sol['c'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['f'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            r_f = numpy.sqrt((x*set['Hh']-set['O_x'])**2 + (y*set['Hh']-set['O_y'])**2)
            if r_f >= set['R_min']:# + numpy.sqrt(set['error']):
                sol['c'][x,y] = 0.5-0.45*numpy.exp(-(r_f**2)/0.45)
                sol['f'][x,y] = 0.5
                #sol['f'][x,y] = 0.5-0.45*numpy.exp(-(set['R_max']-r_f)**2/0.45) 
                
    
    sol['n'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['matrix_tip'] = []
    sol['inner_bound_tip'] = []
    sol['list_tip_movement'] = []
    sol['life_time_tip'] = []
    sol['sp_stop'] = []
    sol['tip_cell'] = []
    
    
    ''''Initial Tips at cente of small circle'''                
    
    '''
                TIP 3
    
    
        TIP 7           TIP 5
    
    
    TIP 0                    TIP 1
    
    
        TIP 6           TIP 4
    
    
                TIP 2
    '''
    if set['initial_prof'] == 'test_1_tip':
        '''Tip 0'''
        y1 = set['Ny']/2 + 1
        x = set['Nx']/2 + 1
        while x > 1:
            #if (x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2 < set['R_min']**2 + set['error'] and (x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2 > set['R_min']**2:
            r_f = numpy.sqrt((x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2)
            if r_f >= set['R_min'] and r_f < set['R_min'] + set['error']:
                sol['matrix_tip'].append([(x,y1)])
                sol['n'][x,y1] = 1
                sol['list_tip_movement'].append('start') #movement tip
                sol['life_time_tip'].append(0) #lifetime
                sol['inner_bound_tip'].append([(x,y1)])
                x = 0
            else:
                x -=2
        '''Other bound'''
        x = set['Nx']/2 + 1
        '''Tip 1'''
        while x < set['Nx']+1:
            #if (x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2 < set['R_min']**2 + set['error'] and (x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2 > set['R_min']**2:
            r_f = numpy.sqrt((x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2)
            if r_f >= set['R_min'] and r_f < set['R_min'] + set['error']:
                sol['inner_bound_tip'].append([(x,y1)])
                x = set['Nx']+1
            else:
                x +=2           
         
        '''TIP 2 & 3'''    
        x1 = set['Nx']/2 + 1
        y = set['Ny']/2 + 1
        '''TIP 2'''
        while y > 1:
            #if (x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2 < set['R_min']**2 + set['error'] and (x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2 > set['R_min']**2:
            r_f = numpy.sqrt((x1*set['Hh']-set['O_x'])**2 + (y*set['Hh']-set['O_y'])**2)
            if r_f >= set['R_min'] and r_f < set['R_min'] + set['error']:
                sol['inner_bound_tip'].append([(x1,y)])
                y = 0
            else:
                y -=2          
        y = set['Ny']/2 + 1
        '''TIP 3'''
        while y < set['Ny']+1:
            r_f = numpy.sqrt((x1*set['Hh']-set['O_x'])**2 + (y*set['Hh']-set['O_y'])**2)
            if r_f >= set['R_min'] and r_f < set['R_min'] + set['error']:
                sol['inner_bound_tip'].append([(x1,y)])
                y = set['Ny']+1
            else:
                y +=2          
        
        '''TIP 4 & 5'''        
        x1 = sol['inner_bound_tip'][2][0][0] + (sol['inner_bound_tip'][1][0][0]- sol['inner_bound_tip'][2][0][0])/2
        if x1 % 2 == 0:
            x1 += 1
        y = set['Ny']/2 + 1
        '''TIP 4'''
        while y > 1:
            r_f = numpy.sqrt((x1*set['Hh']-set['O_x'])**2 + (y*set['Hh']-set['O_y'])**2)
            if r_f >= set['R_min'] and r_f < set['R_min'] + set['error']:
                sol['inner_bound_tip'].append([(x1,y)])
                y = 0
            else:
                y -=2       
        y = set['Ny']/2 + 1
        '''TIP 5'''
        while y < set['Ny']+1:
            r_f = numpy.sqrt((x1*set['Hh']-set['O_x'])**2 + (y*set['Hh']-set['O_y'])**2)
            if r_f >= set['R_min'] and r_f < set['R_min'] + set['error']:
                sol['inner_bound_tip'].append([(x1,y)])
                y = set['Ny']+1
            else:
                y +=2          
        
        '''TIP 6 & 7'''           
        x1 = sol['inner_bound_tip'][0][0][0] + (sol['inner_bound_tip'][2][0][0]-sol['inner_bound_tip'][0][0][0])/2
        if x1 % 2 == 0:
            x1 += 1
        y = set['Ny']/2 + 1
        '''TIP 6'''
        while y > 1:
            r_f = numpy.sqrt((x1*set['Hh']-set['O_x'])**2 + (y*set['Hh']-set['O_y'])**2)
            if r_f >= set['R_min'] and r_f < set['R_min'] + set['error']:
                sol['inner_bound_tip'].append([(x1,y)])
                y = 0
            else:
                y -=2       
        
        y = set['Ny']/2 + 1
        '''TIP 7'''
        while y < set['Ny']+1:
            r_f = numpy.sqrt((x1*set['Hh']-set['O_x'])**2 + (y*set['Hh']-set['O_y'])**2)
            if r_f >= set['R_min'] and r_f < set['R_min'] + set['error']:
                sol['inner_bound_tip'].append([(x1,y)])
                y = set['Ny']+1
            else:
                y +=2 
    elif set['initial_prof'] == 'retina_tip':    
        '''TIP 0 & 1'''
        y1 = set['Ny']/2 + 1
        x = set['Nx']/2 + 1
        '''Tip 0'''
        while x > 1:
            #if (x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2 < set['R_min']**2 + set['error'] and (x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2 > set['R_min']**2:
            r_f = numpy.sqrt((x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2)
            if r_f >= set['R_min'] and r_f < set['R_min'] + set['error']:
                sol['matrix_tip'].append([(x,y1)])
                sol['n'][x,y1] = 1
                sol['list_tip_movement'].append('start') #movement tip
                sol['life_time_tip'].append(0) #lifetime
                sol['inner_bound_tip'].append([(x,y1)])
                x = 0
            else:
                x -=2
        x = set['Nx']/2 + 1
        '''Tip 1'''
        while x < set['Nx']+1:
            #if (x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2 < set['R_min']**2 + set['error'] and (x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2 > set['R_min']**2:
            r_f = numpy.sqrt((x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2)
            if r_f >= set['R_min'] and r_f < set['R_min'] + set['error']:
                sol['matrix_tip'].append([(x,y1)])
                sol['n'][x,y1] = 1
                sol['list_tip_movement'].append('start') #movement tip
                sol['life_time_tip'].append(0) #lifetime
                sol['inner_bound_tip'].append([(x,y1)])
                x = set['Nx']+1
            else:
                x +=2           
         
        '''TIP 2 & 3'''    
        x1 = set['Nx']/2 + 1
        y = set['Ny']/2 + 1
        '''TIP 2'''
        while y > 1:
            #if (x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2 < set['R_min']**2 + set['error'] and (x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2 > set['R_min']**2:
            r_f = numpy.sqrt((x1*set['Hh']-set['O_x'])**2 + (y*set['Hh']-set['O_y'])**2)
            if r_f >= set['R_min'] and r_f < set['R_min'] + set['error']:
                sol['matrix_tip'].append([(x1,y)])
                sol['n'][x1,y] = 1
                sol['list_tip_movement'].append('start') #movement tip
                sol['life_time_tip'].append(0) #lifetime
                sol['inner_bound_tip'].append([(x1,y)])
                y = 0
            else:
                y -=2          
        y = set['Ny']/2 + 1
        '''TIP 3'''
        while y < set['Ny']+1:
            r_f = numpy.sqrt((x1*set['Hh']-set['O_x'])**2 + (y*set['Hh']-set['O_y'])**2)
            if r_f >= set['R_min'] and r_f < set['R_min'] + set['error']:
                sol['matrix_tip'].append([(x1,y)])
                sol['n'][x1,y] = 1
                sol['list_tip_movement'].append('start') #movement tip
                sol['life_time_tip'].append(0) #lifetime
                sol['inner_bound_tip'].append([(x1,y)])
                y = set['Ny']+1
            else:
                y +=2          
        
        '''TIP 4 & 5'''        
        x1 = sol['inner_bound_tip'][2][0][0] + (sol['inner_bound_tip'][1][0][0]- sol['inner_bound_tip'][2][0][0])/2
        if x1 % 2 == 0:
            x1 += 1
        y = set['Ny']/2 + 1
        '''TIP 4'''
        while y > 1:
            r_f = numpy.sqrt((x1*set['Hh']-set['O_x'])**2 + (y*set['Hh']-set['O_y'])**2)
            if r_f >= set['R_min'] and r_f < set['R_min'] + set['error']:
                sol['matrix_tip'].append([(x1,y)])
                sol['n'][x1,y] = 1
                sol['list_tip_movement'].append('start') #movement tip
                sol['life_time_tip'].append(0) #lifetime
                sol['inner_bound_tip'].append([(x1,y)])
                y = 0
            else:
                y -=2       
        y = set['Ny']/2 + 1
        '''TIP 5'''
        while y < set['Ny']+1:
            r_f = numpy.sqrt((x1*set['Hh']-set['O_x'])**2 + (y*set['Hh']-set['O_y'])**2)
            if r_f >= set['R_min'] and r_f < set['R_min'] + set['error']:
                sol['matrix_tip'].append([(x1,y)])
                sol['n'][x1,y] = 1
                sol['list_tip_movement'].append('start') #movement tip
                sol['life_time_tip'].append(0) #lifetime
                sol['inner_bound_tip'].append([(x1,y)])
                y = set['Ny']+1
            else:
                y +=2          
        
        '''TIP 6 & 7'''           
        x1 = sol['inner_bound_tip'][0][0][0] + (sol['inner_bound_tip'][2][0][0]-sol['inner_bound_tip'][0][0][0])/2
        if x1 % 2 == 0:
            x1 += 1
        y = set['Ny']/2 + 1
        '''TIP 6'''
        while y > 1:
            r_f = numpy.sqrt((x1*set['Hh']-set['O_x'])**2 + (y*set['Hh']-set['O_y'])**2)
            if r_f >= set['R_min'] and r_f < set['R_min'] + set['error']:
                sol['matrix_tip'].append([(x1,y)])
                sol['n'][x1,y] = 1
                sol['list_tip_movement'].append('start') #movement tip
                sol['life_time_tip'].append(0) #lifetime
                sol['inner_bound_tip'].append([(x1,y)])
                y = 0
            else:
                y -=2       
        
        y = set['Ny']/2 + 1
        '''TIP 7'''
        while y < set['Ny']+1:
            r_f = numpy.sqrt((x1*set['Hh']-set['O_x'])**2 + (y*set['Hh']-set['O_y'])**2)
            if r_f >= set['R_min'] and r_f < set['R_min'] + set['error']:
                sol['matrix_tip'].append([(x1,y)])
                sol['n'][x1,y] = 1
                sol['list_tip_movement'].append('start') #movement tip
                sol['life_time_tip'].append(0) #lifetime
                sol['inner_bound_tip'].append([(x1,y)])
                y = set['Ny']+1
            else:
                y +=2 

    '''Identifying Tip Cell'''
    for e,ti in enumerate(sol['matrix_tip']):
        sol['tip_cell'].append([sol['matrix_tip'][e][-1][0],sol['matrix_tip'][e][-1][1]])
    
    
    '''Initial Mural & Tie2''' #???????????????????????????
    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
        #sol['number_ec'] = 8
        sol['index_mn'] = []
        sol['m'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
        #sol['cell_m'] = []
        sol['p'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
     
    print 'initial tips:', sol['matrix_tip']
    return sol