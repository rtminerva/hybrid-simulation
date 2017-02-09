import numpy
import math as m

def c_prof_1(coef,set,sol): #2.1.1.(1)
    for x in range(0,set['Nx']+1,2):
        sol['c'][x] = numpy.exp(-(1-x*set['Hh'])**2/0.45)
#         sol['c'][x] = 1*m.exp(-(x*set['Hh']-set['rad'])**2/0.001) #0.25 
    return sol

def n_prof(coef,set,sol):
    for x in range(1,set['Nx'],2):
        sol['n'][x] = 0.4*m.exp(-(x*set['Hh']-set['rad'])**2/0.005) #0.25      
    return sol

def b_prof(coef,set,sol):
    for x in range(1,set['Nx'],2):
        sol['b'][x] = 0.5 + 0.5*m.tanh(((set['rad']-0.05)-x*set['Hh'])/0.01)
#         sol['b'][x] = 0.5*m.exp(-(x*set['Hh']-0.07)**2/0.005)
#         if x*set['Hh'] < set['rad']:
            
            #sol['b'][x] = m.exp(-(x*set['Hh']-(set['rad']-0.05))**2/0.001) #0.25
            #sol['b'][x] = 1            
    return sol

def init_1d_(coef,set,sol): #2.1.1
    sol['c'] = numpy.zeros(set['Nx']+1)
    sol['n'] = numpy.zeros(set['Nx']+1)
    sol['b'] = numpy.zeros(set['Nx']+1)
    sol = c_prof_1(coef,set,sol)
    sol = n_prof(coef,set,sol) 
    sol = b_prof(coef,set,sol)
    sol['Vb_x'] = numpy.zeros(set['Nx']+1)
    
    return sol
        