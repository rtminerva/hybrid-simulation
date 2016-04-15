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
            if r_f >= set['R_min'] + numpy.sqrt(set['error']):
                sol['c'][x,y] = 0.5-0.45*numpy.exp(-(r_f**2)/0.45)
                sol['f'][x,y] = 0.5
                #f[x,y] = 0.5-0.45*numpy.exp(-(set['R_max']-r_f)**2/0.45) 
    
    ''''Initial Tips'''
    sol['matrix_tip'] = []
    sol['list_tip_movement'] = []
    sol['life_time_tip'] = []
    sol['sp_stop'] = []
    sol['tip_cell'] = []
    sol['number_ec'] = 8
                    
    sol['n'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    
    y1 = set['Ny']/2 + 1
    x = 1
    while x < set['Nx']+1:
        if (x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2 < set['R_min']**2 + set['error'] and (x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2 > set['R_min']**2:
                sol['matrix_tip'].append([(x,y1)])
                sol['n'][x,y1] = 1
                sol['list_tip_movement'].append('start') #movement tip
                sol['life_time_tip'].append(0) #lifetime
                u = 10
        else:
            u = 2           
        x += u
        
    y1 = set['Nx']/2 + 1
    x = 1
    while x < set['Nx']+1:
        if (x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2 < set['R_min']**2 + set['error'] and (x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2 > set['R_min']**2:
                sol['matrix_tip'].append([(y1,x)])
                sol['n'][y1,x] = 1
                sol['list_tip_movement'].append('start') #movement tip
                sol['life_time_tip'].append(0) #lifetime
                u = 10
        else:
            u = 2           
        x += u
             
    y1 = sol['matrix_tip'][2][0][0] + (sol['matrix_tip'][1][0][0]- sol['matrix_tip'][2][0][0])/2
    if y1 % 2 == 0:
        y1 += 1
    x = 1
    while x < set['Nx']+1:
        if (x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2 < set['R_min']**2 + set['error'] and (x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2 > set['R_min']**2:
                sol['matrix_tip'].append([(y1,x)])
                sol['n'][y1,x] = 1
                sol['list_tip_movement'].append('start') #movement tip
                sol['life_time_tip'].append(0) #lifetime
                u = 10
        else:
            u = 2           
        x += u
                
    y1 = sol['matrix_tip'][0][0][0] + (sol['matrix_tip'][2][0][0]-sol['matrix_tip'][0][0][0])/2
    if y1 % 2 == 0:
        y1 += 1
    x = 1
    while x < set['Nx']+1:
        if (x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2 < set['R_min']**2 + set['error'] and (x*set['Hh']-set['O_x'])**2 + (y1*set['Hh']-set['O_y'])**2 > set['R_min']**2:
                sol['matrix_tip'].append([(y1,x)])
                sol['n'][y1,x] = 1
                sol['list_tip_movement'].append('start') #movement tip
                sol['life_time_tip'].append(0) #lifetime
                u = 10
        else:
            u = 2           
        x += u

    for e,ti in enumerate(sol['matrix_tip']):
        sol['tip_cell'].append(sol['matrix_tip'][e][-1])
    
    
    '''Initial Mural & Tie2''' #???????????????????????????
    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
        #index_m = []
        sol['index_mn'] = []
        sol['m'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
        sol['p'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
        
        '''Randomly spotted in domain'''
        for tt in range(0,250):
            idx_m_1 = random.sample(range(1,440,2),50)
            idx_m_2 = random.sample(range(1,440,2),50)
            for id in range(0,len(idx_m_1)):
                r_f = numpy.sqrt((idx_m_1[id]*set['Hh']-set['O_x'])**2 + (idx_m_2[id]*set['Hh']-set['O_y'])**2)
                if not sol['m'][idx_m_1[id], idx_m_2[id]] == 1 and not [(idx_m_1[id], idx_m_2[id])] in sol['matrix_tip'] and r_f >= set['R_min']:
                    sol['m'][idx_m_1[id], idx_m_2[id]] = 1
        del idx_m_1
        del idx_m_2
     
    print 'initial tips:', sol['matrix_tip']
    return sol