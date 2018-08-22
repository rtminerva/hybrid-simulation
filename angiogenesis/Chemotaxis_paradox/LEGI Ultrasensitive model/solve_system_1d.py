import numpy
import math as m

def c_kinetic_(coef, set, sol, c_o, A_o, I_o, Ki_o):              
    if coef['C_prof'] == 'exp':
        C_ = coef['A_c']*m.exp(-(coef['vel']*set['dt']*set['k']-set['delay'])**2/coef['vari']) #exponentially
    elif coef['C_prof'] == 'step':
        if set['t'] > 60 and set['t'] < 180:
            C_ = 1
        else:
            C_ = 0
    elif coef['C_prof'] == 'tan':
        C_ = 0.5*m.tanh((set['delay2']-set['t'])/5)+0.5*m.tanh((set['t']-set['delay1'])/5)
    sol['c'].append(C_)
    
    '''Calculate A,I,Ki'''
    A_ = A_o*(1-set['dt']*coef['l_a']) + set['dt']*coef['k_a']*c_o # + set['dt']*coef['teta_a']
    I_ = I_o*(1-set['dt']*coef['l_i']) + set['dt']*coef['k_i']*c_o # + set['dt']*coef['teta_i'] 
    if I_ == 0 and A_ == 0:
        Q_ = coef['k_a']/coef['k_i']*m.exp(set['t']*(coef['l_a']-coef['l_i']))
    else:
        Q_ = A_/I_
        
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
    Qr_ = sol['G_Ki'][-1]/sol['F_Ki'][-1]
    sol['Qr'].append(Qr_)
    
    return sol
 
def system_1d(coef, set, sol): #2.3
    c_o = sol['c'][-1] #to save values at time step k (we are calculating at time step k+1)
    A_o = sol['A'][-1]
    I_o = sol['I'][-1]
    Ki_o = sol['Ki'][-1]
    
    sol = c_kinetic_(coef, set, sol, c_o, A_o, I_o, Ki_o)    

    return sol