from random import randint, sample, uniform
import numpy
import math as m

def system_2d(coef, set, sol): #2.3
    '''Solve c at sub lattice'''
    c_o = numpy.copy(sol['c'])
    
    c_0 = numpy.zeros((set['Nx']+1,set['Ny']+1))
    c_1 = numpy.zeros((set['Nx']+1,set['Ny']+1))
    c_2 = numpy.zeros((set['Nx']+1,set['Ny']+1))
    c_3 = numpy.zeros((set['Nx']+1,set['Ny']+1))
    bb = 0
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            tet = bb+set['t_c'] 
            xb = (x*set['Hh']-0.5)*m.cos(tet) - (y*set['Hh']-0.5)*m.sin(tet)
#             xt = xb*m.cos(set['t_c']) - (y*set['Hh']-0.5)*m.sin(set['t_c'])
            c_0[x,y] = coef['A_c']*m.exp(-(xb)**2/coef['vari'])
            
    bb = m.pi/(3)
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            tet = bb+set['t_c'] 
            xb = (x*set['Hh']-0.5)*m.cos(tet) - (y*set['Hh']-0.5)*m.sin(tet)
#             xt = xb*m.cos(set['t_c']) - (y*set['Hh']-0.5)*m.sin(set['t_c'])
            c_1[x,y] = coef['A_c']*m.exp(-(xb)**2/coef['vari'])
    
    bb = m.pi/(3)*2
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            tet = bb+set['t_c']
            xb = (x*set['Hh']-0.5)*m.cos(tet) - (y*set['Hh']-0.5)*m.sin(tet)
            c_2[x,y] = coef['A_c']*m.exp(-(xb)**2/coef['vari'])
            
    
    
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            if c_0[x,y] > c_1[x,y]:
                if c_0[x,y] > c_2[x,y]:
                    sol['c'][x,y] = c_0[x,y]
            if c_1[x,y] > c_0[x,y]:
                if c_1[x,y] > c_2[x,y]:
                    sol['c'][x,y] = c_1[x,y]
            if c_2[x,y] > c_0[x,y]:
                if c_2[x,y] > c_1[x,y]:
                    sol['c'][x,y] = c_2[x,y]
            if c_0[x,y] == c_1[x,y] or c_0[x,y] == c_2[x,y]:
                sol['c'][x,y] = c_0[x,y]
            if c_1[x,y] == c_2[x,y]:
                sol['c'][x,y] = c_1[x,y]
    
            
#     for y in range(0,set['Ny']+1,2):
#         for x in range(0,set['Nx']+1,2):
#             if c_0[x,y] < c_3[x,y]:
#                 sol['c'][x,y] = c_3[x,y]
#             elif c_0[x,y] > c_3[x,y]:
#                 sol['c'][x,y] = c_0[x,y]
#             else:
#                 sol['c'][x,y] = c_0[x,y]
    
    
    
#     for y in range(0,set['Ny']+1,2):
#         aa = 0
#         for x in range(0,set['Nx']+1,2):
#             aa = coef['A_c']*m.exp(-((x*set['Hh']-0.5)*m.cos(set['t_c']) - (y*set['Hh']-0.5)*m.sin(set['t_c']))**2/coef['vari']) #-coef['vel']*m.sin(set['t'])
# #             for i in range(1,100):
# #                 aa += coef['A_c']*m.exp(-((x*set['Hh']-0.5)*m.cos(set['t']) - (y*set['Hh']-0.5)*m.sin(set['t'])+i*coef['perio'])**2/coef['vari'])   
#             sol['c'][x,y] = aa     
    return sol, c_o