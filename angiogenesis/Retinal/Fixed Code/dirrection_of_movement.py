def movement_dir(coef, set, sol, xb, yb, nom, n_dir = True):
    #ml = 'f'
    #mr = 'f'
    #md = 'f'
    #mu = 'f'
    
    lx = xb - 2
    rx = xb + 2
    dy = yb - 2
    uy = yb + 2

    if n_dir == True:
        if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
            if sol['m'][xb,yb] == 1: #or sol['m'][xb+2,yb] == 1 or sol['m'][xb-2,yb] == 1 or sol['m'][xb,yb+2] == 1 or sol['m'][xb,yb-2] == 1 or sol['m'][xb+2,yb+2] == 1 or sol['m'][xb-2,yb+2] == 1 or sol['m'][xb-2,yb-2] == 1 or sol['m'][xb+2,yb-2] == 1:
                mm_bool = 1
            else:
                mm_bool = 0
            Gijx = coef['Ki_n']/((1+coef['Mic']*mm_bool)*(1+coef['Al_n']*1/4*(sol['c'][xb-1,yb+1]+sol['c'][xb+1,yb+1]+sol['c'][xb-1,yb-1]+sol['c'][xb+1,yb-1])))*1/(2*set['h'])*(sol['c'][xb+1,yb+1]-sol['c'][xb-1,yb+1]+sol['c'][xb+1,yb-1]-sol['c'][xb-1,yb-1])+(coef['Ro']+coef['Kappa']*mm_bool)*1/(2*set['h'])*(sol['f'][xb+1,yb+1]-sol['f'][xb-1,yb+1]+sol['f'][xb+1,yb-1]-sol['f'][xb-1,yb-1])
            Gijy = coef['Ki_n']/((1+coef['Mic']*mm_bool)*(1+coef['Al_n']*1/4*(sol['c'][xb-1,yb+1]+sol['c'][xb+1,yb+1]+sol['c'][xb-1,yb-1]+sol['c'][xb+1,yb-1])))*1/(2*set['h'])*(sol['c'][xb+1,yb+1]-sol['c'][xb+1,yb-1]+sol['c'][xb-1,yb+1]-sol['c'][xb-1,yb-1])+(coef['Ro']+coef['Kappa']*mm_bool)*1/(2*set['h'])*(sol['f'][xb+1,yb+1]-sol['f'][xb+1,yb-1]+sol['f'][xb-1,yb+1]-sol['f'][xb-1,yb-1])
        else:
            Gijx = coef['Ki_n']/(1+coef['Al_n']*1/4*(sol['c'][xb-1,yb+1]+sol['c'][xb+1,yb+1]+sol['c'][xb-1,yb-1]+sol['c'][xb+1,yb-1]))*1/(2*set['h'])*(sol['c'][xb+1,yb+1]-sol['c'][xb-1,yb+1]+sol['c'][xb+1,yb-1]-sol['c'][xb-1,yb-1])+coef['Ro']*1/(2*set['h'])*(sol['f'][xb+1,yb+1]-sol['f'][xb-1,yb+1]+sol['f'][xb+1,yb-1]-sol['f'][xb-1,yb-1])
            Gijy = coef['Ki_n']/(1+coef['Al_n']*1/4*(sol['c'][xb-1,yb+1]+sol['c'][xb+1,yb+1]+sol['c'][xb-1,yb-1]+sol['c'][xb+1,yb-1]))*1/(2*set['h'])*(sol['c'][xb+1,yb+1]-sol['c'][xb+1,yb-1]+sol['c'][xb-1,yb+1]-sol['c'][xb-1,yb-1])+coef['Ro']*1/(2*set['h'])*(sol['f'][xb+1,yb+1]-sol['f'][xb+1,yb-1]+sol['f'][xb-1,yb+1]-sol['f'][xb-1,yb-1])
        
        Gijx_p = max(0,Gijx)
        Gijx_n = max(0,-Gijx)
        Gijy_p = max(0,Gijy)
        Gijy_n = max(0,-Gijy)
        
        P_1 = int((sol['tp']/(set['h']**2)*coef['D_n']+sol['tp']/(set['h'])*Gijx_n)*10000)
        P_2 = int((sol['tp']/(set['h']**2)*coef['D_n']+sol['tp']/(set['h'])*Gijx_p)*10000)
        P_3 = int((sol['tp']/(set['h']**2)*coef['D_n']+sol['tp']/(set['h'])*Gijy_n)*10000)
        P_4 = int((sol['tp']/(set['h']**2)*coef['D_n']+sol['tp']/(set['h'])*Gijy_p)*10000)
        
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
        
        '''Checking Space for n'''
        for tep in range(0,len(sol['matrix_tip'])):
            if not tep == nom:
               # if (lx,yb) in sol['matrix_tip'][tep] and (rx,yb) in sol['matrix_tip'][tep] and (xb,dy) in sol['matrix_tip'][tep] and (xb,uy) in sol['matrix_tip'][tep]:
               #     move = 'stop'
                if (lx,yb) in sol['matrix_tip'][tep]:
                    P_1 = 0
                    #ml = 'stop'
                if (rx,yb) in sol['matrix_tip'][tep]:
                    P_2 = 0
                    #mr = 'stop'
                if (xb,dy) in sol['matrix_tip'][tep]:
                    P_3 = 0
                    #md = 'stop'
                if (xb,uy) in sol['matrix_tip'][tep]:
                    P_4 = 0
                    #mu = 'stop'
        
        
    else:
        Gijx = coef['Ki_m']/(1+coef['Al_m']*1/4*(sol['p'][xb-1,yb+1]+sol['p'][xb+1,yb+1]+sol['p'][xb-1,yb-1]+sol['p'][xb+1,yb-1]))*1/(2*set['h'])*(sol['p'][xb+1,yb+1]-sol['p'][xb-1,yb+1]+sol['p'][xb+1,yb-1]-sol['p'][xb-1,yb-1])
        Gijy = coef['Ki_m']/(1+coef['Al_m']*1/4*(sol['p'][xb-1,yb+1]+sol['p'][xb+1,yb+1]+sol['p'][xb-1,yb-1]+sol['p'][xb+1,yb-1]))*1/(2*set['h'])*(sol['p'][xb+1,yb+1]-sol['p'][xb+1,yb-1]+sol['p'][xb-1,yb+1]-sol['p'][xb-1,yb-1])

        Gijx_p = max(0,Gijx)
        Gijx_n = max(0,-Gijx)
        Gijy_p = max(0,Gijy)
        Gijy_n = max(0,-Gijy)
        
        P_1 = int((sol['tp']/(set['h']**2)*coef['D_n']+sol['tp']/(set['h'])*Gijx_n)*100000)
        P_2 = int((sol['tp']/(set['h']**2)*coef['D_n']+sol['tp']/(set['h'])*Gijx_p)*100000)
        P_3 = int((sol['tp']/(set['h']**2)*coef['D_n']+sol['tp']/(set['h'])*Gijy_n)*100000)
        P_4 = int((sol['tp']/(set['h']**2)*coef['D_n']+sol['tp']/(set['h'])*Gijy_p)*100000)
        
        if not P_1 == 0:
            if sol['m'][lx,yb] == 1:
                P_1 = 0
        if not P_2 == 0:
            if sol['m'][rx,yb] == 1:
                P_2 = 0
        if not P_3 == 0:
            if sol['m'][xb,dy] == 1:
                P_3 = 0
        if not P_4 == 0:
            if sol['m'][xb,uy] == 1:
                P_4 = 0  
    
    if P_1 < 0 or P_2 < 0 or P_3 < 0 or P_4 < 0:
        print 'ADA P yang Negative'
    if P_1 + P_2 + P_3 + P_4 > 10000:
        print 'ADA P yang Big'
      
        
    '''Boundary Checking'''
    import numpy
    Pos = (xb,yb)
    r_f = numpy.sqrt((xb*set['Hh']-set['O_x'])**2 + (yb*set['Hh']-set['O_y'])**2) 
    if Pos == sol['matrix_tip'][0][0]:
        P_2 = 0        
    elif Pos == sol['matrix_tip'][1][0]:
        P_1 = 0
    elif Pos == sol['matrix_tip'][2][0]:
        P_4 = 0
    elif Pos == sol['matrix_tip'][3][0]:
        P_3 = 0
    elif r_f <= (set['R_min'] + set['error']):
        if xb >= sol['matrix_tip'][2][0][0] and yb >= sol['matrix_tip'][0][0][1]:
            P_1 = 0
            P_3 = 0
        elif xb <= sol['matrix_tip'][2][0][0] and yb >= sol['matrix_tip'][0][0][1]:
            P_2 = 0
            P_3 = 0
        elif xb <= sol['matrix_tip'][2][0][0] and yb <= sol['matrix_tip'][0][0][1]:
            P_2 = 0
            P_4 = 0
        elif xb >= sol['matrix_tip'][2][0][0] and yb <= sol['matrix_tip'][0][0][1]:
            P_1 = 0
            P_4 = 0
    elif yb == 1: #batas bawah
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
    
    prob_range = [P_0,P_1,P_2,P_3,P_4]#,ml,mr,md,mu]
#    print 'probability P', P_0, ',',P_1,',',P_2,',',P_3,',',P_4
    return prob_range;
