from random import randint, sample, uniform
import numpy
from dirrection_of_movement import movement_dir #2.2.1

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
    vijx = -coef['D_n']*dijx + coef['Ki_n']/(1+coef['Al_n']*(c_o[xb,yb]))*cijx+coef['Ro']*fijx
    vijy = -coef['D_n']*dijy + coef['Ki_n']/(1+coef['Al_n']*(c_o[xb,yb]))*cijy+coef['Ro']*fijy
    
    vijx_p = max(0,vijx)
    vijx_n = max(0,-vijx)
    vijy_p = max(0,vijy)
    vijy_n = max(0,-vijy)
    
    return vijx_p, vijx_n, vijy_p, vijy_n

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

def system_2d(coef, set, sol): #2.3
    c_o = numpy.copy(sol['c']) #to save values at time step k (we are calculating at time step k+1)
#     f_o = numpy.copy(sol['f']) #to save values at time step k (we are calculating at time step k+1)
    
#     '''Calculate Velocity from tip cell's Vel'''
#     sol['Vel_x'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
#     sol['Vel_y'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
#     for y in range(1,set['Ny'],2):
#         for x in range(1,set['Nx'],2):
#             if n_o[x,y] == 1:
#                 dirr, probb = movement_dir(coef, set, sol, x, y)
#                 sol['Vel_x'][x,y] = -probb[1]+probb[2]
#                 sol['Vel_y'][x,y] = -probb[3]+probb[4]   


#     '''Solve backward space'''
#     c_lrud = coef['D_c']*set['dt']/set['h']**2
#     M = numpy.zeros( ((set['Nx']/2+1)*(set['Ny']/2+1) , (set['Nx']/2+1)*(set['Ny']/2+1)) )
#      
#     kk = 0
#     for j,e_j in enumerate(range(0,set['Ny']+1,2)):
#         for i,e_i in enumerate(range(0,set['Nx']+1,2)):
#             '''TIP CELL?'''
#             if [e_i-1,e_j-1] in sol['tip_cell_area'] or [e_i+1,e_j-1] in sol['tip_cell_area'] or [e_i+1,e_j+1] in sol['tip_cell_area'] or [e_i-1,e_j+1] in sol['tip_cell_area']:
#                 n_tip = 1               
#             else:
#                 n_tip = 0
#              
#             c_c = 1-4*c_lrud-set['dt']*coef['lam']-set['dt']*coef['Nu']*n_tip   
#                  
#             if e_j == 0:
#                 M[j,kk+set['Nx']/2+1] = c_lrud
#                 if e_i == 0:
#                     M[j,i] = c_c - 2*c_lrud
#                     M[j,i+1] = c_lrud
#                 elif e_i == set['Nx']:
#                     M[j,i] = c_c - 2*c_lrud
#                     M[j,i-1] = c_lrud
#                 else:
#                     M[j,i] = c_c - 3*c_lrud
#                     M[j,i-1] = c_lrud
#                     M[j,i+1] = c_lrud
#             elif e_j == set['Ny']:
#                 M[j,kk-set['Nx']/2+1] = c_lrud
#                 if e_i == 0:
#                     M[j,i] = c_c - 2*c_lrud
#                     M[j,i+1] = c_lrud
#                 elif e_i == set['Nx']:
#                     M[j,i] = c_c - 2*c_lrud
#                     M[j,i-1] = c_lrud
#                 else:
#                     M[j,i] = c_c - 3*c_lrud
#                     M[j,i-1] = c_lrud
#                     M[j,i+1] = c_lrud
#             else:
#                 M[j,kk-set['Nx']/2+1] = c_lrud
#                 M[j,kk+set['Nx']/2+1] = c_lrud
#                 if e_i == 0:
#                     M[j,i] = c_c - 3*c_lrud
#                     M[j,i+1] = c_lrud
#                 elif e_i == set['Ny']:
#                     M[j,i] = c_c - 3*c_lrud
#                     M[j,i-1] = c_lrud
#                 else:
#                     M[j,i] = c_c - 4*c_lrud
#                     M[j,i-1] = c_lrud
#                     M[j,i+1] = c_lrud
#             kk += 1
#     C_o = numpy.delete(c_o, numpy.s_[1::2], 0)
#     C_1 = numpy.delete(C_o, numpy.s_[1::2], 1)
#     c_1 = C_1.flatten()
#      
#     #solving
#     c_sol = numpy.dot(M,c_1)
#     #insert solution to sol
#     kk = 0
#     for even_y in range(0,set['Ny']+1,2):
#         for even_x in range(0,set['Nx']+1,2):
#             sol['c'][even_x,even_y] = c_sol[kk]
#             kk += 1 
                  
    '''Solve c & f at sub lattice'''
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            '''TIP CELL?'''
            if [x-1,y-1] in sol['tip_cell_area'] or [x+1,y-1] in sol['tip_cell_area'] or [x+1,y+1] in sol['tip_cell_area'] or [x-1,y+1] in sol['tip_cell_area']:
                n_tip = 1               
            else:
                n_tip = 0
             
            if y == 0: 
                if x == 0:
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_tip - set['dt']*coef['lam'])#+ (c_o[x+2,y]+c_o[x,y+2]-2*c_o[x,y])*coef['D_c']*set['dt']/set['h']**2
#                     sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*sol['n'][1,1]*n_tip - set['dt']*coef['Gama']*f_o[x,y]*sol['n'][1,1]*n_tip
                      
                elif x == set['Nx']:
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_tip - set['dt']*coef['lam'])#+ (c_o[x-2,y]+c_o[x,y+2]-2*c_o[x,y])*coef['D_c']*set['dt']/set['h']**2
#                     sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*sol['n'][set['Nx']-1,1]*n_tip - set['dt']*coef['Gama']*f_o[x,y]*sol['n'][set['Nx']-1,1]*n_tip
                     
                else:
#                     if sol['n'][x+1,1] == 1 or sol['n'][x-1,1] == 1:
#                         n_bool = 1
#                     else:
#                         n_bool = 0
                     
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_tip - set['dt']*coef['lam'])#+ (c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]-3*c_o[x,y])*coef['D_c']*set['dt']/set['h']**2
#                     sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                     
                 
            elif y == set['Ny']:
                if x == 0:
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_tip - set['dt']*coef['lam'])#+ (c_o[x+2,y]+c_o[x,y-2]-2*c_o[x,y])*coef['D_c']*set['dt']/set['h']**2
#                     sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*sol['n'][1,set['Ny']-1]*n_tip - set['dt']*coef['Gama']*f_o[x,y]*sol['n'][1,set['Ny']-1]*n_tip
                     
                elif x == set['Nx']:
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_tip - set['dt']*coef['lam'])#+ (c_o[x-2,y]+c_o[x,y-2]-2*c_o[x,y])*coef['D_c']*set['dt']/set['h']**2
#                     sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*sol['n'][set['Nx']-1,set['Ny']-1]*n_tip - set['dt']*coef['Gama']*f_o[x,y]*sol['n'][set['Nx']-1,set['Ny']-1]*n_tip
                            
                else:
#                     if sol['n'][x+1,set['Ny']-1] == 1 or sol['n'][x-1,set['Ny']-1] == 1:
#                         n_bool = 1
#                     else:
#                         n_bool = 0
                                
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_tip - set['dt']*coef['lam'])#+ (c_o[x+2,y]+c_o[x-2,y]+c_o[x,y-2]-3*c_o[x,y])*coef['D_c']*set['dt']/set['h']**2
#                     sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                     
                         
            else:
                if x == 0:
#                     if sol['n'][x+1,y+1] == 1 or sol['n'][x+1,y-1] == 1:
#                         n_bool = 1
#                     else:
#                         n_bool = 0
                                 
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_tip - set['dt']*coef['lam'])#+ (c_o[x+2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])*coef['D_c']*set['dt']/set['h']**2
#                     sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                     
                elif x == set['Nx']:
#                     if sol['n'][x-1,y+1] == 1 or sol['n'][x-1,y-1] == 1:
#                         n_bool = 1
#                     else:
#                         n_bool = 0
                                 
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_tip - set['dt']*coef['lam'])#+ (c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])*coef['D_c']*set['dt']/set['h']**2
#                     sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                     
                     
                else:
#                     if sol['n'][x+1,y+1] == 1 or sol['n'][x-1,y+1] == 1 or sol['n'][x+1,y-1] == 1 or sol['n'][x-1,y-1] == 1:
#                         n_bool = 1
#                     else:
#                         n_bool = 0
                                
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_tip - set['dt']*coef['lam'])#+ (c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-4*c_o[x,y])*coef['D_c']*set['dt']/set['h']**2
#                     sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
            
#             if sol['c'][x,y] != sol['c_o'][x, set['Ny']]:
#                 sol['c_n'][x,y] = sol['c'][x,y]
    return sol