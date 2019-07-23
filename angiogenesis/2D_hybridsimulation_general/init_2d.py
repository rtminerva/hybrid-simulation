import numpy
import math as m
from click import _winconsole

def ctprof_osci_stable(coef,set,sol):
    viu = (numpy.sqrt(5)-0.1)/(numpy.sqrt(5)-1)
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
            r_c = numpy.sqrt((x*set['Hh'])**2+(y*set['Hh']-0.5)**2)
            if r_c >= 0.2:
#                 sol['c'][x,y] = 1-(viu-r_c)**2/(viu-0.1)**2 #* (1+m.sin((0.5-x*set['Hh'])*m.pi))* set['ga_1']/4* (m.sin(2*m.pi*set['et_1']*set['t'])+1)
#                 sol['c_t'][x,y] = 1-(viu-r_c)**2/(viu-0.1)**2 #* 2*m.pi*set['et_1']*m.cos(2*m.pi*set['et_1']*set['t']) * (1+m.sin((0.5-x*set['Hh'])*m.pi))* set['ga_1']/4
                sol['c'][x,y] = (m.sin(2*m.pi*set['et_1']*set['t'])+1) * (1-m.exp(-1*r_c**2))
                sol['c_t'][x,y] = 2*m.pi*set['et_1']*m.cos(2*m.pi*set['et_1']*set['t']) * (1-m.exp(-1*r_c**2))
            elif r_c>= 0 and r_c < 0.2:
                sol['c'][x,y] = 0
                sol['c_t'][x,y] = 0
            
            #normal
#             sol['c'][x,y] = (1+m.sin((0.5-x*set['Hh'])*m.pi))* set['ga_1']/4* (m.sin(2*m.pi*set['et_1']*set['t'])+1) #* (1+m.cos(set['u']*m.pi*(x*set['Hh']-0.5)))
#             sol['c_t'][x,y] = 2*m.pi*set['et_1']*m.cos(2*m.pi*set['et_1']*set['t']) * (1+m.sin((0.5-x*set['Hh'])*m.pi))* set['ga_1']/4 #* (1+m.cos(set['u']*m.pi*(x*set['Hh']-0.5)))
    return sol

def ctprof_osci_decrease(coef,set,sol): #Ref.2.1.1
#     viu = (numpy.sqrt(5)-0.1)/(numpy.sqrt(5)-1)
    for y in range(0,set['Ny']+1,2):
        for x in range(0,set['Nx']+1,2):
#             #standard
#             r_c = numpy.sqrt((x*set['Hh'])**2+(y*set['Hh']-0.5)**2)
#             if r_c >= 0.1:
#                 sol['c'][x,y] = set['a']*(set['b'] + m.sin(m.pi*set['et_1']*set['t']) * m.exp(-set['alpha']*set['t'])) * (1 - m.exp(-2*r_c**2))
#                 sol['c_t'][x,y] = set['a']*(m.pi*set['et_1']*m.cos(m.pi*set['et_1']*set['t']) - set['alpha']*m.sin(m.pi*set['et_1']*set['t'])) * m.exp(-set['alpha']*set['t']) * (1-m.exp(-2*r_c**2))
#             elif r_c>= 0 and r_c < 0.1:
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
#             sol['c'][x,y] = set['a'] * (set['b'] + m.sin(m.pi*set['et_1']*set['t']) * m.exp(-set['alpha']*set['t'])) * (1 - m.exp(-2*(x*set['Hh'])**2))
#             sol['c_t'][x,y] = set['a'] * (m.pi*set['et_1']*m.cos(m.pi*set['et_1']*set['t']) - set['alpha']*m.sin(m.pi*set['et_1']*set['t'])) * m.exp(-set['alpha']*set['t']) * (1-m.exp(-2*(x*set['Hh'])**2))
            
#             #profile1
#             sol['c'][x,y] = set['ga_1']/4 * (1+m.sin((x*set['Hh']-0.5)*m.pi)) * (m.sin(m.pi*set['et_1']*set['t'])+1) #* (1+m.cos(set['u']*m.pi*(x*set['Hh']-0.5)))
#             sol['c_t'][x,y] = set['ga_1']/4 * (1+m.sin((x*set['Hh']-0.5)*m.pi)) * m.pi*set['et_1']*m.cos(m.pi*set['et_1']*set['t']) #* (1+m.cos(set['u']*m.pi*(x*set['Hh']-0.5)))
    
    return sol


def init_2d_(coef,set,sol): #Ref.2.1
    sol['c'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
    sol['c_t'] = numpy.zeros((set['Nx']+1,set['Ny']+1))

#     sol = ctprof_osci_stable(coef,set,sol)
    sol = ctprof_osci_decrease(coef,set,sol) #Ref.2.1.1
    return sol
        