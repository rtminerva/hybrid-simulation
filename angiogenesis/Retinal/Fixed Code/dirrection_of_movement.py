def movement_dir(xb = 0, yb = 0, cc = 0, sol['f'] = 0, mm = 0,
                 tep = 0, h1 = 0, R_min = 0, error = 0,
                 d_n1 = 0, ki_n1 = 0, al_n1 = 0, ro1 = 0, sol['Mic'] = 0, sol['Kappa'] = 0,
                 n_x = 0, n_y = 0, Matrix_tip = 0, Index_m = 0, n_dir = True, Nom = 0, ml = 'f', mr = 'f', md = 'f', mu = 'f'):

def movement_dir(coef, set, sol, xb, yb, h2, n_dir = True):
    la = sol['tp']/(h2**2)

    vvx = 0.5/h1*(sol['c']xb+1,yb+1]-sol['c']xb-1,yb+1]+sol['c']xb+1,yb-1]-sol['c']xb-1,yb-1])
    vvy = 0.5/h1*(sol['c']xb+1,yb+1]+sol['c']xb-1,yb+1]-sol['c']xb+1,yb-1]-sol['c']xb-1,yb-1])
    
    vvx_p = max(0,vvx)
    vvx_n = max(0,-vvx)
    vvy_p = max(0,vvy)
    vvy_n = max(0,-vvy)
 
    if n_dir == True:
        wwx = 0.5/h1*(sol['f'][xb+1,yb+1]-sol['f'][xb-1,yb+1]+sol['f'][xb+1,yb-1]-sol['f'][xb-1,yb-1])
        wwy = 0.5/h1*(sol['f'][xb+1,yb+1]+sol['f'][xb-1,yb+1]-sol['f'][xb+1,yb-1]-sol['f'][xb-1,yb-1])
        wwx_p = max(0,wwx)
        wwx_n = max(0,-wwx)
        wwy_p = max(0,wwy)
        wwy_n = max(0,-wwy)
        #print 'NILAI M', mm[xb,yb]
        if not sol['Mic'] == 0 or not sol['Kappa'] == 0:
            #if not mm[xb,yb] == 0:
            #    print 'M EXIST'
            if mm[xb,yb] == 1: #or mm[xb+2,yb] == 1 or mm[xb-2,yb] == 1 or mm[xb,yb+2] == 1 or mm[xb,yb-2] == 1 or mm[xb+2,yb+2] == 1 or mm[xb-2,yb+2] == 1 or mm[xb-2,yb-2] == 1 or mm[xb+2,yb-2] == 1:
                mm_bool = 1
            else:
                mm_bool = 0
            P_1 = la*d_n1+la*h1*vvx_n*ki_n1/( (1+sol['Mic']*mm_bool) * (1+al_n1*sol['c']xb-1,yb+1]) ) + la*h1*(ro1+sol['Kappa']*mm_bool)*wwx_n
            P_2 = la*d_n1+la*h1*vvx_p*ki_n1/( (1+sol['Mic']*mm_bool) * (1+al_n1*sol['c']xb+1,yb+1]) ) + la*h1*(ro1+sol['Kappa']*mm_bool)*wwx_p
            
            P_3 = la*d_n1+la*h1*vvy_n*ki_n1/( (1+sol['Mic']*mm_bool) * (1+al_n1*sol['c']xb+1,yb-1]) ) + la*h1*(ro1+sol['Kappa']*mm_bool)*wwy_n
            P_4 = la*d_n1+la*h1*vvy_p*ki_n1/( (1+sol['Mic']*mm_bool) * (1+al_n1*sol['c']xb+1,yb+1]) ) + la*h1*(ro1+sol['Kappa']*mm_bool)*wwy_p
        else:
            P_1 = la*d_n1+la*h1*ki_n1/(1+al_n1*sol['c']xb-1,yb+1])*vvx_n + la*h1*ro1*wwx_n
            P_2 = la*d_n1+la*h1*ki_n1/(1+al_n1*sol['c']xb+1,yb+1])*vvx_p + la*h1*ro1*wwx_p
            
            P_3 = la*d_n1+la*h1*ki_n1/(1+al_n1*sol['c']xb+1,yb-1])*vvy_n + la*h1*ro1*wwy_n
            P_4 = la*d_n1+la*h1*ki_n1/(1+al_n1*sol['c']xb+1,yb+1])*vvy_p + la*h1*ro1*wwy_p
    else:
        #if sol['c']xb,yb] == 1 or sol['c']xb+2,yb] == 1 or sol['c']xb-2,yb] == 1 or sol['c']xb,yb+2] == 1 or sol['c']xb,yb-2] == 1 or sol['c']xb+2,yb+2] == 1 or sol['c']xb-2,yb+2] == 1 or sol['c']xb-2,yb-2] == 1 or sol['c']xb+2,yb-2] == 1:
        #    cc_bool = 1
        #else:
        #    cc_bool = 0
        P_1 = la*d_n1+la*h1*ki_n1/(1+al_n1*sol['c']xb-1,yb+1])*vvx_n #+ la*h1*ro1*wwx_n
        P_2 = la*d_n1+la*h1*ki_n1/(1+al_n1*sol['c']xb+1,yb+1])*vvx_p #+ la*h1*ro1*wwx_p
        
        P_3 = la*d_n1+la*h1*ki_n1/(1+al_n1*sol['c']xb+1,yb-1])*vvy_n #+ la*h1*ro1*wwy_n
        P_4 = la*d_n1+la*h1*ki_n1/(1+al_n1*sol['c']xb+1,yb+1])*vvy_p #+ la*h1*ro1*wwy_p
    
    if P_1 < 0 or P_2 < 0 or P_3 < 0 or P_4 < 0:
        print 'ADA P yang Negative'
    
    '''Boundary on the inner circle'''
    O_x = n_x/2*set['Hh']
    O_y = n_y/2*set['Hh']
    r_f = (xb*set['Hh']-O_x)**2 + (yb*set['Hh']-O_y)**2
    Pos = (xb,yb)
    
    '''Checking space for n & m'''
    lx = xb - 2
    rx = xb + 2
        
    dy = yb - 2
    uy = yb + 2
    if n_dir == True:
        '''Checking space for n'''
        for tep in range(0,len(Matrix_tip)):
            if not tep == Nom:
               # if (lx,yb) in Matrix_tip[tep] and (rx,yb) in Matrix_tip[tep] and (xb,dy) in Matrix_tip[tep] and (xb,uy) in Matrix_tip[tep]:
               #     move = 'stop'
                if (lx,yb) in Matrix_tip[tep]:
                    ml = 'stop'
                if (rx,yb) in Matrix_tip[tep]:
                    mr = 'stop'
                if (xb,dy) in Matrix_tip[tep]:
                    md = 'stop'
                if (xb,uy) in Matrix_tip[tep]:
                    mu = 'stop'
        
        
        '''
        if [lx,yb] in Index_m:
            P_1 = 0
        if [rx,yb] in Index_m:
            P_2 = 0
        if [xb,dy] in Index_m:
            P_3 = 0
        if [xb,uy] in Index_m:
            P_4 = 0
        '''
        
    '''Boundary Checking'''    
    if Pos == Matrix_tip[0][0]:
        P_2 = 0        
    elif Pos == Matrix_tip[1][0]:
        P_1 = 0
    elif Pos == Matrix_tip[2][0]:
        P_4 = 0
    elif Pos == Matrix_tip[3][0]:
        P_3 = 0
    elif r_f <= (R_min**2 + error):
        if xb >= Matrix_tip[2][0][0] and yb >= Matrix_tip[0][0][1]:
            P_1 = 0
            P_3 = 0
        elif xb <= Matrix_tip[2][0][0] and yb >= Matrix_tip[0][0][1]:
            P_2 = 0
            P_3 = 0
        elif xb <= Matrix_tip[2][0][0] and yb <= Matrix_tip[0][0][1]:
            P_2 = 0
            P_4 = 0
        elif xb >= Matrix_tip[2][0][0] and yb <= Matrix_tip[0][0][1]:
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
            if mm[lx,yb] == 1:
                P_1 = 0
        if not P_2 == 0:
            if mm[rx,yb] == 1:
                P_2 = 0
        if not P_3 == 0:
            if mm[xb,dy] == 1:
                P_3 = 0
        if not P_4 == 0:
            if mm[xb,uy] == 1:
                P_4 = 0
    
    '''Using Non-reflection Boundary'''           
    P_0 = 1-(P_1+P_2+P_3+P_4)
    
    
    prob_range = [P_0,P_1,P_2,P_3,P_4,ml,mr,md,mu]
#    print 'probability P', P_0, ',',P_1,',',P_2,',',P_3,',',P_4
    return prob_range;
