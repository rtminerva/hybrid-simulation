import numpy
import math as m

def c_prof(coef,set,sol):
    c_0 = numpy.copy(sol['c'])
    c_1 = numpy.copy(sol['c'])
    c_2 = numpy.copy(sol['c'])
    c_3 = numpy.copy(sol['c'])

    bb = 0
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            xb = (x*set['Hh']-0.5)*m.cos(bb) - (y*set['Hh']-0.5)*m.sin(bb)
            c_0[x,y] = coef['A_c']*m.exp(-(xb)**2/coef['vari'])
    bb = m.pi/(3)
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            xb = (x*set['Hh']-0.5)*m.cos(bb) - (y*set['Hh']-0.5)*m.sin(bb)
            c_1[x,y] = coef['A_c']*m.exp(-(xb)**2/coef['vari'])
    bb = m.pi/(3)*2
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            xb = (x*set['Hh']-0.5)*m.cos(bb) - (y*set['Hh']-0.5)*m.sin(bb)
            c_2[x,y] = coef['A_c']*m.exp(-(xb)**2/coef['vari'])
#     bb = m.pi/(4)
#     for y in range(0,set['Ny']+1,2):
#         for x in range(0,set['Nx']+1,2):
#             c_1[x,y] = coef['A_c']*m.exp(-((x*set['Hh']-0.5)*m.cos(bb) - (y*set['Hh']-0.5)*m.sin(bb))**2/coef['vari'])
#     bb = m.pi/(3)
#     for y in range(0,set['Ny']+1,2):
#         for x in range(0,set['Nx']+1,2):
#             c_2[x,y] = coef['A_c']*m.exp(-((x*set['Hh']-0.5)*m.cos(bb) - (y*set['Hh']-0.5)*m.sin(bb))**2/coef['vari'])
    
    
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
#             if c_0[x,y] == 0:
#                 sol['c'][x,y] = (c_1[x,y]+c_2[x,y])/2
#             elif c_1[x,y] == 0:
#                 sol['c'][x,y] = (c_0[x,y]+c_2[x,y])/2
#             elif c_2[x,y] == 0:
#                 sol['c'][x,y] = (c_0[x,y]+c_1[x,y])/2
#             elif c_0[x,y] == 0 and c_1[x,y] == 0:
#                 sol['c'][x,y] = c_2[x,y]
#             elif c_0[x,y] == 0 and c_2[x,y] == 0:
#                 sol['c'][x,y] = c_1[x,y]
#             elif c_1[x,y] == 0 and c_2[x,y] == 0:
#                 sol['c'][x,y] = c_0[x,y]
#             else:
#                 sol['c'][x,y] = (c_0[x,y]+c_1[x,y]+c_2[x,y])/3
            
        
    return sol

def init_2d_(coef,set,sol): #2.1.1
#     sol['c_n'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['c'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
#     sol['c_o'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol = c_prof(coef,set,sol)   
    return sol
        