import numpy
import math as m



def c_prof_4(coef,set,sol):
    for y in range(0,set['Ny']+1,2):
        aa = 0
        for x in range(0,set['Nx']+1,2):
            aa = coef['A_c']*m.exp(-(x*set['Hh']- 0.5)**2/coef['vari'])
            for i in range(1,100):
                aa += coef['A_c']*m.exp(-(x*set['Hh']+i*coef['perio'])**2/coef['vari'])   
            sol['c'][x,y] = aa 
    return sol

def init_2d_(coef,set,sol): #2.1.1
    sol['c_n'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['c'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['c_o'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol = c_prof_4(coef,set,sol)   
    return sol
        