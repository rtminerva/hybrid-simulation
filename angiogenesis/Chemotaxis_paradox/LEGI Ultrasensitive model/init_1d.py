import numpy
import math as m

def init_1d_(coef,set,sol): #2.1.1
    sol['c'] = [0]
    
    sol['A'] = [0]
    sol['I'] = [0]
    sol['Ki'] = [0]
    sol['Q'] = [0]
    sol['Qr'] = [0]
    
    sol['F_Ki'] = [0]
    sol['G_Ki'] = [0]
       
    
    return sol
        