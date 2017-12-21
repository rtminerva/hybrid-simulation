import numpy
import math as m

def c_prof(coef,set,sol): #2.1.1.(1)
    for x in range(0,set['Nx']+1,2):
        sol['c'][x] = coef['A_c']*m.exp(-(x*set['Hh']+5*set['rad']-coef['vel']*set['t'])**2/coef['vari'])#0.05 set['dt']*set['k']
        for i in range(1,100):
            sol['c'][x] += coef['A_c']*m.exp(-(x*set['Hh']+5*set['rad']+i*coef['perio']-coef['vel']*set['t'])**2/coef['vari'])
    return sol

def init_1d_(coef,set,sol): #2.1.1
    sol['c'] = numpy.zeros(set['Nx']+1)
    sol['n'] = [301]
    sol['vel_n'] = [0]
    sol['in_vel_n'] = [0]
    sol['c_x'] = [0]
    sol['c_'] = [0]
#     sol['n_pos'] = [2]
       
    sol = c_prof(coef,set,sol)
    
    return sol
        