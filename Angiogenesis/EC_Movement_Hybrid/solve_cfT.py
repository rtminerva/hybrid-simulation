from random import randint, sample, uniform
import numpy

def c_f_T(coef, set, sol, n_o): #2.3
    c_o = numpy.copy(sol['c'])
    b_o = numpy.copy(sol['b'])
    
    '''Solve b at main lattice'''
    for y in range(1,set['Ny'],2):
        for x in range(1,set['Nx'],2):
            if y == 1:
                if x == 1:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*((b_o[x,y]*max(sol['Vb_x'][x,y],0)-b_o[x+2,y]*max(-sol['Vb_x'][x+2,y],0))+(b_o[x,y]*max(sol['Vb_y'][x,y],0)-b_o[x,y+2]*max(-sol['Vb_y'][x,y+2],0)))/set['h']
                elif x == set['Nx']-1:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*(-(b_o[x-2,y]*max(sol['Vb_x'][x-2,y],0)-b_o[x,y]*max(-sol['Vb_x'][x,y],0))+(b_o[x,y]*max(sol['Vb_y'][x,y],0)-b_o[x,y+2]*max(-sol['Vb_y'][x,y+2],0)))/set['h']
                else:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*((b_o[x,y]*max(sol['Vb_x'][x,y],0)-b_o[x+2,y]*max(-sol['Vb_x'][x+2,y],0))-(b_o[x-2,y]*max(sol['Vb_x'][x-2,y],0)-b_o[x,y]*max(-sol['Vb_x'][x,y],0))+(b_o[x,y]*max(sol['Vb_y'][x,y],0)-b_o[x,y+2]*max(-sol['Vb_y'][x,y+2],0)))/set['h']
            elif y == set['Ny']-1:
                if x == 1:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*((b_o[x,y]*max(sol['Vb_x'][x,y],0)-b_o[x+2,y]*max(-sol['Vb_x'][x+2,y],0))-(b_o[x,y-2]*max(sol['Vb_y'][x,y-2],0)-b_o[x,y]*max(-sol['Vb_y'][x,y],0)))/set['h']
                elif x == set['Nx']-1:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*(-(b_o[x-2,y]*max(sol['Vb_x'][x-2,y],0)-b_o[x,y]*max(-sol['Vb_x'][x,y],0))-(b_o[x,y-2]*max(sol['Vb_y'][x,y-2],0)-b_o[x,y]*max(-sol['Vb_y'][x,y],0)))/set['h']
                else:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*((b_o[x,y]*max(sol['Vb_x'][x,y],0)-b_o[x+2,y]*max(-sol['Vb_x'][x+2,y],0))-(b_o[x-2,y]*max(sol['Vb_x'][x-2,y],0)-b_o[x,y]*max(-sol['Vb_x'][x,y],0))-(b_o[x,y-2]*max(sol['Vb_y'][x,y-2],0)-b_o[x,y]*max(-sol['Vb_y'][x,y],0)))/set['h']
            else:
                if x == 1:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*((b_o[x,y]*max(sol['Vb_x'][x,y],0)-b_o[x+2,y]*max(-sol['Vb_x'][x+2,y],0))+(b_o[x,y]*max(sol['Vb_y'][x,y],0)-b_o[x,y+2]*max(-sol['Vb_y'][x,y+2],0))-(b_o[x,y-2]*max(sol['Vb_y'][x,y-2],0)-b_o[x,y]*max(-sol['Vb_y'][x,y],0)))/set['h']
                elif x == set['Nx']-1:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*(-(b_o[x-2,y]*max(sol['Vb_x'][x-2,y],0)-b_o[x,y]*max(-sol['Vb_x'][x,y],0))+(b_o[x,y]*max(sol['Vb_y'][x,y],0)-b_o[x,y+2]*max(-sol['Vb_y'][x,y+2],0))-(b_o[x,y-2]*max(sol['Vb_y'][x,y-2],0)-b_o[x,y]*max(-sol['Vb_y'][x,y],0)))/set['h']  
                else:
                    sol['b'][x,y] = b_o[x,y] -set['dt']*((b_o[x,y]*max(sol['Vb_x'][x,y],0)-b_o[x+2,y]*max(-sol['Vb_x'][x+2,y],0))-(b_o[x-2,y]*max(sol['Vb_x'][x-2,y],0)-b_o[x,y]*max(-sol['Vb_x'][x,y],0))+(b_o[x,y]*max(sol['Vb_y'][x,y],0)-b_o[x,y+2]*max(-sol['Vb_y'][x,y+2],0))-(b_o[x,y-2]*max(sol['Vb_y'][x,y-2],0)-b_o[x,y]*max(-sol['Vb_y'][x,y],0)))/set['h']
                                     
    '''Solve c at sub lattice'''
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            if y == 0: 
                if x == 0:
                    mean_b = b_o[x+1,y+1]
                    mean_n = n_o[x+1,y+1]
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*mean_n - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x,y+2]-2*c_o[x,y])/(set['h']**2)
                    
                elif x == set['Nx']:
                    mean_b = b_o[x-1,y+1]
                    mean_n = n_o[x-1,y+1]
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*mean_n - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x-2,y]+c_o[x,y+2]-2*c_o[x,y])/(set['h']**2)
                   
                else:
                    mean_b = (b_o[x-1,y+1] + b_o[x+1,y+1])/2
                    mean_n = (n_o[x-1,y+1] + n_o[x+1,y+1])/2
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0                  
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*mean_n - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]-3*c_o[x,y])/(set['h']**2)
                    
            elif y == set['Ny']:
                if x == 0:
                    mean_b = b_o[x+1,y-1]
                    mean_n = n_o[x+1,y-1]
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*mean_n - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x,y-2]-2*c_o[x,y])/(set['h']**2)
                    
                elif x == set['Nx']:
                    mean_b = b_o[x-1,y-1]
                    mean_n = n_o[x-1,y-1]
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*mean_n - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x-2,y]+c_o[x,y-2]-2*c_o[x,y])/(set['h']**2)
                         
                else:
                    mean_b = (b_o[x-1,y-1] + b_o[x+1,y-1])/2
                    mean_n = (n_o[x-1,y-1] + n_o[x+1,y-1])/2
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0                               
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*mean_n - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y-2]-3*c_o[x,y])/(set['h']**2)
                        
            else:
                if x == 0:
                    mean_b = (b_o[x+1,y-1] + b_o[x+1,y+1])/2
                    mean_n = (n_o[x+1,y-1] + n_o[x+1,y+1])/2
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*mean_n - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])/(set['h']**2)
                    
                elif x == set['Nx']:
                    mean_b = (b_o[x-1,y-1] + b_o[x-1,y+1])/2
                    mean_n = (n_o[x-1,y-1] + n_o[x-1,y+1])/2                    
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*mean_n - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])/(set['h']**2)
                    
                else:
                    mean_b = (b_o[x+1,y+1] + b_o[x-1,y+1] + b_o[x+1,y-1] + b_o[x-1,y-1])/4
                    mean_n = (n_o[x+1,y+1] + n_o[x-1,y+1] + n_o[x+1,y-1] + n_o[x-1,y-1])/4
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*mean_n - set['dt']*coef['gama']) + set['dt']*coef['k_1']*S + coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-4*c_o[x,y])/(set['h']**2)
#     for y in range(1,set['Ny'],2):
#         for x in range(1,set['Nx'],2):
#             if sol['b'][x,y] != 0:
#                 print 'Stalk cell position:[',x,',',y,'], With value:',sol['b'][x,y]                 
    return sol