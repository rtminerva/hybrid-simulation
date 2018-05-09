import numpy
import math as m
from click import _winconsole


def c_prof_1(coef,set,sol): #2.1.1.(1)
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            sol['c'][x,y] = 0.5 + 0.5*m.tanh((x*set['Hh']-(-0.6))/0.6) #((x*set['Hh']-(set['rad']-0.6))/0.6)
#             sol['c_o'][x,y] = 0.5 + 0.5*m.tanh((x*set['Hh']-(-0.6))/0.6)
    return sol

# def c_prof_2(coef,set,sol):
#     for y in range(0,set['Ny']+1,2):
#         for x in range(0,set['Nx']+1,2):
#             r_f = numpy.sqrt((x*set['Hh']-set['O_x'])**2 + (y*set['Hh']-set['O_y'])**2)
#             if r_f >= set['rad']:# + numpy.sqrt(set['error']):
#                 sol['c'][x,y] = 0.5-0.05*numpy.exp(-(r_f**2)/0.6)
#     return sol

def cprof(coef,set,sol):
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            sol['c'][x,y] = 0#set['Hh']*x
    return sol





def init_2d_(coef,set,sol): #2.1.1
    sol['c'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
#     sol['c_n'] = numpy.zeros((set['Nx']+1,set['Ny']+1))

#     sol['c_o'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
#     sol = c_prof_1(coef,set,sol) #2.1.1.(1) #gradually distributed on x-direction 
    sol = cprof(coef,set,sol)
    return sol
        