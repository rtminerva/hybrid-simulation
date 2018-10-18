import numpy
import math as m

def init_1d_(coef,set,sol): #2.1.1
    sol['c'] = [0]#coef['A_c']*m.exp(-(coef['vel']*0-set['delay'])**2/coef['vari'])]
    
    sol['A'] = [0]
    sol['I'] = [0]
    sol['Ki'] = [0]
#     sol['Q'] = [sol['A'][-1]/sol['I'][-1]]
    sol['Q'] = [coef['k_a']/coef['k_i']]
    sol['Qr'] = [0]
    
    sol['F_Ki'] = [0]
    sol['G_Ki'] = [0]
       
    return sol
        