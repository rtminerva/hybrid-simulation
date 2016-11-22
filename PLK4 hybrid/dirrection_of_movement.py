import numpy

def movement_dir(coef, set, sol, xb, yb, nom): #2.2.1
    G_plus_1 = max(0,sol['G_vec_x'][xb,yb])
    G_plus_2 = max(0,sol['G_vec_y'][xb,yb])
    
    G_neg_1 = max(0,-sol['G_vec_x'][xb,yb])
    G_neg_2 = max(0,-sol['G_vec_y'][xb,yb])
    
    Gijx_p = max(0,sol['G_vec_x'][xb,yb])
    Gijx_n = max(0,-sol['G_vec_x'][xb,yb])
    Gijy_p = max(0,sol['G_vec_y'][xb,yb])
    Gijy_n = max(0,-sol['G_vec_y'][xb,yb])
      
    P_1 = int((set['dt']/(set['h']**2)*coef['D_4']+set['dt']/(set['h'])*Gijx_n)*10000)
    P_2 = int((set['dt']/(set['h']**2)*coef['D_4']+set['dt']/(set['h'])*Gijx_p)*10000)
    P_3 = int((set['dt']/(set['h']**2)*coef['D_4']+set['dt']/(set['h'])*Gijy_n)*10000)
    P_4 = int((set['dt']/(set['h']**2)*coef['D_4']+set['dt']/(set['h'])*Gijy_p)*10000)  
    
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
        if xb == 1: #pojok kiri bawah
            P_1 = 0
        elif xb == set['Nx']-1: #pojok kanan bawah
            P_2 = 0
    elif yb == set['Nx']-1: #batas atas
        P_4 = 0
        if xb == 1: #pojok kiri atas
            P_1 = 0
        elif xb == set['Nx']-1: #pojok kanan atas
            P_2 = 0
    else: #selain batas bawah dan atas
        if xb == 1: #batas kiri selain pojok
            P_1 = 0
        elif xb == set['Nx']-1: #batas kanan selain pojok
            P_2 = 0
        #selain batas2, tetap pada nilai P_1 ~ P_4 awal saja
        
    P_0 = 10000-(P_1+P_2+P_3+P_4)
    
    prob_range = [P_0,P_1,P_2,P_3,P_4]
    #print 'probability P', P_0, ',',P_1,',',P_2,',',P_3,',',P_4
    return prob_range
