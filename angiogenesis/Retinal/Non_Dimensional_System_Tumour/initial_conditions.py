import numpy
import random
from random import randint
#from sympy.polys.benchmarks.bench_solvers import sol_10x8


def initial_prof(coef, set, sol):
       
    '''Initial VEGF & Fibronectin'''
    if set['layout'] == '2D':
        sol['c'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
        #sol['f'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
        for y in range(0,set['Ny']+1,2):
            for x in range(0,set['Nx']+1,2):
                sol['c'][x,y] = numpy.exp(-(1-x*set['Hh'])**2/0.45)
                #sol['f'][x,y] = 0.5
                
    
        sol['n'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
        sol['matrix_tip'] = []
        sol['list_tip_movement'] = []
        sol['life_time_tip'] = []
        sol['sp_stop'] = []
        sol['tip_cell'] = []
        
    
        if set['initial_prof'] == 'rectangular_1_tip':
            y = set['Ny']/2 
            if y % 2 == 0:
                y += 1
            sol['matrix_tip'].append([(1,y)])
            sol['n'][1,y] = 1
            sol['list_tip_movement'].append('start') #movement tip
            sol['life_time_tip'].append(0) #lifetime
        elif set['initial_prof'] == 'rectangular_tip':
            '''Tip 0'''
            y = set['Ny']/4
            if y % 2 == 0:
                y += 1
            sol['matrix_tip'].append([(1,y)])
            sol['n'][1,y] = 1
            sol['list_tip_movement'].append('start') #movement tip
            sol['life_time_tip'].append(0) #lifetime
            
            '''TIP 1'''
            y1 = set['Ny']/2 
            if y1 % 2 == 0:
                y1 += 1
            sol['matrix_tip'].append([(1,y1)])
            sol['n'][1,y1] = 1
            sol['list_tip_movement'].append('start') #movement tip
            sol['life_time_tip'].append(0) #lifetime
            
            '''TIP 2'''
            y2 = y + y1
            if y2 % 2 == 0:
                y2 += 1
            sol['matrix_tip'].append([(1,y2)])
            sol['n'][1,y2] = 1
            sol['list_tip_movement'].append('start') #movement tip
            sol['life_time_tip'].append(0) #lifetime
       
        '''Identifying Tip Cell'''
        for e,ti in enumerate(sol['matrix_tip']):
            sol['tip_cell'].append([sol['matrix_tip'][e][-1][0],sol['matrix_tip'][e][-1][1]])
     
    print 'initial tips:', sol['matrix_tip']
    return sol