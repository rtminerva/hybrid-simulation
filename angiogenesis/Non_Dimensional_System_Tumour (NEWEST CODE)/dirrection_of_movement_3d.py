import numpy

def movement_dir_3d(coef, set, sol, xb, yb, zb, nom):

    cijx = 1/(4*set['h'])*(sol['c'][xb+1,yb+1,zb-1]-sol['c'][xb-1,yb+1,zb-1]+sol['c'][xb+1,yb-1,zb-1]-sol['c'][xb-1,yb-1,zb-1]+sol['c'][xb+1,yb+1,zb+1]-sol['c'][xb-1,yb+1,zb+1]+sol['c'][xb+1,yb-1,zb+1]-sol['c'][xb-1,yb-1,zb+1])
    cijy = 1/(4*set['h'])*(sol['c'][xb+1,yb+1,zb-1]-sol['c'][xb+1,yb-1,zb-1]+sol['c'][xb-1,yb+1,zb-1]-sol['c'][xb-1,yb-1,zb-1]+sol['c'][xb+1,yb+1,zb+1]-sol['c'][xb+1,yb-1,zb+1]+sol['c'][xb-1,yb+1,zb+1]-sol['c'][xb-1,yb-1,zb+1])
    cijz = 1/(4*set['h'])*(sol['c'][xb-1,yb-1,zb+1]-sol['c'][xb-1,yb-1,zb-1]+sol['c'][xb+1,yb-1,zb+1]-sol['c'][xb+1,yb-1,zb-1]+sol['c'][xb+1,yb+1,zb+1]-sol['c'][xb+1,yb+1,zb-1]+sol['c'][xb-1,yb+1,zb+1]-sol['c'][xb-1,yb+1,zb-1])
    cijx_p = max(0,cijx)
    cijx_n = max(0,-cijx)
    cijy_p = max(0,cijy)
    cijy_n = max(0,-cijy)
    cijz_p = max(0,cijz)
    cijz_n = max(0,-cijz)
    if not coef['Ro'] == 0:
        fijx = 1/(4*set['h'])*(sol['f'][xb+1,yb+1,zb-1]-sol['f'][xb-1,yb+1,zb-1]+sol['f'][xb+1,yb-1,zb-1]-sol['f'][xb-1,yb-1,zb-1]+sol['f'][xb+1,yb+1,zb+1]-sol['f'][xb-1,yb+1,zb+1]+sol['f'][xb+1,yb-1,zb+1]-sol['f'][xb-1,yb-1,zb+1])
        fijy = 1/(4*set['h'])*(sol['f'][xb+1,yb+1,zb-1]-sol['f'][xb+1,yb-1,zb-1]+sol['f'][xb-1,yb+1,zb-1]-sol['f'][xb-1,yb-1,zb-1]+sol['f'][xb+1,yb+1,zb+1]-sol['f'][xb+1,yb-1,zb+1]+sol['f'][xb-1,yb+1,zb+1]-sol['f'][xb-1,yb-1,zb+1])
        fijz = 1/(4*set['h'])*(sol['f'][xb-1,yb-1,zb+1]-sol['f'][xb-1,yb-1,zb-1]+sol['f'][xb+1,yb-1,zb+1]-sol['f'][xb+1,yb-1,zb-1]+sol['f'][xb+1,yb+1,zb+1]-sol['f'][xb+1,yb+1,zb-1]+sol['f'][xb-1,yb+1,zb+1]-sol['f'][xb-1,yb+1,zb-1])
        fijx_p = max(0,fijx)
        fijx_n = max(0,-fijx)
        fijy_p = max(0,fijy)
        fijy_n = max(0,-fijy)
        fijz_p = max(0,fijz)
        fijz_n = max(0,-fijz)
    else:
        fijx_p = 0
        fijx_n = 0
        fijy_p = 0
        fijy_n = 0
        fijz_p = 0
        fijz_n = 0
    
    Gijx_p = coef['Ki_n']/(1+coef['Al_n']*1/8*(sol['c'][xb-1,yb+1,zb+1]+sol['c'][xb+1,yb+1,zb+1]+sol['c'][xb-1,yb-1,zb+1]+sol['c'][xb+1,yb-1,zb+1]+sol['c'][xb-1,yb+1,zb-1]+sol['c'][xb+1,yb+1,zb-1]+sol['c'][xb-1,yb-1,zb-1]+sol['c'][xb+1,yb-1,zb-1]))*cijx_p+coef['Ro']*fijx_p
    Gijx_n = coef['Ki_n']/(1+coef['Al_n']*1/8*(sol['c'][xb-1,yb+1,zb+1]+sol['c'][xb+1,yb+1,zb+1]+sol['c'][xb-1,yb-1,zb+1]+sol['c'][xb+1,yb-1,zb+1]+sol['c'][xb-1,yb+1,zb-1]+sol['c'][xb+1,yb+1,zb-1]+sol['c'][xb-1,yb-1,zb-1]+sol['c'][xb+1,yb-1,zb-1]))*cijx_n+coef['Ro']*fijx_n
    Gijy_p = coef['Ki_n']/(1+coef['Al_n']*1/8*(sol['c'][xb-1,yb+1,zb+1]+sol['c'][xb+1,yb+1,zb+1]+sol['c'][xb-1,yb-1,zb+1]+sol['c'][xb+1,yb-1,zb+1]+sol['c'][xb-1,yb+1,zb-1]+sol['c'][xb+1,yb+1,zb-1]+sol['c'][xb-1,yb-1,zb-1]+sol['c'][xb+1,yb-1,zb-1]))*cijy_p+coef['Ro']*fijy_p
    Gijy_n = coef['Ki_n']/(1+coef['Al_n']*1/8*(sol['c'][xb-1,yb+1,zb+1]+sol['c'][xb+1,yb+1,zb+1]+sol['c'][xb-1,yb-1,zb+1]+sol['c'][xb+1,yb-1,zb+1]+sol['c'][xb-1,yb+1,zb-1]+sol['c'][xb+1,yb+1,zb-1]+sol['c'][xb-1,yb-1,zb-1]+sol['c'][xb+1,yb-1,zb-1]))*cijy_n+coef['Ro']*fijy_n
    Gijz_p = coef['Ki_n']/(1+coef['Al_n']*1/8*(sol['c'][xb-1,yb+1,zb+1]+sol['c'][xb+1,yb+1,zb+1]+sol['c'][xb-1,yb-1,zb+1]+sol['c'][xb+1,yb-1,zb+1]+sol['c'][xb-1,yb+1,zb-1]+sol['c'][xb+1,yb+1,zb-1]+sol['c'][xb-1,yb-1,zb-1]+sol['c'][xb+1,yb-1,zb-1]))*cijz_p+coef['Ro']*fijz_p
    Gijz_n = coef['Ki_n']/(1+coef['Al_n']*1/8*(sol['c'][xb-1,yb+1,zb+1]+sol['c'][xb+1,yb+1,zb+1]+sol['c'][xb-1,yb-1,zb+1]+sol['c'][xb+1,yb-1,zb+1]+sol['c'][xb-1,yb+1,zb-1]+sol['c'][xb+1,yb+1,zb-1]+sol['c'][xb-1,yb-1,zb-1]+sol['c'][xb+1,yb-1,zb-1]))*cijz_n+coef['Ro']*fijz_n
    
      
    P_1 = int((set['dt']/(set['h']**2)*coef['D_n']+set['dt']/(set['h'])*Gijx_n)*10000)
    P_2 = int((set['dt']/(set['h']**2)*coef['D_n']+set['dt']/(set['h'])*Gijx_p)*10000)
    P_3 = int((set['dt']/(set['h']**2)*coef['D_n']+set['dt']/(set['h'])*Gijy_n)*10000)
    P_4 = int((set['dt']/(set['h']**2)*coef['D_n']+set['dt']/(set['h'])*Gijy_p)*10000)
    P_5 = int((set['dt']/(set['h']**2)*coef['D_n']+set['dt']/(set['h'])*Gijz_n)*10000)
    P_6 = int((set['dt']/(set['h']**2)*coef['D_n']+set['dt']/(set['h'])*Gijz_p)*10000)
    
    

    '''Checking no back movement
    no_back = sol['list_tip_movement'][nom]
    if no_back == 'right':
        P_1 = 0
    elif no_back == 'left':
        P_2 = 0
    elif no_back == 'up':
        P_3 = 0
    elif no_back == 'down':
        P_4 = 0
    '''
    
    '''Checking if other tip meet this tip
    lx = xb - 2
    rx = xb + 2
    dy = yb - 2
    uy = yb + 2
     
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
    '''
        
    '''Boundary Checking'''
    if zb == 1:
        P_5 = 0
        if yb == 1: 
            P_3 = 0
            if xb == 1:
                P_1 = 0
            elif xb == set['Nx']-1:
                P_2 = 0                
        elif yb == set['Ny']-1:
            P_4 = 0
            if xb == 1:
                P_1 = 0
            elif xb == set['Nx']-1:
                P_2 = 0
        else:
            if xb == 1:
                P_1 = 0
            elif xb == set['Nx']-1:
                P_2 = 0                
    elif zb == set['Nz']-1:
        P_6 = 0
        if yb == 1:
            P_3 = 0 
            if xb == 1:
                P_1 = 0
            elif xb == set['Nx']-1:
                P_2 = 0
        elif yb == set['Ny']-1:
            P_4 = 0
            if xb == 1:
                P_1 = 0
            elif xb == set['Nx']-1:
                P_2 = 0      
        else:
            if xb == 1:
                P_1 = 0
            elif xb == set['Nx']-1:
                P_2 = 0
    elif xb == 1 and yb == 1:
        P_1 = 0
        P_3 = 0
    elif xb == set['Nx']-1 and yb == 1:
        P_2 = 0
        P_3 = 0
    elif xb == 1 and yb == set['Ny']-1:
        P_1 = 0
        P_4 = 0
    elif xb == set['Nx']-1 and yb == set['Ny']-1:
        P_2 = 0
        P_4 = 0
    elif xb == 1:
        P_1 = 0        
    elif yb == 1:
        P_3 = 0
    elif xb == set['Nx']-1:
        P_2 = 0    
    elif yb == set['Ny']-1:
        P_4 = 0
        
    P_0 = 10000-(P_1+P_2+P_3+P_4+P_5+P_6)
    
    prob_range = [P_0,P_1,P_2,P_3,P_4,P_5,P_6]
    #print 'probability P', P_0, ',',P_1,',',P_2,',',P_3,',',P_4
    return prob_range
