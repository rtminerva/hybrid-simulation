from random import randint, sample, uniform
import numpy

def c_f_T(coef, set, sol): #2.3
    c_o = numpy.copy(sol['c'])
    b_o = numpy.copy(sol['b'])
    
    '''Solve b at main lattice'''
    for y in range(1,set['Ny'],2):
        for x in range(1,set['Nx'],2):
            if y == 1:
                if x == 1:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*((b_o[x,y]*sol['Vb_x'][x,y]-b_o[x+2,y]*sol['Vb_x'][x+2,y])+(b_o[x,y]*sol['Vb_y'][x,y]-b_o[x,y+2]*sol['Vb_y'][x,y+2]))/set['h']
                elif x == set['Nx']-1:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*(-(b_o[x-2,y]*sol['Vb_x'][x-2,y]-b_o[x,y]*sol['Vb_x'][x,y])+(b_o[x,y]*sol['Vb_y'][x,y]-b_o[x,y+2]*sol['Vb_y'][x,y+2]))/set['h']
                else:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*((b_o[x,y]*sol['Vb_x'][x,y]-b_o[x+2,y]*sol['Vb_x'][x+2,y])-(b_o[x-2,y]*sol['Vb_x'][x-2,y]-b_o[x,y]*sol['Vb_x'][x,y])+(b_o[x,y]*sol['Vb_y'][x,y]-b_o[x,y+2]*sol['Vb_y'][x,y+2]))/set['h']
            elif y == set['Ny']-1:
                if x == 1:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*((b_o[x,y]*sol['Vb_x'][x,y]-b_o[x+2,y]*sol['Vb_x'][x+2,y])-(b_o[x,y-2]*sol['Vb_y'][x,y-2]-b_o[x,y]*sol['Vb_y'][x,y]))/set['h']
                elif x == set['Nx']-1:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*(-(b_o[x-2,y]*sol['Vb_x'][x-2,y]-b_o[x,y]*sol['Vb_x'][x,y])-(b_o[x,y-2]*sol['Vb_y'][x,y-2]-b_o[x,y]*sol['Vb_y'][x,y]))/set['h']
                else:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*((b_o[x,y]*sol['Vb_x'][x,y]-b_o[x+2,y]*sol['Vb_x'][x+2,y])-(b_o[x-2,y]*sol['Vb_x'][x-2,y]-b_o[x,y]*sol['Vb_x'][x,y])-(b_o[x,y-2]*sol['Vb_y'][x,y-2]-b_o[x,y]*sol['Vb_y'][x,y]))/set['h']
            else:
                if x == 1:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*((b_o[x,y]*sol['Vb_x'][x,y]-b_o[x+2,y]*sol['Vb_x'][x+2,y])+(b_o[x,y]*sol['Vb_y'][x,y]-b_o[x,y+2]*sol['Vb_y'][x,y+2])-(b_o[x,y-2]*sol['Vb_y'][x,y-2]-b_o[x,y]*sol['Vb_y'][x,y]))/set['h']
                elif x == set['Nx']-1:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*(-(b_o[x-2,y]*sol['Vb_x'][x-2,y]-b_o[x,y]*sol['Vb_x'][x,y])+(b_o[x,y]*sol['Vb_y'][x,y]-b_o[x,y+2]*sol['Vb_y'][x,y+2])-(b_o[x,y-2]*sol['Vb_y'][x,y-2]-b_o[x,y]*sol['Vb_y'][x,y]))/set['h']  
                else:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*((b_o[x,y]*sol['Vb_x'][x,y]-b_o[x+2,y]*sol['Vb_x'][x+2,y])-(b_o[x-2,y]*sol['Vb_x'][x-2,y]-b_o[x,y]*sol['Vb_x'][x,y])+(b_o[x,y]*sol['Vb_y'][x,y]-b_o[x,y+2]*sol['Vb_y'][x,y+2])-(b_o[x,y-2]*sol['Vb_y'][x,y-2]-b_o[x,y]*sol['Vb_y'][x,y]))/set['h']
                                     
    '''Solve c at sub lattice'''
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            if y == 0: 
                if x == 0:
                    mean_b = b_o[x+1,y+1]
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_o[1,1]*n_tip - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x,y+2]-2*c_o[x,y])/(set['h']**2)
                    
                elif x == set['Nx']:
                    mean_b = b_o[x-1,y+1]
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_o[set['Nx']-1,1]*n_tip - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x-2,y]+c_o[x,y+2]-2*c_o[x,y])/(set['h']**2)
                   
                else:
                    mean_b = (b_o[x-1,y+1] + b_o[x+1,y+1])/2
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    if n_o[x+1,1] == 1 or n_o[x-1,1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]-3*c_o[x,y])/(set['h']**2)
                    
            elif y == set['Ny']:
                if x == 0:
                    mean_b = b_o[x+1,y-1]
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_o[1,set['Ny']-1]*n_tip - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x,y-2]-2*c_o[x,y])/(set['h']**2)
                    
                elif x == set['Nx']:
                    mean_b = b_o[x-1,y-1]
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_o[set['Nx']-1,set['Ny']-1]*n_tip - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x-2,y]+c_o[x,y-2]-2*c_o[x,y])/(set['h']**2)
                         
                else:
                    mean_b = (b_o[x-1,y-1] + b_o[x+1,y-1])/2
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    if n_o[x+1,set['Ny']-1] == 1 or n_o[x-1,set['Ny']-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                               
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y-2]-3*c_o[x,y])/(set['h']**2)
                        
            else:
                if x == 0:
                    mean_b = (b_o[x+1,y-1] + b_o[x+1,y+1])/2
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    if n_o[x+1,y+1] == 1 or n_o[x+1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                                
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])/(set['h']**2)
                    
                elif x == set['Nx']:
                    mean_b = (b_o[x-1,y-1] + b_o[x-1,y+1])/2
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    if n_o[x-1,y+1] == 1 or n_o[x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                                
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])/(set['h']**2)
                    
                else:
                    mean_b = (b_o[x+1,y+1] + b_o[x-1,y+1] + b_o[x+1,y-1] + b_o[x-1,y-1])/4
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    if n_o[x+1,y+1] == 1 or n_o[x-1,y+1] == 1 or n_o[x+1,y-1] == 1 or n_o[x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                               
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_bool*n_tip - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-4*c_o[x,y])/(set['h']**2)
                           
    return sol