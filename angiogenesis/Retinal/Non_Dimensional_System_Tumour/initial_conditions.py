import numpy
import random
from random import randint
#from sympy.polys.benchmarks.bench_solvers import sol_10x8


def initial_prof(coef, set, sol):
       
    '''Initial VEGF & Fibronectin'''
    if set['layout'] == '2D':
        sol['c'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
        #sol['f'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
        if set['c_prof'] == 'C2':
            viu = (numpy.sqrt(5)-0.1)/(numpy.sqrt(5)-1)
            for y in range(0,set['Ny']+1,2):
                for x in range(0,set['Nx']+1,2):
                    r_c = numpy.sqrt((x*set['Hh']-1)**2+(y*set['Hh']-0.5)**2)
                    if r_c >= 0.1:
                        sol['c'][x,y] = (viu-r_c)**2/(viu-0.1)**2
                    elif r_c>= 0 and r_c < 0.1:
                        sol['c'][x,y] = 1
                    #sol['f'][x,y] = numpy.exp(-(x*set['Hh'])**2/0.45)
        elif set['c_prof'] == 'C1':
            for y in range(0,set['Ny']+1,2):
                for x in range(0,set['Nx']+1,2):
                    sol['c'][x,y] = numpy.exp(-(1-x*set['Hh'])**2/0.45)
                    #sol['f'][x,y] = numpy.exp(-(x*set['Hh'])**2/0.45)
                
    
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
            y = set['Ny']/6
            if y % 2 == 0:
                y += 1
            sol['matrix_tip'].append([(1,y)])
            sol['n'][1,y] = 1
            sol['list_tip_movement'].append('start') #movement tip
            sol['life_time_tip'].append(0) #lifetime
            
            '''TIP 1'''
            y1 = 2*y
            if y1 % 2 == 0:
                y1 += 1
            sol['matrix_tip'].append([(1,y1)])
            sol['n'][1,y1] = 1
            sol['list_tip_movement'].append('start') #movement tip
            sol['life_time_tip'].append(0) #lifetime
            
            '''TIP 2'''
            y2 = 3*y
            if y2 % 2 == 0:
                y2 += 1
            sol['matrix_tip'].append([(1,y2)])
            sol['n'][1,y2] = 1
            sol['list_tip_movement'].append('start') #movement tip
            sol['life_time_tip'].append(0) #lifetime
            
            '''TIP 3'''
            y2 = 4*y
            if y2 % 2 == 0:
                y2 += 1
            sol['matrix_tip'].append([(1,y2)])
            sol['n'][1,y2] = 1
            sol['list_tip_movement'].append('start') #movement tip
            sol['life_time_tip'].append(0) #lifetime
            
            '''TIP 4'''
            y2 = 5*y
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