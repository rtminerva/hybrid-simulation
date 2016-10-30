from random import randint, sample, uniform
import numpy

def b_mean_function(set,sol,xb,yb):
    if yb == 1:
        if xb == 1:
            b_mean_ur = (sol['b'][xb+2,yb+2]+sol['b'][xb,yb+2]+sol['b'][xb+2,yb]+sol['b'][xb,yb])/4
            b_mean_ul = (sol['b'][xb,yb]+sol['b'][xb,yb+2])/2
            b_mean_dr = (sol['b'][xb,yb]+sol['b'][xb+2,yb])/2
            b_mean_dl = sol['b'][xb,yb]
        elif xb == set['Nx']-1:
            b_mean_ur = (sol['b'][xb,yb]+sol['b'][xb,yb+2])/2
            b_mean_ul = (sol['b'][xb-2,yb]+sol['b'][xb,yb+2]+sol['b'][xb-2,yb+2]+sol['b'][xb,yb])/4
            b_mean_dr = sol['b'][xb,yb]
            b_mean_dl = (sol['b'][xb,yb]+sol['b'][xb-2,yb])/2
        else:
            b_mean_ur = (sol['b'][xb+2,yb+2]+sol['b'][xb,yb+2]+sol['b'][xb+2,yb]+sol['b'][xb,yb])/4
            b_mean_ul = (sol['b'][xb-2,yb-2]+sol['b'][xb,yb+2]+sol['b'][xb-2,yb]+sol['b'][xb,yb])/4
            b_mean_dr = (sol['b'][xb,yb]+sol['b'][xb+2,yb])/2
            b_mean_dl = (sol['b'][xb,yb]+sol['b'][xb-2,yb])/2
    elif yb == set['Ny']-1:
        if xb == 1:
            b_mean_ur = (sol['b'][xb,yb]+sol['b'][xb+2,yb])/2
            b_mean_ul = sol['b'][xb,yb]
            b_mean_dr = (sol['b'][xb+2,yb-2]+sol['b'][xb,yb-2]+sol['b'][xb+2,yb]+sol['b'][xb,yb])/4
            b_mean_dl = (sol['b'][xb,yb]+sol['b'][xb,yb-2])/2
        elif xb == set['Nx']-1:
            b_mean_ur = sol['b'][xb,yb]
            b_mean_ul = (sol['b'][xb,yb]+sol['b'][xb-2,yb])/2
            b_mean_dr = (sol['b'][xb,yb]+sol['b'][xb,yb-2])/2
            b_mean_dl = (sol['b'][xb-2,yb-2]+sol['b'][xb,yb-2]+sol['b'][xb-2,yb]+sol['b'][xb,yb])/4
        else:
            b_mean_ur = (sol['b'][xb,yb]+sol['b'][xb+2,yb])/2
            b_mean_ul = (sol['b'][xb,yb]+sol['b'][xb-2,yb])/2
            b_mean_dr = (sol['b'][xb+2,yb-2]+sol['b'][xb,yb-2]+sol['b'][xb+2,yb]+sol['b'][xb,yb])/4
            b_mean_dl = (sol['b'][xb-2,yb-2]+sol['b'][xb,yb-2]+sol['b'][xb-2,yb]+sol['b'][xb,yb])/4
    else:
        if xb == 1:
            b_mean_ur = (sol['b'][xb+2,yb+2]+sol['b'][xb,yb+2]+sol['b'][xb+2,yb]+sol['b'][xb,yb])/4
            b_mean_ul = (sol['b'][xb,yb]+sol['b'][xb,yb+2])/2
            b_mean_dr = (sol['b'][xb+2,yb-2]+sol['b'][xb,yb-2]+sol['b'][xb+2,yb]+sol['b'][xb,yb])/4
            b_mean_dl = (sol['b'][xb,yb]+sol['b'][xb,yb-2])/2
        elif xb == set['Nx']-1:
            b_mean_ur = (sol['b'][xb,yb]+sol['b'][xb,yb+2])/2
            b_mean_ul = (sol['b'][xb-2,yb+2]+sol['b'][xb,yb+2]+sol['b'][xb-2,yb]+sol['b'][xb,yb])/4
            b_mean_dr = (sol['b'][xb,yb]+sol['b'][xb,yb-2])/2
            b_mean_dl = (sol['b'][xb-2,yb-2]+sol['b'][xb,yb-2]+sol['b'][xb-2,yb]+sol['b'][xb,yb])/4
        else:
            b_mean_ur = (sol['b'][xb+2,yb+2]+sol['b'][xb,yb+2]+sol['b'][xb+2,yb]+sol['b'][xb,yb])/4
            b_mean_ul = (sol['b'][xb-2,yb+2]+sol['b'][xb,yb+2]+sol['b'][xb-2,yb]+sol['b'][xb,yb])/4
            b_mean_dr = (sol['b'][xb+2,yb-2]+sol['b'][xb,yb-2]+sol['b'][xb+2,yb]+sol['b'][xb,yb])/4
            b_mean_dl = (sol['b'][xb-2,yb-2]+sol['b'][xb,yb-2]+sol['b'][xb-2,yb]+sol['b'][xb,yb])/4
    b_mean = [b_mean_ur, b_mean_ul, b_mean_dr, b_mean_dl]
    return b_mean

def max_min_c(set,sol,x,y): #2.3.(1).(1)
    cijx = (sol['c'][x,y]-sol['c'][x-2,y]+sol['c'][x,y-2]-sol['c'][x-2,y-2])/(2*set['h'])
    cijy = (sol['c'][x,y]-sol['c'][x,y-2]+sol['c'][x-2,y]-sol['c'][x-2,y-2])/(2*set['h'])
    cijx_p = max(0,cijx)
    cijx_n = max(0,-cijx)
    cijy_p = max(0,cijy)
    cijy_n = max(0,-cijy)
    return cijx_p, cijx_n, cijy_p, cijy_n

def max_min_b(set,sol,x,y): #2.3.(1).(2)
    xb = x-1
    yb = y-1
    
    b_mean = b_mean_function(set,sol,xb,yb)
    
    bijx = (b_mean[0]-b_mean[1]+b_mean[2]-b_mean[3])/(2*set['h'])
    bijy = (b_mean[0]-b_mean[2]+b_mean[1]-b_mean[3])/(2*set['h'])
    #print bijx,bijy

    bijx_p = max(0,bijx)
    bijx_n = max(0,-bijx)
    bijy_p = max(0,bijy)
    bijy_n = max(0,-bijy)
    return bijx_p, bijx_n, bijy_p, bijy_n

def F_vector_sol(coef,set,sol,n_o): #2.3.(1)
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
                        chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(sol['c'][x,y]+sol['c'][x-2,y]+sol['c'][x,y-2]+sol['c'][x-2,y-2])/4)
                        cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x,y) #2.3.(1).(1)
                        bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x,y) #2.3.(1).(2)
                        G_plus_1 = chemo_coef*cijx_p-coef['Si']*bijx_p
                        
                        chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(sol['c'][x,y]+sol['c'][x+2,y]+sol['c'][x,y-2]+sol['c'][x+2,y-2])/4)
                        cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x+2,y) #2.3.(1).(1)
                        bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x+2,y) #2.3.(1).(2)
                        G_neg_1 = chemo_coef*cijx_n-coef['Si']*bijx_n
                        
                        F_sol_1[x,y] = -coef['D_n']/(set['h'])*(n_o[x+1,y-1]-n_o[x-1,y-1])+n_o[x-1,y-1]*G_plus_1-n_o[x+1,y-1]*G_neg_1
                        
            elif not y == 0:
                if x == set['Nx']:
                    chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(sol['c'][x,y]+sol['c'][x-2,y]+sol['c'][x,y-2]+sol['c'][x-2,y-2])/4)
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x,y) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x,y) #2.3.(1).(2)
                    G_plus_2 = chemo_coef*cijy_p-coef['Si']*bijy_p
                    
                    chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(sol['c'][x,y]+sol['c'][x-2,y]+sol['c'][x-2,y+2]+sol['c'][x,y+2])/4)
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x,y+2) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x,y+2) #2.3.(1).(2)
                    G_neg_2 = chemo_coef*cijy_n-coef['Si']*bijy_n
                    
                    F_sol_2[x,y] = -coef['D_n']/(set['h'])*(n_o[x-1,y+1]-n_o[x-1,y-1])+n_o[x-1,y-1]*G_plus_2-n_o[x-1,y+1]*G_neg_2
                elif not x == 0:
                    chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(sol['c'][x,y]+sol['c'][x-2,y]+sol['c'][x,y-2]+sol['c'][x-2,y-2])/4)
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x,y) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x,y) #2.3.(1).(2)
                    G_plus_1 = chemo_coef*cijx_p-coef['Si']*bijx_p
                    G_plus_2 = chemo_coef*cijy_p-coef['Si']*bijy_p
                    
                    chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(sol['c'][x,y]+sol['c'][x+2,y]+sol['c'][x,y-2]+sol['c'][x+2,y-2])/4)
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x+2,y) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x+2,y) #2.3.(1).(2)
                    G_neg_1 = chemo_coef*cijx_n-coef['Si']*bijx_n
                    
                    chemo_coef = coef['Ki_n']/(1+coef['Al_n']*(sol['c'][x,y]+sol['c'][x-2,y]+sol['c'][x-2,y+2]+sol['c'][x,y+2])/4)
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x,y+2) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x,y+2) #2.3.(1).(2)
                    G_neg_2 = chemo_coef*cijy_n-coef['Si']*bijy_n
                    
                    F_sol_1[x,y] = -coef['D_n']*(n_o[x+1,y-1]-n_o[x-1,y-1])/(set['h'])+n_o[x-1,y-1]*G_plus_1-n_o[x+1,y-1]*G_neg_1
                    F_sol_2[x,y] = -coef['D_n']*(n_o[x-1,y+1]-n_o[x-1,y-1])/(set['h'])+n_o[x-1,y-1]*G_plus_2-n_o[x-1,y+1]*G_neg_2
   
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

def c_f_T(coef, set, sol, n_o): #2.3
    c_o = numpy.copy(sol['c'])
    #f_o = sol['f'][:]
    b_o = numpy.copy(sol['b'])
    if set['con'] == True:
        n_o = numpy.copy(sol['n'])
    
    '''Calculate F on each sub lattice'''
    ##2nd method*
    F_sol_1, F_sol_2 = F_vector_sol(coef, set, sol, n_o) #2.3.(1)
    #print F_sol_1, F_sol_2
    F_mean_sol_1, F_mean_sol_2 = F_mean_vector_sol(F_sol_1, F_sol_2, set)
    #del F_sol_1, F_sol_2
    
    '''Solve b at main lattice'''
    coef_b = 1
    for y in range(1,set['Ny'],2):
        for x in range(1,set['Nx'],2):
            #b_mean = b_mean_function(set,sol,x,y)
            if y == 1:
                if x == 1:
                    #Solving n
                    if set['con'] == True:
                        sol['n'][x,y] = n_o[x,y] - set['dt']/set['h']*(F_sol_1[x+1,y+1]+F_sol_2[x+1,y+1])
                    
                    #1# H formula (awal)
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*(H(i,j,1)-0+H(i,j,2)-0)
                    
                    #2# F formula with coef_b
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*coef_b*(F_sol_1[x+1,y+1]+F_sol_2[x+1,y+1])
                    
                    #3# F formula (lengkap dengan b)
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*(b_mean[0]*F_sol_1[x+1,y+1]+b_mean[0]*F_sol_2[x+1,y+1])
                    
                    #4# H formula (lengkap dengan b)
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*((sol['b'][x,y]*max(F_mean_sol_1[x,y],0)-sol['b'][x+2,y]*max(-F_mean_sol_1[x+2,y],0)) + (sol['b'][x,y]*max(F_mean_sol_2[x,y],0)-sol['b'][x,y+2]*max(-F_mean_sol_2[x,y+2],0)))
                    
                    #4# H formula (lengkap dengan b) with growth rate
                    sol['b'][x,y] = b_o[x,y]*(1+set['dt']*(1-b_o[x,y])) - set['dt']/set['h']*((sol['b'][x,y]*max(F_mean_sol_1[x,y],0)-sol['b'][x+2,y]*max(-F_mean_sol_1[x+2,y],0)) + (sol['b'][x,y]*max(F_mean_sol_2[x,y],0)-sol['b'][x,y+2]*max(-F_mean_sol_2[x,y+2],0)))
                    #*1 T4_Con
                    #*(1+n_o[x,y]*set['dt']*(1-b_o[x,y])) T5 _Con
                    #*(1+3*set['dt']*(1-b_o[x,y])+5*set['dt']*n_o[x,y]*(1-b_o[x,y]))+0.2*(n_o[x,y])**2 T6_Con
                    ##+set['dt']*0.5*n_o[x,y] failed (eventually neg b) (*1 also failed)
                    #*(1+3*set['dt']*(1-b_o[x,y])+5*set['dt']*n_o[x,y]*(1-b_o[x,y]))+set['dt']*0.2*(n_o[x,y])**2 T7_Con (with and without constant)
                    ##*(1+3*set['dt']*(1-b_o[x,y])+5*set['dt']*n_o[x,y]*(1-b_o[x,y]))+set['dt']*n_o[x,y] failed (eventually neg b) (*5 also failed)
                    #*(1+set['dt']*(1-b_o[x,y])+set['dt']*n_o[x,y]*(1-b_o[x,y])+set['dt']*n_o[x,y]) T8_Con
                    #*(1+set['dt']*(1-b_o[x,y])+set['dt']*n_o[x,y]*(1-b_o[x,y])+set['dt']*n_o[x,y])+set['dt']*(n_o[x,y])**2 T9_Con
                    #*(1+set['dt']*(1-b_o[x,y]) T10_Con
                    #+set['dt']*(n_o[x,y])**2 T11_Con
                    #*(1+set['dt']*(1-b_o[x,y])+set['dt']*n_o[x,y]*(1-b_o[x,y]))+set['dt']*0.2*(n_o[x,y])**2 N1 hybrid
                    #+set['dt']*(n_o[x,y])**2 N2 hybrid with init diff
                    
                    #5# H formula (dengan coef_b)
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*((coef_b*max(F_mean_sol_1[x,y],0)-coef_b*max(-F_mean_sol_1[x+2,y],0)) + (coef_b*max(F_mean_sol_2[x,y],0)-coef_b*max(-F_mean_sol_2[x,y+2],0)))
                elif x == set['Nx']-1:
                    if set['con'] == True:
                        sol['n'][x,y] = n_o[x,y] - set['dt']/set['h']*(F_sol_1[x-1,y+1]+F_sol_2[x+1,y+1])
                    
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*(0-H(i-1,j,1)+H(i,j,2)-0)
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*coef_b*(F_sol_1[x-1,y+1]+F_sol_2[x+1,y+1])
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*(b_mean[1]*F_sol_1[x-1,y+1]+b_mean[0]*F_sol_2[x+1,y+1])
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*((sol['b'][x,y]*max(F_mean_sol_2[x,y],0)-sol['b'][x,y+2]*max(-F_mean_sol_2[x,y+2],0)) - (sol['b'][x-2,y]*max(F_mean_sol_1[x-2,y],0)-sol['b'][x,y]*max(-F_mean_sol_1[x,y],0)))
                    sol['b'][x,y] = b_o[x,y]*(1+set['dt']*(1-b_o[x,y])) - set['dt']/set['h']*((sol['b'][x,y]*max(F_mean_sol_2[x,y],0)-sol['b'][x,y+2]*max(-F_mean_sol_2[x,y+2],0)) - (sol['b'][x-2,y]*max(F_mean_sol_1[x-2,y],0)-sol['b'][x,y]*max(-F_mean_sol_1[x,y],0)))
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*( - (coef_b*max(F_mean_sol_1[x-2,y],0)-coef_b*max(-F_mean_sol_1[x,y],0)) + (coef_b*max(F_mean_sol_2[x,y],0)-coef_b*max(-F_mean_sol_2[x,y+2],0)))
                else:
                    if set['con'] == True:
                        sol['n'][x,y] = n_o[x,y] - set['dt']/set['h']*(F_sol_1[x+1,y+1]-F_sol_1[x-1,y+1]+F_sol_2[x+1,y+1])
                    
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*(H(i,j,1)-H(i-1,j,1)+H(i,j,2)-0)
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*coef_b*(F_sol_1[x+1,y+1]-F_sol_1[x-1,y+1]+F_sol_2[x+1,y+1])
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*(b_mean[0]*F_sol_1[x+1,y+1]-b_mean[1]*F_sol_1[x-1,y+1]+b_mean[0]*F_sol_2[x+1,y+1])
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*((sol['b'][x,y]*max(F_mean_sol_1[x,y],0)-sol['b'][x+2,y]*max(-F_mean_sol_1[x+2,y],0)) + (sol['b'][x,y]*max(F_mean_sol_2[x,y],0)-sol['b'][x,y+2]*max(-F_mean_sol_2[x,y+2],0)) - (sol['b'][x-2,y]*max(F_mean_sol_1[x-2,y],0)-sol['b'][x,y]*max(-F_mean_sol_1[x,y],0)))
                    sol['b'][x,y] = b_o[x,y]*(1+set['dt']*(1-b_o[x,y])) - set['dt']/set['h']*((sol['b'][x,y]*max(F_mean_sol_1[x,y],0)-sol['b'][x+2,y]*max(-F_mean_sol_1[x+2,y],0)) + (sol['b'][x,y]*max(F_mean_sol_2[x,y],0)-sol['b'][x,y+2]*max(-F_mean_sol_2[x,y+2],0)) - (sol['b'][x-2,y]*max(F_mean_sol_1[x-2,y],0)-sol['b'][x,y]*max(-F_mean_sol_1[x,y],0)))
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*((coef_b*max(F_mean_sol_1[x,y],0)-coef_b*max(-F_mean_sol_1[x+2,y],0)) - (coef_b*max(F_mean_sol_1[x-2,y],0)-coef_b*max(-F_mean_sol_1[x,y],0)) + (coef_b*max(F_mean_sol_2[x,y],0)-coef_b*max(-F_mean_sol_2[x,y+2],0)))
            elif y == set['Ny']-1:
                if x == 1:
                    if set['con'] == True:
                        sol['n'][x,y] = n_o[x,y] - set['dt']/set['h']*(F_sol_1[x+1,y+1]-F_sol_2[x+1,y-1])
                    
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*(H(i,j,1)-0+0-H(i,j-1,2))
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*coef_b*(F_sol_1[x+1,y+1]-F_sol_2[x+1,y-1])
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*(b_mean[0]*F_sol_1[x+1,y+1]-b_mean[2]*F_sol_2[x+1,y-1])
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*((sol['b'][x,y]*max(F_mean_sol_1[x,y],0)-sol['b'][x+2,y]*max(-F_mean_sol_1[x+2,y],0)) - (sol['b'][x,y-2]*max(F_mean_sol_2[x,y-2],0)-sol['b'][x,y]*max(-F_mean_sol_2[x,y],0)))
                    sol['b'][x,y] = b_o[x,y]*(1+set['dt']*(1-b_o[x,y])) - set['dt']/set['h']*((sol['b'][x,y]*max(F_mean_sol_1[x,y],0)-sol['b'][x+2,y]*max(-F_mean_sol_1[x+2,y],0)) - (sol['b'][x,y-2]*max(F_mean_sol_2[x,y-2],0)-sol['b'][x,y]*max(-F_mean_sol_2[x,y],0)))
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*((coef_b*max(F_mean_sol_1[x,y],0)-coef_b*max(-F_mean_sol_1[x+2,y],0)) - (coef_b*max(F_mean_sol_2[x,y-2],0)-coef_b*max(-F_mean_sol_2[x,y],0)))
                elif x == set['Nx']-1:
                    if set['con'] == True:
                        sol['n'][x,y] = n_o[x,y] - set['dt']/set['h']*(-F_sol_1[x-1,y+1]-F_sol_2[x+1,y-1])
                    
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*(0-H(i-1,j,1)+0-H(i,j-1,2))
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*coef_b*(-F_sol_1[x-1,y+1]-F_sol_2[x+1,y-1])
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*(-b_mean[1]*F_sol_1[x-1,y+1]-b_mean[2]*F_sol_2[x+1,y-1])
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*(-(sol['b'][x-2,y]*max(F_mean_sol_1[x-2,y],0)-sol['b'][x,y]*max(-F_mean_sol_1[x,y],0)) - (sol['b'][x,y-2]*max(F_mean_sol_2[x,y-2],0)-sol['b'][x,y]*max(-F_mean_sol_2[x,y],0)))
                    sol['b'][x,y] = b_o[x,y]*(1+set['dt']*(1-b_o[x,y])) - set['dt']/set['h']*(-(sol['b'][x-2,y]*max(F_mean_sol_1[x-2,y],0)-sol['b'][x,y]*max(-F_mean_sol_1[x,y],0)) - (sol['b'][x,y-2]*max(F_mean_sol_2[x,y-2],0)-sol['b'][x,y]*max(-F_mean_sol_2[x,y],0)))
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*(-(coef_b*max(F_mean_sol_1[x-2,y],0)-coef_b*max(-F_mean_sol_1[x,y],0)) - (coef_b*max(F_mean_sol_2[x,y-2],0)-coef_b*max(-F_mean_sol_2[x,y],0)))
                else:
                    if set['con'] == True:
                        sol['n'][x,y] = n_o[x,y] - set['dt']/set['h']*(F_sol_1[x+1,y+1]-F_sol_1[x-1,y+1]-F_sol_2[x+1,y-1])
                    
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*(H(i,j,1)-H(i-1,j,1)+0-H(i,j-1,2))
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*coef_b*(F_sol_1[x+1,y+1]-F_sol_1[x-1,y+1]-F_sol_2[x+1,y-1])
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*(b_mean[0]*F_sol_1[x+1,y+1]-b_mean[1]*F_sol_1[x-1,y+1]-b_mean[2]*F_sol_2[x+1,y-1])
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*((sol['b'][x,y]*max(F_mean_sol_1[x,y],0)-sol['b'][x+2,y]*max(-F_mean_sol_1[x+2,y],0)) - (sol['b'][x-2,y]*max(F_mean_sol_1[x-2,y],0)-sol['b'][x,y]*max(-F_mean_sol_1[x,y],0)) - (sol['b'][x,y-2]*max(F_mean_sol_2[x,y-2],0)-sol['b'][x,y]*max(-F_mean_sol_2[x,y],0)))
                    sol['b'][x,y] = b_o[x,y]*(1+set['dt']*(1-b_o[x,y])) - set['dt']/set['h']*((sol['b'][x,y]*max(F_mean_sol_1[x,y],0)-sol['b'][x+2,y]*max(-F_mean_sol_1[x+2,y],0)) - (sol['b'][x-2,y]*max(F_mean_sol_1[x-2,y],0)-sol['b'][x,y]*max(-F_mean_sol_1[x,y],0)) - (sol['b'][x,y-2]*max(F_mean_sol_2[x,y-2],0)-sol['b'][x,y]*max(-F_mean_sol_2[x,y],0)))
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*((coef_b*max(F_mean_sol_1[x,y],0)-coef_b*max(-F_mean_sol_1[x+2,y],0)) - (coef_b*max(F_mean_sol_1[x-2,y],0)-coef_b*max(-F_mean_sol_1[x,y],0)) - (coef_b*max(F_mean_sol_2[x,y-2],0)-coef_b*max(-F_mean_sol_2[x,y],0)))
            else:
                if x == 1:
                    if set['con'] == True:
                        sol['n'][x,y] = n_o[x,y] - set['dt']/set['h']*(F_sol_1[x+1,y+1]+F_sol_2[x+1,y+1]-F_sol_2[x+1,y-1])
                    
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*(H(i,j,1)-0+H(i,j,2)-H(i,j-1,2))
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*coef_b*(F_sol_1[x+1,y+1]+F_sol_2[x+1,y+1]-F_sol_2[x+1,y-1])
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*(b_mean[0]*F_sol_1[x+1,y+1]+b_mean[0]*F_sol_2[x+1,y+1]-b_mean[2]*F_sol_2[x+1,y-1])
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*((sol['b'][x,y]*max(F_mean_sol_1[x,y],0)-sol['b'][x+2,y]*max(-F_mean_sol_1[x+2,y],0)) + (sol['b'][x,y]*max(F_mean_sol_2[x,y],0)-sol['b'][x,y+2]*max(-F_mean_sol_2[x,y+2],0)) - (sol['b'][x,y-2]*max(F_mean_sol_2[x,y-2],0)-sol['b'][x,y]*max(-F_mean_sol_2[x,y],0)))
                    sol['b'][x,y] = b_o[x,y]*(1+set['dt']*(1-b_o[x,y])) - set['dt']/set['h']*((sol['b'][x,y]*max(F_mean_sol_1[x,y],0)-sol['b'][x+2,y]*max(-F_mean_sol_1[x+2,y],0)) + (sol['b'][x,y]*max(F_mean_sol_2[x,y],0)-sol['b'][x,y+2]*max(-F_mean_sol_2[x,y+2],0)) - (sol['b'][x,y-2]*max(F_mean_sol_2[x,y-2],0)-sol['b'][x,y]*max(-F_mean_sol_2[x,y],0)))
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*((coef_b*max(F_mean_sol_1[x,y],0)-coef_b*max(-F_mean_sol_1[x+2,y],0)) + (coef_b*max(F_mean_sol_2[x,y],0)-coef_b*max(-F_mean_sol_2[x,y+2],0)) - (coef_b*max(F_mean_sol_2[x,y-2],0)-coef_b*max(-F_mean_sol_2[x,y],0)))
                elif x == set['Nx']-1:
                    if set['con'] == True:
                        sol['n'][x,y] = n_o[x,y] - set['dt']/set['h']*(-F_sol_1[x-1,y+1]+F_sol_2[x+1,y+1]-F_sol_2[x+1,y-1])
                    
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*(0-H(i-1,j,1)+H(i,j,2)-H(i,j-1,2))
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*coef_b*(-F_sol_1[x-1,y+1]+F_sol_2[x+1,y+1]-F_sol_2[x+1,y-1])
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*(-b_mean[1]*F_sol_1[x-1,y+1]+b_mean[0]*F_sol_2[x+1,y+1]-b_mean[2]*F_sol_2[x+1,y-1])
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*(-(sol['b'][x-2,y]*max(F_mean_sol_1[x-2,y],0)-sol['b'][x,y]*max(-F_mean_sol_1[x,y],0)) + (sol['b'][x,y]*max(F_mean_sol_2[x,y],0)-sol['b'][x,y+2]*max(-F_mean_sol_2[x,y+2],0)) - (sol['b'][x,y-2]*max(F_mean_sol_2[x,y-2],0)-sol['b'][x,y]*max(-F_mean_sol_2[x,y],0)))
                    sol['b'][x,y] = b_o[x,y]*(1+set['dt']*(1-b_o[x,y])) - set['dt']/set['h']*(-(sol['b'][x-2,y]*max(F_mean_sol_1[x-2,y],0)-sol['b'][x,y]*max(-F_mean_sol_1[x,y],0)) + (sol['b'][x,y]*max(F_mean_sol_2[x,y],0)-sol['b'][x,y+2]*max(-F_mean_sol_2[x,y+2],0)) - (sol['b'][x,y-2]*max(F_mean_sol_2[x,y-2],0)-sol['b'][x,y]*max(-F_mean_sol_2[x,y],0)))
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*(-(coef_b*max(F_mean_sol_1[x-2,y],0)-coef_b*max(-F_mean_sol_1[x,y],0)) + (coef_b*max(F_mean_sol_2[x,y],0)-coef_b*max(-F_mean_sol_2[x,y+2],0)) - (coef_b*max(F_mean_sol_2[x,y-2],0)-coef_b*max(-F_mean_sol_2[x,y],0)))
                else:
                    if set['con'] == True:
                        sol['n'][x,y] = n_o[x,y] - set['dt']/set['h']*(F_sol_1[x+1,y+1]-F_sol_1[x-1,y+1]+F_sol_2[x+1,y+1]-F_sol_2[x+1,y-1])
                    
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*(H(i,j,1)-H(i-1,j,1)+H(i,j,2)-H(i,j-1,2))
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*coef_b*(F_sol_1[x+1,y+1]-F_sol_1[x-1,y+1]+F_sol_2[x+1,y+1]-F_sol_2[x+1,y-1])
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*(b_mean[0]*F_sol_1[x+1,y+1]-b_mean[1]*F_sol_1[x-1,y+1]+b_mean[0]*F_sol_2[x+1,y+1]-b_mean[2]*F_sol_2[x+1,y-1])
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*((sol['b'][x,y]*max(F_mean_sol_1[x,y],0)-sol['b'][x+2,y]*max(-F_mean_sol_1[x+2,y],0)) - (sol['b'][x-2,y]*max(F_mean_sol_1[x-2,y],0)-sol['b'][x,y]*max(-F_mean_sol_1[x,y],0)) + (sol['b'][x,y]*max(F_mean_sol_2[x,y],0)-sol['b'][x,y+2]*max(-F_mean_sol_2[x,y+2],0)) - (sol['b'][x,y-2]*max(F_mean_sol_2[x,y-2],0)-sol['b'][x,y]*max(-F_mean_sol_2[x,y],0)))
                    sol['b'][x,y] = b_o[x,y]*(1+set['dt']*(1-b_o[x,y])) - set['dt']/set['h']*((sol['b'][x,y]*max(F_mean_sol_1[x,y],0)-sol['b'][x+2,y]*max(-F_mean_sol_1[x+2,y],0)) - (sol['b'][x-2,y]*max(F_mean_sol_1[x-2,y],0)-sol['b'][x,y]*max(-F_mean_sol_1[x,y],0)) + (sol['b'][x,y]*max(F_mean_sol_2[x,y],0)-sol['b'][x,y+2]*max(-F_mean_sol_2[x,y+2],0)) - (sol['b'][x,y-2]*max(F_mean_sol_2[x,y-2],0)-sol['b'][x,y]*max(-F_mean_sol_2[x,y],0)))
                    #sol['b'][x,y] = b_o[x,y] - set['dt']/set['h']*((coef_b*max(F_mean_sol_1[x,y],0)-coef_b*max(-F_mean_sol_1[x+2,y],0)) - (coef_b*max(F_mean_sol_1[x-2,y],0)-coef_b*max(-F_mean_sol_1[x,y],0)) + (coef_b*max(F_mean_sol_2[x,y],0)-coef_b*max(-F_mean_sol_2[x,y+2],0)) - (coef_b*max(F_mean_sol_2[x,y-2],0)-coef_b*max(-F_mean_sol_2[x,y],0)))
                    
                    #if F_sol_1[x+1,y+1]!= 0 or F_sol_2[x+1,y+1]!= 0 or F_sol_1[x-1,y+1]!= 0 or F_sol_2[x-1,y+1]!= 0 or F_sol_1[x+1,y-1]!= 0 or F_sol_2[x+1,y-1]!= 0 or F_sol_1[x-1,y-1]!= 0 or F_sol_2[x-1,y-1] != 0:
#                     if y == 119 or y == 121 or y == 123:
#                         if x == 13 or x == 15 or x == 17:
#                             print F_sol_1[x+1,y+1], F_sol_2[x+1,y+1], F_sol_1[x-1,y+1], F_sol_2[x-1,y+1], F_sol_1[x+1,y-1], F_sol_2[x+1,y-1], F_sol_1[x-1,y-1], F_sol_2[x-1,y-1]
#                             print x,y
#                             HH = (b_mean[0]*F_sol_1[x+1,y+1]-b_mean[1]*F_sol_1[x-1,y+1]+b_mean[0]*F_sol_2[x+1,y+1]-b_mean[2]*F_sol_2[x+1,y-1])
#                             print 'Nilai F scheme:', HH, ',', 'Nilai RHS:', set['dt']/set['h']*coef_b*HH
#                             print 'Nilai B new, old:',sol['b'][x,y], b_o[x,y]
#                             print 'Nilai B mean:', b_mean[0], b_mean[1], b_mean[2]
#                             print 'Rhs per part:', b_mean[0]*F_sol_1[x+1,y+1], -b_mean[1]*F_sol_1[x-1,y+1], b_mean[0]*F_sol_2[x+1,y+1], -b_mean[2]*F_sol_2[x+1,y-1]
#                             print 
                    
                    
    '''Solve c at sub lattice'''
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            if set['con'] == False:                       
                '''TIP CELL?'''
                if [x-1,y-1] in sol['tip_cell'] or [x+1,y-1] in sol['tip_cell'] or [x+1,y+1] in sol['tip_cell'] or [x-1,y+1] in sol['tip_cell']:
                    n_tip = 1
                else:
                    n_tip = 0
                n_stacks = 1-n_tip
            elif set['con'] == True:
                n_tip = 1     
            
            if y == 0: 
                if x == 0:
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_o[1,1]*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x,y+2]-2*c_o[x,y])
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_o[1,1]*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_o[1,1]*n_tip
                    
                elif x == set['Nx']:
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_o[set['Nx']-1,1]*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x-2,y]+c_o[x,y+2]-2*c_o[x,y])
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_o[set['Nx']-1,1]*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_o[set['Nx']-1,1]*n_tip
                    
                else:
                    if n_o[x+1,1] == 1 or n_o[x-1,1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]-3*c_o[x,y])
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
            elif y == set['Ny']:
                if x == 0:
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_o[1,set['Ny']-1]*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x,y-2]-2*c_o[x,y])
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_o[1,set['Ny']-1]*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_o[1,set['Ny']-1]*n_tip
                    
                elif x == set['Nx']:
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_o[set['Nx']-1,set['Ny']-1]*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x-2,y]+c_o[x,y-2]-2*c_o[x,y])
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_o[set['Nx']-1,set['Ny']-1]*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_o[set['Nx']-1,set['Ny']-1]*n_tip
                           
                else:
                    if n_o[x+1,set['Ny']-1] == 1 or n_o[x-1,set['Ny']-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                               
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y-2]-3*c_o[x,y])
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                        
            else:
                if x == 0:
                    if n_o[x+1,y+1] == 1 or n_o[x+1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                                
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
                elif x == set['Nx']:
                    if n_o[x-1,y+1] == 1 or n_o[x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                                
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
                else:
                    if n_o[x+1,y+1] == 1 or n_o[x-1,y+1] == 1 or n_o[x+1,y-1] == 1 or n_o[x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                               
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-4*c_o[x,y])
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
    return sol