import numpy
import math as m
import random

def X1_prof(coef,set,sol): #2.1.1.(1)
    idx_m_1 = random.sample(range(1,set['Nx'],2),10)
    idx_m_2 = random.sample(range(1,set['Ny'],2),10)
    for id in range(0,len(idx_m_1)):
        sol['X1'][idx_m_1[id], idx_m_2[id]] = m.exp(-(idx_m_1[id]*set['Hh'])**2/0.01)*(m.sin(1*m.pi*idx_m_2[id]*set['Hh']))**2
    del idx_m_1
    del idx_m_2
    return sol
    
def X3_prof(coef,set,sol): #2.1.1.(2)
    idx_m_1 = random.sample(range(1,set['Nx'],2),10)
    idx_m_2 = random.sample(range(1,set['Ny'],2),10)
    for id in range(0,len(idx_m_1)):
        sol['X3'][idx_m_1[id], idx_m_2[id]] = m.exp(-(idx_m_1[id]*set['Hh'])**2/0.01)*(m.sin(1*m.pi*idx_m_2[id]*set['Hh']))**2
    del idx_m_1
    del idx_m_2
    return sol

def G_vec(coef,set,sol):
    aa = 0.75
    bb = 0.5
    for x in range(225,set['Nx'],2):
        sol['G_vec_x'][319,x] = aa
        sol['G_vec_x'][321,x] = aa
        sol['G_vec_x'][323,x] = aa
        sol['G_vec_x'][325,x] = aa
        sol['G_vec_x'][327,x] = aa
        sol['G_vec_x'][329,x] = aa
                
        sol['G_vec_x'][119,x] = bb
        sol['G_vec_x'][121,x] = bb
        sol['G_vec_x'][123,x] = bb
        sol['G_vec_x'][125,x] = bb
        sol['G_vec_x'][127,x] = bb
        sol['G_vec_x'][129,x] = bb
        aa -= 0.001
        bb -= 0.001
    


def init_2d_(coef,set,sol): #2.1.1
    sol['X1'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['X2'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['X3'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['X4'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['G_vec_x'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['G_vec_y'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    
    #sol['G_vec_'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol = X1_prof(coef,set,sol) #2.1.1.(1)
    sol = X3_prof(coef,set,sol) #2.1.1.(2)
    sol = G_vec(coef,set,sol) #2.1.1.(3)
    return sol
        