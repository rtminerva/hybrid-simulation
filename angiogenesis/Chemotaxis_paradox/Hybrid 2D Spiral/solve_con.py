from random import randint, sample, uniform
import numpy
import math as m

def system_2d(coef, set, sol): #2.3
    '''Solve c at sub lattice'''
    for y in range(0,set['Ny']+1,2):
        aa = 0
        for x in range(0,set['Nx']+1,2):
            aa = coef['A_c']*m.exp(-((x*set['Hh']-0.5)*m.cos(set['t_c']) - (y*set['Hh']-0.5)*m.sin(set['t_c']))**2/coef['vari']) #-coef['vel']*m.sin(set['t'])
#             for i in range(1,100):
#                 aa += coef['A_c']*m.exp(-((x*set['Hh']-0.5)*m.cos(set['t']) - (y*set['Hh']-0.5)*m.sin(set['t'])+i*coef['perio'])**2/coef['vari'])   
            sol['c'][x,y] = aa     
    return sol