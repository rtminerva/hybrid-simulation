import numpy
import math as m
import random

def X1_prof(coef,set,sol): #2.1.1.(1)
    idx_m_1 = random.sample(range(1,set['Nx'],2),200)
    idx_m_2 = random.sample(range(1,set['Ny'],2),200)
    for id in range(0,len(idx_m_1)):
        sol['X1'][idx_m_1[id],idx_m_2[id]] = random.uniform(0,1)
    del idx_m_1
    del idx_m_2
    return sol
    
def X3_prof(coef,set,sol): #2.1.1.(2)
    idx_m_1 = random.sample(range(1,set['Nx'],2),200)
    idx_m_2 = random.sample(range(1,set['Ny'],2),200)
    for id in range(0,len(idx_m_1)):
        sol['X3'][idx_m_1[id],idx_m_2[id]] = random.uniform(0,1)
    del idx_m_1
    del idx_m_2
    return sol

def G_vec(coef,set,sol):
    aa = 0.75
    bb = 0.5
    yy1 = [319,321,323,325,327,329]
    yy2 = [119,121,123,125,127,129]
    '''
    sol['G_vec_x'][321,x] = aa
    sol['G_vec_x'][323,x] = aa
    sol['G_vec_x'][325,x] = aa
    sol['G_vec_x'][327,x] = aa
    sol['G_vec_x'][329,x] = aa
    sol['G_vec_x'][121,x] = bb
    sol['G_vec_x'][123,x] = bb
    sol['G_vec_x'][125,x] = bb
    sol['G_vec_x'][127,x] = bb
    sol['G_vec_x'][129,x] = bb
    '''
    for y in yy1:
        aa = 0.75
        for x in range(225,set['Nx']-1,2):
            sol['G_vec_x'][y,x] = aa
            aa += 0.001
    for y in yy2:
        bb = 0.25
        for x in range(225,set['Nx']-1,2):    
            sol['G_vec_x'][y,x] = bb
            bb += 0.001
    x = set['Nx']-1
    for y in yy1:
        sol['G_vec_x'][y,x] = 1
    for y in yy2:
        sol['G_vec_x'][y,x] = 1    
    return sol


def init_2d_(coef,set,sol): #2.1.1
    sol['X1'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['X2'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['X3'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['X4'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['G_vec_x'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['G_vec_y'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['jum_X4'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    
    #sol['G_vec_'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol = X1_prof(coef,set,sol) #2.1.1.(1)
    sol = X3_prof(coef,set,sol) #2.1.1.(2)
    sol = G_vec(coef,set,sol) #2.1.1.(3)
    return sol
        