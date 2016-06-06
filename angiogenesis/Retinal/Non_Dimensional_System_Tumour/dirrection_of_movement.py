import numpy

def movement_dir(coef, set, sol, xb, yb, nom):

    cijx = 1/(2*set['h'])*(sol['c'][xb+1,yb+1]-sol['c'][xb-1,yb+1]+sol['c'][xb+1,yb-1]-sol['c'][xb-1,yb-1])
    cijy = 1/(2*set['h'])*(sol['c'][xb+1,yb+1]-sol['c'][xb+1,yb-1]+sol['c'][xb-1,yb+1]-sol['c'][xb-1,yb-1])
    
    cijx_p = max(0,cijx)
    cijx_n = max(0,-cijx)
    cijy_p = max(0,cijy)
    cijy_n = max(0,-cijy)
    
    '''
    fijx = 1/(2*set['h'])*(sol['f'][xb+1,yb+1]-sol['f'][xb-1,yb+1]+sol['f'][xb+1,yb-1]-sol['f'][xb-1,yb-1])
    fijy = 1/(2*set['h'])*(sol['f'][xb+1,yb+1]-sol['f'][xb+1,yb-1]+sol['f'][xb-1,yb+1]-sol['f'][xb-1,yb-1])
    fijx_p = max(0,fijx)
    fijx_n = max(0,-fijx)
    fijy_p = max(0,fijy)
    fijy_n = max(0,-fijy)
    '''
    
    Gijx_p = coef['Ki_n']/(1+coef['Al_n']*1/4*(sol['c'][xb-1,yb+1]+sol['c'][xb+1,yb+1]+sol['c'][xb-1,yb-1]+sol['c'][xb+1,yb-1]))*cijx_p#+coef['Ro']*fijx_p
    Gijx_n = coef['Ki_n']/(1+coef['Al_n']*1/4*(sol['c'][xb-1,yb+1]+sol['c'][xb+1,yb+1]+sol['c'][xb-1,yb-1]+sol['c'][xb+1,yb-1]))*cijx_n#+coef['Ro']*fijx_n
    Gijy_p = coef['Ki_n']/(1+coef['Al_n']*1/4*(sol['c'][xb-1,yb+1]+sol['c'][xb+1,yb+1]+sol['c'][xb-1,yb-1]+sol['c'][xb+1,yb-1]))*cijy_p#+coef['Ro']*fijy_p
    Gijy_n = coef['Ki_n']/(1+coef['Al_n']*1/4*(sol['c'][xb-1,yb+1]+sol['c'][xb+1,yb+1]+sol['c'][xb-1,yb-1]+sol['c'][xb+1,yb-1]))*cijy_n#+coef['Ro']*fijy_n
    
      
    P_1 = int((set['dt']/(set['h']**2)*coef['D_n']+set['dt']/(set['h'])*Gijx_n)*10000)
    P_2 = int((set['dt']/(set['h']**2)*coef['D_n']+set['dt']/(set['h'])*Gijx_p)*10000)
    P_3 = int((set['dt']/(set['h']**2)*coef['D_n']+set['dt']/(set['h'])*Gijy_n)*10000)
    P_4 = int((set['dt']/(set['h']**2)*coef['D_n']+set['dt']/(set['h'])*Gijy_p)*10000)
    

    '''Checking no back movement'''
    no_back = sol['list_tip_movement'][nom]
    if no_back == 'right':
        P_1 = 0
    elif no_back == 'left':
        P_2 = 0
    elif no_back == 'up':
        P_3 = 0
    elif no_back == 'down':
        P_4 = 0
    
    '''Checking if other tip meet this tip'''
    cek = str(nom)
    if cek in sol['pp']:
        print 'HEREE'
        if sol['pp'][nom][0] == 'right':
            P_2 = 0
        elif sol['pp'][nom][1] == 'left':
            P_1 = 0
        elif sol['pp'][nom][2] == 'up':
            P_4 = 0
        elif sol['pp'][nom][3] == 'down':
            P_3 = 0
    
    if P_1 < 0 or P_2 < 0 or P_3 < 0 or P_4 < 0:
        print 'ADA P yang Negative'
    if P_1 + P_2 + P_3 + P_4 > 10000:
        print 'ADA P yang Big'
      
        
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
