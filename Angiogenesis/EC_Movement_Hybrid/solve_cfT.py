from random import randint, sample, uniform
import numpy

def b_mean_function(set,sol,xb,yb,b_o):
    if yb == 1:
        if xb == 1:
            b_mean_ur = (b_o[xb+2,yb+2]+b_o[xb,yb+2]+b_o[xb+2,yb]+b_o[xb,yb])/4
            b_mean_ul = (b_o[xb,yb]+b_o[xb,yb+2])/2
            b_mean_dr = (b_o[xb,yb]+b_o[xb+2,yb])/2
            b_mean_dl = b_o[xb,yb]
        elif xb == set['Nx']-1:
            b_mean_ur = (b_o[xb,yb]+b_o[xb,yb+2])/2
            b_mean_ul = (b_o[xb-2,yb]+b_o[xb,yb+2]+b_o[xb-2,yb+2]+b_o[xb,yb])/4
            b_mean_dr = b_o[xb,yb]
            b_mean_dl = (b_o[xb,yb]+b_o[xb-2,yb])/2
        else:
            b_mean_ur = (b_o[xb+2,yb+2]+b_o[xb,yb+2]+b_o[xb+2,yb]+b_o[xb,yb])/4
            b_mean_ul = (b_o[xb-2,yb-2]+b_o[xb,yb+2]+b_o[xb-2,yb]+b_o[xb,yb])/4
            b_mean_dr = (b_o[xb,yb]+b_o[xb+2,yb])/2
            b_mean_dl = (b_o[xb,yb]+b_o[xb-2,yb])/2
    elif yb == set['Ny']-1:
        if xb == 1:
            b_mean_ur = (b_o[xb,yb]+b_o[xb+2,yb])/2
            b_mean_ul = b_o[xb,yb]
            b_mean_dr = (b_o[xb+2,yb-2]+b_o[xb,yb-2]+b_o[xb+2,yb]+b_o[xb,yb])/4
            b_mean_dl = (b_o[xb,yb]+b_o[xb,yb-2])/2
        elif xb == set['Nx']-1:
            b_mean_ur = b_o[xb,yb]
            b_mean_ul = (b_o[xb,yb]+b_o[xb-2,yb])/2
            b_mean_dr = (b_o[xb,yb]+b_o[xb,yb-2])/2
            b_mean_dl = (b_o[xb-2,yb-2]+b_o[xb,yb-2]+b_o[xb-2,yb]+b_o[xb,yb])/4
        else:
            b_mean_ur = (b_o[xb,yb]+b_o[xb+2,yb])/2
            b_mean_ul = (b_o[xb,yb]+b_o[xb-2,yb])/2
            b_mean_dr = (b_o[xb+2,yb-2]+b_o[xb,yb-2]+b_o[xb+2,yb]+b_o[xb,yb])/4
            b_mean_dl = (b_o[xb-2,yb-2]+b_o[xb,yb-2]+b_o[xb-2,yb]+b_o[xb,yb])/4
    else:
        if xb == 1:
            b_mean_ur = (b_o[xb+2,yb+2]+b_o[xb,yb+2]+b_o[xb+2,yb]+b_o[xb,yb])/4
            b_mean_ul = (b_o[xb,yb]+b_o[xb,yb+2])/2
            b_mean_dr = (b_o[xb+2,yb-2]+b_o[xb,yb-2]+b_o[xb+2,yb]+b_o[xb,yb])/4
            b_mean_dl = (b_o[xb,yb]+b_o[xb,yb-2])/2
        elif xb == set['Nx']-1:
            b_mean_ur = (b_o[xb,yb]+b_o[xb,yb+2])/2
            b_mean_ul = (b_o[xb-2,yb+2]+b_o[xb,yb+2]+b_o[xb-2,yb]+b_o[xb,yb])/4
            b_mean_dr = (b_o[xb,yb]+b_o[xb,yb-2])/2
            b_mean_dl = (b_o[xb-2,yb-2]+b_o[xb,yb-2]+b_o[xb-2,yb]+b_o[xb,yb])/4
        else:
            b_mean_ur = (b_o[xb+2,yb+2]+b_o[xb,yb+2]+b_o[xb+2,yb]+b_o[xb,yb])/4
            b_mean_ul = (b_o[xb-2,yb+2]+b_o[xb,yb+2]+b_o[xb-2,yb]+b_o[xb,yb])/4
            b_mean_dr = (b_o[xb+2,yb-2]+b_o[xb,yb-2]+b_o[xb+2,yb]+b_o[xb,yb])/4
            b_mean_dl = (b_o[xb-2,yb-2]+b_o[xb,yb-2]+b_o[xb-2,yb]+b_o[xb,yb])/4
    b_mean = [b_mean_ur, b_mean_ul, b_mean_dr, b_mean_dl]
    return b_mean

def max_min_c(set,sol,x,y,c_o): #2.3.(1).(1)
    cijx = (c_o[x,y]-c_o[x-2,y]+c_o[x,y-2]-c_o[x-2,y-2])/(2*set['h'])
    cijy = (c_o[x,y]-c_o[x,y-2]+c_o[x-2,y]-c_o[x-2,y-2])/(2*set['h'])
    cijx_p = max(0,cijx)
    cijx_n = max(0,-cijx)
    cijy_p = max(0,cijy)
    cijy_n = max(0,-cijy)
    return cijx_p, cijx_n, cijy_p, cijy_n

def max_min_b(set,sol,x,y,b_o): #2.3.(1).(2)
    xb = x-1
    yb = y-1
    
    b_mean = b_mean_function(set,sol,xb,yb,b_o)
    
    bijx = (b_mean[0]-b_mean[1]+b_mean[2]-b_mean[3])/(2*set['h'])
    bijy = (b_mean[0]-b_mean[2]+b_mean[1]-b_mean[3])/(2*set['h'])
    #print bijx,bijy

    bijx_p = max(0,bijx)
    bijx_n = max(0,-bijx)
    bijy_p = max(0,bijy)
    bijy_n = max(0,-bijy)
    return bijx_p, bijx_n, bijy_p, bijy_n

def F_vector_sol(coef,set,sol,n_o,b_o,c_o): #2.3.(1)
    F_sol_1 = numpy.zeros((set['Nx']+1,set['Ny']+1))
    F_sol_2 = numpy.zeros((set['Nx']+1,set['Ny']+1))
    G_plus_1 = 0
    G_plus_2 = 0
    G_neg_1 = 0
    G_neg_2 = 0
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
#             if G_plus_1 != 0 or G_plus_2 != 0 or G_neg_1 != 0 or G_neg_2 != 0:
#                 print G_plus_1, G_plus_2, G_neg_1, G_neg_2
#                 print x,y
            if y == set['Ny']:
                if not x == 0:
                    if not x == set['Nx']:
                        #chemo_coef = coef['Ki']/(1+coef['Al_n']*(c_o[x,y]+c_o[x-2,y]+c_o[x,y-2]+c_o[x-2,y-2])/4)
                        cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x,y,c_o) #2.3.(1).(1)
                        bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x,y,b_o) #2.3.(1).(2)
                        G_plus_1 = coef['Ki']*cijx_p-coef['C_2']*bijx_p
                        
                        #chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(c_o[x,y]+c_o[x+2,y]+c_o[x,y-2]+c_o[x+2,y-2])/4)
                        cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x+2,y,c_o) #2.3.(1).(1)
                        bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x+2,y,b_o) #2.3.(1).(2)
                        G_neg_1 = coef['Ki']*cijx_n-coef['C_2']*bijx_n
                        
                        F_sol_1[x,y] = -coef['C_1']/(set['h'])*(n_o[x+1,y-1]-n_o[x-1,y-1])+n_o[x-1,y-1]*G_plus_1-n_o[x+1,y-1]*G_neg_1
                        
            elif not y == 0:
                if x == set['Nx']:
                    #chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(c_o[x,y]+c_o[x-2,y]+c_o[x,y-2]+c_o[x-2,y-2])/4)
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x,y,c_o) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x,y,b_o) #2.3.(1).(2)
                    G_plus_2 = coef['Ki']*cijy_p-coef['C_2']*bijy_p
                    
                    #chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(c_o[x,y]+c_o[x-2,y]+c_o[x-2,y+2]+c_o[x,y+2])/4)
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x,y+2,c_o) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x,y+2,b_o) #2.3.(1).(2)
                    G_neg_2 = coef['Ki']*cijy_n-coef['C_2']*bijy_n
                    
                    F_sol_2[x,y] = -coef['C_1']/(set['h'])*(n_o[x-1,y+1]-n_o[x-1,y-1])+n_o[x-1,y-1]*G_plus_2-n_o[x-1,y+1]*G_neg_2
                elif not x == 0:
                    #chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(c_o[x,y]+c_o[x-2,y]+c_o[x,y-2]+c_o[x-2,y-2])/4)
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x,y,c_o) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x,y,b_o) #2.3.(1).(2)
                    G_plus_1 = coef['Ki']*cijx_p-coef['C_2']*bijx_p
                    G_plus_2 = coef['Ki']*cijy_p-coef['C_2']*bijy_p
                    
                    #chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(c_o[x,y]+c_o[x+2,y]+c_o[x,y-2]+c_o[x+2,y-2])/4)
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x+2,y,c_o) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x+2,y,b_o) #2.3.(1).(2)
                    G_neg_1 = coef['Ki']*cijx_n-coef['C_2']*bijx_n
                    
                    #chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(c_o[x,y]+c_o[x-2,y]+c_o[x-2,y+2]+c_o[x,y+2])/4)
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x,y+2,c_o) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x,y+2,b_o) #2.3.(1).(2)
                    G_neg_2 = coef['Ki']*cijy_n-coef['C_2']*bijy_n
                    
                    F_sol_1[x,y] = -coef['C_1']*(n_o[x+1,y-1]-n_o[x-1,y-1])/(set['h'])+n_o[x-1,y-1]*G_plus_1-n_o[x+1,y-1]*G_neg_1
                    F_sol_2[x,y] = -coef['C_1']*(n_o[x-1,y+1]-n_o[x-1,y-1])/(set['h'])+n_o[x-1,y-1]*G_plus_2-n_o[x-1,y+1]*G_neg_2
   
    return F_sol_1, F_sol_2      

def F_mean_vector_sol(F_sol_1, F_sol_2, set):
    F_mean_sol_1 = numpy.zeros((set['Nx']+1,set['Ny']+1))
    F_mean_sol_2 = numpy.zeros((set['Nx']+1,set['Ny']+1))
    for y in range(1,set['Ny'],2):
        for x in range(1,set['Nx'],2):
            #print F_sol_1[x,y]+F_sol_1[x-1,y+1]+F_sol_1[x+1,y-1]+F_sol_1[x-1,y-1]
            F_mean_sol_1[x,y] = (F_sol_1[x+1,y+1]+F_sol_1[x-1,y+1]+F_sol_1[x+1,y-1]+F_sol_1[x-1,y-1])/4
            F_mean_sol_2[x,y] = (F_sol_2[x+1,y+1]+F_sol_2[x-1,y+1]+F_sol_2[x+1,y-1]+F_sol_2[x-1,y-1])/4
                
    return F_mean_sol_1, F_mean_sol_2

'''For Continuous Method:start
def F_vector_sol_con(coef,set,sol,n1_o,b1_o,c1_o): #2.3.(1)
    F_sol_1_con = numpy.zeros((set['Nx']+1,set['Ny']+1))
    F_sol_2_con = numpy.zeros((set['Nx']+1,set['Ny']+1))
    G_plus_1 = 0
    G_plus_2 = 0
    G_neg_1 = 0
    G_neg_2 = 0
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
#             if G_plus_1 != 0 or G_plus_2 != 0 or G_neg_1 != 0 or G_neg_2 != 0:
#                 print G_plus_1, G_plus_2, G_neg_1, G_neg_2
#                 print x,y
            if y == set['Ny']:
                if not x == 0:
                    if not x == set['Nx']:
                        #chemo_coef = coef['Ki']/(1+coef['Al_n']*(c_o[x,y]+c_o[x-2,y]+c_o[x,y-2]+c_o[x-2,y-2])/4)
                        cijx_p, cijx_n, cijy_p, cijy_n = max_min_c_con(set,sol,x,y,c1_o) #2.3.(1).(1)
                        bijx_p, bijx_n, bijy_p, bijy_n = max_min_b_con(set,sol,x,y,b1_o) #2.3.(1).(2)
                        G_plus_1 = coef['Ki']*cijx_p-coef['C_2']*bijx_p
                        
                        #chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(c_o[x,y]+c_o[x+2,y]+c_o[x,y-2]+c_o[x+2,y-2])/4)
                        cijx_p, cijx_n, cijy_p, cijy_n = max_min_c_con(set,sol,x+2,y,c1_o) #2.3.(1).(1)
                        bijx_p, bijx_n, bijy_p, bijy_n = max_min_b_con(set,sol,x+2,y,b1_o) #2.3.(1).(2)
                        G_neg_1 = coef['Ki']*cijx_n-coef['C_2']*bijx_n
                        
                        F_sol_1_con[x,y] = -coef['C_1']/(set['h'])*(n1_o[x+1,y-1]-n1_o[x-1,y-1])+n1_o[x-1,y-1]*G_plus_1-n1_o[x+1,y-1]*G_neg_1
                        
            elif not y == 0:
                if x == set['Nx']:
                    #chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(c_o[x,y]+c_o[x-2,y]+c_o[x,y-2]+c_o[x-2,y-2])/4)
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c_con(set,sol,x,y,c1_o) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b_con(set,sol,x,y,b1_o) #2.3.(1).(2)
                    G_plus_2 = coef['Ki']*cijy_p-coef['C_2']*bijy_p
                    
                    #chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(c_o[x,y]+c_o[x-2,y]+c_o[x-2,y+2]+c_o[x,y+2])/4)
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c_con(set,sol,x,y+2,c1_o) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b_con(set,sol,x,y+2,b1_o) #2.3.(1).(2)
                    G_neg_2 = coef['Ki']*cijy_n-coef['C_2']*bijy_n
                    
                    F_sol_2_con[x,y] = -coef['C_1']/(set['h'])*(n1_o[x-1,y+1]-n1_o[x-1,y-1])+n1_o[x-1,y-1]*G_plus_2-n1_o[x-1,y+1]*G_neg_2
                elif not x == 0:
                    #chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(c_o[x,y]+c_o[x-2,y]+c_o[x,y-2]+c_o[x-2,y-2])/4)
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c_con(set,sol,x,y,c1_o) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b_con(set,sol,x,y,b1_o) #2.3.(1).(2)
                    G_plus_1 = coef['Ki']*cijx_p-coef['C_2']*bijx_p
                    G_plus_2 = coef['Ki']*cijy_p-coef['C_2']*bijy_p
                    
                    #chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(c_o[x,y]+c_o[x+2,y]+c_o[x,y-2]+c_o[x+2,y-2])/4)
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c_con(set,sol,x+2,y,c1_o) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b_con(set,sol,x+2,y,b1_o) #2.3.(1).(2)
                    G_neg_1 = coef['Ki']*cijx_n-coef['C_2']*bijx_n
                    
                    #chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(c_o[x,y]+c_o[x-2,y]+c_o[x-2,y+2]+c_o[x,y+2])/4)
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c_con(set,sol,x,y+2,c1_o) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b_con(set,sol,x,y+2,b1_o) #2.3.(1).(2)
                    G_neg_2 = coef['Ki']*cijy_n-coef['C_2']*bijy_n
                    
                    F_sol_1_con[x,y] = -coef['C_1']*(n1_o[x+1,y-1]-n1_o[x-1,y-1])/(set['h'])+n1_o[x-1,y-1]*G_plus_1-n1_o[x+1,y-1]*G_neg_1
                    F_sol_2_con[x,y] = -coef['C_1']*(n1_o[x-1,y+1]-n1_o[x-1,y-1])/(set['h'])+n1_o[x-1,y-1]*G_plus_2-n1_o[x-1,y+1]*G_neg_2
   
    return F_sol_1_con, F_sol_2_con 

def F_mean_vector_sol_con(F_sol_1_con, F_sol_2_con, set):
    F_mean_sol_1_con = numpy.zeros((set['Nx']+1,set['Ny']+1))
    F_mean_sol_2_con = numpy.zeros((set['Nx']+1,set['Ny']+1))
    for y in range(1,set['Ny'],2):
        for x in range(1,set['Nx'],2):
            #print F_sol_1[x,y]+F_sol_1[x-1,y+1]+F_sol_1[x+1,y-1]+F_sol_1[x-1,y-1]
            F_mean_sol_1_con[x,y] = (F_sol_1_con[x+1,y+1]+F_sol_1_con[x-1,y+1]+F_sol_1_con[x+1,y-1]+F_sol_1_con[x-1,y-1])/4
            F_mean_sol_2_con[x,y] = (F_sol_2_con[x+1,y+1]+F_sol_2_con[x-1,y+1]+F_sol_2_con[x+1,y-1]+F_sol_2_con[x-1,y-1])/4
                
    return F_mean_sol_1_con, F_mean_sol_2_con
For Continuous Method:end'''

def h_funct(norm,x):
    if norm < 1:
        hs = 0
    elif norm < 25:
        hs = 1+(0.5-1)*()/(25-1)

def c_f_T(coef, set, sol): #2.3
    c_o = numpy.copy(sol['c'])
    b_o = numpy.copy(sol['b'])
    
    '''Solve b at main lattice'''
    for y in range(1,set['Ny'],2):
        for x in range(1,set['Nx'],2):
            if y == 1:
                if x == 1:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*((b_o[x,y]*sol['Vb_x'][x,y]-b_o[x+2,y]*sol['Vb_x'][x+2,y])+(b_o[x,y]*sol['Vb_y'][x,y]-b_o[x,y+2]*sol['Vb_y'][x,y+2]))/set['h']
                elif x == set['Nx']-1:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*(-(b_o[x-2,y]*sol['Vb_x'][x-2,y]-b_o[x,y]*sol['Vb_x'][x,y])+(b_o[x,y]*sol['Vb_y'][x,y]-b_o[x,y+2]*sol['Vb_y'][x,y+2]))/set['h']
                else:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*((b_o[x,y]*sol['Vb_x'][x,y]-b_o[x+2,y]*sol['Vb_x'][x+2,y])-(b_o[x-2,y]*sol['Vb_x'][x-2,y]-b_o[x,y]*sol['Vb_x'][x,y])+(b_o[x,y]*sol['Vb_y'][x,y]-b_o[x,y+2]*sol['Vb_y'][x,y+2]))/set['h']
            elif y == set['Ny']-1:
                if x == 1:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*((b_o[x,y]*sol['Vb_x'][x,y]-b_o[x+2,y]*sol['Vb_x'][x+2,y])-(b_o[x,y-2]*sol['Vb_y'][x,y-2]-b_o[x,y]*sol['Vb_y'][x,y]))/set['h']
                elif x == set['Nx']-1:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*(-(b_o[x-2,y]*sol['Vb_x'][x-2,y]-b_o[x,y]*sol['Vb_x'][x,y])-(b_o[x,y-2]*sol['Vb_y'][x,y-2]-b_o[x,y]*sol['Vb_y'][x,y]))/set['h']
                else:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*((b_o[x,y]*sol['Vb_x'][x,y]-b_o[x+2,y]*sol['Vb_x'][x+2,y])-(b_o[x-2,y]*sol['Vb_x'][x-2,y]-b_o[x,y]*sol['Vb_x'][x,y])-(b_o[x,y-2]*sol['Vb_y'][x,y-2]-b_o[x,y]*sol['Vb_y'][x,y]))/set['h']
            else:
                if x == 1:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*((b_o[x,y]*sol['Vb_x'][x,y]-b_o[x+2,y]*sol['Vb_x'][x+2,y])+(b_o[x,y]*sol['Vb_y'][x,y]-b_o[x,y+2]*sol['Vb_y'][x,y+2])-(b_o[x,y-2]*sol['Vb_y'][x,y-2]-b_o[x,y]*sol['Vb_y'][x,y]))/set['h']
                elif x == set['Nx']-1:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*(-(b_o[x-2,y]*sol['Vb_x'][x-2,y]-b_o[x,y]*sol['Vb_x'][x,y])+(b_o[x,y]*sol['Vb_y'][x,y]-b_o[x,y+2]*sol['Vb_y'][x,y+2])-(b_o[x,y-2]*sol['Vb_y'][x,y-2]-b_o[x,y]*sol['Vb_y'][x,y]))/set['h']  
                else:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*((b_o[x,y]*sol['Vb_x'][x,y]-b_o[x+2,y]*sol['Vb_x'][x+2,y])-(b_o[x-2,y]*sol['Vb_x'][x-2,y]-b_o[x,y]*sol['Vb_x'][x,y])+(b_o[x,y]*sol['Vb_y'][x,y]-b_o[x,y+2]*sol['Vb_y'][x,y+2])-(b_o[x,y-2]*sol['Vb_y'][x,y-2]-b_o[x,y]*sol['Vb_y'][x,y]))/set['h']
                                     
    '''Solve c at sub lattice'''
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            if set['con'] == False:                       
                '''TIP CELL?'''
                if [x-1,y-1] in sol['tip_cell'] or [x+1,y-1] in sol['tip_cell'] or [x+1,y+1] in sol['tip_cell'] or [x-1,y+1] in sol['tip_cell']:
                    n_tip = 1
                else:
                    n_tip = 0
            elif set['con'] == True:
                n_tip = 1     
            
            if y == 0: 
                if x == 0:
                    mean_b = b_o[x+1,y+1]
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_o[1,1]*n_tip - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x,y+2]-2*c_o[x,y])/(set['h']**2)
                    
                    mean_b = b1_o[x+1,y+1]
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c1'][x,y] = c1_o[x,y]*(1 - set['dt']*coef['Nu']*n1_o[1,1] - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c1_o[x+2,y]+c1_o[x,y+2]-2*c1_o[x,y])/(set['h']**2)
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_o[1,1]*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_o[1,1]*n_tip
                    
                elif x == set['Nx']:
                    mean_b = b_o[x-1,y+1]
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_o[set['Nx']-1,1]*n_tip - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x-2,y]+c_o[x,y+2]-2*c_o[x,y])/(set['h']**2)
                   
                    mean_b = b1_o[x-1,y+1]
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c1'][x,y] = c1_o[x,y]*(1 - set['dt']*coef['Nu']*n1_o[set['Nx']-1,1] - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c1_o[x-2,y]+c1_o[x,y+2]-2*c1_o[x,y])/(set['h']**2)
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_o[set['Nx']-1,1]*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_o[set['Nx']-1,1]*n_tip
                    
                else:
                    mean_b = (b_o[x-1,y+1] + b_o[x+1,y+1])/2
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    if n_o[x+1,1] == 1 or n_o[x-1,1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]-3*c_o[x,y])/(set['h']**2)
                    
                    mean_b = (b1_o[x-1,y+1] + b1_o[x+1,y+1])/2
                    mean_n = (n1_o[x-1,y+1] + n1_o[x+1,y+1])/2
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c1'][x,y] = c1_o[x,y]*(1 - set['dt']*coef['Nu']*mean_n - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c1_o[x+2,y]+c1_o[x-2,y]+c1_o[x,y+2]-3*c1_o[x,y])/(set['h']**2)
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
            elif y == set['Ny']:
                if x == 0:
                    mean_b = b_o[x+1,y-1]
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_o[1,set['Ny']-1]*n_tip - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x,y-2]-2*c_o[x,y])/(set['h']**2)
                    
                    mean_b = b1_o[x+1,y-1]
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c1'][x,y] = c1_o[x,y]*(1 - set['dt']*coef['Nu']*n1_o[1,set['Ny']-1] - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c1_o[x+2,y]+c1_o[x,y-2]-2*c1_o[x,y])/(set['h']**2)
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_o[1,set['Ny']-1]*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_o[1,set['Ny']-1]*n_tip
                    
                elif x == set['Nx']:
                    mean_b = b_o[x-1,y-1]
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_o[set['Nx']-1,set['Ny']-1]*n_tip - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x-2,y]+c_o[x,y-2]-2*c_o[x,y])/(set['h']**2)
                    
                    mean_b = b1_o[x-1,y-1]
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c1'][x,y] = c1_o[x,y]*(1 - set['dt']*coef['Nu']*n1_o[set['Nx']-1,set['Ny']-1] - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c1_o[x-2,y]+c1_o[x,y-2]-2*c1_o[x,y])/(set['h']**2)
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_o[set['Nx']-1,set['Ny']-1]*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_o[set['Nx']-1,set['Ny']-1]*n_tip
                           
                else:
                    mean_b = (b_o[x-1,y-1] + b_o[x+1,y-1])/2
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    if n_o[x+1,set['Ny']-1] == 1 or n_o[x-1,set['Ny']-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                               
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y-2]-3*c_o[x,y])/(set['h']**2)
                    
                    mean_b = (b1_o[x-1,y-1] + b1_o[x+1,y-1])/2
                    mean_n = (n1_o[x-1,y-1] + n1_o[x+1,y-1])/2
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c1'][x,y] = c1_o[x,y]*(1 - set['dt']*coef['Nu']*mean_n - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c1_o[x+2,y]+c1_o[x-2,y]+c1_o[x,y-2]-3*c1_o[x,y])/(set['h']**2)
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                        
            else:
                if x == 0:
                    mean_b = (b_o[x+1,y-1] + b_o[x+1,y+1])/2
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    if n_o[x+1,y+1] == 1 or n_o[x+1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                                
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])/(set['h']**2)
                    
                    mean_b = (b1_o[x+1,y-1] + b1_o[x+1,y+1])/2
                    mean_n = (n1_o[x+1,y-1] + n1_o[x+1,y+1])/2
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c1'][x,y] = c1_o[x,y]*(1 - set['dt']*coef['Nu']*mean_n - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c1_o[x+2,y]+c1_o[x,y+2]+c1_o[x,y-2]-3*c1_o[x,y])/(set['h']**2)
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
                elif x == set['Nx']:
                    mean_b = (b_o[x-1,y-1] + b_o[x-1,y+1])/2
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    if n_o[x-1,y+1] == 1 or n_o[x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                                
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])/(set['h']**2)
                    
                    mean_b = (b1_o[x-1,y-1] + b1_o[x-1,y+1])/2
                    mean_n = (n1_o[x-1,y-1] + n1_o[x-1,y+1])/2
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c1'][x,y] = c1_o[x,y]*(1 - set['dt']*coef['Nu']*mean_n - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c1_o[x-2,y]+c1_o[x,y+2]+c1_o[x,y-2]-3*c1_o[x,y])/(set['h']**2)
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
                else:
                    mean_b = (b_o[x+1,y+1] + b_o[x-1,y+1] + b_o[x+1,y-1] + b_o[x-1,y-1])/4
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    if n_o[x+1,y+1] == 1 or n_o[x-1,y+1] == 1 or n_o[x+1,y-1] == 1 or n_o[x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                               
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-4*c_o[x,y])/(set['h']**2)
                    
                    mean_b = (b1_o[x+1,y+1] + b1_o[x-1,y+1] + b1_o[x+1,y-1] + b1_o[x-1,y-1])/4
                    mean_n = (n1_o[x+1,y+1] + n1_o[x-1,y+1] + n1_o[x+1,y-1] + n1_o[x-1,y-1])/4
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c1'][x,y] = c1_o[x,y]*(1 - set['dt']*coef['Nu']*mean_n - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c1_o[x+2,y]+c1_o[x-2,y]+c1_o[x,y+2]+c1_o[x,y-2]-4*c1_o[x,y])/(set['h']**2)
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
            #print mean_b        
    return sol