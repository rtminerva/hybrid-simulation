from random import randint, sample, uniform
import numpy
import math as m

def system_2d(coef, set, sol):
#     c_o = sol['c'][:]
    
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            sol['c'][x,y] = (1+m.sin(2*m.pi*set['ga_1']*x*set['Hh']-set['et_1']*set['t']))*m.exp(-set['xi_1']*set['t'])
            sol['c_t'][x,y] = (-set['et_1']*m.cos(2*m.pi*set['ga_1']*x*set['Hh']-set['et_1']*set['t']))*m.exp(-set['xi_1']*set['t']) - set['xi_1']*(1+m.sin(2*m.pi*set['ga_1']*x*set['Hh']-set['et_1']*set['t']))*m.exp(-set['xi_1']*set['t'])

#     '''Solve c, f, p at sub lattice'''
#     for y in range(0,set['Ny']+1,2):
#         for x in range(0,set['Nx']+1,2):                       
#             '''TIP CELL?'''
#             if [x,y] in sol['tip_cell_area']:
#                 n_tip = 1               
#             else:
#                 n_tip = 0
#             
#             if y == 0: 
#                 if x == 0:
#                     sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x,y+2]-2*c_o[x,y])
#                      
#                 elif x == set['Nx']:
#                     sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x-2,y]+c_o[x,y+2]-2*c_o[x,y])
#                    
#                 else:
#                     sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]-3*c_o[x,y])
#                     
#             elif y == set['Ny']:
#                 if x == 0:
#                     sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x,y-2]-2*c_o[x,y])
# 
#                 elif x == set['Nx']:
#                     sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x-2,y]+c_o[x,y-2]-2*c_o[x,y])
#                            
#                 else:
#                     sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y-2]-3*c_o[x,y])
#                         
#             else:
#                 if x == 0:
#                     sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])
#                     
#                 elif x == set['Nx']:
#                     sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])
#                     
#                 else: 
#                     sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['Nu']*n_tip)#+ coef['D_c']*set['dt']/set['h']**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-4*c_o[x,y])
#                     
    sol['tip_cell_area'] = []
    
    return sol