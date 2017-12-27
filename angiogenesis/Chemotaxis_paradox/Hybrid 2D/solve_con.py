from random import randint, sample, uniform
import numpy
import math as m

def system_2d(coef, set, sol): #2.3
    '''Solve c at sub lattice'''
#     print sol
    for y in range(0,set['Ny']+1,2):
        aa = 0
        for x in range(0,set['Nx']+1,2):
            aa = coef['A_c']*m.exp(-(x*set['Hh']+(-3)*set['rad']-coef['vel']*set['t'])**2/coef['vari'])
            for i in range(1,10):
                aa += coef['A_c']*m.exp(-(x*set['Hh']+(-3)*set['rad']+i*coef['perio']-coef['vel']*set['t'])**2/coef['vari'])   
#             sol['c'][x,y]# = aa     
    return sol