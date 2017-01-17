from random import randint, sample, uniform
import numpy

def c_f_T(coef, set, sol, n_o): #2.3
    c_o = numpy.copy(sol['c']) #to save values at time step k (we are calculating at time step k+1)
    b_o = numpy.copy(sol['b']) #to save values at time step k (we are calculating at time step k+1)
    
    '''Solve b at main lattice'''
    for y in range(1,set['Ny'],2):
        for x in range(1,set['Nx'],2):
            prolifer_1 = set['dt']*coef['vi']*b_o[x,y]*(1-b_o[x,y]) #proliferation term
            #we put the convection term as move variable
            if y == 1:
                if x == 1:
                    move = set['dt']*coef['C_4']*((b_o[x,y]*max(sol['Vb_x'][x,y],0)-b_o[x+2,y]*max(-sol['Vb_x'][x+2,y],0))+(b_o[x,y]*max(sol['Vb_y'][x,y],0)-b_o[x,y+2]*max(-sol['Vb_y'][x,y+2],0)))/set['h']
                elif x == set['Nx']-1:
                    move = set['dt']*coef['C_4']*(-(b_o[x-2,y]*max(sol['Vb_x'][x-2,y],0)-b_o[x,y]*max(-sol['Vb_x'][x,y],0))+(b_o[x,y]*max(sol['Vb_y'][x,y],0)-b_o[x,y+2]*max(-sol['Vb_y'][x,y+2],0)))/set['h']
                else:
                    move = set['dt']*coef['C_4']*((b_o[x,y]*max(sol['Vb_x'][x,y],0)-b_o[x+2,y]*max(-sol['Vb_x'][x+2,y],0))-(b_o[x-2,y]*max(sol['Vb_x'][x-2,y],0)-b_o[x,y]*max(-sol['Vb_x'][x,y],0))+(b_o[x,y]*max(sol['Vb_y'][x,y],0)-b_o[x,y+2]*max(-sol['Vb_y'][x,y+2],0)))/set['h']
            elif y == set['Ny']-1:
                if x == 1:
                    move = set['dt']*coef['C_4']*((b_o[x,y]*max(sol['Vb_x'][x,y],0)-b_o[x+2,y]*max(-sol['Vb_x'][x+2,y],0))-(b_o[x,y-2]*max(sol['Vb_y'][x,y-2],0)-b_o[x,y]*max(-sol['Vb_y'][x,y],0)))/set['h']
                elif x == set['Nx']-1:
                    move = set['dt']*coef['C_4']*(-(b_o[x-2,y]*max(sol['Vb_x'][x-2,y],0)-b_o[x,y]*max(-sol['Vb_x'][x,y],0))-(b_o[x,y-2]*max(sol['Vb_y'][x,y-2],0)-b_o[x,y]*max(-sol['Vb_y'][x,y],0)))/set['h']
                else:
                    move = set['dt']*coef['C_4']*((b_o[x,y]*max(sol['Vb_x'][x,y],0)-b_o[x+2,y]*max(-sol['Vb_x'][x+2,y],0))-(b_o[x-2,y]*max(sol['Vb_x'][x-2,y],0)-b_o[x,y]*max(-sol['Vb_x'][x,y],0))-(b_o[x,y-2]*max(sol['Vb_y'][x,y-2],0)-b_o[x,y]*max(-sol['Vb_y'][x,y],0)))/set['h']
            else:
                if x == 1:
                    move = set['dt']*coef['C_4']*((b_o[x,y]*max(sol['Vb_x'][x,y],0)-b_o[x+2,y]*max(-sol['Vb_x'][x+2,y],0))+(b_o[x,y]*max(sol['Vb_y'][x,y],0)-b_o[x,y+2]*max(-sol['Vb_y'][x,y+2],0))-(b_o[x,y-2]*max(sol['Vb_y'][x,y-2],0)-b_o[x,y]*max(-sol['Vb_y'][x,y],0)))/set['h']
                elif x == set['Nx']-1:
                    set['dt']*coef['C_4']*(-(b_o[x-2,y]*max(sol['Vb_x'][x-2,y],0)-b_o[x,y]*max(-sol['Vb_x'][x,y],0))+(b_o[x,y]*max(sol['Vb_y'][x,y],0)-b_o[x,y+2]*max(-sol['Vb_y'][x,y+2],0))-(b_o[x,y-2]*max(sol['Vb_y'][x,y-2],0)-b_o[x,y]*max(-sol['Vb_y'][x,y],0)))/set['h']  
                else:
                    move = set['dt']*coef['C_4']*((b_o[x,y]*max(sol['Vb_x'][x,y],0)-b_o[x+2,y]*max(-sol['Vb_x'][x+2,y],0))-(b_o[x-2,y]*max(sol['Vb_x'][x-2,y],0)-b_o[x,y]*max(-sol['Vb_x'][x,y],0))+(b_o[x,y]*max(sol['Vb_y'][x,y],0)-b_o[x,y+2]*max(-sol['Vb_y'][x,y+2],0))-(b_o[x,y-2]*max(sol['Vb_y'][x,y-2],0)-b_o[x,y]*max(-sol['Vb_y'][x,y],0)))/set['h'] 
            sol['b'][x,y] = b_o[x,y] + prolifer_1 - move
            sol['b'][1,set['Ny']/2+1] = 1 #the supply of stalk from pre-existing vessel
#             if b_o[x,y] != 0:
#                 print 'Value of proliferation:', prolifer_1
#                 print 'Value of degradation by movement:', move                         
    '''Solve c at sub lattice'''
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            degradation_c = set['dt']*coef['gama']*c_o[x,y]
            if y == 0: 
                if x == 0:
                    mean_b = b_o[x+1,y+1]
                    mean_n = n_o[x+1,y+1]
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    move_c = coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x,y+2]-2*c_o[x,y])/(set['h']**2) 
                                     
                elif x == set['Nx']:
                    mean_b = b_o[x-1,y+1]
                    mean_n = n_o[x-1,y+1]
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    move_c = coef['C_3']*set['dt']*(c_o[x-2,y]+c_o[x,y+2]-2*c_o[x,y])/(set['h']**2)
                   
                else:
                    mean_b = (b_o[x-1,y+1] + b_o[x+1,y+1])/2
                    mean_n = (n_o[x-1,y+1] + n_o[x+1,y+1])/2
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0   
                    move_c = coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]-3*c_o[x,y])/(set['h']**2)               
                    
            elif y == set['Ny']:
                if x == 0:
                    mean_b = b_o[x+1,y-1]
                    mean_n = n_o[x+1,y-1]
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    move_c = coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x,y-2]-2*c_o[x,y])/(set['h']**2)
                    
                elif x == set['Nx']:
                    mean_b = b_o[x-1,y-1]
                    mean_n = n_o[x-1,y-1]
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    move_c = coef['C_3']*set['dt']*(c_o[x-2,y]+c_o[x,y-2]-2*c_o[x,y])/(set['h']**2)
                         
                else:
                    mean_b = (b_o[x-1,y-1] + b_o[x+1,y-1])/2
                    mean_n = (n_o[x-1,y-1] + n_o[x+1,y-1])/2
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0                               
                    move_c = coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y-2]-3*c_o[x,y])/(set['h']**2)
                        
            else:
                if x == 0:
                    mean_b = (b_o[x+1,y-1] + b_o[x+1,y+1])/2
                    mean_n = (n_o[x+1,y-1] + n_o[x+1,y+1])/2
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    move_c = coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])/(set['h']**2)
                    
                elif x == set['Nx']:
                    mean_b = (b_o[x-1,y-1] + b_o[x-1,y+1])/2
                    mean_n = (n_o[x-1,y-1] + n_o[x-1,y+1])/2                    
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    move_c = coef['C_3']*set['dt']*(c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])/(set['h']**2)
                    
                else:
                    mean_b = (b_o[x+1,y+1] + b_o[x-1,y+1] + b_o[x+1,y-1] + b_o[x-1,y-1])/4
                    mean_n = (n_o[x+1,y+1] + n_o[x-1,y+1] + n_o[x+1,y-1] + n_o[x-1,y-1])/4
                    if mean_b < coef['beta2']:
                        S = 1- (mean_b/coef['beta2'])
                    else:
                        S = 0
                    move_c = coef['C_3']*set['dt']*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-4*c_o[x,y])/(set['h']**2)
                        
            prolifer_c = set['dt']*coef['k_1']*S
            digestion_c = set['dt']*coef['Nu']*c_o[x,y]*mean_n
            sol['c'][x,y] = c_o[x,y] + prolifer_c - digestion_c - degradation_c + move_c
        
#     for y in range(1,set['Ny'],2):
#         for x in range(1,set['Nx'],2):
#             if sol['b'][x,y] != 0:
#                 print 'Stalk cell position:[',x,',',y,'], With value:',sol['b'][x,y]                 
    return sol