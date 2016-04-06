from random import randint, sample, uniform

def c_f_T(coef, set, sol, h2, O_x, O_y):
    c_o = sol['c'][:]
    f_o = sol['f'][:]
    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
        p_o = sol['p'][:]
    
    '''Solve c, f, p at sub lattice'''
    if len(sol['index_mn']) > 16: 
        sol['Ang2_pos'] = []
        
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):           
            r_f = (x*set['Hh']-O_x)**2 + (y*set['Hh']-O_y)**2
            
            '''Indicate if (x,y) is tip cell'''
            n_tip = 0
            for tip in sol['sp_stop']:
                if (x,y) == sol['matrix_tip'][tip][-1]:
                    n_tip == 1
            n_stacks = abs(n_tip-1)
            
            '''Prob Ang2'''
            if len(sol['index_mn']) > 16:
                if [x,y] in sol['index_mn']:
                    line = sample(range(1,11), 5)
                    test = uniform(1,10)
                    if test in line:
                        sol['Ang2_pos'].append([x,y])                 
            
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
                        if not [x,y] in sol['Ang2_pos']:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang1
                        elif coef['Ang2'] == True:
                            sol['p'][x,y] = n_bool*n_stacks*sol['tp']/(coef['A_p']*m_bool+coef['B_p']) + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang2
                    c[x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*n_bool*n_tip) + coef['D_c']*sol['tp']/h2**2*(c_o[x+2,y]+c_o[x,y+2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + sol['tp']*coef['Beta']*n_bool*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
    
                elif x < sol['matrix_tip'][2][0][0] and y > sol['matrix_tip'][0][0][1]: #area 2
                    if n[x-1,y+1] == 1 or n[x+1,y+1] == 1 or n[x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if sol['m'][x-1,y+1] == 1 or sol['m'][x+1,y+1] == 1 or sol['m'][x-1,y-1] == 1:
                            m_bool = 1
                        else:
                            m_bool = 0
                        if not [x,y] in sol['Ang2_pos']:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang1
                        elif coef['Ang2'] == True:
                            sol['p'][x,y] = n_bool*n_stacks*sol['tp']/(coef['A_p']*m_bool+coef['B_p']) + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang2
                    c[x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*n_bool*n_tip)+ coef['D_c']*sol['tp']/h2**2*(c_o[x-2,y]+c_o[x,y+2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + sol['tp']*coef['Beta']*n_bool*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
                        
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
                        if not [x,y] in sol['Ang2_pos']:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang1
                        elif coef['Ang2'] == True:
                            sol['p'][x,y] = n_bool*n_stacks*sol['tp']/(coef['A_p']*m_bool+coef['B_p']) + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang2
                    c[x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*n_bool*n_tip)+ coef['D_c']*sol['tp']/h2**2*(c_o[x-2,y]+c_o[x,y-2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + sol['tp']*coef['Beta']*n_bool*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
                        
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
                        if not [x,y] in sol['Ang2_pos']:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang1
                        elif coef['Ang2'] == True:
                            sol['p'][x,y] = n_bool*n_stacks*sol['tp']/(coef['A_p']*m_bool+coef['B_p']) + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang2
                    c[x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*n_bool*n_tip)+ coef['D_c']*sol['tp']/h2**2*(c_o[x+2,y]+c_o[x,y-2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + sol['tp']*coef['Beta']*n_bool*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
                    
            elif y == 0: #diluar lingkaran kecil
                if x == 0:
                    c[x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*sol['n'][1,1])+ coef['D_c']*sol['tp']/h2**2*(c_o[x+2,y]+c_o[x,y+2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + sol['tp']*coef['Beta']*sol['n'][1,1] - sol['tp']*coef['Gama']*f_o[x,y]*sol['n'][1,1]
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if not [x,y] in sol['Ang2_pos']:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][1,1]+coef['B_p'])*sol['n'][1,1]*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang1
                        else:
                            sol['p'][x,y] = sol['n'][1,1]*n_stacks*sol['tp']/(coef['A_p']*sol['m'][1,1]+coef['B_p']) + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang2                        
                elif x == Nx:
                    c[x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*sol['n'][Nx-1,1])+ coef['D_c']*sol['tp']/h2**2*(c_o[x-2,y]+c_o[x,y+2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + sol['tp']*coef['Beta']*sol['n'][Nx-1,1] - sol['tp']*coef['Gama']*f_o[x,y]*sol['n'][Nx-1,1]
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if not [x,y] in sol['Ang2_pos']:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][Nx-1,1]+coef['B_p'])*sol['n'][Nx-1,1]*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang1
                        elif coef['Ang2'] == True:
                            sol['p'][x,y] = sol['n'][Nx-1,1]*n_stacks*sol['tp']/(coef['A_p']*sol['m'][Nx-1,1]+coef['B_p']) + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang2
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
                        if not [x,y] in sol['Ang2_pos']:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang1
                        elif coef['Ang2'] == True:
                            sol['p'][x,y] = n_bool*n_stacks*sol['tp']/(coef['A_p']*m_bool+coef['B_p']) + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang2
                    c[x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*n_bool*n_tip)+ coef['D_c']*sol['tp']/h2**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]-3*c_o[x,y])
                    f[x,y] = f_o[x,y] + sol['tp']*coef['Beta']*n_bool*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
                
            elif y == Ny:
                if x == 0:
                    c[x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*sol['n'][1,Ny-1]*n_tip)+ coef['D_c']*sol['tp']/h2**2*(c_o[x+2,y]+c_o[x,y-2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + sol['tp']*coef['Beta']*sol['n'][1,Ny-1]*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*sol['n'][1,Ny-1]*n_tip
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if not [x,y] in sol['Ang2_pos']:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][1,Ny-1]+coef['B_p'])*sol['n'][1,Ny-1]*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang1
                        elif coef['Ang2'] == True:
                            sol['p'][x,y] = sol['n'][1,Ny-1]*n_stacks*sol['tp']/(coef['A_p']*sol['m'][1,Ny-1]+coef['B_p']) + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang2
                    
                elif x == Nx:
                    c[x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*sol['n'][Nx-1,Ny-1]*n_tip)+ coef['D_c']*sol['tp']/h2**2*(c_o[x-2,y]+c_o[x,y-2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + sol['tp']*coef['Beta']*sol['n'][Nx-1,Ny-1]*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*sol['n'][Nx-1,Ny-1]*n_tip
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if not [x,y] in sol['Ang2_pos']:
                            sol['p'][x,y] = (coef['A_p']*sol['m'][Nx-1,Ny-1]+coef['B_p'])*sol['n'][Nx-1,Ny-1]*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang1
                        elif coef['Ang2'] == True:
                            sol['p'][x,y] = sol['n'][Nx-1,Ny-1]*n_stacks*sol['tp']/(coef['A_p']*sol['m'][Nx-1,Ny-1]+coef['B_p']) + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang2
                    
                else:
                    if sol['n'][x+1,Ny-1] == 1 or sol['n'][x-1,Ny-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if sol['m'][x+1,Ny-1] == 1 or sol['m'][x-1,Ny-1] == 1:
                            m_bool = 1
                        else:
                            m_bool = 0
                        if not [x,y] in sol['Ang2_pos']:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang1
                        elif coef['Ang2'] == True:
                            sol['p'][x,y] = n_bool*n_stacks*sol['tp']/(coef['A_p']*m_bool+coef['B_p']) + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang2
                    c[x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*n_bool*n_tip)+ coef['D_c']*sol['tp']/h2**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y-2]-3*c_o[x,y])
                    f[x,y] = f_o[x,y] + sol['tp']*coef['Beta']*n_bool*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
                        
            else:
                if x == 0:
                    if sol['n'][x+1,y+1] == 1 or sol['n'][x+1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if m[x+1,y+1] == 1 or m[x+1,y-1] == 1:
                            m_bool = 1
                        else:
                            m_bool = 0
                        if not [x,y] in sol['Ang2_pos']:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang1
                        elif coef['Ang2'] == True:
                            sol['p'][x,y] = n_bool*n_stacks*sol['tp']/(coef['A_p']*m_bool+coef['B_p']) + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang2
                    c[x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*n_bool*n_tip)+ coef['D_c']*sol['tp']/h2**2*(c_o[x+2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])
                    f[x,y] = f_o[x,y] + sol['tp']*coef['Beta']*n_bool*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
                elif x == Nx:
                    if sol['n'][x-1,y+1] == 1 or sol['n'][x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if m[x-1,y+1] == 1 or m[x-1,y-1] == 1:
                            m_bool = 1
                        else:
                            m_bool = 0
                        if not [x,y] in sol['Ang2_pos']:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang1
                        elif coef['Ang2'] == True:
                            sol['p'][x,y] = n_bool*n_stacks*sol['tp']/(coef['A_p']*m_bool+coef['B_p']) + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang2
                    c[x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*n_bool*n_tip)+ coef['D_c']*sol['tp']/h2**2*(c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])
                    f[x,y] = f_o[x,y] + sol['tp']*coef['Beta']*n_bool*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    
                    
                else:
                    if sol['n'][x+1,y+1] == 1 or sol['n'][x-1,y+1] == 1 or sol['n'][x+1,y-1] == 1 or sol['n'][x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                        if m[x+1,y+1] == 1 or m[x-1,y+1] == 1 or m[x+1,y-1] == 1 or m[x-1,y-1] == 1:
                            m_bool = 1
                        else:
                            m_bool = 0
                        if not [x,y] in sol['Ang2_pos']:
                            sol['p'][x,y] = (coef['A_p']*m_bool+coef['B_p'])*n_bool*n_stacks*sol['tp'] + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang1
                        elif coef['Ang2'] == True:
                            sol['p'][x,y] = n_bool*n_stacks*sol['tp']/(coef['A_p']*m_bool+coef['B_p']) + p_o[x,y]*(1-coef['Dl']*sol['tp']) #Ang2
                    c[x,y] = c_o[x,y]*(1 - sol['tp']*coef['Nu']*n_bool*n_tip)+ coef['D_c']*sol['tp']/h2**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-4*c_o[x,y])
                    f[x,y] = f_o[x,y] + sol['tp']*coef['Beta']*n_bool*n_tip - sol['tp']*coef['Gama']*f_o[x,y]*n_bool*n_tip
    return sol