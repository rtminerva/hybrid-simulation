from random import randint, sample, uniform
import numpy
import math as m

def system_2d(coef, set, sol):
#     c_o = sol['c'][:]
    viu = (numpy.sqrt(5)-0.1)/(numpy.sqrt(5)-1)
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            r_c = numpy.sqrt((x*set['Hh'])**2+(y*set['Hh']-0.5)**2)
            if r_c >= 0.1:
                sol['c'][x,y] = (0.8 + m.sin(m.pi*set['et_1']*set['t']) * m.exp(-set['alpha']*set['t'])) * (1 - m.exp(-4*r_c**2))
                sol['c_t'][x,y] = (m.pi*set['et_1']*m.cos(m.pi*set['et_1']*set['t']) - set['alpha']*m.sin(m.pi*set['et_1']*set['t'])) * m.exp(-set['alpha']*set['t']) * (1-m.exp(-1*r_c**2))
#                 sol['c'][x,y] = (m.sin(2*m.pi*set['et_1']*set['t'])+1) * (1-m.exp(-1*r_c**2))
#                 sol['c_t'][x,y] = 2*m.pi*set['et_1']*m.cos(2*m.pi*set['et_1']*set['t']) * (1-m.exp(-1*r_c**2))
            elif r_c >= 0 and r_c < 0.1:
                sol['c'][x,y] = 0
                sol['c_t'][x,y] = 0
            
#             #normal
#             sol['c'][x,y] = (0.8 + m.sin(m.pi*set['et_1']*set['t']) * m.exp(-set['alpha']*set['t'])) * (1 - m.exp(-4*(x*set['Hh'])**2))
#             sol['c_t'][x,y] = (m.pi*set['et_1']*m.cos(m.pi*set['et_1']*set['t']) - set['alpha']*m.sin(m.pi*set['et_1']*set['t'])) * m.exp(-set['alpha']*set['t']) * (1-m.exp(-1*(x*set['Hh'])**2))
            
            #normal
#             sol['c'][x,y] = (1+m.sin((0.5-x*set['Hh'])*m.pi))* set['ga_1']/4* (m.sin(2*m.pi*set['et_1']*set['t'])+1) #* (1+m.cos(set['u']*m.pi*(x*set['Hh']-0.5)))
#             sol['c_t'][x,y] = 2*m.pi*set['et_1']*m.cos(2*m.pi*set['et_1']*set['t']) * (1+m.sin((0.5-x*set['Hh'])*m.pi))* set['ga_1']/4 #* (1+m.cos(set['u']*m.pi*(x*set['Hh']-0.5)))
                     
#     sol['tip_cell_area'] = []
    
    return sol