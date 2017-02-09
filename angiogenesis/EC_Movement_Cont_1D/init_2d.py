import numpy
import math as m

def c_prof_1(coef,set,sol): #2.1.1.(1)
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            sol['c'][x,y] = numpy.exp(-(1-x*set['Hh'])**2/0.45)
    return sol
    
def c_prof_2(coef,set,sol): #2.1.1.(2)
    viu = (numpy.sqrt(5)-0.1)/(numpy.sqrt(5)-1)
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            r_c = numpy.sqrt((x*set['Hh']-1)**2+(y*set['Hh']-0.5)**2)
            if r_c >= 0.1:
                sol['c'][x,y] = (viu-r_c)**2/(viu-0.1)**2
            elif r_c>= 0 and r_c < 0.1:
                sol['c'][x,y] = 1
    return sol

def n_b_prof(coef,set,sol):
    tip = 7
    for y in range(1,set['Ny'],2):
        for x in range(1,set['Nx'],2):
            step = int(set['Ny']/(tip))
            range_1 = step
            range_2 = step*2+1
            range_3 = step*3
            range_4 = step*4+1
            range_5 = step*5
            range_6 = step*6+1
            
            if y > range_1 and y < range_2: 
                sol['n'][x,y] = 0.4*m.exp(-(x*set['Hh']-set['rad'])**2/0.0005)*(m.sin(tip*m.pi*y*set['Hh']))**2 
                sol['b'][x,y] = (0.5 + 0.5*m.tanh(((set['rad']-0.05)-x*set['Hh'])/0.01))*(m.sin(tip*m.pi*y*set['Hh']))**2 
            if y > range_3 and y < range_4:
                sol['n'][x,y] = 0.4*m.exp(-(x*set['Hh']-set['rad'])**2/0.0005)*(m.sin(tip*m.pi*y*set['Hh']))**2 
                sol['b'][x,y] = (0.5 + 0.5*m.tanh(((set['rad']-0.05)-x*set['Hh'])/0.01))*(m.sin(tip*m.pi*y*set['Hh']))**2
            if y > range_5 and y < range_6:
                sol['n'][x,y] = 0.4*m.exp(-(x*set['Hh']-set['rad'])**2/0.0005)*(m.sin(tip*m.pi*y*set['Hh']))**2 
                sol['b'][x,y] = (0.5 + 0.5*m.tanh(((set['rad']-0.05)-x*set['Hh'])/0.01))*(m.sin(tip*m.pi*y*set['Hh']))**2
            
#             sol['n'][x,y] = 0.4*m.exp(-(x*set['Hh']-set['rad'])**2/0.01)*(m.sin(tip*m.pi*y*set['Hh']))**2 
#             sol['b'][x,y] = (m.sin(tip*m.pi*y*set['Hh']))**2*(0.5 + 0.5*m.tanh(((set['rad']-0.05)-x*set['Hh'])/0.01))  
#             if x*set['Hh'] <= set['rad']: 
    return sol


def init_2d_(coef,set,sol):
    sol['n'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['c'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['b'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol = n_b_prof(coef,set,sol)
    if set['c_prof'] == 'C2':
        sol = c_prof_2(coef,set,sol) #2.1.1.(2)
    elif set['c_prof'] == 'C1':
        sol = c_prof_1(coef,set,sol) #2.1.1.(1)
    return sol
        