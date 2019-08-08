from random import randint, sample, uniform
import numpy
import math as m

def system_2d(coef, set, sol): #4.2
    c_o = sol['c'][:]
    f_o = sol['f'][:]
    
    '''Solve c, f at sub lattice'''
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):                       
            '''TIP CELL?'''
            if [x,y] in sol['tip_cell_area']:
                n_tip = 1 
                sol['f'][x,y] = 0              
            else:
                n_tip = 0
            
            sol['c'][x,y] = c_o[x,y]*(1 - set['dt']*coef['c_1']*n_tip)
#             sol['f'][x,y] = f_o[x,y]*(1 - set['dt']*coef['f_1']*n_tip)
#             if n_tip == 1:
#                 print 'f', x, y, sol['f'][x,y]
            
    sol['tip_cell_area'] = []
    return sol