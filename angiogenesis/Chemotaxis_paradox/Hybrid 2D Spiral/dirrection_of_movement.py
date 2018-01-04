import numpy
import math as m

def movement_dir(coef, set, sol, xb, yb): #2.2.1
    #xb, yb are on main-lattices

    cijx = (sol['c'][xb+1,yb+1]-sol['c'][xb-1,yb+1]+sol['c'][xb+1,yb-1]-sol['c'][xb-1,yb-1])/(2*set['h'])
    cijy = (sol['c'][xb+1,yb+1]-sol['c'][xb+1,yb-1]+sol['c'][xb-1,yb+1]-sol['c'][xb-1,yb-1])/(2*set['h'])
     
    '''NEW Velocity'''    
    vijx = coef['alpha']*cijx - coef['beta']
    vijy = coef['alpha']*cijy# - coef['beta']
    
    '''Velocity cx'''
    vijx = coef['alpha']*cijx - (coef['beta']/(m.sqrt(cijx**2+cijy**2)+0.0001))*cijx
    vijy = coef['alpha']*cijy - (coef['beta']/(m.sqrt(cijx**2+cijy**2)+0.0001))*cijy
    
#     print 'cx', cijx, cijy
#     print 'VVVV', vijx, vijy
#     print 'vel_c', vijx, vijy
    
    vijx_p = max(0,vijx)
    vijx_n = max(0,-vijx)
    vijy_p = max(0,vijy)
    vijy_n = max(0,-vijy)
    
    p_1 = (set['dt']/(set['h']**2)*coef['D_n']+set['dt']/(set['h'])*vijx_n)
    p_2 = (set['dt']/(set['h']**2)*coef['D_n']+set['dt']/(set['h'])*vijx_p)
    p_3 = (set['dt']/(set['h']**2)*coef['D_n']+set['dt']/(set['h'])*vijy_n)
    p_4 = (set['dt']/(set['h']**2)*coef['D_n']+set['dt']/(set['h'])*vijy_p)
    
    P_1 = int(p_1*10000)
    P_2 = int(p_2*10000)
    P_3 = int(p_3*10000)
    P_4 = int(p_4*10000)

    if P_1 < 0 or P_2 < 0 or P_3 < 0 or P_4 < 0:
        print 'ADA P yang Negative'
        print 'probability P', P_1,',',P_2,',',P_3,',',P_4
        if P_1 <0:
            P_1 = 0
        elif P_2<0:
            P_2 = 0
        elif P_3<0:
            P_3 = 0
        elif P_4<0:
            P_4 = 0
            
    if P_1 + P_2 + P_3 + P_4 > 10000:
        print 'ADA P yang Big'
        print 'probability P', P_1,',',P_2,',',P_3,',',P_4
        if P_1 > 10000:
            P_1 = 0
        elif P_2 > 10000:
            P_2 = 0
        elif P_3 > 10000:
            P_3 = 0
        elif P_4 > 10000:
            P_4 = 0
      
    '''Boundary Checking'''
    if yb == 1: #batas bawah
        P_3 = 0
        p_3 = 0
        if xb == 1: #pojok kiri bawah
            P_1 = 0
            p_1 = 0
        elif xb == set['Nx']-1: #pojok kanan bawah
            P_2 = 0
            p_2 = 0
    elif yb == set['Nx']-1: #batas atas
        P_4 = 0
        p_4 = 0
        if xb == 1: #pojok kiri atas
            P_1 = 0
            p_1 = 0
        elif xb == set['Nx']-1: #pojok kanan atas
            P_2 = 0
            p_2 = 0
    else: #selain batas bawah dan atas
        if xb == 1: #batas kiri selain pojok
            P_1 = 0
            p_1 = 0
        elif xb == set['Nx']-1: #batas kanan selain pojok
            P_2 = 0
            p_2 = 0
        #selain batas2, tetap pada nilai P_1 ~ P_4 awal saja
        
    P_0 = 10000-(P_1+P_2+P_3+P_4)
    p_0 = 1- (p_1+p_2+p_3+p_4)
    
    prob_range = [P_0,P_1,P_2,P_3,P_4]
    prob = [p_0,p_1,p_2,p_3,p_4]
#     print prob_range
    if p_1 == 0 and p_2 == 0 and p_3 == 0 and p_4 == 0:
        print 'ALL P ZEROS', prob_range
    
    #print 'probability P', P_0, ',',P_1,',',P_2,',',P_3,',',P_4
    return prob_range, prob