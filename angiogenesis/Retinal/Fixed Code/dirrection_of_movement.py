def movement_dir(coef, set, sol, xb, yb, nom, n_dir = True):
    ml = 'f'
    mr = 'f'
    md = 'f'
    mu = 'f'
    la = sol['tp']/(set['h']**2)
    
    if n_dir == True:
        vvx = 0.5/set['h']*(sol['c']xb+1,yb+1]-sol['c']xb-1,yb+1]+sol['c']xb+1,yb-1]-sol['c']xb-1,yb-1])
        vvy = 0.5/set['h']*(sol['c']xb+1,yb+1]+sol['c']xb-1,yb+1]-sol['c']xb+1,yb-1]-sol['c']xb-1,yb-1])
        vvx_p = max(0,vvx)
        vvx_n = max(0,-vvx)
        vvy_p = max(0,vvy)
        vvy_n = max(0,-vvy)
        
        wwx = 0.5/set['h']*(sol['f'][xb+1,yb+1]-sol['f'][xb-1,yb+1]+sol['f'][xb+1,yb-1]-sol['f'][xb-1,yb-1])
        wwy = 0.5/set['h']*(sol['f'][xb+1,yb+1]+sol['f'][xb-1,yb+1]-sol['f'][xb+1,yb-1]-sol['f'][xb-1,yb-1])
        wwx_p = max(0,wwx)
        wwx_n = max(0,-wwx)
        wwy_p = max(0,wwy)
        wwy_n = max(0,-wwy)
        
        if not sol['Mic'] == 0 or not sol['Kappa'] == 0:
            
            if mm[xb,yb] == 1: #or mm[xb+2,yb] == 1 or mm[xb-2,yb] == 1 or mm[xb,yb+2] == 1 or mm[xb,yb-2] == 1 or mm[xb+2,yb+2] == 1 or mm[xb-2,yb+2] == 1 or mm[xb-2,yb-2] == 1 or mm[xb+2,yb-2] == 1:
                mm_bool = 1
            else:
                mm_bool = 0
            P_1 = la*coef['D_n']+la*set['h']*vvx_n*coef['Ki_n']/( (1+sol['Mic']*mm_bool) * (1+coef['Al_n']*sol['c']xb-1,yb+1]) ) + la*set['h']*(coef['Ro']+sol['Kappa']*mm_bool)*wwx_n
            P_2 = la*coef['D_n']+la*set['h']*vvx_p*coef['Ki_n']/( (1+sol['Mic']*mm_bool) * (1+coef['Al_n']*sol['c']xb+1,yb+1]) ) + la*set['h']*(coef['Ro']+sol['Kappa']*mm_bool)*wwx_p
            
            P_3 = la*coef['D_n']+la*set['h']*vvy_n*coef['Ki_n']/( (1+sol['Mic']*mm_bool) * (1+coef['Al_n']*sol['c']xb+1,yb-1]) ) + la*set['h']*(coef['Ro']+sol['Kappa']*mm_bool)*wwy_n
            P_4 = la*coef['D_n']+la*set['h']*vvy_p*coef['Ki_n']/( (1+sol['Mic']*mm_bool) * (1+coef['Al_n']*sol['c']xb+1,yb+1]) ) + la*set['h']*(coef['Ro']+sol['Kappa']*mm_bool)*wwy_p
        else:
            P_1 = la*coef['D_n']+la*set['h']*coef['Ki_n']/(1+coef['Al_n']*sol['c']xb-1,yb+1])*vvx_n + la*set['h']*coef['Ro']*wwx_n
            P_2 = la*coef['D_n']+la*set['h']*coef['Ki_n']/(1+coef['Al_n']*sol['c']xb+1,yb+1])*vvx_p + la*set['h']*coef['Ro']*wwx_p
            
            P_3 = la*coef['D_n']+la*set['h']*coef['Ki_n']/(1+coef['Al_n']*sol['c']xb+1,yb-1])*vvy_n + la*set['h']*coef['Ro']*wwy_n
            P_4 = la*coef['D_n']+la*set['h']*coef['Ki_n']/(1+coef['Al_n']*sol['c']xb+1,yb+1])*vvy_p + la*set['h']*coef['Ro']*wwy_p
    else:
        vvx = 0.5/set['h']*(sol['p']xb+1,yb+1]-sol['p']xb-1,yb+1]+sol['p']xb+1,yb-1]-sol['p']xb-1,yb-1])
        vvy = 0.5/set['h']*(sol['p']xb+1,yb+1]+sol['p']xb-1,yb+1]-sol['p']xb+1,yb-1]-sol['p']xb-1,yb-1])
        vvx_p = max(0,vvx)
        vvx_n = max(0,-vvx)
        vvy_p = max(0,vvy)
        vvy_n = max(0,-vvy)

        P_1 = la*coef['D_n']+la*set['h']*coef['Ki_n']/(1+coef['Al_n']*sol['p']xb-1,yb+1])*vvx_n
        P_2 = la*coef['D_n']+la*set['h']*coef['Ki_n']/(1+coef['Al_n']*sol['p']xb+1,yb+1])*vvx_p 
        
        P_3 = la*coef['D_n']+la*set['h']*coef['Ki_n']/(1+coef['Al_n']*sol['p']xb+1,yb-1])*vvy_n 
        P_4 = la*coef['D_n']+la*set['h']*coef['Ki_n']/(1+coef['Al_n']*sol['p']xb+1,yb+1])*vvy_p 
    
    if P_1 < 0 or P_2 < 0 or P_3 < 0 or P_4 < 0:
        print 'ADA P yang Negative'
    
    '''Boundary on the inner circle'''
    r_f = (xb*set['Hh']-set['O_x'])**2 + (yb*set['Hh']-set['O_y'])**2
    Pos = (xb,yb)
    
    '''Checking space for n & m'''
    lx = xb - 2
    rx = xb + 2
        
    dy = yb - 2
    uy = yb + 2
    if n_dir == True:
        '''Checking space for n'''
        for tep in range(0,len(sol['matrix_tip'])):
            if not tep == nom:
               # if (lx,yb) in sol['matrix_tip'][tep] and (rx,yb) in sol['matrix_tip'][tep] and (xb,dy) in sol['matrix_tip'][tep] and (xb,uy) in sol['matrix_tip'][tep]:
               #     move = 'stop'
                if (lx,yb) in sol['matrix_tip'][tep]:
                    ml = 'stop'
                if (rx,yb) in sol['matrix_tip'][tep]:
                    mr = 'stop'
                if (xb,dy) in sol['matrix_tip'][tep]:
                    md = 'stop'
                if (xb,uy) in sol['matrix_tip'][tep]:
                    mu = 'stop'
        
    '''Boundary Checking'''    
    if Pos == sol['matrix_tip'][0][0]:
        P_2 = 0        
    elif Pos == sol['matrix_tip'][1][0]:
        P_1 = 0
    elif Pos == sol['matrix_tip'][2][0]:
        P_4 = 0
    elif Pos == sol['matrix_tip'][3][0]:
        P_3 = 0
    elif r_f <= (R_min**2 + error):
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
        elif xb == n_x-1: #pojok kanan bawah
            P_2 = 0
    elif yb == n_x-1: #batas atas
        P_4 = 0
        if xb == 1: #pojok kiri atas
            P_1 = 0
        elif xb == n_x-1: #pojok kanan atas
            P_2 = 0
    else: #selain batas bawah dan atas
        if xb == 1: #batas kiri selain pojok
            P_1 = 0
        elif xb == n_x-1: #batas kanan selain pojok
            P_2 = 0
        #selain batas2, tetap pada nilai P_1 ~ P_4 awal saja
    
    if not n_dir == True:
        '''Checking space for m'''
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
    
    '''Using Non-reflection Boundary'''           
    P_0 = 1-(P_1+P_2+P_3+P_4)
    
    
    prob_range = [P_0,P_1,P_2,P_3,P_4,ml,mr,md,mu]
#    print 'probability P', P_0, ',',P_1,',',P_2,',',P_3,',',P_4
    return prob_range;
