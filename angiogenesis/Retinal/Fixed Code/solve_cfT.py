from random import randint, sample, uniform

def c_f_T(coef, set, sol):
    #, set['h'], set['O_x'], set['O_y']):
    c_o = sol['c'][:]
    f_o = sol['f'][:]
    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
        p_o = sol['p'][:]
    
    '''Solve c, f, p at sub lattice'''
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):           
            r_f = (x*set['Hh']-set['O_x'])**2 + (y*set['Hh']-set['O_y'])**2
            
            '''TIP CELL?'''
            if (x,y) in sol['tip_cell']:
                n_tip = 1
            else:
                n_tip = 0
            n_stacks = 1-n_tip                               
            
            if r_f <= (set['R_min']**2 + set['error'] + set['Hh']):
                if x >= sol['matrix_tip'][2][0][0] and y >= sol['matrix_tip'][0][0][1]: #area 1
                    if sol['n'][x+1,y+1] == 1 or sol['n'][x-1,y+1] == 1 or sol['n'][x+1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                        
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if sol['m'][x+1,y+1] == 1 or sol['m'][x-1,y+1] == 1 or sol['m'][x+1,y-1] == 1:
                            m_bool = 1
                        else:
                            m_bool = 0
                            
                        if coef['Ang2'] == False: ## Without Ang2
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*n_bool*n_stacks*(1-m_bool)) #Ang2
                            #sol['p'][x,y] = sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*m_bool+coef['B_p'])*sol['tp']*n_tip) #Ang2
                            
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*n_bool*n_tip) + coef['D_c']*sol['tp']/set['h']**2*(c_o[x+2,y]+c_o[x,y+2]-2*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y] + sol['tp']*coef['Beta']*n_bool*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
    
                elif x < sol['matrix_tip'][2][0][0] and y > sol['matrix_tip'][0][0][1]: #area 2
                    if sol['n'][x-1,y+1] == 1 or sol['n'][x+1,y+1] == 1 or sol['n'][x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                        
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if sol['m'][x-1,y+1] == 1 or sol['m'][x+1,y+1] == 1 or sol['m'][x-1,y-1] == 1:
                            m_bool = 1
                        else:
                            m_bool = 0
                            
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*n_bool*n_stacks*(1-m_bool)) #Ang2
                            #sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*m_bool+coef['B_p'])*sol['tp']*n_tip) #Ang2
                            
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*n_bool*n_tip)+ coef['D_c']*sol['tp']/set['h']**2*(c_o[x-2,y]+c_o[x,y+2]-2*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y] + sol['tp']*coef['Beta']*n_bool*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
                        
                elif x <= sol['matrix_tip'][2][0][0] and y <= sol['matrix_tip'][0][0][1]: #area 3
                    if sol['n'][x+1,y-1] == 1 or sol['n'][x-1,y+1] == 1 or sol['n'][x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                        
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if sol['m'][x+1,y-1] == 1 or sol['m'][x-1,y+1] == 1 or sol['m'][x-1,y-1] == 1:
                            m_bool = 1
                        else:
                            m_bool = 0
                            
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*n_bool*n_stacks*(1-m_bool)) #Ang2
                            #sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*m_bool+coef['B_p'])*sol['tp']*n_tip) #Ang2
                            
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*n_bool*n_tip)+ coef['D_c']*sol['tp']/set['h']**2*(c_o[x-2,y]+c_o[x,y-2]-2*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y] + sol['tp']*coef['Beta']*n_bool*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
                        
                elif x > sol['matrix_tip'][2][0][0] and y < sol['matrix_tip'][0][0][1]: #area 4
                    if sol['n'][x+1,y+1] == 1 or sol['n'][x-1,y-1] == 1 or sol['n'][x+1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                        
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if sol['m'][x+1,y+1] == 1 or sol['m'][x-1,y-1] == 1 or sol['m'][x+1,y-1] == 1:
                            m_bool = 1
                        else:
                            m_bool = 0
                            
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*n_bool*n_stacks*(1-m_bool)) #Ang2
                            #sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*m_bool+coef['B_p'])*sol['tp']*n_tip) #Ang2
                            
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*n_bool*n_tip)+ coef['D_c']*sol['tp']/set['h']**2*(c_o[x+2,y]+c_o[x,y-2]-2*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y] + sol['tp']*coef['Beta']*n_bool*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
                    
            elif y == 0: #diluar lingkaran kecil
                if x == 0:
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*sol['n'][1,1]*n_tip)+ coef['D_c']*sol['tp']/set['h']**2*(c_o[x+2,y]+c_o[x,y+2]-2*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y] + sol['tp']*coef['Beta']*sol['n'][1,1]*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*sol['n'][1,1]*n_tip
                    
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][1,1]+coef['B_p'])*sol['n'][1,1]*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][1,1]+coef['B_p'])*sol['n'][1,1]*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*sol['n'][1,1]*n_stacks*(1-sol['m'][1,1])) #Ang2   
                            #sol['p'][x,y] = (coef['A_p']*sol['m'][1,1]+coef['B_p'])*sol['n'][1,1]*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*sol['m'][1,1]+coef['B_p'])*sol['tp']*n_tip) #Ang2   
                                                 
                elif x == set['Nx']:
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*sol['n'][set['Nx']-1,1]*n_tip)+ coef['D_c']*sol['tp']/set['h']**2*(c_o[x-2,y]+c_o[x,y+2]-2*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y] + sol['tp']*coef['Beta']*sol['n'][set['Nx']-1,1]*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*sol['n'][set['Nx']-1,1]*n_tip
                    
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][set['Nx']-1,1]+coef['B_p'])*sol['n'][set['Nx']-1,1]*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][set['Nx']-1,1]+coef['B_p'])*sol['n'][set['Nx']-1,1]*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*sol['n'][set['Nx']-1,1]*n_stacks*(1-sol['m'][set['Nx']-1,1])) #Ang2
                            #sol['p'][x,y] = (coef['A_p']*sol['m'][set['Nx']-1,1]+coef['B_p'])*sol['n'][set['Nx']-1,1]*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*sol['m'][set['Nx']-1,1]+coef['B_p'])*sol['tp']*n_tip) #Ang2
                
                else:
                    if sol['n'][x+1,1] == 1 or sol['n'][x-1,1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if sol['m'][x+1,1] == 1 or sol['m'][x-1,1] == 1:
                            m_bool = 1
                        else:
                            m_bool = 0
                            
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*n_bool*n_stacks*(1-m_bool)) #Ang2
                            #sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*m_bool+coef['B_p'])*sol['tp']*n_tip) #Ang2
                             
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*n_bool*n_tip)+ coef['D_c']*sol['tp']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]-3*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y] + sol['tp']*coef['Beta']*n_bool*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
                
            elif y == set['Ny']:
                if x == 0:
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*sol['n'][1,set['Ny']-1]*n_tip)+ coef['D_c']*sol['tp']/set['h']**2*(c_o[x+2,y]+c_o[x,y-2]-2*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y] + sol['tp']*coef['Beta']*sol['n'][1,set['Ny']-1]*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*sol['n'][1,set['Ny']-1]*n_tip
                    
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][1,set['Ny']-1]+coef['B_p'])*sol['n'][1,set['Ny']-1]*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][1,set['Ny']-1]+coef['B_p'])*sol['n'][1,set['Ny']-1]*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*sol['n'][1,set['Ny']-1]*n_stacks*(1-sol['m'][1,set['Ny']-1])) #Ang2
                            #sol['p'][x,y] = (coef['A_p']*sol['m'][1,set['Ny']-1]+coef['B_p'])*sol['n'][1,set['Ny']-1]*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*sol['m'][1,set['Ny']-1]+coef['B_p'])*sol['tp']*n_tip) #Ang2
                    
                elif x == set['Nx']:
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*sol['n'][set['Nx']-1,set['Ny']-1]*n_tip)+ coef['D_c']*sol['tp']/set['h']**2*(c_o[x-2,y]+c_o[x,y-2]-2*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y] + sol['tp']*coef['Beta']*sol['n'][set['Nx']-1,set['Ny']-1]*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*sol['n'][set['Nx']-1,set['Ny']-1]*n_tip
                    
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][set['Nx']-1,set['Ny']-1]+coef['B_p'])*sol['n'][set['Nx']-1,set['Ny']-1]*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][set['Nx']-1,set['Ny']-1]+coef['B_p'])*sol['n'][set['Nx']-1,set['Ny']-1]*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*sol['n'][set['Nx']-1,set['Ny']-1]*n_stacks*(1-sol['m'][set['Nx']-1,set['Ny']-1])) #Ang2
                            #sol['p'][x,y] = (coef['A_p']*sol['m'][set['Nx']-1,set['Ny']-1]+coef['B_p'])*sol['n'][set['Nx']-1,set['Ny']-1]*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*sol['m'][set['Nx']-1,set['Ny']-1]+coef['B_p'])*sol['tp']*n_tip) #Ang2
                            
                else:
                    if sol['n'][x+1,set['Ny']-1] == 1 or sol['n'][x-1,set['Ny']-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                        
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if sol['m'][x+1,set['Ny']-1] == 1 or sol['m'][x-1,set['Ny']-1] == 1:
                            m_bool = 1
                        else:
                            m_bool = 0
                            
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*n_bool*n_stacks*(1-m_bool)) #Ang2
                            #sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*m_bool+coef['B_p'])*sol['tp']*n_tip) #Ang2
                            
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*n_bool*n_tip)+ coef['D_c']*sol['tp']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y-2]-3*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y] + sol['tp']*coef['Beta']*n_bool*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
                        
            else:
                if x == 0:
                    if sol['n'][x+1,y+1] == 1 or sol['n'][x+1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                        
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if sol['m'][x+1,y+1] == 1 or sol['m'][x+1,y-1] == 1:
                            m_bool = 1
                        else:
                            m_bool = 0
                            
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*n_bool*n_stacks*(1-m_bool)) #Ang2
                            #sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*m_bool+coef['B_p'])*sol['tp']*n_tip) #Ang2
                            
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*n_bool*n_tip)+ coef['D_c']*sol['tp']/set['h']**2*(c_o[x+2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y] + sol['tp']*coef['Beta']*n_bool*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
                elif x == set['Nx']:
                    if sol['n'][x-1,y+1] == 1 or sol['n'][x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                        
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if sol['m'][x-1,y+1] == 1 or sol['m'][x-1,y-1] == 1:
                            m_bool = 1
                        else:
                            m_bool = 0
                            
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*n_bool*n_stacks*(1-m_bool)) #Ang2
                            #sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*m_bool+coef['B_p'])*sol['tp']*n_tip) #Ang2
                            
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*n_bool*n_tip)+ coef['D_c']*sol['tp']/set['h']**2*(c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y] + sol['tp']*coef['Beta']*n_bool*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
                    
                else:
                    if sol['n'][x+1,y+1] == 1 or sol['n'][x-1,y+1] == 1 or sol['n'][x+1,y-1] == 1 or sol['n'][x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                        
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if sol['m'][x+1,y+1] == 1 or sol['m'][x-1,y+1] == 1 or sol['m'][x+1,y-1] == 1 or sol['m'][x-1,y-1] == 1:
                            m_bool = 1
                        else:
                            m_bool = 0
                            
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*n_bool*n_stacks*(1-m_bool)) #Ang2
                            #sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*m_bool+coef['B_p'])*sol['tp']*n_tip) #Ang2
                            
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*n_bool*n_tip)+ coef['D_c']*sol['tp']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-4*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y] + sol['tp']*coef['Beta']*n_bool*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*n_bool*n_tip
    return sol['c'], sol['f'], sol['p']