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

def init_2d_(coef,set,sol): #2.1.1
    sol['X1'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['X2'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['X3'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['X4'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['G_vec_x'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['G_vec_y'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol = X1_prof(coef,set,sol) #2.1.1.(1)
    sol = X3_prof(coef,set,sol) #2.1.1.(2)
    sol['matrix_tip'] = []
    return sol
        