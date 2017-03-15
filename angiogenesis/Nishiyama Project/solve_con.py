from random import randint, sample, uniform
import numpy

def velocity_max(coef,set,sol,n_o,c_o,f_o,xb,yb):
    c_mean = c_mean_function(set,xb,yb,c_o)
    f_mean = f_mean_function(set,xb,yb,f_o)
    '''Diffusion term'''
#     if xb > 0 and xb < set['Nx']:
#         if yb > 0 and yb < set['Ny']:
    dijx = (n_o[xb+1,yb+1]-n_o[xb-1,yb+1]+n_o[xb+1,yb-1]-n_o[xb-1,yb-1])/(2*set['h'])
    dijy = (n_o[xb+1,yb+1]-n_o[xb+1,yb-1]+n_o[xb-1,yb+1]-n_o[xb-1,yb-1])/(2*set['h'])
    
    '''Chemotaxis term'''
    cijx = (c_mean[0]-c_mean[1]+c_mean[2]-c_mean[3])/(2*set['h'])
    cijy = (c_mean[0]-c_mean[2]+c_mean[1]-c_mean[3])/(2*set['h'])
    
    '''Haptotaxis term'''
    fijx = (f_mean[0]-f_mean[1]+f_mean[2]-f_mean[3])/(2*set['h'])
    fijy = (f_mean[0]-f_mean[2]+f_mean[1]-f_mean[3])/(2*set['h'])
    
    '''Total velocity''' #first trial without
    vijx = -coef['D_n']*dijx #+ coef['Ki_n']/(1+coef['Al_n']*(c_o[xb,yb]))*cijx+coef['Ro']*fijx
    vijy = -coef['D_n']*dijy #+ coef['Ki_n']/(1+coef['Al_n']*(c_o[xb,yb]))*cijy+coef['Ro']*fijy
    
    vijx_p = max(0,vijx)
    vijx_n = max(0,-vijx)
    vijy_p = max(0,vijy)
    vijy_n = max(0,-vijy)
    
    return vijx_p, vijx_n, vijy_p, vijy_n

def velocity_max_down_bound(coef,set,sol,n_o,c_o,f_o,xb,yb):
    c_mean = c_mean_function(set,xb,yb,c_o)
    f_mean = f_mean_function(set,xb,yb,f_o)
    '''Diffusion term'''
    dijx = (n_o[xb+1,yb+1]-n_o[xb-1,yb+1]+n_o[xb+1,yb-1]-n_o[xb-1,yb-1])/(2*set['h'])
    
    '''Chemotaxis term'''
    cijx = (c_mean[0]-c_mean[1]+c_mean[2]-c_mean[3])/(2*set['h'])
    
    '''Haptotaxis term'''
    fijx = (f_mean[0]-f_mean[1]+f_mean[2]-f_mean[3])/(2*set['h'])
    
    '''Total velocity''' #first trial without
    vijx =  coef['Ki_n']/(1+coef['Al_n']*(c_o[xb,yb]))*cijx+coef['Ro']*fijx
    
    vijx_p = max(0,vijx)
    vijx_n = max(0,-vijx)
    return vijx_p, vijx_n

def c_mean_function(set,xb,yb,c_o):
    if yb == 0:
        if xb == 0:
            c_mean_ur = (c_o[xb+2,yb+2]+c_o[xb,yb+2]+c_o[xb+2,yb]+c_o[xb,yb])/4
            c_mean_ul = (c_o[xb,yb]+c_o[xb,yb+2])/4
            c_mean_dr = (c_o[xb,yb]+c_o[xb+2,yb])/4
            c_mean_dl = c_o[xb,yb]/4
        elif xb == set['Nx']:
            c_mean_ur = (c_o[xb,yb]+c_o[xb,yb+2])//4
            c_mean_ul = (c_o[xb-2,yb]+c_o[xb,yb+2]+c_o[xb-2,yb+2]+c_o[xb,yb])/4
            c_mean_dr = c_o[xb,yb]/4
            c_mean_dl = (c_o[xb,yb]+c_o[xb-2,yb])/4
        else:
            c_mean_ur = (c_o[xb+2,yb+2]+c_o[xb,yb+2]+c_o[xb+2,yb]+c_o[xb,yb])/4
            c_mean_ul = (c_o[xb-2,yb-2]+c_o[xb,yb+2]+c_o[xb-2,yb]+c_o[xb,yb])/4
            c_mean_dr = (c_o[xb,yb]+c_o[xb+2,yb])/4
            c_mean_dl = (c_o[xb,yb]+c_o[xb-2,yb])/4
    elif yb == set['Ny']:
        if xb == 0:
            c_mean_ur = (c_o[xb,yb]+c_o[xb+2,yb])/4
            c_mean_ul = c_o[xb,yb]/4
            c_mean_dr = (c_o[xb+2,yb-2]+c_o[xb,yb-2]+c_o[xb+2,yb]+c_o[xb,yb])/4
            c_mean_dl = (c_o[xb,yb]+c_o[xb,yb-2])/4
        elif xb == set['Nx']:
            c_mean_ur = c_o[xb,yb]/4
            c_mean_ul = (c_o[xb,yb]+c_o[xb-2,yb])/4
            c_mean_dr = (c_o[xb,yb]+c_o[xb,yb-2])/4
            c_mean_dl = (c_o[xb-2,yb-2]+c_o[xb,yb-2]+c_o[xb-2,yb]+c_o[xb,yb])/4
        else:
            c_mean_ur = (c_o[xb,yb]+c_o[xb+2,yb])/4
            c_mean_ul = (c_o[xb,yb]+c_o[xb-2,yb])/4
            c_mean_dr = (c_o[xb+2,yb-2]+c_o[xb,yb-2]+c_o[xb+2,yb]+c_o[xb,yb])/4
            c_mean_dl = (c_o[xb-2,yb-2]+c_o[xb,yb-2]+c_o[xb-2,yb]+c_o[xb,yb])/4
    else:
        if xb == 0:
            c_mean_ur = (c_o[xb+2,yb+2]+c_o[xb,yb+2]+c_o[xb+2,yb]+c_o[xb,yb])/4
            c_mean_ul = (c_o[xb,yb]+c_o[xb,yb+2])/4
            c_mean_dr = (c_o[xb+2,yb-2]+c_o[xb,yb-2]+c_o[xb+2,yb]+c_o[xb,yb])/4
            c_mean_dl = (c_o[xb,yb]+c_o[xb,yb-2])/4
        elif xb == set['Nx']:
            c_mean_ur = (c_o[xb,yb]+c_o[xb,yb+2])/4
            c_mean_ul = (c_o[xb-2,yb+2]+c_o[xb,yb+2]+c_o[xb-2,yb]+c_o[xb,yb])/4
            c_mean_dr = (c_o[xb,yb]+c_o[xb,yb-2])/4
            c_mean_dl = (c_o[xb-2,yb-2]+c_o[xb,yb-2]+c_o[xb-2,yb]+c_o[xb,yb])/4
        else:
            c_mean_ur = (c_o[xb+2,yb+2]+c_o[xb,yb+2]+c_o[xb+2,yb]+c_o[xb,yb])/4
            c_mean_ul = (c_o[xb-2,yb+2]+c_o[xb,yb+2]+c_o[xb-2,yb]+c_o[xb,yb])/4
            c_mean_dr = (c_o[xb+2,yb-2]+c_o[xb,yb-2]+c_o[xb+2,yb]+c_o[xb,yb])/4
            c_mean_dl = (c_o[xb-2,yb-2]+c_o[xb,yb-2]+c_o[xb-2,yb]+c_o[xb,yb])/4
    c_mean = [c_mean_ur, c_mean_ul, c_mean_dr, c_mean_dl]
    return c_mean

def f_mean_function(set,xb,yb,f_o):
    if yb == 0:
        if xb == 0:
            f_mean_ur = (f_o[xb+2,yb+2]+f_o[xb,yb+2]+f_o[xb+2,yb]+f_o[xb,yb])/4
            f_mean_ul = (f_o[xb,yb]+f_o[xb,yb+2])/4
            f_mean_dr = (f_o[xb,yb]+f_o[xb+2,yb])/4
            f_mean_dl = f_o[xb,yb]/4
        elif xb == set['Nx']:
            f_mean_ur = (f_o[xb,yb]+f_o[xb,yb+2])//4
            f_mean_ul = (f_o[xb-2,yb]+f_o[xb,yb+2]+f_o[xb-2,yb+2]+f_o[xb,yb])/4
            f_mean_dr = f_o[xb,yb]/4
            f_mean_dl = (f_o[xb,yb]+f_o[xb-2,yb])/4
        else:
            f_mean_ur = (f_o[xb+2,yb+2]+f_o[xb,yb+2]+f_o[xb+2,yb]+f_o[xb,yb])/4
            f_mean_ul = (f_o[xb-2,yb-2]+f_o[xb,yb+2]+f_o[xb-2,yb]+f_o[xb,yb])/4
            f_mean_dr = (f_o[xb,yb]+f_o[xb+2,yb])/4
            f_mean_dl = (f_o[xb,yb]+f_o[xb-2,yb])/4
    elif yb == set['Ny']:
        if xb == 0:
            f_mean_ur = (f_o[xb,yb]+f_o[xb+2,yb])/4
            f_mean_ul = f_o[xb,yb]/4
            f_mean_dr = (f_o[xb+2,yb-2]+f_o[xb,yb-2]+f_o[xb+2,yb]+f_o[xb,yb])/4
            f_mean_dl = (f_o[xb,yb]+f_o[xb,yb-2])/4
        elif xb == set['Nx']:
            f_mean_ur = f_o[xb,yb]/4
            f_mean_ul = (f_o[xb,yb]+f_o[xb-2,yb])/4
            f_mean_dr = (f_o[xb,yb]+f_o[xb,yb-2])/4
            f_mean_dl = (f_o[xb-2,yb-2]+f_o[xb,yb-2]+f_o[xb-2,yb]+f_o[xb,yb])/4
        else:
            f_mean_ur = (f_o[xb,yb]+f_o[xb+2,yb])/4
            f_mean_ul = (f_o[xb,yb]+f_o[xb-2,yb])/4
            f_mean_dr = (f_o[xb+2,yb-2]+f_o[xb,yb-2]+f_o[xb+2,yb]+f_o[xb,yb])/4
            f_mean_dl = (f_o[xb-2,yb-2]+f_o[xb,yb-2]+f_o[xb-2,yb]+f_o[xb,yb])/4
    else:
        if xb == 0:
            f_mean_ur = (f_o[xb+2,yb+2]+f_o[xb,yb+2]+f_o[xb+2,yb]+f_o[xb,yb])/4
            f_mean_ul = (f_o[xb,yb]+f_o[xb,yb+2])/4
            f_mean_dr = (f_o[xb+2,yb-2]+f_o[xb,yb-2]+f_o[xb+2,yb]+f_o[xb,yb])/4
            f_mean_dl = (f_o[xb,yb]+f_o[xb,yb-2])/4
        elif xb == set['Nx']:
            f_mean_ur = (f_o[xb,yb]+f_o[xb,yb+2])/4
            f_mean_ul = (f_o[xb-2,yb+2]+f_o[xb,yb+2]+f_o[xb-2,yb]+f_o[xb,yb])/4
            f_mean_dr = (f_o[xb,yb]+f_o[xb,yb-2])/4
            f_mean_dl = (f_o[xb-2,yb-2]+f_o[xb,yb-2]+f_o[xb-2,yb]+f_o[xb,yb])/4
        else:
            f_mean_ur = (f_o[xb+2,yb+2]+f_o[xb,yb+2]+f_o[xb+2,yb]+f_o[xb,yb])/4
            f_mean_ul = (f_o[xb-2,yb+2]+f_o[xb,yb+2]+f_o[xb-2,yb]+f_o[xb,yb])/4
            f_mean_dr = (f_o[xb+2,yb-2]+f_o[xb,yb-2]+f_o[xb+2,yb]+f_o[xb,yb])/4
            f_mean_dl = (f_o[xb-2,yb-2]+f_o[xb,yb-2]+f_o[xb-2,yb]+f_o[xb,yb])/4
    f_mean = [f_mean_ur, f_mean_ul, f_mean_dr, f_mean_dl]
    return f_mean

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

def system_2d(coef, set, sol, n_o): #2.3
    c_o = numpy.copy(sol['c']) #to save values at time step k (we are calculating at time step k+1)
    f_o = numpy.copy(sol['f']) #to save values at time step k (we are calculating at time step k+1)
                                     
    '''Solve c & f at sub lattice'''
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            c_star = sol['c_o'][x,y] - c_o[x,y]
            gam_f = coef['Beta']*c_star/((1/(coef['Gama']))+c_star)
            move_f = 0
            if y == 0: 
                if x == 0:
                    mean_n = n_o[x+1,y+1]/4
                    move_c = 0
                    
                elif x == set['Nx']:
                    mean_n = n_o[x-1,y+1]/4
                    move_c = 0
                   
                else:
                    mean_n = (n_o[x-1,y+1] + n_o[x+1,y+1])/4
                    move_c = 0#coef['Alp_c']*set['dt']*(vijx_p*(c_o[x,y]-c_o[x-2,y])-vijx_n*(c_o[x+2,y]-c_o[x,y])+vijy_p*(0)-vijy_n*(c_o[x,y+2]-c_o[x,y]))/(set['h']**2)
                    
            elif y == set['Ny']:
                if x == 0:
                    mean_n = n_o[x+1,y-1]/4
                    move_c = 0
                    
                elif x == set['Nx']:
                    mean_n = n_o[x-1,y-1]/4
                    move_c = 0
                           
                else:
                    mean_n = (n_o[x-1,y-1] + n_o[x+1,y-1])/4
                    move_c = 0#coef['Alp_c']*set['dt']*(vijx_p*(c_o[x,y]-c_o[x-2,y])-vijx_n*(c_o[x+2,y]-c_o[x,y])+vijy_p*(c_o[x,y]-c_o[x,y-2])-vijy_n*(0))/(set['h']**2)
                       
            else:
                if x == 0:
                    mean_n = (n_o[x+1,y-1] + n_o[x+1,y+1])/2
                    move_c = 0#coef['Alp_c']*set['dt']*(vijx_p*(0)-vijx_n*(c_o[x+2,y]-c_o[x,y])+vijy_p*(c_o[x,y]-c_o[x,y-2])-vijy_n*(c_o[x,y+2]-c_o[x,y]))/(set['h']**2)
                    
                elif x == set['Nx']:
                    mean_n = (n_o[x-1,y-1] + n_o[x-1,y+1])/4

                    move_c = 0#coef['Alp_c']*set['dt']*(vijx_p*(c_o[x,y]-c_o[x-2,y])-vijx_n*(0)+vijy_p*(c_o[x,y]-c_o[x,y-2])-vijy_n*(c_o[x,y+2]-c_o[x,y]))/(set['h']**2)
                    
                else:
                    vijx_p, vijx_n, vijy_p, vijy_n = velocity_max(coef,set,sol,n_o,c_o,f_o,x,y)
                    mean_n = (n_o[x+1,y+1] + n_o[x-1,y+1] + n_o[x+1,y-1] + n_o[x-1,y-1])/4
                    move_c = coef['Alp_c']*set['dt']*(vijx_p*(c_o[x,y]-c_o[x-2,y])-vijx_n*(c_o[x+2,y]-c_o[x,y])+vijy_p*(c_o[x,y]-c_o[x,y-2])-vijy_n*(c_o[x,y+2]-c_o[x,y]))/(set['h'])
                    move_f = coef['Alp_f']*set['dt']*(vijx_p*(f_o[x,y]-f_o[x-2,y])-vijx_n*(f_o[x+2,y]-f_o[x,y])+vijy_p*(f_o[x,y]-f_o[x,y-2])-vijy_n*(f_o[x,y+2]-f_o[x,y]))/(set['h'])
                    
            digestion_c = set['dt']*coef['Nu']*c_o[x,y]*mean_n
            
            digestion_f = set['dt']*gam_f*f_o[x,y]*mean_n
            prolifer_f = set['dt']*coef['Beta']*mean_n
            
            sol['c'][x,y] = c_o[x,y] - digestion_c - move_c 
            sol['f'][x,y] = f_o[x,y] + prolifer_f - digestion_f - move_f     
    return sol