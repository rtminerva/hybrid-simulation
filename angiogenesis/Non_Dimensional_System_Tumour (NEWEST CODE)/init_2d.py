import numpy

def f_prof_1(coef,set,sol,x,y):
    sol['f'][x,y] = 0.5
    return sol

def f_prof_2(coef,set,sol,x,y):
    sol['f'][x,y] = numpy.exp(-(x*set['Hh'])**2/0.45)
    return sol

def c_prof_1(coef,set,sol):
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            sol['c'][x,y] = 0.1#numpy.exp(-(1-x*set['Hh'])**2/0.45)
            if set['f_prof'] == 'F2':
                sol = f_prof_2(coef,set,sol,x,y)
            elif set['f_prof'] == 'F1':
                sol = f_prof_1(coef,set,sol,x,y)
    return sol
    
def c_prof_2(coef,set,sol):
    viu = (numpy.sqrt(5)-0.1)/(numpy.sqrt(5)-1)
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            r_c = numpy.sqrt((x*set['Hh']-1)**2+(y*set['Hh']-0.5)**2)
            if r_c >= 0.1:
                sol['c'][x,y] = (viu-r_c)**2/(viu-0.1)**2
            elif r_c>= 0 and r_c < 0.1:
                sol['c'][x,y] = 1
            if set['f_prof'] == 'F2':
                sol = f_prof_2(coef,set,sol,x,y)
            elif set['f_prof'] == 'F1':
                sol = f_prof_1(coef,set,sol,x,y)
    return sol

def init_2d_(coef,set,sol):
    sol['c'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['c_n'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['f'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    if set['c_prof'] == 'C2':
        sol = c_prof_2(coef,set,sol)
    elif set['c_prof'] == 'C1':
        sol = c_prof_1(coef,set,sol)
    return sol
        