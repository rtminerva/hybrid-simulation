from random import randint, sample, uniform
import numpy

def n_mean_function(set,sol,xb,yb,n_o):
    if yb == 1:
        if xb == 1:
            n_mean_ur = (n_o[xb+2,yb+2]+n_o[xb,yb+2]+n_o[xb+2,yb]+n_o[xb,yb])/4
            n_mean_ul = (n_o[xb,yb]+n_o[xb,yb+2])/4
            n_mean_dr = (n_o[xb,yb]+n_o[xb+2,yb])/4
            n_mean_dl = n_o[xb,yb]/4
        elif xb == set['Nx']-1:
            n_mean_ur = (n_o[xb,yb]+n_o[xb,yb+2])//4
            n_mean_ul = (n_o[xb-2,yb]+n_o[xb,yb+2]+n_o[xb-2,yb+2]+n_o[xb,yb])/4
            n_mean_dr = n_o[xb,yb]/4
            n_mean_dl = (n_o[xb,yb]+n_o[xb-2,yb])/4
        else:
            n_mean_ur = (n_o[xb+2,yb+2]+n_o[xb,yb+2]+n_o[xb+2,yb]+n_o[xb,yb])/4
            n_mean_ul = (n_o[xb-2,yb-2]+n_o[xb,yb+2]+n_o[xb-2,yb]+n_o[xb,yb])/4
            n_mean_dr = (n_o[xb,yb]+n_o[xb+2,yb])/4
            n_mean_dl = (n_o[xb,yb]+n_o[xb-2,yb])/4
    elif yb == set['Ny']-1:
        if xb == 1:
            n_mean_ur = (n_o[xb,yb]+n_o[xb+2,yb])/4
            n_mean_ul = n_o[xb,yb]/4
            n_mean_dr = (n_o[xb+2,yb-2]+n_o[xb,yb-2]+n_o[xb+2,yb]+n_o[xb,yb])/4
            n_mean_dl = (n_o[xb,yb]+n_o[xb,yb-2])/4
        elif xb == set['Nx']-1:
            n_mean_ur = n_o[xb,yb]/4
            n_mean_ul = (n_o[xb,yb]+n_o[xb-2,yb])/4
            n_mean_dr = (n_o[xb,yb]+n_o[xb,yb-2])/4
            n_mean_dl = (n_o[xb-2,yb-2]+n_o[xb,yb-2]+n_o[xb-2,yb]+n_o[xb,yb])/4
        else:
            n_mean_ur = (n_o[xb,yb]+n_o[xb+2,yb])/4
            n_mean_ul = (n_o[xb,yb]+n_o[xb-2,yb])/4
            n_mean_dr = (n_o[xb+2,yb-2]+n_o[xb,yb-2]+n_o[xb+2,yb]+n_o[xb,yb])/4
            n_mean_dl = (n_o[xb-2,yb-2]+n_o[xb,yb-2]+n_o[xb-2,yb]+n_o[xb,yb])/4
    else:
        if xb == 1:
            n_mean_ur = (n_o[xb+2,yb+2]+n_o[xb,yb+2]+n_o[xb+2,yb]+n_o[xb,yb])/4
            n_mean_ul = (n_o[xb,yb]+n_o[xb,yb+2])/4
            n_mean_dr = (n_o[xb+2,yb-2]+n_o[xb,yb-2]+n_o[xb+2,yb]+n_o[xb,yb])/4
            n_mean_dl = (n_o[xb,yb]+n_o[xb,yb-2])/4
        elif xb == set['Nx']-1:
            n_mean_ur = (n_o[xb,yb]+n_o[xb,yb+2])/4
            n_mean_ul = (n_o[xb-2,yb+2]+n_o[xb,yb+2]+n_o[xb-2,yb]+n_o[xb,yb])/4
            n_mean_dr = (n_o[xb,yb]+n_o[xb,yb-2])/4
            n_mean_dl = (n_o[xb-2,yb-2]+n_o[xb,yb-2]+n_o[xb-2,yb]+n_o[xb,yb])/4
        else:
            n_mean_ur = (n_o[xb+2,yb+2]+n_o[xb,yb+2]+n_o[xb+2,yb]+n_o[xb,yb])/4
            n_mean_ul = (n_o[xb-2,yb+2]+n_o[xb,yb+2]+n_o[xb-2,yb]+n_o[xb,yb])/4
            n_mean_dr = (n_o[xb+2,yb-2]+n_o[xb,yb-2]+n_o[xb+2,yb]+n_o[xb,yb])/4
            n_mean_dl = (n_o[xb-2,yb-2]+n_o[xb,yb-2]+n_o[xb-2,yb]+n_o[xb,yb])/4
    n_mean = [n_mean_ur, n_mean_ul, n_mean_dr, n_mean_dl]
    return n_mean

def max_min_c(set,sol,x,y,c_o): #2.3.(1).(1)
    cijx = (c_o[x,y]-c_o[x-2,y]+c_o[x,y-2]-c_o[x-2,y-2])/(2*set['h'])
    cijy = (c_o[x,y]-c_o[x,y-2]+c_o[x-2,y]-c_o[x-2,y-2])/(2*set['h'])
    cijx_p = max(0,cijx)
    cijx_n = max(0,-cijx)
    cijy_p = max(0,cijy)
    cijy_n = max(0,-cijy)
    return cijx_p, cijx_n, cijy_p, cijy_n

def max_min_c(set,sol,x,y,c_o): #2.3.(1).(1)
    cijx = (c_o[x,y]-c_o[x-2,y]+c_o[x,y-2]-c_o[x-2,y-2])/(2*set['h'])
    cijy = (c_o[x,y]-c_o[x,y-2]+c_o[x-2,y]-c_o[x-2,y-2])/(2*set['h'])
    cijx_p = max(0,cijx)
    cijx_n = max(0,-cijx)
    cijy_p = max(0,cijy)
    cijy_n = max(0,-cijy)
    return cijx_p, cijx_n, cijy_p, cijy_n

def F_vector_sol(coef,set,sol,n_o,b_o,c_o): #2.3.(1)
    F_sol_1 = numpy.zeros((set['Nx']+1,set['Ny']+1))
    F_sol_2 = numpy.zeros((set['Nx']+1,set['Ny']+1))
    G_plus_1 = 0
    G_plus_2 = 0
    G_neg_1 = 0
    G_neg_2 = 0
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            if y == set['Ny']:
                if not x == 0:
                    if not x == set['Nx']:
                        #chemo_coef = coef['Ki']/(1+coef['Al_n']*(c_o[x,y]+c_o[x-2,y]+c_o[x,y-2]+c_o[x-2,y-2])/4)
                        cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x,y,c_o) #2.3.(1).(1)
                        bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x,y,b_o) #2.3.(1).(2)
                        G_plus_1 = coef['Ki_n']*cijx_p-coef['Ro_n']*bijx_p
                        
                        #chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(c_o[x,y]+c_o[x+2,y]+c_o[x,y-2]+c_o[x+2,y-2])/4)
                        cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x+2,y,c_o) #2.3.(1).(1)
                        bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x+2,y,b_o) #2.3.(1).(2)
                        G_neg_1 = coef['Ki_n']*cijx_n-coef['Ro_n']*bijx_n
                        
                        F_sol_1[x,y] = -coef['D_n']/(set['h'])*(n_o[x+1,y-1]-n_o[x-1,y-1])+n_o[x-1,y-1]*G_plus_1-n_o[x+1,y-1]*G_neg_1
                        
            elif not y == 0:
                if x == set['Nx']:
                    #chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(c_o[x,y]+c_o[x-2,y]+c_o[x,y-2]+c_o[x-2,y-2])/4)
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x,y,c_o) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x,y,b_o) #2.3.(1).(2)
                    G_plus_2 = coef['Ki_n']*cijy_p-coef['Ro_n']*bijy_p
                    
                    #chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(c_o[x,y]+c_o[x-2,y]+c_o[x-2,y+2]+c_o[x,y+2])/4)
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x,y+2,c_o) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x,y+2,b_o) #2.3.(1).(2)
                    G_neg_2 = coef['Ki_n']*cijy_n-coef['Ro_n']*bijy_n
                    
                    F_sol_2[x,y] = -coef['D_n']/(set['h'])*(n_o[x-1,y+1]-n_o[x-1,y-1])+n_o[x-1,y-1]*G_plus_2-n_o[x-1,y+1]*G_neg_2
                elif not x == 0:
                    #chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(c_o[x,y]+c_o[x-2,y]+c_o[x,y-2]+c_o[x-2,y-2])/4)
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x,y,c_o) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x,y,b_o) #2.3.(1).(2)
                    G_plus_1 = coef['Ki_n']*cijx_p-coef['Ro_n']*bijx_p
                    G_plus_2 = coef['Ki_n']*cijy_p-coef['Ro_n']*bijy_p
                    
                    #chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(c_o[x,y]+c_o[x+2,y]+c_o[x,y-2]+c_o[x+2,y-2])/4)
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x+2,y,c_o) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x+2,y,b_o) #2.3.(1).(2)
                    G_neg_1 = coef['Ki_n']*cijx_n-coef['Ro_n']*bijx_n
                    
                    #chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(c_o[x,y]+c_o[x-2,y]+c_o[x-2,y+2]+c_o[x,y+2])/4)
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x,y+2,c_o) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x,y+2,b_o) #2.3.(1).(2)
                    G_neg_2 = coef['Ki_n']*cijy_n-coef['Ro_n']*bijy_n
                    
                    F_sol_1[x,y] = -coef['D_n']*(n_o[x+1,y-1]-n_o[x-1,y-1])/(set['h'])+n_o[x-1,y-1]*G_plus_1-n_o[x+1,y-1]*G_neg_1
                    F_sol_2[x,y] = -coef['D_n']*(n_o[x-1,y+1]-n_o[x-1,y-1])/(set['h'])+n_o[x-1,y-1]*G_plus_2-n_o[x-1,y+1]*G_neg_2
    return F_sol_1, F_sol_2      


def max_min_n(set,sol,x,y,n_o): #2.3.(1).(2)
    xb = x-1
    yb = y-1
    
    n_mean = n_mean_function(set,sol,xb,yb,n_o)
    
    nijx = (n_mean[0]-n_mean[1]+n_mean[2]-n_mean[3])/(2*set['h'])
    nijy = (n_mean[0]-n_mean[2]+n_mean[1]-n_mean[3])/(2*set['h'])
    #print nijx,nijy

    nijx_p = max(0,nijx)
    nijx_n = max(0,-nijx)
    nijy_p = max(0,nijy)
    nijy_n = max(0,-nijy)
    return nijx_p, nijx_n, nijy_p, nijy_n

def grad_n_vector_sol(coef,set,sol,n_o,b_o,c_o): #2.3.(1)
    grad_n_sol_1 = numpy.zeros((set['Nx']+1,set['Ny']+1))
    grad_n_sol_2 = numpy.zeros((set['Nx']+1,set['Ny']+1))
    G_plus_1 = 0
    G_plus_2 = 0
    G_neg_1 = 0
    G_neg_2 = 0
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            if y == set['Ny']:
                if not x == 0:
                    if not x == set['Nx']:
                        nijx_p, nijx_n, nijy_p, nijy_n = max_min_n(set,sol,x,y,n_o) #2.3.(1).(2)
                        G_plus_1 = coef['Ki_b']*nijx_p
                        
                        nijx_p, nijx_n, nijy_p, nijy_n = max_min_n(set,sol,x+2,y,n_o) #2.3.(1).(2)
                        G_neg_1 = coef['Ki_b']*nijx_n
                        
                        grad_n_sol_1[x,y] = b_o[x-1,y-1]*G_plus_1-b_o[x+1,y-1]*G_neg_1
                        
            elif not y == 0:
                if x == set['Nx']:
                    nijx_p, nijx_n, nijy_p, nijy_n = max_min_n(set,sol,x,y,n_o) #2.3.(1).(2)
                    G_plus_2 = coef['Ki_b']*nijy_p
                    
                    nijx_p, nijx_n, nijy_p, nijy_n = max_min_n(set,sol,x,y+2,n_o) #2.3.(1).(2)
                    G_neg_2 = coef['Ki_b']*nijy_n
                    
                    grad_n_sol_2[x,y] = b_o[x-1,y-1]*G_plus_2-b_o[x-1,y+1]*G_neg_2
                elif not x == 0:
                    nijx_p, nijx_n, nijy_p, nijy_n = max_min_n(set,sol,x,y,n_o) #2.3.(1).(2)
                    G_plus_1 = coef['Ki_b']*nijx_p
                    G_plus_2 = coef['Ki_b']*nijy_p
                    
                    nijx_p, nijx_n, nijy_p, nijy_n = max_min_n(set,sol,x+2,y,n_o) #2.3.(1).(2)
                    G_neg_1 = coef['Ki_b']*nijx_n
                    
                    nijx_p, nijx_n, nijy_p, nijy_n = max_min_n(set,sol,x,y+2,n_o) #2.3.(1).(2)
                    G_neg_2 = coef['Ki_b']*nijy_n
                    
                    grad_n_sol_1[x,y] = b_o[x-1,y-1]*G_plus_1-b_o[x+1,y-1]*G_neg_1
                    grad_n_sol_2[x,y] = b_o[x-1,y-1]*G_plus_2-b_o[x-1,y+1]*G_neg_2
    return grad_n_sol_1, grad_n_sol_2      

def system_2d(coef, set, sol): #2.3
    c_o = numpy.copy(sol['c']) #to save values at time step k (we are calculating at time step k+1)
    n_o = numpy.copy(sol['n']) #to save values at time step k (we are calculating at time step k+1)
    b_o = numpy.copy(sol['b']) #to save values at time step k (we are calculating at time step k+1)
    
    '''Calculate F on each sub lattice'''
    ##2nd method*
    F_sol_1, F_sol_2 = F_vector_sol(coef, set, sol, n_o, b_o, c_o) #2.3.(1)
    grad_n_sol_1, grad_n_sol_2  = grad_n_vector_sol(coef,set,sol,n_o,b_o,c_o)
    
    '''Solve b at main lattice'''
    coef_b = 1
    for y in range(1,set['Ny'],2):
        for x in range(1,set['Nx'],2):
            #b_mean = b_mean_function(set,sol,x,y)
            kinetic_b =0# set['dt']*coef['mu2']*b_o[x,y]*(1-b_o[x,y]) + set['dt']*coef['mu3']*n_o[x,y]*b_o[x,y]*(1-(b_o[x,y])/(coef['beta1'])) + set['dt']*coef['Lam_3']*(coef['Lam_1']*(n_o[x,y])**2+coef['Lam_2']*n_o[x,y]*b_o[x,y])
            kinetic_n =0# set['dt']*coef['mu1']*n_o[x,y] - set['dt']*coef['Lam_1']*(n_o[x,y])**2-set['dt']*coef['Lam_2']*n_o[x,y]*b_o[x,y]
            if y == 1:
                if x == 1:                 
                    move_n = set['dt']*(F_sol_1[x+1,y+1]+F_sol_2[x+1,y+1])/set['h']
                    move_b = set['dt']*coef['Ki_b']*(grad_n_sol_1[x+1,y+1]+grad_n_sol_2[x+1,y+1])/set['h'] - coef['D_b']*set['dt']*(b_o[x+2,y]+b_o[x,y+2]-2*b_o[x,y])/(set['h']**2)
                
                elif x == set['Nx']-1:
                    move_n = set['dt']*(-F_sol_1[x-1,y+1]+F_sol_2[x+1,y+1])/set['h']
                    move_b = set['dt']*coef['Ki_b']*(-grad_n_sol_1[x-1,y+1]+grad_n_sol_2[x+1,y+1])/set['h'] - coef['D_b']*set['dt']*(b_o[x-2,y]+b_o[x,y+2]-2*b_o[x,y])/(set['h']**2)
                    
                else:
                    move_n = set['dt']*(F_sol_1[x+1,y+1]-F_sol_1[x-1,y+1]+F_sol_2[x+1,y+1])/set['h']
                    move_b = set['dt']*coef['Ki_b']*(grad_n_sol_1[x+1,y+1]-grad_n_sol_1[x-1,y+1]+grad_n_sol_2[x+1,y+1])/set['h'] - coef['D_b']*set['dt']*(b_o[x+2,y]+b_o[x-2,y]+b_o[x,y+2]-3*b_o[x,y])/(set['h']**2)
                    
            elif y == set['Ny']-1:
                if x == 1:
                    move_n = set['dt']*(F_sol_1[x+1,y+1]-F_sol_2[x+1,y-1])/set['h']
                    move_b = set['dt']*coef['Ki_b']*(grad_n_sol_1[x+1,y+1]-grad_n_sol_2[x+1,y-1])/set['h'] - coef['D_b']*set['dt']*(b_o[x+2,y]+b_o[x,y-2]-2*b_o[x,y])/(set['h']**2)
                    
                elif x == set['Nx']-1:
                    move_n = set['dt']*(-F_sol_1[x-1,y+1]-F_sol_2[x+1,y-1])/set['h']
                    move_b = set['dt']*coef['Ki_b']*(-grad_n_sol_1[x-1,y+1]-grad_n_sol_2[x+1,y-1])/set['h'] - coef['D_b']*set['dt']*(b_o[x-2,y]+b_o[x,y-2]-2*b_o[x,y])/(set['h']**2)
                    
                else:
                    move_n = set['dt']*(F_sol_1[x+1,y+1]-F_sol_1[x-1,y+1]-F_sol_2[x+1,y-1])/set['h']
                    move_b = set['dt']*coef['Ki_b']*(grad_n_sol_1[x+1,y+1]-grad_n_sol_1[x-1,y+1]-grad_n_sol_2[x+1,y-1])/set['h'] - coef['D_b']*set['dt']*(b_o[x+2,y]+b_o[x-2,y]+b_o[x,y-2]-3*b_o[x,y])/(set['h']**2)
                    
            else:
                if x == 1:
                    move_n = set['dt']*(F_sol_1[x+1,y+1]+F_sol_2[x+1,y+1]-F_sol_2[x+1,y-1])/set['h']
                    move_b = set['dt']*coef['Ki_b']*(grad_n_sol_1[x+1,y+1]+grad_n_sol_2[x+1,y+1]-grad_n_sol_2[x+1,y-1])/set['h'] - coef['D_b']*set['dt']*(b_o[x+2,y]+b_o[x,y+2]+b_o[x,y-2]-3*b_o[x,y])/(set['h']**2)
                    
                elif x == set['Nx']-1:
                    move_n = set['dt']*(-F_sol_1[x-1,y+1]+F_sol_2[x+1,y+1]-F_sol_2[x+1,y-1])/set['h']
                    move_b = set['dt']*coef['Ki_b']*(-grad_n_sol_1[x-1,y+1]+grad_n_sol_2[x+1,y+1]-grad_n_sol_2[x+1,y-1])/set['h'] - coef['D_b']*set['dt']*(b_o[x-2,y]+b_o[x,y+2]+b_o[x,y-2]-3*b_o[x,y])/(set['h']**2)
                    
                else:
                    move_n = set['dt']*(F_sol_1[x+1,y+1]-F_sol_1[x-1,y+1]+F_sol_2[x+1,y+1]-F_sol_2[x+1,y-1])/set['h']
                    move_b = set['dt']*coef['Ki_b']*(grad_n_sol_1[x+1,y+1]-grad_n_sol_1[x-1,y+1]+grad_n_sol_2[x+1,y+1]-grad_n_sol_2[x+1,y-1])/set['h'] - coef['D_b']*set['dt']*(b_o[x+2,y]+b_o[x-2,y]+b_o[x,y+2]+b_o[x,y-2]-4*b_o[x,y])/(set['h']**2)
            sol['n'][x,y] = n_o[x,y] - move_n + kinetic_n
            sol['b'][x,y] = b_o[x,y] - move_b + kinetic_b
                    
                                     
    '''Solve c at sub lattice'''
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            if y == 0: 
                if x == 0:
                    mean_b = b_o[x+1,y+1]/4
                    mean_n = n_o[x+1,y+1]/4
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    move_c = coef['D_c']*set['dt']*(c_o[x+2,y]+c_o[x,y+2]-2*c_o[x,y])/(set['h']**2)
                    
                elif x == set['Nx']:
                    mean_b = b_o[x-1,y+1]/4
                    mean_n = n_o[x-1,y+1]/4
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    move_c = coef['D_c']*set['dt']*(c_o[x-2,y]+c_o[x,y+2]-2*c_o[x,y])/(set['h']**2)
                   
                else:
                    mean_b = (b_o[x-1,y+1] + b_o[x+1,y+1])/4
                    mean_n = (n_o[x-1,y+1] + n_o[x+1,y+1])/4
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    move_c = coef['D_c']*set['dt']*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]-3*c_o[x,y])/(set['h']**2)
                    
            elif y == set['Ny']:
                if x == 0:
                    mean_b = b_o[x+1,y-1]/4
                    mean_n = n_o[x+1,y-1]/4
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    move_c = coef['D_c']*set['dt']*(c_o[x+2,y]+c_o[x,y-2]-2*c_o[x,y])/(set['h']**2)
                    
                elif x == set['Nx']:
                    mean_b = b_o[x-1,y-1]/4
                    mean_n = n_o[x-1,y-1]/4
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    move_c = coef['D_c']*set['dt']*(c_o[x-2,y]+c_o[x,y-2]-2*c_o[x,y])/(set['h']**2)
                           
                else:
                    mean_b = (b_o[x-1,y-1] + b_o[x+1,y-1])/4
                    mean_n = (n_o[x-1,y-1] + n_o[x+1,y-1])/4
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0          
                    move_c = coef['D_c']*set['dt']*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y-2]-3*c_o[x,y])/(set['h']**2)
                       
            else:
                if x == 0:
                    mean_b = (b_o[x+1,y-1] + b_o[x+1,y+1])/2
                    mean_n = (n_o[x+1,y-1] + n_o[x+1,y+1])/2
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    move_c = coef['D_c']*set['dt']*(c_o[x+2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])/(set['h']**2)
                    
                elif x == set['Nx']:
                    mean_b = (b_o[x-1,y-1] + b_o[x-1,y+1])/4
                    mean_n = (n_o[x-1,y-1] + n_o[x-1,y+1])/4
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    move_c = coef['D_c']*set['dt']*(c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])/(set['h']**2)
                    
                else:
                    mean_b = (b_o[x+1,y+1] + b_o[x-1,y+1] + b_o[x+1,y-1] + b_o[x-1,y-1])/4
                    mean_n = (n_o[x+1,y+1] + n_o[x-1,y+1] + n_o[x+1,y-1] + n_o[x-1,y-1])/4
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    move_c = coef['D_c']*set['dt']*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-4*c_o[x,y])/(set['h']**2)
            prolifer_c = set['dt']*coef['mu4']*S
            digestion_c = set['dt']*coef['Lam_4']*c_o[x,y]*mean_n
            degradation_c = set['dt']*coef['mu5']*c_o[x,y] 
            sol['c'][x,y] = c_o[x,y] + prolifer_c - digestion_c - degradation_c + move_c        
    return sol