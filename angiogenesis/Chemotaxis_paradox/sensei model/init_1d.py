import numpy
import math as m

def c_prof(coef,set,sol): #2.1.1.(1)
    for x in range(0,set['Nx']+1,2):
        sol['c'][x] = coef['A_c']*m.exp(-(x*set['Hh']-coef['vel']*set['dt']*set['k'])**2/0.02)
        for i in range(1,100):
            sol['c'][x] += coef['A_c']*m.exp(-(x*set['Hh']+i*coef['perio']-coef['vel']*set['dt']*set['k'])**2/0.02)
    return sol

def n_prof(coef,set,sol):
    for x in range(1,set['Nx'],2):
        sol['n'][x] = 0.25*m.exp(-(1-x*set['Hh']-2*set['rad'])**2/0.002)
    return sol


def init_1d_(coef,set,sol): #2.1.1
    sol['c'] = numpy.zeros(set['Nx']+1)
    sol['n'] = numpy.zeros(set['Nx']+1)
       
    sol = c_prof(coef,set,sol)
    sol = n_prof(coef,set,sol)
    
    return sol
        