import numpy
import math as m

def c_prof(coef,set,sol): #2.1.1.(1)
    for x in range(0,set['Nx']+1,2):
        sol['c'][x] = coef['A_c']*m.exp(-(x*set['Hh']+5*set['rad']-coef['vel']*set['dt']*set['k'])**2/0.05)#0.05
        for i in range(1,100):
            sol['c'][x] += coef['A_c']*m.exp(-(x*set['Hh']+5*set['rad']+i*coef['perio']-coef['vel']*set['dt']*set['k'])**2/0.05)
    return sol

def init_1d_(coef,set,sol): #2.1.1
    sol['c'] = numpy.zeros(set['Nx']+1)
    sol['n'] = [301]
    sol['vel_n'] = []
       
    sol = c_prof(coef,set,sol)
    
    return sol
        