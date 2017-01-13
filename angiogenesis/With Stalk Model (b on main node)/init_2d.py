import numpy
import math as m

#def f_prof_1(coef,set,sol,x,y):
#    sol['f'][x,y] = 0.5
#    return sol

#def f_prof_2(coef,set,sol,x,y):
#    sol['f'][x,y] = numpy.exp(-(x*set['Hh'])**2/0.45)
#    return sol

def c_prof_1(coef,set,sol): #2.1.1.(1)
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            sol['c'][x,y] = numpy.exp(-(1-x*set['Hh'])**2/0.45)
            sol['c1'][x,y] = numpy.exp(-(1-x*set['Hh'])**2/0.45)
#            if set['f_prof'] == 'F2':
#                sol = f_prof_2(coef,set,sol,x,y)
#            elif set['f_prof'] == 'F1':
#                sol = f_prof_1(coef,set,sol,x,y)
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
#            if set['f_prof'] == 'F2':
#                sol = f_prof_2(coef,set,sol,x,y)
#            elif set['f_prof'] == 'F1':
#                sol = f_prof_1(coef,set,sol,x,y)
    return sol

def n_b_con_prof(coef,set,sol):
    tip = 5
    for y in range(1,set['Ny'],2):
        for x in range(1,set['Nx'],2):
            sol['n'][x,y] = m.exp(-(x*set['Hh']-set['rad'])**2/0.01)*(m.sin(tip*m.pi*y*set['Hh']))**2 
            if x*set['Hh'] <= set['rad']:
                sol['b'][x,y] = (m.sin(tip*m.pi*y*set['Hh']))**2             
    return sol

# def b_prof(coef,set,sol): #2.1.1.(3)
#     for y in range(1,set['Ny'],2):
#         sol['b'][1,y] = 1
#     return sol


def init_2d_(coef,set,sol): #2.1.1
    sol['c'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['c1'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    #sol['f'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    if set['c_prof'] == 'C2':
        sol = c_prof_2(coef,set,sol) #2.1.1.(2)
    elif set['c_prof'] == 'C1':
        sol = c_prof_1(coef,set,sol) #2.1.1.(1)
    if set['con'] == True:
        sol['n'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
        sol['b'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
        sol = n_b_con_prof(coef,set,sol)
    #b_prof(coef,set,sol) #2.1.1.(3)
    return sol
        