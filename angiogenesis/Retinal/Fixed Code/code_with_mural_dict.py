#import continuous_run as cont
def second_largest(numbers):
    count = 0
    m1 = m2 = float('-inf')
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1            
            else:
                m2 = x
    return m2 if count >= 2 else None


def movement_dir(x_pos = 0, y_pos = 0, cc = 0, ff = 0, mm = 0,
                 tep = 0, h1 = 0, R_min = 0, error = 0,
                 d_n1 = 0, ki_n1 = 0, al_n1 = 0, ro1 = 0, Mic = 0, Kappa = 0,
                 n_x = 0, n_y = 0, Matrix_tip = 0, Index_m = 0, n_dir = True, Nom = 0, ml = 'f', mr = 'f', md = 'f', mu = 'f'):

    la = tep/(h1**2)
    h2 = h1/2

    vvx = 0.5/h1*(cc[x_pos+1,y_pos+1]-cc[x_pos-1,y_pos+1]+cc[x_pos+1,y_pos-1]-cc[x_pos-1,y_pos-1])
    vvy = 0.5/h1*(cc[x_pos+1,y_pos+1]+cc[x_pos-1,y_pos+1]-cc[x_pos+1,y_pos-1]-cc[x_pos-1,y_pos-1])
    
    vvx_p = max(0,vvx)
    vvx_n = max(0,-vvx)
    vvy_p = max(0,vvy)
    vvy_n = max(0,-vvy)
 
    if n_dir == True:
        wwx = 0.5/h1*(ff[x_pos+1,y_pos+1]-ff[x_pos-1,y_pos+1]+ff[x_pos+1,y_pos-1]-ff[x_pos-1,y_pos-1])
        wwy = 0.5/h1*(ff[x_pos+1,y_pos+1]+ff[x_pos-1,y_pos+1]-ff[x_pos+1,y_pos-1]-ff[x_pos-1,y_pos-1])
        wwx_p = max(0,wwx)
        wwx_n = max(0,-wwx)
        wwy_p = max(0,wwy)
        wwy_n = max(0,-wwy)
        #print 'NILAI M', mm[x_pos,y_pos]
        if not Mic == 0 or not Kappa == 0:
            #if not mm[x_pos,y_pos] == 0:
            #    print 'M EXIST'
            if mm[x_pos,y_pos] == 1: #or mm[x_pos+2,y_pos] == 1 or mm[x_pos-2,y_pos] == 1 or mm[x_pos,y_pos+2] == 1 or mm[x_pos,y_pos-2] == 1 or mm[x_pos+2,y_pos+2] == 1 or mm[x_pos-2,y_pos+2] == 1 or mm[x_pos-2,y_pos-2] == 1 or mm[x_pos+2,y_pos-2] == 1:
                mm_bool = 1
            else:
                mm_bool = 0
            P_1 = la*d_n1+la*h1*vvx_n*ki_n1/( (1+Mic*mm_bool) * (1+al_n1*cc[x_pos-1,y_pos+1]) ) + la*h1*(ro1+Kappa*mm_bool)*wwx_n
            P_2 = la*d_n1+la*h1*vvx_p*ki_n1/( (1+Mic*mm_bool) * (1+al_n1*cc[x_pos+1,y_pos+1]) ) + la*h1*(ro1+Kappa*mm_bool)*wwx_p
            
            P_3 = la*d_n1+la*h1*vvy_n*ki_n1/( (1+Mic*mm_bool) * (1+al_n1*cc[x_pos+1,y_pos-1]) ) + la*h1*(ro1+Kappa*mm_bool)*wwy_n
            P_4 = la*d_n1+la*h1*vvy_p*ki_n1/( (1+Mic*mm_bool) * (1+al_n1*cc[x_pos+1,y_pos+1]) ) + la*h1*(ro1+Kappa*mm_bool)*wwy_p
        else:
            P_1 = la*d_n1+la*h1*ki_n1/(1+al_n1*cc[x_pos-1,y_pos+1])*vvx_n + la*h1*ro1*wwx_n
            P_2 = la*d_n1+la*h1*ki_n1/(1+al_n1*cc[x_pos+1,y_pos+1])*vvx_p + la*h1*ro1*wwx_p
            
            P_3 = la*d_n1+la*h1*ki_n1/(1+al_n1*cc[x_pos+1,y_pos-1])*vvy_n + la*h1*ro1*wwy_n
            P_4 = la*d_n1+la*h1*ki_n1/(1+al_n1*cc[x_pos+1,y_pos+1])*vvy_p + la*h1*ro1*wwy_p
    else:
        #if cc[x_pos,y_pos] == 1 or cc[x_pos+2,y_pos] == 1 or cc[x_pos-2,y_pos] == 1 or cc[x_pos,y_pos+2] == 1 or cc[x_pos,y_pos-2] == 1 or cc[x_pos+2,y_pos+2] == 1 or cc[x_pos-2,y_pos+2] == 1 or cc[x_pos-2,y_pos-2] == 1 or cc[x_pos+2,y_pos-2] == 1:
        #    cc_bool = 1
        #else:
        #    cc_bool = 0
        P_1 = la*d_n1+la*h1*ki_n1/(1+al_n1*cc[x_pos-1,y_pos+1])*vvx_n #+ la*h1*ro1*wwx_n
        P_2 = la*d_n1+la*h1*ki_n1/(1+al_n1*cc[x_pos+1,y_pos+1])*vvx_p #+ la*h1*ro1*wwx_p
        
        P_3 = la*d_n1+la*h1*ki_n1/(1+al_n1*cc[x_pos+1,y_pos-1])*vvy_n #+ la*h1*ro1*wwy_n
        P_4 = la*d_n1+la*h1*ki_n1/(1+al_n1*cc[x_pos+1,y_pos+1])*vvy_p #+ la*h1*ro1*wwy_p
    
    if P_1 < 0 or P_2 < 0 or P_3 < 0 or P_4 < 0:
        print 'ADA P yang Negative'
    
    '''Boundary on the inner circle'''
    O_x = n_x/2*h2
    O_y = n_y/2*h2
    r_f = (x_pos*h2-O_x)**2 + (y_pos*h2-O_y)**2
    Pos = (x_pos,y_pos)
    
    '''Checking space for n & m'''
    lx = x_pos - 2
    rx = x_pos + 2
        
    dy = y_pos - 2
    uy = y_pos + 2
    if n_dir == True:
        '''Checking space for n'''
        for tep in range(0,len(Matrix_tip)):
            if not tep == Nom:
               # if (lx,y_pos) in Matrix_tip[tep] and (rx,y_pos) in Matrix_tip[tep] and (x_pos,dy) in Matrix_tip[tep] and (x_pos,uy) in Matrix_tip[tep]:
               #     move = 'stop'
                if (lx,y_pos) in Matrix_tip[tep]:
                    ml = 'stop'
                if (rx,y_pos) in Matrix_tip[tep]:
                    mr = 'stop'
                if (x_pos,dy) in Matrix_tip[tep]:
                    md = 'stop'
                if (x_pos,uy) in Matrix_tip[tep]:
                    mu = 'stop'
        
        
        '''
        if [lx,y_pos] in Index_m:
            P_1 = 0
        if [rx,y_pos] in Index_m:
            P_2 = 0
        if [x_pos,dy] in Index_m:
            P_3 = 0
        if [x_pos,uy] in Index_m:
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
        if x_pos >= Matrix_tip[2][0][0] and y_pos >= Matrix_tip[0][0][1]:
            P_1 = 0
            P_3 = 0
        elif x_pos <= Matrix_tip[2][0][0] and y_pos >= Matrix_tip[0][0][1]:
            P_2 = 0
            P_3 = 0
        elif x_pos <= Matrix_tip[2][0][0] and y_pos <= Matrix_tip[0][0][1]:
            P_2 = 0
            P_4 = 0
        elif x_pos >= Matrix_tip[2][0][0] and y_pos <= Matrix_tip[0][0][1]:
            P_1 = 0
            P_4 = 0
    elif y_pos == 1: #batas bawah
        P_3 = 0
        if x_pos == 1: #pojok kiri bawah
            P_1 = 0
        elif x_pos == n_x-1: #pojok kanan bawah
            P_2 = 0
    elif y_pos == n_x-1: #batas atas
        P_4 = 0
        if x_pos == 1: #pojok kiri atas
            P_1 = 0
        elif x_pos == n_x-1: #pojok kanan atas
            P_2 = 0
    else: #selain batas bawah dan atas
        if x_pos == 1: #batas kiri selain pojok
            P_1 = 0
        elif x_pos == n_x-1: #batas kanan selain pojok
            P_2 = 0
        #selain batas2, tetap pada nilai P_1 ~ P_4 awal saja
    
    if not n_dir == True:
        '''Checking space for m'''
        if not P_1 == 0:
            if mm[lx,y_pos] == 1:
                P_1 = 0
        if not P_2 == 0:
            if mm[rx,y_pos] == 1:
                P_2 = 0
        if not P_3 == 0:
            if mm[x_pos,dy] == 1:
                P_3 = 0
        if not P_4 == 0:
            if mm[x_pos,uy] == 1:
                P_4 = 0
    
    '''Using Non-reflection Boundary'''           
    P_0 = 1-(P_1+P_2+P_3+P_4)
    
    
    prob_range = [P_0,P_1,P_2,P_3,P_4,ml,mr,md,mu]
#    print 'probability P', P_0, ',',P_1,',',P_2,',',P_3,',',P_4
    return prob_range;

def boolean_1_iter(coef, set, sol):
#     iter = 0, hh = 0, Nx = 0, Ny = 0,
#                     r_min = 0, r_max = 0,
#                     ro = 0, d_n = 0, ki_n = 0, al_n = 0,
#                     kappa = 0, mic = 0,
#                     d_c = 0, nu = 0,
#                     be = 0, ga = 0,
#                     d_m = 0, ki_m = 0, al_m = 0, #ro_m = 0,
#                     a_p = 0, b_p = 0, dl = 0,
#                     matrix_tip = 0,
#                     list_tip_movement = 0, life_time_tip = 0,
#                     stop_iter = 0, sp_stop = 0,
#                     n = 0, c = 0, f = 0, tp = 0, m = 0, p = 0, #index_m = 0,
#                     t_branch = 0,
#                     Error = 0, Rec = 0, index_mn = 0
#                     
    import numpy
    import random
    from random import randint
    
    h2 = 2*set['Hh']
    O_x = set['Nx']/2*set['Hh']
    O_y = set['Ny']/2*set['Hh']
    
    '''Initial Profile'''
    if set['k'] == 0:
        sol['c'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
        sol['f'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
        
        for y in range(0,set['Ny']+1,2):
            for x in range(0,set['Nx']+1,2):
                r_f = numpy.sqrt((x*set['Hh']-O_x)**2 + (y*set['Hh']-O_y)**2)
                if r_f >= set['R_min'] + numpy.sqrt(set['error']):
                    sol['c'][x,y] = 0.5-0.45*numpy.exp(-(r_f**2)/0.45)
                    sol['f'][x,y] = 0.5
                    #f[x,y] = 0.5-0.45*numpy.exp(-(set['R_max']-r_f)**2/0.45) 
        
        sol['matrix_tip'] = []
        sol['list_tip_movement'] = []
        sol['life_time_tip'] = []
        sol['sp_stop'] = []
                        
        ''''Initial Tips'''
        sol['n'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
        
        y1 = set['Ny']/2 + 1
        x = 1
        while x < set['Nx']+1:
            if (x*set['Hh']-O_x)**2 + (y1*set['Hh']-O_y)**2 < set['R_min']**2 + set['error'] and (x*set['Hh']-O_x)**2 + (y1*set['Hh']-O_y)**2 > set['R_min']**2:
                    sol['matrix_tip'].append([(x,y1)])
                    sol['n'][x,y1] = 1
                    sol['list_tip_movement'].append('start') #movement tip
                    sol['life_time_tip'].append(0) #lifetime
                    u = 10
            else:
                u = 2           
            x += u
            
        y1 = set['Nx']/2 + 1
        x = 1
        while x < set['Nx']+1:
            if (x*set['Hh']-O_x)**2 + (y1*set['Hh']-O_y)**2 < set['R_min']**2 + set['error'] and (x*set['Hh']-O_x)**2 + (y1*set['Hh']-O_y)**2 > set['R_min']**2:
                    sol['matrix_tip'].append([(y1,x)])
                    sol['n'][y1,x] = 1
                    sol['list_tip_movement'].append('start') #movement tip
                    sol['life_time_tip'].append(0) #lifetime
                    u = 10
            else:
                u = 2           
            x += u
                 
        y1 = sol['matrix_tip'][2][0][0] + (sol['matrix_tip'][1][0][0]- sol['matrix_tip'][2][0][0])/2
        if y1 % 2 == 0:
            y1 += 1
        x = 1
        while x < set['Nx']+1:
            if (x*set['Hh']-O_x)**2 + (y1*set['Hh']-O_y)**2 < set['R_min']**2 + set['error'] and (x*set['Hh']-O_x)**2 + (y1*set['Hh']-O_y)**2 > set['R_min']**2:
                    sol['matrix_tip'].append([(y1,x)])
                    sol['n'][y1,x] = 1
                    sol['list_tip_movement'].append('start') #movement tip
                    sol['life_time_tip'].append(0) #lifetime
                    u = 10
            else:
                u = 2           
            x += u
                    
        y1 = sol['matrix_tip'][0][0][0] + (sol['matrix_tip'][2][0][0]-sol['matrix_tip'][0][0][0])/2
        if y1 % 2 == 0:
            y1 += 1
        x = 1
        while x < set['Nx']+1:
            if (x*set['Hh']-O_x)**2 + (y1*set['Hh']-O_y)**2 < set['R_min']**2 + set['error'] and (x*set['Hh']-O_x)**2 + (y1*set['Hh']-O_y)**2 > set['R_min']**2:
                    sol['matrix_tip'].append([(y1,x)])
                    sol['n'][y1,x] = 1
                    sol['list_tip_movement'].append('start') #movement tip
                    sol['life_time_tip'].append(0) #lifetime
                    u = 10
            else:
                u = 2           
            x += u
        
        if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
            #index_m = []
            sol['index_mn'] = []
            sol['m'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
            sol['p'] = numpy.zeros((set['Nx']+1,set['Ny']+1))
            
            '''Randomly spotted in domain'''
            for tt in range(0,250):
                idx_m_1 = random.sample(range(1,440,2),100)
                idx_m_2 = random.sample(range(1,440,2),100)
                for id in range(0,len(idx_m_1)):
                    r_f = numpy.sqrt((idx_m_1[id]*set['Hh']-O_x)**2 + (idx_m_2[id]*set['Hh']-O_y)**2)
                    if not sol['m'][idx_m_1[id], idx_m_2[id]] == 1 and not [[idx_m_1[id], idx_m_2[id]]] in sol['matrix_tip'] and r_f >= set['R_min']:
                        sol['m'][idx_m_1[id], idx_m_2[id]] = 1

                        #print idx_m_1[id], idx_m_2[id]
                    #if not [idx_m_1[id], idx_m_2[id]] in index_m and not [[idx_m_1[id], idx_m_2[id]]] in sol['matrix_tip'] and r_f >= set['R_min']: #and r_f <= set['R_max'] + numpy.sqrt(set['error']):
                    #    index_m.append([idx_m_1[id], idx_m_2[id]])
            del idx_m_1
            del idx_m_2
            #for dot in index_m:
            #    m[dot[0],dot[1]] = 1
            #print len(index_m)
            
            
            '''Randomly spotted in right area
            for tt in range(0,10000):
                idx_m_1 = random.sample(range(221,402,2),80)
                idx_m_2 = random.sample(range(101,402,2),80)
                for id in range(0,len(idx_m_1)):
                    r_f = numpy.sqrt((idx_m_1[id]*set['Hh']-O_x)**2 + (idx_m_2[id]*set['Hh']-O_y)**2)
                    if not [idx_m_1[id], idx_m_2[id]] in index_m and r_f >= set['R_min'] and r_f <= set['R_max'] + numpy.sqrt(set['error']):
                        index_m.append([idx_m_1[id], idx_m_2[id]])
            del idx_m_1
            del idx_m_2
            for dot in index_m:
                m[dot[0],dot[1]] = 1
            print len(index_m)
            Randomly spotted in right area'''
            
            '''
            for y in range(0, set['Ny'],2):
                for x in range(221, set['Nx'],2):
                    r_f = numpy.sqrt((x*set['Hh']-O_x)**2 + (y*set['Hh']-O_y)**2)
                    if r_f >= set['R_min'] and r_f <= set['R_max'] + numpy.sqrt(set['error']):
                        index_m.append([x,y])
                        m[x,y] = 1
            '''
         
        print 'initial tips:', sol['matrix_tip']
        '''Initial Tips'''

            
    return sol
    