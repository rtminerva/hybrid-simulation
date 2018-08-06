import numpy
import math as m

def c_kinetic_(coef, set, sol, c_o, A_o, I_o, Ki_o):              
    '''at sub lattice'''
    C_ = coef['A_c']*m.exp(-(coef['vel']*set['dt']*set['k']-set['delay'])**2/coef['vari'])
    sol['c'].append(C_)
    
    '''Calculate A,I,Ki'''
    A_ = A_o*(1-set['dt']*coef['l_a']) + set['dt']*coef['k_a']*c_o # + set['dt']*coef['teta_a']
    I_ = I_o*(1-set['dt']*coef['l_i']) + set['dt']*coef['k_i']*c_o # + set['dt']*coef['teta_i'] 
    if I_ != 0 :
        Q_ = A_/I_
    else:
        Q_ = 0
        
    
    sol['A'].append(A_)
    sol['I'].append(I_)
    sol['Q'].append(Q_)
    
    if coef['LEGI'] == 'basic':
        ##Basic LEGI
        sol['F_Ki'].append(coef['k_A']*(coef['R_o']-Ki_o))
        sol['G_Ki'].append(coef['k_I']*Ki_o)
    elif coef['LEGI'] == 'ultrasensitive':
        ##Ultrasensitive LEGI
        sol['F_Ki'].append(coef['k_A']*(coef['R_o']-Ki_o)/((coef['R_o']-Ki_o)+coef['K_A']))
        sol['G_Ki'].append(coef['k_I']*Ki_o/(Ki_o+coef['K_I']))
    
    Ki_ = Ki_o + set['dt']*(sol['F_Ki'][-1]*A_o - sol['G_Ki'][-1]*I_o)
    sol['Ki'].append(Ki_)
    
    return sol
 
def system_1d(coef, set, sol): #2.3
    c_o = sol['c'][-1] #to save values at time step k (we are calculating at time step k+1)
    A_o = sol['A'][-1]
    I_o = sol['I'][-1]
    Ki_o = sol['Ki'][-1]
    
    sol = c_kinetic_(coef, set, sol, c_o, A_o, I_o, Ki_o)    

    return sol