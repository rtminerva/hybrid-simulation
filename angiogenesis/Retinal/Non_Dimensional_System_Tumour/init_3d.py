import numpy

def f_prof_1(coef,set,sol,x,y,z):
    sol['f'][x,y,z] = 0.5
    return sol

def f_prof_2(coef,set,sol,x,y,z):
    sol['f'][x,y,z] = numpy.exp(-(x*set['Hh'])**2/0.45)
    return sol

def c_prof_1(coef,set,sol):
    for z in range(0,set['Nz']+1,2):
        for y in range(0,set['Ny']+1,2):
            for x in range(0,set['Nx']+1,2):
                sol['c'][x,y,z] = numpy.exp(-(1-x*set['Hh'])**2/0.45)
                if not set['Ro'] == 0:
                    if set['f_prof'] == 'F2':
                        sol = f_prof_2(coef,set,sol,x,y,z)
                    elif set['f_prof'] == 'F1':
                        sol = f_prof_1(coef,set,sol,x,y,z)
    return sol
    
def c_prof_2(coef,set,sol):
    viu = (numpy.sqrt(5)-0.1)/(numpy.sqrt(5)-1)
    for z in range(0,set['Nz']+1,2):
        for y in range(0,set['Ny']+1,2):
            for x in range(0,set['Nx']+1,2):
                r_c = numpy.sqrt((x*set['Hh']-0.5)**2+(y*set['Hh']-0.5)**2+(z*set['Hh']-1)**2)
                if r_c >= 0.1:
                    sol['c'][x,y,z] = (viu-r_c)**2/(viu-0.1)**2
                    #sol['tumor'][x,y,z] = r_c
                elif r_c>= 0 and r_c < 0.1:
                    sol['c'][x,y,z] = 1
                if not set['Ro'] == 0:
                    if set['f_prof'] == 'F2':
                        sol = f_prof_2(coef,set,sol,x,y,z)
                    elif set['f_prof'] == 'F1':
                        sol = f_prof_1(coef,set,sol,x,y,z)
    return sol

def init_3d_(coef,set,sol):
    sol['c'] = numpy.zeros((set['Nx']+1,set['Ny']+1,set['Nz']+1))
    if not set['Ro'] == 0:
        sol['f'] = numpy.zeros((set['Nx']+1,set['Ny']+1,set['Nz']+1))
    #sol['tumor'] = numpy.zeros((set['Nx']+1,set['Ny']+1,set['Nz']+1))
    if set['c_prof'] == 'C2':
        sol = c_prof_2(coef,set,sol)
    elif set['c_prof'] == 'C1':
        sol = c_prof_1(coef,set,sol)
    return sol
        