from random import randint, sample, uniform
import numpy

def c_f_T(coef, set, sol):
    #, set['h'], set['O_x'], set['O_y']):
    c_o = sol['c'][:]
    f_o = sol['f'][:]
    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
        p_o = sol['p'][:]
    
    '''Solve c, f, p at sub lattice'''
    for y in range(0,set['Ny']+1):
        for x in range(0,set['Nx']+1):           
            r_f = (x*set['h']-set['O_x'])**2 + (y*set['h']-set['O_y'])**2
            r_f1 = numpy.sqrt((x*set['h']-set['O_x'])**2 + (y*set['h']-set['O_y'])**2)
            
            '''TIP CELL?'''
            if (x,y) in sol['tip_cell']:
                n_tip = 1
            else:
                n_tip = 0
            n_stacks = 1-n_tip                               
            
            '''
            Area2|Area1
            -----------
            Area3|Area4
            
            '''
            
            if r_f <= (set['R_min']**2 + set['error']):
                if x >= sol['matrix_tip'][2][0][0] and y >= sol['matrix_tip'][0][0][1]: #area 1                       
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:  
                        if coef['Ang2'] == False: ## Without Ang2
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks #Ang1
                        else:
                            sol['p'][x,y] (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*sol['n'][x,y]*n_stacks*(1-sol['m'][x,y])) #Ang2
                            #sol['p'][x,y] = sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*m_bool+coef['B_p'])*sol['tp']*n_tip) #Ang2
                            
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*sol['n'][x,y]*n_tip) + coef['D_c']*sol['tp']/(set['h']**2)*(c_o[x+1,y]+c_o[x,y+1]-2*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y]*(1-sol['tp']*coef['Gama']*sol['n'][x,y]*n_tip) + sol['tp']*coef['Beta']*sol['n'][x,y]*n_tip
                    
    
                elif x < sol['matrix_tip'][2][0][0] and y > sol['matrix_tip'][0][0][1]: #area 2
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*sol['n'][x,y]*n_stacks*(1-sol['m'][x,y])) #Ang2
                            #sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*m_bool+coef['B_p'])*sol['tp']*n_tip) #Ang2
                            
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*sol['n'][x,y]*n_tip)+ coef['D_c']*sol['tp']/(set['h']**2)*(c_o[x-1,y]+c_o[x,y+1]-2*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y]*(1-sol['tp']*coef['Gama']*sol['n'][x,y]*n_tip) + sol['tp']*coef['Beta']*sol['n'][x,y]*n_tip
                    
                        
                elif x <= sol['matrix_tip'][2][0][0] and y <= sol['matrix_tip'][0][0][1]: #area 3
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*sol['n'][x,y]*n_stacks*(1-sol['m'][x,y])) #Ang2
                            #sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*m_bool+coef['B_p'])*sol['tp']*n_tip) #Ang2
                    
                    sol['c'][x,y] = c_o[x,y]*(1-sol['tp']*coef['Nu']*sol['n'][x,y]*n_tip)+ coef['D_c']*sol['tp']/(set['h']**2)*(c_o[x-1,y]+c_o[x,y-1]-2*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y]*(1-sol['tp']*coef['Gama']*sol['n'][x,y]*n_tip) + sol['tp']*coef['Beta']*sol['n'][x,y]*n_tip
                    
                        
                elif x > sol['matrix_tip'][2][0][0] and y < sol['matrix_tip'][0][0][1]: #area 4
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:                            
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*sol['n'][x,y]*n_stacks*(1-sol['m'][x,y])) #Ang2
                            #sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*m_bool+coef['B_p'])*sol['tp']*n_tip) #Ang2
                            
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*sol['n'][x,y]*n_tip)+ coef['D_c']*sol['tp']/(set['h']**2)*(c_o[x+1,y]+c_o[x,y-1]-2*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y]*(1-sol['tp']*coef['Gama']*sol['n'][x,y]*n_tip) + sol['tp']*coef['Beta']*sol['n'][x,y]*n_tip
                    
                    
            elif y == 0: #diluar lingkaran kecil
                if x == 0:
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*sol['n'][x,y]*n_tip)+ coef['D_c']*sol['tp']/(set['h']**2)*(c_o[x+1,y]+c_o[x,y+1]-2*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y]*(1-sol['tp']*coef['Gama']*sol['n'][x,y]*n_tip) + sol['tp']*coef['Beta']*sol['n'][x,y]*n_tip                    
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*sol['n'][x,y]*n_stacks*(1-sol['m'][x,y])) #Ang2   
                            #sol['p'][x,y] = (coef['A_p']*sol['m'][1,1]+coef['B_p'])*sol['n'][1,1]*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*sol['m'][1,1]+coef['B_p'])*sol['tp']*n_tip) #Ang2   
                                                 
                elif x == set['Nx']:
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*sol['n'][x,y]*n_tip)+ coef['D_c']*sol['tp']/(set['h']**2)*(c_o[x-1,y]+c_o[x,y+1]-2*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y]*(1-sol['tp']*coef['Gama']*sol['n'][x,y]*n_tip) + sol['tp']*coef['Beta']*sol['n'][x,y]*n_tip
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*sol['n'][x,y]*n_stacks*(1-sol['m'][x,y])) #Ang2
                            #sol['p'][x,y] = (coef['A_p']*sol['m'][set['Nx']-1,1]+coef['B_p'])*sol['n'][set['Nx']-1,1]*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*sol['m'][set['Nx']-1,1]+coef['B_p'])*sol['tp']*n_tip) #Ang2
                
                else:
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*sol['n'][x,y]*n_stacks*(1-sol['m'][x,y])) #Ang2
                            #sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*m_bool+coef['B_p'])*sol['tp']*n_tip) #Ang2
                             
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*sol['n'][x,y]*n_tip)+ coef['D_c']*sol['tp']/(set['h']**2)*(c_o[x+1,y]+c_o[x-1,y]+c_o[x,y+1]-3*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y]*(1-sol['tp']*coef['Gama']*sol['n'][x,y]*n_tip) + sol['tp']*coef['Beta']*sol['n'][x,y]*n_tip
                
            elif y == set['Ny']:
                if x == 0:
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*sol['n'][x,y]*n_tip)+ coef['D_c']*sol['tp']/(set['h']**2)*(c_o[x+1,y]+c_o[x,y-1]-2*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y]*(1-sol['tp']*coef['Gama']*sol['n'][x,y]*n_tip) + sol['tp']*coef['Beta']*sol['n'][x,y]*n_tip
                
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*sol['n'][x,y]*n_stacks*(1-sol['m'][x,y])) #Ang2
                            #sol['p'][x,y] = (coef['A_p']*sol['m'][1,set['Ny']-1]+coef['B_p'])*sol['n'][1,set['Ny']-1]*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*sol['m'][1,set['Ny']-1]+coef['B_p'])*sol['tp']*n_tip) #Ang2
                    
                elif x == set['Nx']:
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*sol['n'][x,y]*n_tip)+ coef['D_c']*sol['tp']/(set['h']**2)*(c_o[x-1,y]+c_o[x,y-1]-2*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y]*(1-sol['tp']*coef['Gama']*sol['n'][x,y]*n_tip) + sol['tp']*coef['Beta']*sol['n'][x,y]*n_tip
                    
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['n'][x,y]*n_stacks*(1-sol['m'][x,y])) #Ang2
                            #sol['p'][x,y] = (coef['A_p']*sol['m'][set['Nx']-1,set['Ny']-1]+coef['B_p'])*sol['n'][set['Nx']-1,set['Ny']-1]*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*sol['m'][set['Nx']-1,set['Ny']-1]+coef['B_p'])*sol['tp']*n_tip) #Ang2
                            
                else:
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*sol['n'][x,y]*n_stacks*(1-sol['m'][x,y])) #Ang2
                            #sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*m_bool+coef['B_p'])*sol['tp']*n_tip) #Ang2
                            
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*sol['n'][x,y]*n_tip)+ coef['D_c']*sol['tp']/(set['h']**2)*(c_o[x+1,y]+c_o[x-1,y]+c_o[x,y-2]-3*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y]*(1-sol['tp']*coef['Gama']*sol['n'][x,y]*n_tip) + sol['tp']*coef['Beta']*sol['n'][x,y]*n_tip
                        
            else:
                if x == 0:   
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:  
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*sol['n'][x,y]*n_stacks*(1-sol['m'][x,y])) #Ang2
                            #sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*m_bool+coef['B_p'])*sol['tp']*n_tip) #Ang2
                            
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*sol['n'][x,y]*n_tip)+ coef['D_c']*sol['tp']/(set['h']**2)*(c_o[x+1,y]+c_o[x,y+1]+c_o[x,y-1]-3*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y]*(1-sol['tp']*coef['Gama']*sol['n'][x,y]*n_tip) + sol['tp']*coef['Beta']*sol['n'][x,y]*n_tip
                    
                elif x == set['Nx']:  
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0: 
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*sol['n'][x,y]*n_stacks*(1-sol['m'][x,y])) #Ang2
                            #sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*m_bool+coef['B_p'])*sol['tp']*n_tip) #Ang2
                            
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*sol['n'][x,y]*n_tip)+ coef['D_c']*sol['tp']/(set['h']**2)*(c_o[x-1,y]+c_o[x,y+1]+c_o[x,y-1]-3*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y]*(1-sol['tp']*coef['Gama']*sol['n'][x,y]*n_tip) + sol['tp']*coef['Beta']*sol['n'][x,y]*n_tip
                    
                    
                else:
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if coef['Ang2'] == False:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks #Ang1
                        else:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][x,y]+coef['B_p'])*sol['n'][x,y]*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']*sol['n'][x,y]*n_stacks*(1-sol['m'][x,y])) #Ang2
                            #sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-(coef['A_p']*m_bool+coef['B_p'])*sol['tp']*n_tip) #Ang2
                            
                    sol['c'][x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*sol['n'][x,y]*n_tip)+ coef['D_c']*sol['tp']/(set['h']**2)*(c_o[x+1,y]+c_o[x-1,y]+c_o[x,y+1]+c_o[x,y-1]-4*c_o[x,y])
                    sol['f'][x,y] = f_o[x,y]*(1-sol['tp']*coef['Gama']*sol['n'][x,y]*n_tip) + sol['tp']*coef['Beta']*sol['n'][x,y]*n_tip
            if r_f1 <= set['R_min']:
                sol['c'][x,y] = 0
                sol['f'][x,y] = 0
    return sol['c'], sol['f'], sol['p']