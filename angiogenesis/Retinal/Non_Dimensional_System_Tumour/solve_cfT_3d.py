from random import randint, sample, uniform
import numpy

def c_f_T_3d(coef, set, sol):
    c_o = sol['c'][:]
    if not set['Ro'] == 0:
        f_o = sol['f'][:]
    
    '''Solve c, f, p at sub lattice'''
    for z in range(0,set['Nz']+1,2):
        for y in range(0,set['Ny']+1,2):
            for x in range(0,set['Nx']+1,2):                       
                '''TIP CELL?'''
                if [x-1,y-1,z-1] in sol['tip_cell'] or [x+1,y-1,z-1] in sol['tip_cell'] or [x+1,y+1,z-1] in sol['tip_cell'] or [x-1,y+1,z-1] in sol['tip_cell'] or [x-1,y-1,z+1] in sol['tip_cell'] or [x+1,y-1,z+1] in sol['tip_cell'] or [x+1,y+1,z+1] in sol['tip_cell'] or [x-1,y+1,z+1] in sol['tip_cell']:
                    n_tip = 1
                else:
                    n_tip = 0
                n_stacks = 1-n_tip     
                if z == 0:
                    if y == 0: 
                        if x == 0:
                            sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*sol['n'][1,1,1]*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x,y,z+2]-2*c_o[x,y,z])
                            if not set['Ro'] == 0:
                                sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*sol['n'][1,1,1]*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*sol['n'][1,1,1]*n_tip
                             
                        elif x == set['Nx']:
                            sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*sol['n'][set['Nx']-1,1,1]*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x-2,y]+c_o[x,y,z+2]-2*c_o[x,y,z])
                            if not set['Ro'] == 0:
                                sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*sol['n'][set['Nx']-1,1,1]*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*sol['n'][set['Nx']-1,1,1]*n_tip
                            
                        else:
                            if sol['n'][x+1,1,1] == 1 or sol['n'][x-1,1,1] == 1:
                                n_bool = 1
                            else:
                                n_bool = 0
                            
                            sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y,z+2]-3*c_o[x,y,z])
                            if not set['Ro'] == 0:
                                sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*n_bool*n_tip
                            
                        
                    elif y == set['Ny']:
                        if x == 0:
                            sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*sol['n'][1,set['Ny']-1,1]*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x,y,z-2]-2*c_o[x,y,z])
                            if not set['Ro'] == 0:
                                sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*sol['n'][1,set['Ny']-1,1]*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*sol['n'][1,set['Ny']-1,1]*n_tip
                            
                        elif x == set['Nx']:
                            sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*sol['n'][set['Nx']-1,set['Ny']-1,1]*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x-2,y]+c_o[x,y,z-2]-2*c_o[x,y,z])
                            if not set['Ro'] == 0:
                                sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*sol['n'][set['Nx']-1,set['Ny']-1,1]*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*sol['n'][set['Nx']-1,set['Ny']-1,1]*n_tip
                                   
                        else:
                            if sol['n'][x+1,set['Ny']-1,1] == 1 or sol['n'][x-1,set['Ny']-1,1] == 1:
                                n_bool = 1
                            else:
                                n_bool = 0
                                       
                            sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y,z-2]-3*c_o[x,y,z])
                            if not set['Ro'] == 0:
                                sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*n_bool*n_tip
                            
                                
                    else:
                        if x == 0:
                            if sol['n'][x+1,y+1,1] == 1 or sol['n'][x+1,y-1,1] == 1:
                                n_bool = 1
                            else:
                                n_bool = 0
                                        
                            sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x,y,z+2]+c_o[x,y,z-2]-3*c_o[x,y,z])
                            if not set['Ro'] == 0:
                                sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*n_bool*n_tip
                            
                        elif x == set['Nx']:
                            if sol['n'][x-1,y+1,1] == 1 or sol['n'][x-1,y-1,1] == 1:
                                n_bool = 1
                            else:
                                n_bool = 0
                                        
                            sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x-2,y]+c_o[x,y,z+2]+c_o[x,y,z-2]-3*c_o[x,y,z])
                            if not set['Ro'] == 0:
                                sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*n_bool*n_tip
                            
                            
                        else:
                            if sol['n'][x+1,y+1,1] == 1 or sol['n'][x-1,y+1,1] == 1 or sol['n'][x+1,y-1,1] == 1 or sol['n'][x-1,y-1,1] == 1:
                                n_bool = 1
                            else:
                                n_bool = 0
                                       
                            sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y,z+2]+c_o[x,y,z-2]-4*c_o[x,y,z])
                            if not set['Ro'] == 0:
                                sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*n_bool*n_tip
                elif z == set['Nz']:
                    if y == 0: 
                        if x == 0:
                            sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*sol['n'][1,1,set['Nz']]*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x,y,z+2]-2*c_o[x,y,z])
                            if not set['Ro'] == 0:
                                sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*sol['n'][1,1,set['Nz']]*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*sol['n'][1,1,set['Nz']]*n_tip
                             
                        elif x == set['Nx']:
                            sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*sol['n'][set['Nx']-1,1,set['Nz']]*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x-2,y]+c_o[x,y,z+2]-2*c_o[x,y,z])
                            if not set['Ro'] == 0:
                                sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*sol['n'][set['Nx']-1,1,set['Nz']]*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*sol['n'][set['Nx']-1,1,set['Nz']]*n_tip
                            
                        else:
                            if sol['n'][x+1,1,set['Nz']] == 1 or sol['n'][x-1,1,set['Nz']] == 1:
                                n_bool = 1
                            else:
                                n_bool = 0
                            
                            sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y,z+2]-3*c_o[x,y,z])
                            if not set['Ro'] == 0:
                                sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*n_bool*n_tip
                            
                        
                    elif y == set['Ny']:
                        if x == 0:
                            sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*sol['n'][1,set['Ny']-1,set['Nz']]*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x,y,z-2]-2*c_o[x,y,z])
                            if not set['Ro'] == 0:
                                sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*sol['n'][1,set['Ny']-1,set['Nz']]*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*sol['n'][1,set['Ny']-1,set['Nz']]*n_tip
                            
                        elif x == set['Nx']:
                            sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*sol['n'][set['Nx']-1,set['Ny']-1,set['Nz']]*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x-2,y]+c_o[x,y,z-2]-2*c_o[x,y,z])
                            if not set['Ro'] == 0:
                                sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*sol['n'][set['Nx']-1,set['Ny']-1,set['Nz']]*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*sol['n'][set['Nx']-1,set['Ny']-1,set['Nz']]*n_tip
                                   
                        else:
                            if sol['n'][x+1,set['Ny']-1,set['Nz']] == 1 or sol['n'][x-1,set['Ny']-1,set['Nz']] == 1:
                                n_bool = 1
                            else:
                                n_bool = 0
                                       
                            sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y,z-2]-3*c_o[x,y,z])
                            if not set['Ro'] == 0:
                                sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*n_bool*n_tip           
                    else:
                        if x == 0:
                            if sol['n'][x+1,y+1,set['Nz']] == 1 or sol['n'][x+1,y-1,set['Nz']] == 1:
                                n_bool = 1
                            else:
                                n_bool = 0
                                        
                            sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x,y,z+2]+c_o[x,y,z-2]-3*c_o[x,y,z])
                            if not set['Ro'] == 0:
                                sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*n_bool*n_tip
                            
                        elif x == set['Nx']:
                            if sol['n'][x-1,y+1,set['Nz']] == 1 or sol['n'][x-1,y-1,set['Nz']] == 1:
                                n_bool = 1
                            else:
                                n_bool = 0
                                        
                            sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x-2,y]+c_o[x,y,z+2]+c_o[x,y,z-2]-3*c_o[x,y,z])
                            if not set['Ro'] == 0:
                                sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*n_bool*n_tip
                            
                            
                        else:
                            if sol['n'][x+1,y+1,set['Nz']] == 1 or sol['n'][x-1,y+1,set['Nz']] == 1 or sol['n'][x+1,y-1,set['Nz']] == 1 or sol['n'][x-1,y-1,set['Nz']] == 1:
                                n_bool = 1
                            else:
                                n_bool = 0
                                       
                            sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y,z+2]+c_o[x,y,z-2]-4*c_o[x,y,z])
                            if not set['Ro'] == 0:
                                sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*n_bool*n_tip
                elif x == 0 and y == 0:
                    if sol['n'][x+1,y+1,z+1] == 1 or sol['n'][x+1,y+1,z-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                        
                    sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y,z+2]+c_o[x,y,z-2]-4*c_o[x,y,z])
                    if not set['Ro'] == 0:
                        sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*n_bool*n_tip
                elif x == set['Nx'] and y == 0:
                    if sol['n'][set['Nx']-1,y+1,z+1] == 1 or sol['n'][set['Nx']-1,y+1,z-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                        
                    sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y,z+2]+c_o[x,y,z-2]-4*c_o[x,y,z])
                    if not set['Ro'] == 0:
                        sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*n_bool*n_tip
                elif x == 0 and y == set['Ny']:
                    if sol['n'][x+1,set['Ny'],z+1] == 1 or sol['n'][x+1,set['Ny']-1,z-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                        
                    sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y,z+2]+c_o[x,y,z-2]-4*c_o[x,y,z])
                    if not set['Ro'] == 0:
                        sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*n_bool*n_tip
                elif x == set['Nx'] and y == set['Ny']:
                    if sol['n'][set['Nx']-1,set['Ny'],z+1] == 1 or sol['n'][set['Nx']-1,set['Ny']-1,z-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                        
                    sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y,z+2]+c_o[x,y,z-2]-4*c_o[x,y,z])
                    if not set['Ro'] == 0:
                        sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*n_bool*n_tip
                elif x == 0:
                    if sol['n'][x+1,y+1,z+1] == 1 or sol['n'][x+1,y-1,z+1] == 1 or sol['n'][x+1,y-1,z-1] == 1 or sol['n'][x+1,y+1,z-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                        
                    sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y,z+2]+c_o[x,y,z-2]-4*c_o[x,y,z])
                    if not set['Ro'] == 0:
                        sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*n_bool*n_tip
                elif y == 0:
                    if sol['n'][x+1,y+1,z+1] == 1 or sol['n'][x-1,y+1,z+1] == 1 or sol['n'][x+1,y+1,z-1] == 1 or sol['n'][x-1,y+1,z-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                        
                    sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y,z+2]+c_o[x,y,z-2]-4*c_o[x,y,z])
                    if not set['Ro'] == 0:
                        sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*n_bool*n_tip

                elif x == set['Nx']:
                    if sol['n'][set['Nx']-1,y+1,z+1] == 1 or sol['n'][set['Nx']-1,y-1,z+1] == 1 or sol['n'][set['Nx']-1,y-1,z-1] == 1 or sol['n'][set['Nx']-1,y+1,z-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y,z+2]+c_o[x,y,z-2]-4*c_o[x,y,z])
                    if not set['Ro'] == 0:
                        sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*n_bool*n_tip
                
                elif y == set['Ny']:
                    if sol['n'][x+1,set['Ny']-1,z+1] == 1 or sol['n'][x-1,set['Ny']-1,z+1] == 1 or sol['n'][x+1,set['Ny']-1,z-1] == 1 or sol['n'][x-1,set['Ny']-1,z-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                        
                    sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y,z+2]+c_o[x,y,z-2]-4*c_o[x,y,z])
                    if not set['Ro'] == 0:
                        sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*n_bool*n_tip
                else:
                    if sol['n'][x-1,y-1,z-1] == 1 or sol['n'][x+1,y-1,z-1] == 1 or sol['n'][x+1,y+1,z-1] == 1 or sol['n'][x-1,y+1,z-1] == 1 or sol['n'][x-1,y-1,z+1] == 1 or sol['n'][x+1,y-1,z+1] == 1 or sol['n'][x+1,y+1,z+1] == 1 or sol['n'][x-1,y+1,z+1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                        
                    sol['c'][x,y,z] = c_o[x,y,z]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y,z+2]+c_o[x,y,z-2]-4*c_o[x,y,z])
                    if not set['Ro'] == 0:
                        sol['f'][x,y,z] = f_o[x,y,z] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y,z]*n_bool*n_tip
    return sol