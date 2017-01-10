import numpy

def movement_dir(coef, set, sol, xb, yb, nom): #2.2.1

    cijx = (sol['c'][xb+1,yb+1]-sol['c'][xb-1,yb+1]+sol['c'][xb+1,yb-1]-sol['c'][xb-1,yb-1])/(2*set['h'])
    cijy = (sol['c'][xb+1,yb+1]-sol['c'][xb+1,yb-1]+sol['c'][xb-1,yb+1]-sol['c'][xb-1,yb-1])/(2*set['h'])

    cijx_p = max(0,cijx)
    cijx_n = max(0,-cijx)
    cijy_p = max(0,cijy)
    cijy_n = max(0,-cijy)
    
    if yb == 1:
        if xb == 1:
            b_mean_ur = (sol['b'][xb+2,yb+2]+sol['b'][xb,yb+2]+sol['b'][xb+2,yb]+sol['b'][xb,yb])/4
            b_mean_ul = (sol['b'][xb,yb]+sol['b'][xb,yb+2])/2
            b_mean_dr = (sol['b'][xb,yb]+sol['b'][xb+2,yb])/2
            b_mean_dl = sol['b'][xb,yb]
        elif xb == set['Nx']-1:
            b_mean_ur = (sol['b'][xb,yb]+sol['b'][xb,yb+2])/2
            b_mean_ul = (sol['b'][xb-2,yb]+sol['b'][xb,yb+2]+sol['b'][xb-2,yb+2]+sol['b'][xb,yb])/4
            b_mean_dr = sol['b'][xb,yb]
            b_mean_dl = (sol['b'][xb,yb]+sol['b'][xb-2,yb])/2
        else:
            b_mean_ur = (sol['b'][xb+2,yb+2]+sol['b'][xb,yb+2]+sol['b'][xb+2,yb]+sol['b'][xb,yb])/4
            b_mean_ul = (sol['b'][xb-2,yb-2]+sol['b'][xb,yb+2]+sol['b'][xb-2,yb]+sol['b'][xb,yb])/4
            b_mean_dr = (sol['b'][xb,yb]+sol['b'][xb+2,yb])/2
            b_mean_dl = (sol['b'][xb,yb]+sol['b'][xb-2,yb])/2
    elif yb == set['Ny']-1:
        if xb == 1:
            b_mean_ur = (sol['b'][xb,yb]+sol['b'][xb+2,yb])/2
            b_mean_ul = sol['b'][xb,yb]
            b_mean_dr = (sol['b'][xb+2,yb-2]+sol['b'][xb,yb-2]+sol['b'][xb+2,yb]+sol['b'][xb,yb])/4
            b_mean_dl = (sol['b'][xb,yb]+sol['b'][xb,yb-2])/2
        elif xb == set['Nx']-1:
            b_mean_ur = sol['b'][xb,yb]
            b_mean_ul = (sol['b'][xb,yb]+sol['b'][xb-2,yb])/2
            b_mean_dr = (sol['b'][xb,yb]+sol['b'][xb,yb-2])/2
            b_mean_dl = (sol['b'][xb-2,yb-2]+sol['b'][xb,yb-2]+sol['b'][xb-2,yb]+sol['b'][xb,yb])/4
        else:
            b_mean_ur = (sol['b'][xb,yb]+sol['b'][xb+2,yb])/2
            b_mean_ul = (sol['b'][xb,yb]+sol['b'][xb-2,yb])/2
            b_mean_dr = (sol['b'][xb+2,yb-2]+sol['b'][xb,yb-2]+sol['b'][xb+2,yb]+sol['b'][xb,yb])/4
            b_mean_dl = (sol['b'][xb-2,yb-2]+sol['b'][xb,yb-2]+sol['b'][xb-2,yb]+sol['b'][xb,yb])/4
    else:
        if xb == 1:
            b_mean_ur = (sol['b'][xb+2,yb+2]+sol['b'][xb,yb+2]+sol['b'][xb+2,yb]+sol['b'][xb,yb])/4
            b_mean_ul = (sol['b'][xb,yb]+sol['b'][xb,yb+2])/2
            b_mean_dr = (sol['b'][xb+2,yb-2]+sol['b'][xb,yb-2]+sol['b'][xb+2,yb]+sol['b'][xb,yb])/4
            b_mean_dl = (sol['b'][xb,yb]+sol['b'][xb,yb-2])/2
        elif xb == set['Nx']-1:
            b_mean_ur = (sol['b'][xb,yb]+sol['b'][xb,yb+2])/2
            b_mean_ul = (sol['b'][xb-2,yb+2]+sol['b'][xb,yb+2]+sol['b'][xb-2,yb]+sol['b'][xb,yb])/4
            b_mean_dr = (sol['b'][xb,yb]+sol['b'][xb,yb-2])/2
            b_mean_dl = (sol['b'][xb-2,yb-2]+sol['b'][xb,yb-2]+sol['b'][xb-2,yb]+sol['b'][xb,yb])/4
        else:
            b_mean_ur = (sol['b'][xb+2,yb+2]+sol['b'][xb,yb+2]+sol['b'][xb+2,yb]+sol['b'][xb,yb])/4
            b_mean_ul = (sol['b'][xb-2,yb+2]+sol['b'][xb,yb+2]+sol['b'][xb-2,yb]+sol['b'][xb,yb])/4
            b_mean_dr = (sol['b'][xb+2,yb-2]+sol['b'][xb,yb-2]+sol['b'][xb+2,yb]+sol['b'][xb,yb])/4
            b_mean_dl = (sol['b'][xb-2,yb-2]+sol['b'][xb,yb-2]+sol['b'][xb-2,yb]+sol['b'][xb,yb])/4
        
    bijx = (b_mean_ur-b_mean_ul+b_mean_dr-b_mean_dl)/(2*set['h'])
    bijy = (b_mean_ur-b_mean_dr+b_mean_ul-b_mean_dl)/(2*set['h'])
    
    bijx_p = max(0,bijx)
    bijx_n = max(0,-bijx)
    bijy_p = max(0,bijy)
    bijy_n = max(0,-bijy)
    
    #print b_mean_ur,b_mean_ul,b_mean_dr,b_mean_dl
    #print sol['b'][xb,yb]
    #print 'bijx,dst', bijx, bijy

    Gijx_p = coef['Ki']*cijx_p-coef['C_2']*bijx_p
    Gijx_n = coef['Ki']*cijx_n-coef['C_2']*bijx_n
    Gijy_p = coef['Ki']*cijy_p-coef['C_2']*bijy_p
    Gijy_n = coef['Ki']*cijy_n-coef['C_2']*bijy_n
    
#     print cijx_p, cijx_n, cijy_p, cijy_n
#     print Gijx_p, Gijx_n, Gijy_p, Gijy_n

      
    P_1 = int((set['dt']/(set['h']**2)*coef['C_1']+set['dt']/(set['h'])*Gijx_n)*10000)
    P_2 = int((set['dt']/(set['h']**2)*coef['C_1']+set['dt']/(set['h'])*Gijx_p)*10000)
    P_3 = int((set['dt']/(set['h']**2)*coef['C_1']+set['dt']/(set['h'])*Gijy_n)*10000)
    P_4 = int((set['dt']/(set['h']**2)*coef['C_1']+set['dt']/(set['h'])*Gijy_p)*10000)

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
