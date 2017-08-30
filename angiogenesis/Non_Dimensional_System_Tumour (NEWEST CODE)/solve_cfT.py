from random import randint, sample, uniform
import numpy

def c_f_T(coef, set, sol):
    c_o = sol['c'][:]
    f_o = sol['f'][:]
    
    '''Solve c, f, p at sub lattice'''
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):                       
            '''TIP CELL?'''
            if [x-1,y-1] in sol['tip_cell_area'] or [x+1,y-1] in sol['tip_cell_area'] or [x+1,y+1] in sol['tip_cell_area'] or [x-1,y+1] in sol['tip_cell_area']:
                n_tip = 1               
            else:
                n_tip = 0
            
            if y == 0: 
                if x == 0:
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*sol['n'][1,1]*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x,y+2]-2*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*sol['n'][1,1]*n_tip - set['dt']*coef['Gama']*f_o[x,y]*sol['n'][1,1]*n_tip
                     
                elif x == set['Nx']:
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*sol['n'][set['Nx']-1,1]*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x-2,y]+c_o[x,y+2]-2*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*sol['n'][set['Nx']-1,1]*n_tip - set['dt']*coef['Gama']*f_o[x,y]*sol['n'][set['Nx']-1,1]*n_tip
                    
                else:
                    if sol['n'][x+1,1] == 1 or sol['n'][x-1,1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]-3*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
                
            elif y == set['Ny']:
                if x == 0:
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*sol['n'][1,set['Ny']-1]*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x,y-2]-2*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*sol['n'][1,set['Ny']-1]*n_tip - set['dt']*coef['Gama']*f_o[x,y]*sol['n'][1,set['Ny']-1]*n_tip
                    
                elif x == set['Nx']:
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*sol['n'][set['Nx']-1,set['Ny']-1]*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x-2,y]+c_o[x,y-2]-2*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*sol['n'][set['Nx']-1,set['Ny']-1]*n_tip - set['dt']*coef['Gama']*f_o[x,y]*sol['n'][set['Nx']-1,set['Ny']-1]*n_tip
                           
                else:
                    if sol['n'][x+1,set['Ny']-1] == 1 or sol['n'][x-1,set['Ny']-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                               
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y-2]-3*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
                        
            else:
                if x == 0:
                    if sol['n'][x+1,y+1] == 1 or sol['n'][x+1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                                
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
                elif x == set['Nx']:
                    if sol['n'][x-1,y+1] == 1 or sol['n'][x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                                
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
                    
                else:
                    if sol['n'][x+1,y+1] == 1 or sol['n'][x-1,y+1] == 1 or sol['n'][x+1,y-1] == 1 or sol['n'][x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                               
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-4*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
    
    sol['tip_cell_area'] = []
    
    return sol