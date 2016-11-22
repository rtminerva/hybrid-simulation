from random import randint, sample, uniform
import numpy

def F_vector_sol(coef,set,sol,X4_o): #2.3.(1)
    F_sol_1 = numpy.zeros((set['Nx']+1,set['Ny']+1))
    F_sol_2 = numpy.zeros((set['Nx']+1,set['Ny']+1))
    G_plus_1 = 0
    G_plus_2 = 0
    G_neg_1 = 0
    G_neg_2 = 0
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            if y == set['Ny']:
                if not x == 0:
                    if not x == set['Nx']:
                        G_plus_1 = max(0,sol['G_vec_x'][x,y])
                        G_neg_1 = max(0,-sol['G_vec_x'][x,y])
                        
                        F_sol_1[x,y] = -coef['D4']/(set['h'])*(X4_o[x+1,y-1]-X4_o[x-1,y-1])+X4_o[x-1,y-1]*G_plus_1-X4_o[x+1,y-1]*G_neg_1
                        
            elif not y == 0:
                if x == set['Nx']:
                    G_plus_2 = max(0,sol['G_vec_y'][x,y])
                    G_neg_2 = max(0,-sol['G_vec_y'][x,y])
                    
                    F_sol_2[x,y] = -coef['D4']/(set['h'])*(X4_o[x-1,y+1]-X4_o[x-1,y-1])+X4_o[x-1,y-1]*G_plus_2-X4_o[x-1,y+1]*G_neg_2
                elif not x == 0:
                    G_plus_1 = max(0,sol['G_vec_x'][x,y])
                    G_plus_2 = max(0,sol['G_vec_y'][x,y])
                    
                    G_neg_1 = max(0,-sol['G_vec_x'][x,y])
                    G_neg_2 = max(0,-sol['G_vec_y'][x,y])
                    
                    F_sol_1[x,y] = -coef['D4']*(X4_o[x+1,y-1]-X4_o[x-1,y-1])/(set['h'])+X4_o[x-1,y-1]*G_plus_1-X4_o[x+1,y-1]*G_neg_1
                    F_sol_2[x,y] = -coef['D4']*(X4_o[x-1,y+1]-X4_o[x-1,y-1])/(set['h'])+X4_o[x-1,y-1]*G_plus_2-X4_o[x-1,y+1]*G_neg_2
   
    return F_sol_1, F_sol_2      

def c_f_T(coef, set, sol): #2.3
    X1_o = numpy.copy(sol['X1'])
    X2_o = numpy.copy(sol['X2'])
    X3_o = numpy.copy(sol['X3'])
    X4_o = numpy.copy(sol['X4'])
    
    '''Calculate F on each sub lattice'''
    F_sol_1, F_sol_2 = F_vector_sol(coef, set, sol, X4_o) #2.3.(1)

    '''Solve X1,X2,X3 at main lattice'''
    for y in range(1,set['Ny'],2):
        for x in range(1,set['Nx'],2):            
            if y == 1:
                if x == 1:
                    #grad X4
                    grad = - set['dt']*(F_sol_1[x+1,y+1]+F_sol_2[x+1,y+1])/set['h']
                    
                    #X1
                    sol['X1'][x,y] = X1_o[x,y] - set['dt']*(coef['k_1']*(X1_o[x,y])**2 + 2*coef['l_1']*X2_o[x,y] + coef['D1']*(-4*X1_o[x,y]+2*X1_o[x+2,y]+2*X1_o[x,y+2])/((set['h'])**2))
                    
                    #X2
                    sol['X2'][x,y] = X2_o[x,y] - set['dt']*(coef['k_1']*(X1_o[x,y])**2/2 - coef['l_1']*X2_o[x,y] - coef['k_2']*X2_o[x,y]*X3_o[x,y] + coef['l_2']*X4_o[x,y] + coef['D2']*(-4*X2_o[x,y]+2*X2_o[x+2,y]+2*X2_o[x,y+2])/((set['h'])**2))
                    
                    #X3
                    sol['X3'][x,y] = X3_o[x,y] - set['dt']*(-coef['k_2']*X2_o[x,y]*X3_o[x,y] + coef['l_2']*X4_o[x,y] + coef['D3']*(-4*X3_o[x,y]+2*X3_o[x+2,y]+2*X3_o[x,y+2])/((set['h'])**2))
                elif x == set['Nx']-1:
                    #grad X4
                    grad = - set['dt']*(-F_sol_1[x-1,y+1]+F_sol_2[x+1,y+1])/set['h']
                    
                    #X1
                    sol['X1'][x,y] = X1_o[x,y] - set['dt']*(coef['k_1']*(X1_o[x,y])**2 + 2*coef['l_1']*X2_o[x,y] + coef['D1']*(-4*X1_o[x,y]+2*X1_o[x-2,y]+2*X1_o[x,y+2])/((set['h'])**2))
                    
                    #X2
                    sol['X2'][x,y] = X2_o[x,y] - set['dt']*(coef['k_1']*(X1_o[x,y])**2/2 - coef['l_1']*X2_o[x,y] - coef['k_2']*X2_o[x,y]*X3_o[x,y] + coef['l_2']*X4_o[x,y] + coef['D2']*(-4*X2_o[x,y]+2*X2_o[x-2,y]+2*X2_o[x,y+2])/((set['h'])**2))
                    
                    #X3
                    sol['X3'][x,y] = X3_o[x,y] - set['dt']*(-coef['k_2']*X2_o[x,y]*X3_o[x,y] + coef['l_2']*X4_o[x,y] + coef['D3']*(-4*X3_o[x,y]+2*X3_o[x-2,y]+2*X3_o[x,y+2])/((set['h'])**2))
                else:
                    #grad X4
                    grad = - set['dt']*(F_sol_1[x+1,y+1]-F_sol_1[x-1,y+1]+F_sol_2[x+1,y+1])/set['h']
                    
                    #X1
                    sol['X1'][x,y] = X1_o[x,y] - set['dt']*(coef['k_1']*(X1_o[x,y])**2 + 2*coef['l_1']*X2_o[x,y] + coef['D1']*(X1_o[x-2,y]-4*X1_o[x,y]+X1_o[x+2,y]+2*X1_o[x,y+2])/((set['h'])**2))
                    
                    #X2
                    sol['X2'][x,y] = X2_o[x,y] - set['dt']*(coef['k_1']*(X1_o[x,y])**2/2 - coef['l_1']*X2_o[x,y] - coef['k_2']*X2_o[x,y]*X3_o[x,y] + coef['l_2']*X4_o[x,y] + coef['D2']*(X2_o[x-2,y]-4*X2_o[x,y]+X2_o[x+2,y]+2*X2_o[x,y+2])/((set['h'])**2))
                    
                    #X3
                    sol['X3'][x,y] = X3_o[x,y] - set['dt']*(-coef['k_2']*X2_o[x,y]*X3_o[x,y] + coef['l_2']*X4_o[x,y] + coef['D3']*(X3_o[x-2,y]-4*X3_o[x,y]+X3_o[x+2,y]+2*X3_o[x,y+2])/((set['h'])**2))
            elif y == set['Ny']-1:
                if x == 1:
                    #grad X4
                    grad = - set['dt']*(F_sol_1[x+1,y+1]-F_sol_2[x+1,y-1])/set['h']
                    
                    #X1
                    sol['X1'][x,y] = X1_o[x,y] - set['dt']*(coef['k_1']*(X1_o[x,y])**2 + 2*coef['l_1']*X2_o[x,y] + coef['D1']*(-4*X1_o[x,y]+2*X1_o[x+2,y]+2*X1_o[x,y-2])/((set['h'])**2))
                    
                    #X2
                    sol['X2'][x,y] = X2_o[x,y] - set['dt']*(coef['k_1']*(X1_o[x,y])**2/2 - coef['l_1']*X2_o[x,y] - coef['k_2']*X2_o[x,y]*X3_o[x,y] + coef['l_2']*X4_o[x,y] + coef['D2']*(-4*X2_o[x,y]+2*X2_o[x+2,y]+2*X2_o[x,y-2])/((set['h'])**2))
                    
                    #X3
                    sol['X3'][x,y] = X3_o[x,y] - set['dt']*(-coef['k_2']*X2_o[x,y]*X3_o[x,y] + coef['l_2']*X4_o[x,y] + coef['D3']*(-4*X3_o[x,y]+2*X3_o[x+2,y]+2*X3_o[x,y-2])/((set['h'])**2))    
                elif x == set['Nx']-1:
                    #grad X4
                    grad = - set['dt']*(-F_sol_1[x-1,y+1]-F_sol_2[x+1,y-1])/set['h']
                    
                    #X1
                    sol['X1'][x,y] = X1_o[x,y] - set['dt']*(coef['k_1']*(X1_o[x,y])**2 + 2*coef['l_1']*X2_o[x,y] + coef['D1']*(-4*X1_o[x,y]+2*X1_o[x-2,y]+2*X1_o[x,y-2])/((set['h'])**2))
                    
                    #X2
                    sol['X2'][x,y] = X2_o[x,y] - set['dt']*(coef['k_1']*(X1_o[x,y])**2/2 - coef['l_1']*X2_o[x,y] - coef['k_2']*X2_o[x,y]*X3_o[x,y] + coef['l_2']*X4_o[x,y] + coef['D2']*(-4*X2_o[x,y]+2*X2_o[x-2,y]+2*X2_o[x,y-2])/((set['h'])**2))
                    
                    #X3
                    sol['X3'][x,y] = X3_o[x,y] - set['dt']*(-coef['k_2']*X2_o[x,y]*X3_o[x,y] + coef['l_2']*X4_o[x,y] + coef['D3']*(-4*X3_o[x,y]+2*X3_o[x-2,y]+2*X3_o[x,y-2])/((set['h'])**2))
                else:
                    #grad X4
                    grad = - set['dt']*(F_sol_1[x+1,y+1]-F_sol_1[x-1,y+1]-F_sol_2[x+1,y-1])/set['h']
                    
                    #X1
                    sol['X1'][x,y] = X1_o[x,y] - set['dt']*(coef['k_1']*(X1_o[x,y])**2 + 2*coef['l_1']*X2_o[x,y] + coef['D1']*(X1_o[x-2,y]-4*X1_o[x,y]+X1_o[x+2,y]+2*X1_o[x,y-2])/((set['h'])**2))
                    
                    #X2
                    sol['X2'][x,y] = X2_o[x,y] - set['dt']*(coef['k_1']*(X1_o[x,y])**2/2 - coef['l_1']*X2_o[x,y] - coef['k_2']*X2_o[x,y]*X3_o[x,y] + coef['l_2']*X4_o[x,y] + coef['D2']*(X2_o[x-2,y]-4*X2_o[x,y]+X2_o[x+2,y]+2*X2_o[x,y-2])/((set['h'])**2))
                    
                    #X3
                    sol['X3'][x,y] = X3_o[x,y] - set['dt']*(-coef['k_2']*X2_o[x,y]*X3_o[x,y] + coef['l_2']*X4_o[x,y] + coef['D3']*(X3_o[x-2,y]-4*X3_o[x,y]+X3_o[x+2,y]+2*X3_o[x,y-2])/((set['h'])**2))
            else:
                if x == 1:
                    #grad X4
                    grad = - set['dt']*(F_sol_1[x+1,y+1]+F_sol_2[x+1,y+1]-F_sol_2[x+1,y-1])/set['h']
                    
                    #X1
                    sol['X1'][x,y] = X1_o[x,y] - set['dt']*(coef['k_1']*(X1_o[x,y])**2 + 2*coef['l_1']*X2_o[x,y] + coef['D1']*(-4*X1_o[x,y]+2*X1_o[x+2,y]+X1_o[x,y-2]+X1_o[x,y+2])/((set['h'])**2))
                    
                    #X2
                    sol['X2'][x,y] = X2_o[x,y] - set['dt']*(coef['k_1']*(X1_o[x,y])**2/2 - coef['l_1']*X2_o[x,y] - coef['k_2']*X2_o[x,y]*X3_o[x,y] + coef['l_2']*X4_o[x,y] + coef['D2']*(-4*X2_o[x,y]+2*X2_o[x+2,y]+X2_o[x,y-2]+X2_o[x,y+2])/((set['h'])**2))
                    
                    #X3
                    sol['X3'][x,y] = X3_o[x,y] - set['dt']*(-coef['k_2']*X2_o[x,y]*X3_o[x,y] + coef['l_2']*X4_o[x,y] + coef['D3']*(-4*X3_o[x,y]+2*X3_o[x+2,y]+X3_o[x,y-2]+X3_o[x,y+2])/((set['h'])**2))
                elif x == set['Nx']-1:
                    #grad X4
                    grad = - set['dt']*(-F_sol_1[x-1,y+1]+F_sol_2[x+1,y+1]-F_sol_2[x+1,y-1])/set['h']
                    
                    #X1
                    sol['X1'][x,y] = X1_o[x,y] - set['dt']*(coef['k_1']*(X1_o[x,y])**2 + 2*coef['l_1']*X2_o[x,y] + coef['D1']*(-4*X1_o[x,y]+2*X1_o[x-2,y]+X1_o[x,y-2]+X1_o[x,y+2])/((set['h'])**2))
                    
                    #X2
                    sol['X2'][x,y] = X2_o[x,y] - set['dt']*(coef['k_1']*(X1_o[x,y])**2/2 - coef['l_1']*X2_o[x,y] - coef['k_2']*X2_o[x,y]*X3_o[x,y] + coef['l_2']*X4_o[x,y] + coef['D2']*(-4*X2_o[x,y]+2*X2_o[x-2,y]+X2_o[x,y-2]+X2_o[x,y+2])/((set['h'])**2))
                    
                    #X3
                    sol['X3'][x,y] = X3_o[x,y] - set['dt']*(-coef['k_2']*X2_o[x,y]*X3_o[x,y] + coef['l_2']*X4_o[x,y] + coef['D3']*(-4*X3_o[x,y]+2*X3_o[x-2,y]+X3_o[x,y-2]+X3_o[x,y+2])/((set['h'])**2))
                else:
                    #grad X4
                    grad = - set['dt']*(F_sol_1[x+1,y+1]-F_sol_1[x-1,y+1]+F_sol_2[x+1,y+1]-F_sol_2[x+1,y-1])/set['h']
                    
                    #X1
                    sol['X1'][x,y] = X1_o[x,y] - set['dt']*(coef['k_1']*(X1_o[x,y])**2 + 2*coef['l_1']*X2_o[x,y] + coef['D1']*(X1_o[x-2,y]-2*X1_o[x,y]+X1_o[x+2,y]+X1_o[x,y-2]-2*X1_o[x,y]+X1_o[x,y+2])/((set['h'])**2))
                    
                    #X2
                    sol['X2'][x,y] = X2_o[x,y] - set['dt']*(coef['k_1']*(X1_o[x,y])**2/2 - coef['l_1']*X2_o[x,y] - coef['k_2']*X2_o[x,y]*X3_o[x,y] + coef['l_2']*X4_o[x,y] + coef['D2']*(X2_o[x-2,y]-2*X2_o[x,y]+X2_o[x+2,y]+X2_o[x,y-2]-2*X2_o[x,y]+X2_o[x,y+2])/((set['h'])**2))
                    
                    #X3
                    sol['X3'][x,y] = X3_o[x,y] - set['dt']*(-coef['k_2']*X2_o[x,y]*X3_o[x,y] + coef['l_2']*X4_o[x,y] + coef['D3']*(X3_o[x-2,y]-2*X3_o[x,y]+X3_o[x+2,y]+X3_o[x,y-2]-2*X3_o[x,y]+X3_o[x,y+2])/((set['h'])**2))
            #X4
            sol['X4'][x,y] = X4_o[x,y] - set['dt']*(coef['k_2']*X2_o[x,y]*X3_o[x,y] - coef['l_2']*X4_o[x,y]) + grad
            
    '''Determining the new born of X4'''
    sum_val_X4 = sol['X4'].sum() #jumlah seluruh element matrix sol X4
    if sum_val_X4>0:
        max_dot = 100 #jumlah max dots
        for y in range(1,set['Ny'],2):
            for x in range(1,set['Nx'],2):
                dot_X4 = int(sol['X4'][x,y]/(sum_val_X4)*max_dot) #how many dots that is supposed to live in the x,y node
                n_sp = len(sol['matrix_tip'])
                jum_dot = 0
                ind_dot = [] 
                for nom in range(0,n_sp): #detecting how many dots recently in the x,y node
                    if sol['matrix_tip'][nom][-1] == [x,y]:
                        jum_dot +=1
                        ind_dot.append(nom)
                if jum_dot < dot_X4[x,y]: #the new X4 is born
                    g = dot_X4[x,y] - jum_dot
                    for e in range(0,g):
                        sol['matrix_tip'].append([[x,y]])
                elif jum_dot > dot_X4[x,y]: #some X4 die
                    g = jum_dot - dot_X4[x,y]
                    gg = 0
                    while gg < g:
                        a = random.choice(ind_dot)
                        sol['matrix_tip_die'].append(sol['matrix_tip'][a])
                        sol['matrix_tip'].pop(a)
                        ind_dot.remove(a)
                        gg += 1
    return sol