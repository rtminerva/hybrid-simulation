from random import randint, sample, uniform
import numpy

def max_min_c(set,sol,x,y): #2.3.(1).(1)
    cijx = 1/(2*set['h'])*(sol['c'][x,y]-sol['c'][x-2,y]+sol['c'][x,y-2]-sol['c'][x-2,y-2])
    cijy = 1/(2*set['h'])*(sol['c'][x,y]-sol['c'][x,y-2]+sol['c'][x-2,y]-sol['c'][x-2,y-2])
    cijx_p = max(0,cijx)
    cijx_n = max(0,-cijx)
    cijy_p = max(0,cijy)
    cijy_n = max(0,-cijy)
    return cijx_p, cijx_n, cijy_p, cijy_n

def max_min_b(set,sol,x,y): #2.3.(1).(2)
    bijx = 1/(2*set['h'])*(sol['b'][x,y]-sol['b'][x-2,y]+sol['b'][x,y-2]-sol['b'][x-2,y-2])
    bijy = 1/(2*set['h'])*(sol['b'][x,y]-sol['b'][x,y-2]+sol['b'][x-2,y]-sol['b'][x-2,y-2])
    bijx_p = max(0,bijx)
    bijx_n = max(0,-bijx)
    bijy_p = max(0,bijy)
    bijy_n = max(0,-bijy)
    return bijx_p, bijx_n, bijy_p, bijy_n

def F_vector_sol(coef,set,sol): #2.3.(1)
    F_sol_1 = numpy.zeros((set['Nx']+1,set['Ny']+1))
    F_sol_2 = numpy.zeros((set['Nx']+1,set['Ny']+1))
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            '''
            chemo_coef = coef['Ki_n']/(1+coef['Al_n']*1/4*(sol['c'][x,y]+sol['c'][x-2,y]+sol['c'][x,y-2]+sol['c'][x-2,y-2]))
            cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x,y) #2.3.(1).(1)
            bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x,y) #2.3.(1).(2)
            G_plus_1 = chemo_coef*cijx_p-coef['Si']*bijx_p
            G_plus_2 = chemo_coef*cijy_p-coef['Si']*bijy_p
            
            chemo_coef = coef['Ki_n']/(1+coef['Al_n']*1/4*(sol['c'][x,y]+sol['c'][x+2,y]+sol['c'][x,y-2]+sol['c'][x+2,y-2]))
            cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x+2,y) #2.3.(1).(1)
            bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x+2,y) #2.3.(1).(2)
            G_neg_1 = chemo_coef*cijx_n-coef['Si']*bijx_n
            
            chemo_coef = coef['Ki_n']/(1+coef['Al_n']*1/4*(sol['c'][x,y]+sol['c'][x-2,y]+sol['c'][x-2,y+2]+sol['c'][x,y+2]))
            cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x,y+2) #2.3.(1).(1)
            bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x,y+2) #2.3.(1).(2)
            G_neg_2 = chemo_coef*cijy_n-coef['Si']*bijy_n
            
            F_sol_1[x,y] = -coef['D_n']/(set['h'])*(sol['n'][x+1,y-1]-sol['n'][x-1,y-1])+sol['n'][x-1,y-1]*G_plus_1-sol['n'][x+1,y-1]*G_neg_1
            F_sol_2[x,y] = -coef['D_n']/(set['h'])*(sol['n'][x-1,y+1]-sol['n'][x-1,y-1])+sol['n'][x-1,y-1]*G_plus_2-sol['n'][x-1,y+1]*G_neg_2
            '''
            if y == set['Ny']:
                if not x == 0:
                    if not x == set['Nx']:
                        chemo_coef = coef['Ki_n']/(1+coef['Al_n']*1/4*(sol['c'][x,y]+sol['c'][x-2,y]+sol['c'][x,y-2]+sol['c'][x-2,y-2]))
                        cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x,y) #2.3.(1).(1)
                        bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x,y) #2.3.(1).(2)
                        G_plus_1 = chemo_coef*cijx_p-coef['Si']*bijx_p
                        
                        chemo_coef = coef['Ki_n']/(1+coef['Al_n']*1/4*(sol['c'][x,y]+sol['c'][x+2,y]+sol['c'][x,y-2]+sol['c'][x+2,y-2]))
                        cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x+2,y) #2.3.(1).(1)
                        bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x+2,y) #2.3.(1).(2)
                        G_neg_1 = chemo_coef*cijx_n-coef['Si']*bijx_n
                        
                        F_sol_1[x,y] = -coef['D_n']/(set['h'])*(sol['n'][x+1,y-1]-sol['n'][x-1,y-1])+sol['n'][x-1,y-1]*G_plus_1-sol['n'][x+1,y-1]*G_neg_1
            
            elif not y == 0:
                if x == 0:
                    chemo_coef = coef['Ki_n']/(1+coef['Al_n']*1/4*(sol['c'][x,y]+sol['c'][x-2,y]+sol['c'][x,y-2]+sol['c'][x-2,y-2]))
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x,y) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x,y) #2.3.(1).(2)
                    G_plus_2 = chemo_coef*cijy_p-coef['Si']*bijy_p
                    
                    chemo_coef = coef['Ki_n']/(1+coef['Al_n']*1/4*(sol['c'][x,y]+sol['c'][x-2,y]+sol['c'][x-2,y+2]+sol['c'][x,y+2]))
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x,y+2) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x,y+2) #2.3.(1).(2)
                    G_neg_2 = chemo_coef*cijy_n-coef['Si']*bijy_n
                    
                    F_sol_2[x,y] = -coef['D_n']/(set['h'])*(sol['n'][x-1,y+1]-sol['n'][x-1,y-1])+sol['n'][x-1,y-1]*G_plus_2-sol['n'][x-1,y+1]*G_neg_2
                elif not x == set['Nx']:
                    chemo_coef = coef['Ki_n']/(1+coef['Al_n']*1/4*(sol['c'][x,y]+sol['c'][x-2,y]+sol['c'][x,y-2]+sol['c'][x-2,y-2]))
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x,y) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x,y) #2.3.(1).(2)
                    G_plus_1 = chemo_coef*cijx_p-coef['Si']*bijx_p
                    G_plus_2 = chemo_coef*cijy_p-coef['Si']*bijy_p
                    
                    chemo_coef = coef['Ki_n']/(1+coef['Al_n']*1/4*(sol['c'][x,y]+sol['c'][x+2,y]+sol['c'][x,y-2]+sol['c'][x+2,y-2]))
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x+2,y) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x+2,y) #2.3.(1).(2)
                    G_neg_1 = chemo_coef*cijx_n-coef['Si']*bijx_n
                    
                    chemo_coef = coef['Ki_n']/(1+coef['Al_n']*1/4*(sol['c'][x,y]+sol['c'][x-2,y]+sol['c'][x-2,y+2]+sol['c'][x,y+2]))
                    cijx_p, cijx_n, cijy_p, cijy_n = max_min_c(set,sol,x,y+2) #2.3.(1).(1)
                    bijx_p, bijx_n, bijy_p, bijy_n = max_min_b(set,sol,x,y+2) #2.3.(1).(2)
                    G_neg_2 = chemo_coef*cijy_n-coef['Si']*bijy_n
                    
                    F_sol_1[x,y] = -coef['D_n']/(set['h'])*(sol['n'][x+1,y-1]-sol['n'][x-1,y-1])+sol['n'][x-1,y-1]*G_plus_1-sol['n'][x+1,y-1]*G_neg_1
                    F_sol_2[x,y] = -coef['D_n']/(set['h'])*(sol['n'][x-1,y+1]-sol['n'][x-1,y-1])+sol['n'][x-1,y-1]*G_plus_2-sol['n'][x-1,y+1]*G_neg_2
                
    return F_sol_1, F_sol_2        

def c_f_T(coef, set, sol): #2.3
    c_o = sol['c'][:]
    #f_o = sol['f'][:]
    b_o = sol['b'][:]
    
    '''Calculate F on each sub lattice'''
    ##2nd method*
    F_sol_1, F_sol_2 = F_vector_sol(coef, set, sol) #2.3.(1)
    
    '''Solve c, f, p at sub lattice'''
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):                       
            '''TIP CELL?'''
            if [x-1,y-1] in sol['tip_cell'] or [x+1,y-1] in sol['tip_cell'] or [x+1,y+1] in sol['tip_cell'] or [x-1,y+1] in sol['tip_cell']:
                n_tip = 1
            else:
                n_tip = 0
            n_stacks = 1-n_tip     
            
            if y == 0: 
                if x == 0:
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*sol['n'][1,1]*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x,y+2]-2*c_o[x,y])
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*sol['n'][1,1]*n_tip - set['dt']*coef['Gama']*f_o[x,y]*sol['n'][1,1]*n_tip
                    sol['b'][x,y] = b_o[x,y]# - set['dt']/(2*set['h'])*(b_o[x+2,y]*F_sol_1[x+2,y]+b_o[x,y+2]*F_sol_2[x,y+2])
                    
                elif x == set['Nx']:
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*sol['n'][set['Nx']-1,1]*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x-2,y]+c_o[x,y+2]-2*c_o[x,y])
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*sol['n'][set['Nx']-1,1]*n_tip - set['dt']*coef['Gama']*f_o[x,y]*sol['n'][set['Nx']-1,1]*n_tip
                    sol['b'][x,y] = b_o[x,y]# - set['dt']/(2*set['h'])*(-b_o[x-2,y]*F_sol_1[x-2,y]+b_o[x,y+2]*F_sol_2[x,y+2])
                    
                else:
                    if sol['n'][x+1,1] == 1 or sol['n'][x-1,1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]-3*c_o[x,y])
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    sol['b'][x,y] = b_o[x,y]# - set['dt']/(2*set['h'])*(b_o[x+2,y]*F_sol_1[x+2,y]-b_o[x-2,y]*F_sol_1[x-2,y]+b_o[x,y+2]*F_sol_2[x,y+2])
                
            elif y == set['Ny']:
                if x == 0:
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*sol['n'][1,set['Ny']-1]*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x,y-2]-2*c_o[x,y])
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*sol['n'][1,set['Ny']-1]*n_tip - set['dt']*coef['Gama']*f_o[x,y]*sol['n'][1,set['Ny']-1]*n_tip
                    sol['b'][x,y] = b_o[x,y]# - set['dt']/(2*set['h'])*(b_o[x+2,y]*F_sol_1[x+2,y]-b_o[x,y-2]*F_sol_2[x,y-2])
                    
                elif x == set['Nx']:
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*sol['n'][set['Nx']-1,set['Ny']-1]*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x-2,y]+c_o[x,y-2]-2*c_o[x,y])
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*sol['n'][set['Nx']-1,set['Ny']-1]*n_tip - set['dt']*coef['Gama']*f_o[x,y]*sol['n'][set['Nx']-1,set['Ny']-1]*n_tip
                    sol['b'][x,y] = b_o[x,y]# - set['dt']/(2*set['h'])*(-b_o[x-2,y]*F_sol_1[x-2,y]-b_o[x,y-2]*F_sol_2[x,y-2])
                           
                else:
                    if sol['n'][x+1,set['Ny']-1] == 1 or sol['n'][x-1,set['Ny']-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                               
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y-2]-3*c_o[x,y])
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    sol['b'][x,y] = b_o[x,y]# - set['dt']/(2*set['h'])*(b_o[x+2,y]*F_sol_1[x+2,y]-b_o[x-2,y]*F_sol_1[x-2,y]-b_o[x,y-2]*F_sol_2[x,y-2])
                        
            else:
                if x == 0:
                    if sol['n'][x+1,y+1] == 1 or sol['n'][x+1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                                
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    sol['b'][x,y] = b_o[x,y]# - set['dt']/(2*set['h'])*(b_o[x+2,y]*F_sol_1[x+2,y]+b_o[x,y+2]*F_sol_2[x,y+2]-b_o[x,y-2]*F_sol_2[x,y-2])
                    
                elif x == set['Nx']:
                    if sol['n'][x-1,y+1] == 1 or sol['n'][x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                                
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    sol['b'][x,y] = b_o[x,y]# - set['dt']/(2*set['h'])*(-b_o[x-2,y]*F_sol_1[x-2,y]+b_o[x,y+2]*F_sol_2[x,y+2]-b_o[x,y-2]*F_sol_2[x,y-2])
                    
                else:
                    if sol['n'][x+1,y+1] == 1 or sol['n'][x-1,y+1] == 1 or sol['n'][x+1,y-1] == 1 or sol['n'][x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                               
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-4*c_o[x,y])
                    #sol['f'][x,y] = f_o[x,y] + set['dt']*coef['Beta']*n_bool*n_tip - set['dt']*coef['Gama']*f_o[x,y]*n_bool*n_tip
                    jy = set['dt']/(2*set['h'])*(b_o[x+2,y]*F_sol_1[x+2,y]-b_o[x-2,y]*F_sol_1[x-2,y]+b_o[x,y+2]*F_sol_2[x,y+2]-b_o[x,y-2]*F_sol_2[x,y-2])
                    if not jy == 0:
                        print 'nilai b', jy
                    sol['b'][x,y] = b_o[x,y] - set['dt']/(2*set['h'])*(b_o[x+2,y]*F_sol_1[x+2,y]-b_o[x-2,y]*F_sol_1[x-2,y]+b_o[x,y+2]*F_sol_2[x,y+2]-b_o[x,y-2]*F_sol_2[x,y-2])
    
    return sol