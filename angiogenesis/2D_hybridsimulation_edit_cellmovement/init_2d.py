import numpy
import math as m
from click import _winconsole

def c_prof_1(coef,set,sol): #Ref.2.1.1
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
#             sol['c'][x,y] = 0.5
            sol['f'][x,y] = 0.5
            sol['c'][x,y] = numpy.exp(-(1-x*set['Hh'])**2/0.45)
#             sol['c_o'][x,y] = numpy.exp(-(1-x*set['Hh'])**2/0.45)
    return sol


def init_2d_(coef,set,sol): #Ref.2.1
    sol['c'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['f'] = numpy.zeros((set['Nx']+1,set['Ny']+1))

    sol = c_prof_1(coef,set,sol) #Ref.2.1.1
    return sol
        