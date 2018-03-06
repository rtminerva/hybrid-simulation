import numpy
import math as m

def c_prof(coef,set,sol): #2.1.1.(1)
    for x in range(0,set['Nx']+1,2):
        sol['c'][x] = numpy.exp(-(1-x*set['Hh'])**2/15) #0.45
#         sol['c'][x] = 1*m.exp(-(x*set['Hh']-set['rad'])**2/0.001) #0.25 
#         sol['c'][x] = set['c_init']
    return sol

def n_prof(coef,set,sol):
    for x in range(1,set['Nx'],2):
#         if x*set['Hh'] < set['rad']-0.03:
#             sol['n'][x] = 0.25
#         else:
#             sol['n'][x] = 0.25*m.exp(-(x*set['Hh']-set['rad']+0.03)**2/0.007) #0.25      
        sol['n'][x] = 0.35*m.exp(-(x*set['Hh']-set['rad'])**2/0.002)
    return sol

def b_prof(coef,set,sol):
    for x in range(1,set['Nx'],2):
        sol['b'][x] = 0#0.5 + 0.5*m.tanh(((set['rad']-0.08)-x*set['Hh'])/0.01) #0.01
#         sol['b'][x] = 0.5*m.exp(-(x*set['Hh']-0.07)**2/0.005)
#         if x*set['Hh'] < set['rad']:
            
            #sol['b'][x] = m.exp(-(x*set['Hh']-(set['rad']-0.05))**2/0.001) #0.25
            #sol['b'][x] = 1            
    return sol

def m_prof(coef,set,sol):
    for x in range(1,set['Nx'],2):
        sol['m'][x] = 0.4 + 0.4*m.tanh(((set['rad']-0.05)-x*set['Hh'])/0.01)
#         sol['e'][x] = 0.1 + 0.1*m.tanh(((set['rad']-0.05)-x*set['Hh'])/0.01)
#         sol['a1'][x] = 0.2 + 0.2*m.tanh(((set['rad']-0.05)-x*set['Hh'])/0.01)
#         sol['a2'][x] = 0.1 + 0.1*m.tanh(((set['rad']-0.05)-x*set['Hh'])/0.01)
    return sol

def init_1d_(coef,set,sol): #2.1.1
    sol['c'] = numpy.zeros(set['Nx']+1)
    sol['n'] = numpy.zeros(set['Nx']+1)
    sol['b'] = numpy.zeros(set['Nx']+1)
    sol['ma'] = numpy.zeros(set['Nx']+1)
    
    sol = c_prof(coef,set,sol)
    sol = n_prof(coef,set,sol) 
    sol = b_prof(coef,set,sol)
    
#     sol['n_0'] = numpy.zeros(set['Nx']/2)
#     sol['n_1'] = numpy.zeros(set['Nx']/2)
#     sol['n_2'] = numpy.zeros(set['Nx']/2)
#     sol['n_3'] = numpy.zeros(set['Nx']/2)
#     sol['n_4'] = numpy.zeros(set['Nx']/2)
#     sol['n_5'] = numpy.zeros(set['Nx']/2)
#     sol['n_6'] = numpy.zeros(set['Nx']/2)
#     sol['n_7'] = numpy.zeros(set['Nx']/2)
#     sol['n_8'] = numpy.zeros(set['Nx']/2)
#     
# #     sol['n_00'] = numpy.zeros(set['Nx']/2)
# #     sol['n_22'] = numpy.zeros(set['Nx']/2)
# #     sol['n_44'] = numpy.zeros(set['Nx']/2)
# #     sol['n_66'] = numpy.zeros(set['Nx']/2)
# #     sol['n_88'] = numpy.zeros(set['Nx']/2)
# #     sol['n_1010'] = numpy.zeros(set['Nx']/2)
#     
#     sol['b_0'] = numpy.zeros(set['Nx']/2)
#     sol['b_1'] = numpy.zeros(set['Nx']/2)
#     sol['b_2'] = numpy.zeros(set['Nx']/2)
#     sol['b_3'] = numpy.zeros(set['Nx']/2)
#     sol['b_4'] = numpy.zeros(set['Nx']/2)
#     sol['b_5'] = numpy.zeros(set['Nx']/2)
#     sol['b_6'] = numpy.zeros(set['Nx']/2)
#     sol['b_7'] = numpy.zeros(set['Nx']/2)
#     sol['b_8'] = numpy.zeros(set['Nx']/2)
#     
# #     sol['b_00'] = numpy.zeros(set['Nx']/2)
# #     sol['b_22'] = numpy.zeros(set['Nx']/2)
# #     sol['b_44'] = numpy.zeros(set['Nx']/2)
# #     sol['b_66'] = numpy.zeros(set['Nx']/2)
# #     sol['b_88'] = numpy.zeros(set['Nx']/2)
# #     sol['b_1010'] = numpy.zeros(set['Nx']/2)
#     
#     sol['c_0'] = numpy.zeros(set['Nx']/2+1)
#     sol['c_1'] = numpy.zeros(set['Nx']/2+1)
#     sol['c_2'] = numpy.zeros(set['Nx']/2+1)
#     sol['c_3'] = numpy.zeros(set['Nx']/2+1)
#     sol['c_4'] = numpy.zeros(set['Nx']/2+1)
#     sol['c_5'] = numpy.zeros(set['Nx']/2+1)
#     sol['c_6'] = numpy.zeros(set['Nx']/2+1)
#     sol['c_7'] = numpy.zeros(set['Nx']/2+1)
#     sol['c_8'] = numpy.zeros(set['Nx']/2+1)
    
#     sol['Vb_x'] = numpy.zeros(set['Nx']+1)
    
    
    '''Model extension'''
    if set['Model'] == 'extension':
        sol['p'] = numpy.zeros(set['Nx']+1)
        sol['e'] = numpy.zeros(set['Nx']+1)
        sol['a1'] = numpy.zeros(set['Nx']+1)
        sol['a2'] = numpy.zeros(set['Nx']+1)
        sol['r1'] = numpy.zeros(set['Nx']+1)
        sol['r2'] = numpy.zeros(set['Nx']+1)
        sol['m'] = numpy.zeros(set['Nx']+1)
        sol['ma'] = numpy.zeros(set['Nx']+1)
        sol = m_prof(coef,set,sol) 
    
    return sol
        