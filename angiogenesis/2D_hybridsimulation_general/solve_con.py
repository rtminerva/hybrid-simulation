from random import randint, sample, uniform
import numpy
import math as m

def system_2d(coef, set, sol): #4.2
#     c_o = sol['c'][:]
#     viu = (numpy.sqrt(5)-0.1)/(numpy.sqrt(5)-1)
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
#             #standard
#             r_c = numpy.sqrt((x*set['Hh'])**2+(y*set['Hh']-0.5)**2)
#             if r_c >= 0.1:
#                 sol['c'][x,y] = set['a']*(set['b'] + m.sin(m.pi*set['et_1']*set['t']) * m.exp(-set['alpha']*set['t'])) * (1 - m.exp(-2*r_c**2))
#                 sol['c_t'][x,y] = set['a']*(m.pi*set['et_1']*m.cos(m.pi*set['et_1']*set['t']) - set['alpha']*m.sin(m.pi*set['et_1']*set['t'])) * m.exp(-set['alpha']*set['t']) * (1-m.exp(-2*r_c**2))
#             elif r_c >= 0 and r_c < 0.1:
#                 sol['c'][x,y] = 0
#                 sol['c_t'][x,y] = 0
            
            #chaplain
            r_c = numpy.sqrt((x*set['Hh'])**2+(y*set['Hh']-0.5)**2)
            if r_c >= 0.1:
                sol['c'][x,y] = set['a']*(set['b'] + m.sin(m.pi*set['et_1']*set['t']) * m.exp(-set['alpha']*set['t'])) * (1-(3-r_c)**2/(3-0.1)**2)
                sol['c_t'][x,y] = set['a']*(m.pi*set['et_1']*m.cos(m.pi*set['et_1']*set['t']) - set['alpha']*m.sin(m.pi*set['et_1']*set['t'])) * m.exp(-set['alpha']*set['t']) * (1-(3-r_c)**2/(3-0.1)**2)
            elif r_c>= 0 and r_c < 0.1:
                sol['c'][x,y] = 0
                sol['c_t'][x,y] = 0
              
#             #normal
#              sol['c'][x,y] = set['a'] * (set['b'] + m.sin(m.pi*set['et_1']*set['t']) * m.exp(-set['alpha']*set['t'])) * (1 - m.exp(-2*(x*set['Hh'])**2))
#              sol['c_t'][x,y] = set['a'] * (m.pi*set['et_1']*m.cos(m.pi*set['et_1']*set['t']) - set['alpha']*m.sin(m.pi*set['et_1']*set['t'])) * m.exp(-set['alpha']*set['t']) * (1-m.exp(-2*(x*set['Hh'])**2))
    
#             #profile1
#              sol['c'][x,y] = set['ga_1']/4 * (1+m.sin((x*set['Hh']-0.5)*m.pi)) * (m.sin(m.pi*set['et_1']*set['t'])+1) #* (1+m.cos(set['u']*m.pi*(x*set['Hh']-0.5)))
#              sol['c_t'][x,y] = set['ga_1']/4 * (1+m.sin((x*set['Hh']-0.5)*m.pi)) * m.pi*set['et_1']*m.cos(m.pi*set['et_1']*set['t']) #* (1+m.cos(set['u']*m.pi*(x*set['Hh']-0.5)))
    
    return sol