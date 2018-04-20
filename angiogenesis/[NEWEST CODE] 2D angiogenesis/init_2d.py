import numpy
import math as m
from click import _winconsole


# def c_prof_1(coef,set,sol): #2.1.1.(1)
#     for y in range(0,set['Ny']+1,2):
#         for x in range(0,set['Nx']+1,2):
# #             sol['c'][x,y] = 0.5
# #             sol['c_o'][x,y] = 0.5
#             sol['c'][x,y] = numpy.exp(-(1-x*set['Hh'])**2/0.45)
# #             sol['c_o'][x,y] = numpy.exp(-(1-x*set['Hh'])**2/0.45)
#     return sol
    
# def c_prof_2(coef,set,sol): #2.1.1.(2)
#     viu = (numpy.sqrt(5)-0.1)/(numpy.sqrt(5)-1)
#     for y in range(0,set['Ny']+1,2):
#         for x in range(0,set['Nx']+1,2):
#             r_c = numpy.sqrt((x*set['Hh']-1)**2+(y*set['Hh']-0.5)**2)
#             if r_c >= 0.1:
#                 sol['c'][x,y] = (viu-r_c)**2/(viu-0.1)**2
#             elif r_c>= 0 and r_c < 0.1:
#                 sol['c'][x,y] = 1
#     return sol

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
    return sol

def init_2d_(coef,set,sol): #2.1.1
    sol['c_n'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['c'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
#     sol['c_o'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol = c_prof_1(coef,set,sol) #2.1.1.(1) #gradually distributed on x-direction    
    return sol
        