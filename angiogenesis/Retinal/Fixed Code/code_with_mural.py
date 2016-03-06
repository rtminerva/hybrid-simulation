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

def discrete_1_iter(iter = 0, hh = 0, Nx = 0, Ny = 0,
                    r_min = 0, r_max = 0,
                    ro = 0, d_n = 0, ki_n = 0, al_n = 0,
                    kappa = 0, mic = 0,
                    d_c = 0, nu = 0,
                    be = 0, ga = 0,
                    d_m = 0, ki_m = 0, al_m = 0, #ro_m = 0,
                    a_p = 0, b_p = 0, dl = 0,
                    matrix_tip = 0,
                    list_tip_movement = 0, life_time_tip = 0,
                    stop_iter = 0, sp_stop = 0,
                    n = 0, c = 0, f = 0, tp = 0, m = 0, p = 0, #index_m = 0,
                    t_branch = 0,
                    Error = 0, Rec = 0, index_mn = 0):
                    
    import numpy
    import random
    from random import randint
    h2 = 2*hh
    O_x = Nx/2*hh
    O_y = Ny/2*hh
    
    fake = numpy.zeros((Nx+1,Ny+1))
    
    '''Define Initial Profile'''
    if iter == 1:
        c = numpy.zeros((Nx+1,Ny+1))
        f = numpy.zeros((Nx+1,Ny+1))
        
        for y in range(0,Ny+1,2):
            for x in range(0,Nx+1,2):
                r_f = numpy.sqrt((x*hh-O_x)**2 + (y*hh-O_y)**2)
                if r_f >= r_min + numpy.sqrt(Error):
                    c[x,y] = 0.5-0.45*numpy.exp(-(r_f**2)/0.45)
                    f[x,y] = 0.5
                    #f[x,y] = 0.5-0.45*numpy.exp(-(r_max-r_f)**2/0.45) 
        
        matrix_tip = []
        list_tip_movement = []
        life_time_tip = []
        sp_stop = []
                        
        ''''Initial Tips'''
        n = numpy.zeros((Nx+1,Ny+1))
        
        y1 = Ny/2 + 1
        x = 1
        while x < Nx+1:
            if (x*hh-O_x)**2 + (y1*hh-O_y)**2 < r_min**2 + Error and (x*hh-O_x)**2 + (y1*hh-O_y)**2 > r_min**2:
                    matrix_tip.append([(x,y1)])
                    n[x,y1] = 1
                    list_tip_movement.append('start') #movement tip
                    life_time_tip.append(0) #lifetime
                    u = 10
            else:
                u = 2           
            x += u
            
        y1 = Nx/2 + 1
        x = 1
        while x < Nx+1:
            if (x*hh-O_x)**2 + (y1*hh-O_y)**2 < r_min**2 + Error and (x*hh-O_x)**2 + (y1*hh-O_y)**2 > r_min**2:
                    matrix_tip.append([(y1,x)])
                    n[y1,x] = 1
                    list_tip_movement.append('start') #movement tip
                    life_time_tip.append(0) #lifetime
                    u = 10
            else:
                u = 2           
            x += u
                 
        y1 = matrix_tip[2][0][0] + (matrix_tip[1][0][0]- matrix_tip[2][0][0])/2
        if y1 % 2 == 0:
            y1 += 1
        x = 1
        while x < Nx+1:
            if (x*hh-O_x)**2 + (y1*hh-O_y)**2 < r_min**2 + Error and (x*hh-O_x)**2 + (y1*hh-O_y)**2 > r_min**2:
                    matrix_tip.append([(y1,x)])
                    n[y1,x] = 1
                    list_tip_movement.append('start') #movement tip
                    life_time_tip.append(0) #lifetime
                    u = 10
            else:
                u = 2           
            x += u
                    
        y1 = matrix_tip[0][0][0] + (matrix_tip[2][0][0]-matrix_tip[0][0][0])/2
        if y1 % 2 == 0:
            y1 += 1
        x = 1
        while x < Nx+1:
            if (x*hh-O_x)**2 + (y1*hh-O_y)**2 < r_min**2 + Error and (x*hh-O_x)**2 + (y1*hh-O_y)**2 > r_min**2:
                    matrix_tip.append([(y1,x)])
                    n[y1,x] = 1
                    list_tip_movement.append('start') #movement tip
                    life_time_tip.append(0) #lifetime
                    u = 10
            else:
                u = 2           
            x += u
        
        if not mic == 0 or not kappa == 0:
            #index_m = []
            index_mn = []
            m = numpy.zeros((Nx+1,Ny+1))
            p = numpy.zeros((Nx+1,Ny+1))
            
            '''Randomly spotted in domain'''
            for tt in range(0,250):
                idx_m_1 = random.sample(range(1,440,2),100)
                idx_m_2 = random.sample(range(1,440,2),100)
                for id in range(0,len(idx_m_1)):
                    r_f = numpy.sqrt((idx_m_1[id]*hh-O_x)**2 + (idx_m_2[id]*hh-O_y)**2)
                    if not m[idx_m_1[id], idx_m_2[id]] == 1 and not [[idx_m_1[id], idx_m_2[id]]] in matrix_tip and r_f >= r_min:
                        m[idx_m_1[id], idx_m_2[id]] = 1

                        #print idx_m_1[id], idx_m_2[id]
                    #if not [idx_m_1[id], idx_m_2[id]] in index_m and not [[idx_m_1[id], idx_m_2[id]]] in matrix_tip and r_f >= r_min: #and r_f <= r_max + numpy.sqrt(Error):
                    #    index_m.append([idx_m_1[id], idx_m_2[id]])
            del idx_m_1
            del idx_m_2
            #for dot in index_m:
            #    m[dot[0],dot[1]] = 1
            #print len(index_m)
            '''Randomly spotted in domain'''
            
            '''Randomly spotted in right area
            for tt in range(0,10000):
                idx_m_1 = random.sample(range(221,402,2),80)
                idx_m_2 = random.sample(range(101,402,2),80)
                for id in range(0,len(idx_m_1)):
                    r_f = numpy.sqrt((idx_m_1[id]*hh-O_x)**2 + (idx_m_2[id]*hh-O_y)**2)
                    if not [idx_m_1[id], idx_m_2[id]] in index_m and r_f >= r_min and r_f <= r_max + numpy.sqrt(Error):
                        index_m.append([idx_m_1[id], idx_m_2[id]])
            del idx_m_1
            del idx_m_2
            for dot in index_m:
                m[dot[0],dot[1]] = 1
            print len(index_m)
            Randomly spotted in right area'''
            
            '''
            for y in range(0, Ny,2):
                for x in range(221, Nx,2):
                    r_f = numpy.sqrt((x*hh-O_x)**2 + (y*hh-O_y)**2)
                    if r_f >= r_min and r_f <= r_max + numpy.sqrt(Error):
                        index_m.append([x,y])
                        m[x,y] = 1
            '''
            ''
         
        print 'initial tips:', matrix_tip
        '''Initial Tips'''

    '''1. Anastomosis''' #not yet
    #creating list of tips to be checked if the tip meets
    sp_in = []
    for noms in range(0,len(matrix_tip)):         
        if not noms in sp_stop:
            sp_in.append(noms)
    for tip_o in sp_in:
        for tips in sp_in:
            if tips > tip_o:
                if matrix_tip[tip_o][-1] == matrix_tip[tips][-1]:
                    sp_stop.append(tip_o)
                    list_tip_movement[tip_o] = 'stop'
    '''2. Branching and Movement'''        
    if len(sp_stop) == len(matrix_tip):
        stop_iter = 100000 #sp_stop harus dicek di setiap movement and branching. karena sudah tidak bergerak lagi yang ada di list ini.
        print 'all looping itself or anastomosis'
    else:    
        ##branching decision and action. Also movement   
        line = range(1,11) #for Pb
        n_sp = len(matrix_tip) #to save original number of tips before branching
        
        for nom in range(0,n_sp): #dicek setiap tip
            if nom in sp_stop: #kalo dia sudah anastomosis, gak perlu branching dan move lg.
#                 print 'no_moving for tip', nom
                pass
            else:
                xb = matrix_tip[nom][-1][0] #get x position of last tip position
                yb = matrix_tip[nom][-1][1] #get y position of last tip position
                #print 'xb,yb', xb,',',yb
                dirr = movement_dir(x_pos = xb, y_pos = yb, cc = c, ff = f, mm = m,
                                    tep = tp, h1 = h2, R_min = r_min, error = Error,
                                    d_n1 = d_n, ki_n1 = ki_n, al_n1 = al_n, ro1 = ro, Mic = mic, Kappa = kappa,
                                    n_x = Nx, n_y = Ny, Matrix_tip = matrix_tip, Nom = nom)
                dirr1 = [dirr[0],dirr[0]+dirr[1],dirr[0]+dirr[1]+dirr[2],dirr[0]+dirr[1]+dirr[2]+dirr[3],1]
                #print dirr                
                no_back = list_tip_movement[nom]
                k = 0
                while no_back == list_tip_movement[nom]:
                    trial = random.uniform(0,1)
                    if trial <= dirr1[0]: #stay
                        no_back = 'pro' #stay
                    elif trial <= dirr1[1]: #left
                        no_back = 'right'
                    elif trial <= dirr1[2]: #right
                        no_back = 'left'
                    elif trial <= dirr1[3]: #down
                        no_back = 'up'
                    else: #>dirr1[3] #up
                        no_back = 'down'
                    k += 1
                    if k >= 100:
                        print 'Error code 1 here'
                #print 'check 1'
                if no_back == 'pro':
                    tipp = 'stay'
                elif no_back == 'right':
                    tipp = 'left'
                    xpos_new = matrix_tip[nom][-1][0] - 2
                    ypos_new = matrix_tip[nom][-1][1]
                    matrix_tip[nom].append((xpos_new,ypos_new))
                    n[xpos_new,ypos_new] = 1
                    list_tip_movement[nom] = tipp
                elif no_back == 'left':
                    tipp = 'right'
                    xpos_new = matrix_tip[nom][-1][0] + 2
                    ypos_new = matrix_tip[nom][-1][1]
                    matrix_tip[nom].append((xpos_new,ypos_new)) 
                    n[xpos_new,ypos_new] = 1
                    list_tip_movement[nom] = tipp
                elif no_back == 'up':
                    tipp = 'down'
                    xpos_new = matrix_tip[nom][-1][0]
                    ypos_new = matrix_tip[nom][-1][1] - 2
                    matrix_tip[nom].append((xpos_new,ypos_new)) 
                    n[xpos_new,ypos_new] = 1
                    list_tip_movement[nom] = tipp
                else:
                    tipp = 'up'
                    xpos_new = matrix_tip[nom][-1][0]
                    ypos_new = matrix_tip[nom][-1][1] + 2
                    matrix_tip[nom].append((xpos_new,ypos_new))
                    n[xpos_new,ypos_new] = 1
                    list_tip_movement[nom] = tipp
                '''2.1 Branching Decision'''
                if not tipp == 'stay':
                    if dirr[5] == 'stop' and tipp == 'left':
                        sp_stop.append(nom)
                    if dirr[6] == 'stop' and tipp == 'right':
                        sp_stop.append(nom)
                    if dirr[7] == 'stop' and tipp == 'down':
                        sp_stop.append(nom)
                    if dirr[8] == 'stop' and tipp == 'up':
                        sp_stop.append(nom)
                    if life_time_tip[nom] >= t_branch: #being able to branch by life time               
                        #probabilty of branching
    #                    print 'NILAI C', c[xb+1,yb+1]
                        if c[xb+1,yb+1] >= 0 and c[xb+1,yb+1] < 0.1:
                            prob_weight = 7 # set the number to select here.
                            list_prob = random.sample(line, prob_weight) #list of selected numbers from line
                        elif c[xb+1,yb+1] >= 0.05 and c[xb+1,yb+1] < 0.2:
                            prob_weight = 8 # set the number to select here.
                            list_prob = random.sample(line, prob_weight)   
                        elif c[xb+1,yb+1] >= 0.2 and c[xb+1,yb+1] < 0.3:
                            prob_weight = 9 # set the number to select here.
                            list_prob = random.sample(line, prob_weight)  
                        elif c[xb+1,yb+1] >= 0.3: #do branching
                            list_prob = line
                        #apakah branching? meaning masuk dalam probability of branching?
                        tes = randint(1,10) #select integer number randomly between 1 and 10
                        #print 'check 3'
                        if tes in list_prob:#do branching
                            '''2.1 Branhcing'''
                            life_time_tip[nom] = 0
                            
                            matrix_tip.append([(xb,yb)])
                            life_time_tip.append(0)
                            list_tip_movement.append('start')

                            dom = tipp #other movement
                            no_back = list_tip_movement[-1]
                 #           print 'check 2'
                            k = 0
                            while no_back == list_tip_movement[-1] or dom == tipp:
                                trial = random.uniform(0,1)
                                if trial <= dirr1[0]: #stay
                                    no_back = 'pro' #stay
                                    dom = 'pro'
                                elif trial <= dirr1[1]: #left
                                    no_back = 'right'
                                    dom = 'left'
                                elif trial <= dirr1[2]: #right
                                    no_back = 'left'
                                    dom = 'right'
                                elif trial <= dirr1[3]: #down
                                    no_back = 'up'
                                    dom = 'down'
                                else: #>dirr1[3] #up
                                    no_back = 'down'
                                    dom = 'up'
                                k += 1
                                if k >= 100:
                                    print 'Error code 2 here'
                            #print 'check 3'
                            if no_back == 'pro':
                                tipp = 'stay'
                            elif no_back == 'right':
                                tipp = 'left'
                                xpos_new = matrix_tip[-1][-1][0] - 2
                                ypos_new = matrix_tip[-1][-1][1]
                                matrix_tip[nom].append((xpos_new,ypos_new))
                                n[xpos_new,ypos_new] = 1
                                list_tip_movement[-1] = tipp
                            elif no_back == 'left':
                                tipp = 'right'
                                xpos_new = matrix_tip[-1][-1][0] + 2
                                ypos_new = matrix_tip[-1][-1][1]
                                matrix_tip[nom].append((xpos_new,ypos_new)) 
                                n[xpos_new,ypos_new] = 1
                                list_tip_movement[-1] = tipp
                            elif no_back == 'up':
                                tipp = 'down'
                                xpos_new = matrix_tip[-1][-1][0]
                                ypos_new = matrix_tip[-1][-1][1] - 2
                                matrix_tip[nom].append((xpos_new,ypos_new)) 
                                n[xpos_new,ypos_new] = 1
                                list_tip_movement[-1] = tipp
                            else:
                                tipp = 'up'
                                xpos_new = matrix_tip[-1][-1][0]
                                ypos_new = matrix_tip[-1][-1][1] + 2
                                matrix_tip[nom].append((xpos_new,ypos_new))
                                n[xpos_new,ypos_new] = 1
                                list_tip_movement[-1] = tipp
                            if not tipp == 'stay':
                                if dirr[5] == 'stop' and tipp == 'left':
                                    sp_stop.append(len(matrix_tip)-1)
                                if dirr[6] == 'stop' and tipp == 'right':
                                    sp_stop.append(len(matrix_tip)-1)
                                if dirr[7] == 'stop' and tipp == 'down':
                                    sp_stop.append(len(matrix_tip)-1)
                                if dirr[8] == 'stop' and tipp == 'up':
                                    sp_stop.append(len(matrix_tip)-1)
                        else:
                            life_time_tip[nom] += tp    
                    else: 
                        life_time_tip[nom] += tp       
                else:
                    life_time_tip[nom] += tp            
                                       
   # for i in range(0, len(matrix_tip)):
    #    print 'tip',i,':',matrix_tip[i]
#         print 'life time tip',i+1,':', life_time_tip[i]   
#         print 'last tip movement of tip',i+1,':', list_last_movement[i]      
  #  print 'List Stop Tips:', sp_stop
    print 'Total Tips:', len(matrix_tip)
    print 'Total Stop Tips:', len(sp_stop)    
    '''***BRANCHING/PY END***'''
    c_o = c[:]
    f_o = f[:]
    if not mic == 0 or not kappa == 0:
        p_o = p[:]
    
    '''Solve c, f, p at sub lattice'''
    h3 = h2 
    for y in range(0,Ny+1,2):
        for x in range(0,Nx+1,2):
            r_f = (x*hh-O_x)**2 + (y*hh-O_y)**2
            if r_f <= (r_min**2 + Error + hh):
                if x >= matrix_tip[2][0][0] and y >= matrix_tip[0][0][1]: #area 1
                    if n[x+1,y+1] == 1 or n[x-1,y+1] == 1 or n[x+1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    if not mic == 0 or not kappa == 0:
                        if m[x+1,y+1] == 1 or m[x-1,y+1] == 1 or [x+1,y-1] == 1:
                            m_bool = 1
                        else:
                            m_bool = 0
                        if Rec == 'Ang1':
                            p[x,y] = (a_p*m_bool+b_p)*n_bool*tp + p_o[x,y]*(1-dl*tp) #Ang1
                        elif Rec == 'Ang2':
                            p[x,y] = n_bool*tp/(a_p*m_bool+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                        else:
                            p[x,y] = n_bool*tp/(a_p*n_bool+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                        #if ga_change == True and Rec == 'Ang1':
                        #    ga = 
                        #elif ga_change == True and Rec == 'Ang2':
                        #    ga =
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool) + d_c*tp/h3**2*(c_o[x+2,y]+c_o[x,y+2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
                    
    
                elif x < matrix_tip[2][0][0] and y > matrix_tip[0][0][1]: #area 2
                    if n[x-1,y+1] == 1 or n[x+1,y+1] == 1 or n[x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    if not mic == 0 or not kappa == 0:
                        if m[x-1,y+1] == 1 or m[x+1,y+1] == 1 or m[x-1,y-1] == 1:
                            m_bool = 1
                        else:
                            m_bool = 0
                        if Rec == 'Ang1':
                            p[x,y] = (a_p*m_bool+b_p)*n_bool*tp + p_o[x,y]*(1-dl*tp) #Ang1
                        elif Rec == 'Ang2':
                            p[x,y] = n_bool*tp/(a_p*m_bool+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                        else:
                            p[x,y] = n_bool*tp/(a_p*n_bool+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x-2,y]+c_o[x,y+2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
                    
                        
                elif x <= matrix_tip[2][0][0] and y <= matrix_tip[0][0][1]: #area 3
                    if n[x+1,y-1] == 1 or n[x-1,y+1] == 1 or n[x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    if not mic == 0 or not kappa == 0:
                        if m[x+1,y-1] == 1 or m[x-1,y+1] == 1 or m[x-1,y-1] == 1:
                            m_bool = 1
                        else:
                            m_bool = 0
                        if Rec == 'Ang1':
                            p[x,y] = (a_p*m_bool+b_p)*n_bool*tp + p_o[x,y]*(1-dl*tp) #Ang1
                        elif Rec == 'Ang2':
                            p[x,y] = n_bool*tp/(a_p*m_bool+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                        else:
                            p[x,y] = n_bool*tp/(a_p*n_bool+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x-2,y]+c_o[x,y-2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
                    
                        
                elif x > matrix_tip[2][0][0] and y < matrix_tip[0][0][1]: #area 4
                    if n[x+1,y+1] == 1 or n[x-1,y-1] == 1 or n[x+1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    if not mic == 0 or not kappa == 0:
                        if m[x+1,y+1] == 1 or m[x-1,y-1] == 1 or m[x+1,y-1] == 1:
                            m_bool = 1
                        else:
                            m_bool = 0
                        if Rec == 'Ang1':
                            p[x,y] = (a_p*m_bool+b_p)*n_bool*tp + p_o[x,y]*(1-dl*tp) #Ang1
                        elif Rec == 'Ang2':
                            p[x,y] = n_bool*tp/(a_p*m_bool+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                        else:
                            p[x,y] = n_bool*tp/(a_p*n_bool+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x+2,y]+c_o[x,y-2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
                    
                    
            elif y == 0:
                if x == 0:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n[1,1])+ d_c*tp/h3**2*(c_o[x+2,y]+c_o[x,y+2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n[1,1] - tp*ga*f_o[x,y]*n[1,1]
                    if not mic == 0 or not kappa == 0:
                        if Rec == 'Ang1':
                            p[x,y] = (a_p*m[1,1]+b_p)*n[1,1]*tp + p_o[x,y]*(1-dl*tp) #Ang1
                        elif Rec == 'Ang2':
                            p[x,y] = n[1,1]*tp/(a_p*m[1,1]+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                        else:
                            p[x,y] = n[1,1]*tp/(a_p*n[1,1]+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                        
                elif x == Nx:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n[Nx-1,1])+ d_c*tp/h3**2*(c_o[x-2,y]+c_o[x,y+2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n[Nx-1,1] - tp*ga*f_o[x,y]*n[Nx-1,1]
                    if not mic == 0 or not kappa == 0:
                        if Rec == 'Ang1':
                            p[x,y] = (a_p*m[Nx-1,1]+b_p)*n[Nx-1,1]*tp + p_o[x,y]*(1-dl*tp) #Ang1
                        elif Rec == 'Ang2':
                            p[x,y] = n[Nx-1,1]*tp/(a_p*m[Nx-1,1]+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                        else:
                            p[x,y] = n[Nx-1,1]*tp/(a_p*n[Nx-1,1]+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                    
                else:
                    if n[x+1,1] == 1 or n[x-1,1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    if not mic == 0 or not kappa == 0:
                        if m[x+1,1] == 1 or m[x-1,1] == 1:
                            m_bool = 1
                        else:
                            m_bool = 0
                        if Rec == 'Ang1':
                            p[x,y] = (a_p*m_bool+b_p)*n_bool*tp + p_o[x,y]*(1-dl*tp) #Ang1
                        elif Rec == 'Ang2':
                            p[x,y] = n_bool*tp/(a_p*m_bool+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                        else:
                            p[x,y] = n_bool*tp/(a_p*n_bool+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]-3*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
                    
                
            elif y == Ny:
                if x == 0:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n[1,Ny-1])+ d_c*tp/h3**2*(c_o[x+2,y]+c_o[x,y-2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n[1,Ny-1]
                    if not mic == 0 or not kappa == 0:
                        if Rec == 'Ang1':
                            p[x,y] = (a_p*m[1,Ny-1]+b_p)*n[1,Ny-1]*tp + p_o[x,y]*(1-dl*tp) #Ang1
                        elif Rec == 'Ang2':
                            p[x,y] = n[1,Ny-1]*tp/(a_p*m[1,Ny-1]+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                        else:
                            p[x,y] = n[1,Ny-1]*tp/(a_p*n[1,Ny-1]+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                    
                elif x == Nx:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n[Nx-1,Ny-1])+ d_c*tp/h3**2*(c_o[x-2,y]+c_o[x,y-2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n[Nx-1,Ny-1]
                    if not mic == 0 or not kappa == 0:
                        if Rec == 'Ang1':
                            p[x,y] = (a_p*m[Nx-1,Ny-1]+b_p)*n[Nx-1,Ny-1]*tp + p_o[x,y]*(1-dl*tp) #Ang1
                        elif Rec == 'Ang2':
                            p[x,y] = n[Nx-1,Ny-1]*tp/(a_p*m[Nx-1,Ny-1]+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                        else:
                            p[x,y] = n[Nx-1,Ny-1]*tp/(a_p*n[Nx-1,Ny-1]+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                    
                else:
                    if n[x+1,Ny-1] == 1 or n[x-1,Ny-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    if not mic == 0 or not kappa == 0:
                        if m[x+1,Ny-1] == 1 or m[x-1,Ny-1] == 1:
                            m_bool = 1
                        else:
                            m_bool = 0
                        if Rec == 'Ang1':
                            p[x,y] = (a_p*m_bool+b_p)*n_bool*tp + p_o[x,y]*(1-dl*tp) #Ang1
                        elif Rec == 'Ang2':
                            p[x,y] = n_bool*tp/(a_p*m_bool+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                        else:
                            p[x,y] = n_bool*tp/(a_p*n_bool+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y-2]-3*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
                    
                        
            else:
                if x == 0:
                    if n[x+1,y+1] == 1 or n[x+1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    if not mic == 0 or not kappa == 0:
                        if m[x+1,y+1] == 1 or m[x+1,y-1] == 1:
                            m_bool = 1
                        else:
                            m_bool = 0
                        if Rec == 'Ang1':
                            p[x,y] = (a_p*m_bool+b_p)*n_bool*tp + p_o[x,y]*(1-dl*tp) #Ang1
                        elif Rec == 'Ang2':
                            p[x,y] = n_bool*tp/(a_p*m_bool+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                        else:
                            p[x,y] = n_bool*tp/(a_p*n_bool+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x+2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
                    
                elif x == Nx:
                    if n[x-1,y+1] == 1 or n[x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    if not mic == 0 or not kappa == 0:
                        if m[x-1,y+1] == 1 or m[x-1,y-1] == 1:
                            m_bool = 1
                        else:
                            m_bool = 0
                        if Rec == 'Ang1':
                            p[x,y] = (a_p*m_bool+b_p)*n_bool*tp + p_o[x,y]*(1-dl*tp) #Ang1
                        elif Rec == 'Ang2':
                            p[x,y] = n_bool*tp/(a_p*m_bool+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                        else:
                            p[x,y] = n_bool*tp/(a_p*n_bool+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
                    
                    
                else:
                    if n[x+1,y+1] == 1 or n[x-1,y+1] == 1 or n[x+1,y-1] == 1 or n[x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    if not mic == 0 or not kappa == 0:
                        if m[x+1,y+1] == 1 or m[x-1,y+1] == 1 or m[x+1,y-1] == 1 or m[x-1,y-1] == 1:
                            m_bool = 1
                        else:
                            m_bool = 0
                        if Rec == 'Ang1':
                            p[x,y] = (a_p*m_bool+b_p)*n_bool*tp + p_o[x,y]*(1-dl*tp) #Ang1
                        elif Rec == 'Ang2':
                            p[x,y] = n_bool*tp/(a_p*m_bool+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                        else:
                            p[x,y] = n_bool*tp/(a_p*n_bool+b_p) + p_o[x,y]*(1-dl*tp) #Ang2
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-4*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
                    
    '''m movement'''
    if not mic == 0 or not kappa == 0:
        mo = m[:]
        for yb in range(1,Ny,2):
            for xb in range(1,Nx,2):
                #print mo[xb,yb]
                if mo[xb,yb] == 1 and not [xb,yb] in index_mn:
                    #print mo[xb,yb]
                    dirr = movement_dir(x_pos = xb, y_pos = yb, cc = p_o, mm = m, #ff = fake,
                                        tep = tp, h1 = h2, R_min = r_min, error = Error,
                                        d_n1 = d_m, ki_n1 = ki_m, al_n1 = al_m, #ro1 = ro_m, 
                                        n_x = Nx, n_y = Ny, Matrix_tip = matrix_tip, n_dir = False)
                    dirr_m = [dirr[0],dirr[0]+dirr[1],dirr[0]+dirr[1]+dirr[2],dirr[0]+dirr[1]+dirr[2]+dirr[3],1]
                    #print dirr
                    trial = random.uniform(0,1)
                    if trial <= dirr_m[0]: #stay
                        lop = 1
                        #print 'STAY'
                        #do nothing
                    elif trial <= dirr_m[1]: #left
                        #print 'LEFT'
                        #print m[xb,yb]
                        #index_m[dot][0] = xb - 2
                        m[xb - 2, yb] = 1
                        m[xb,yb] = 0
                        #print m[xb,yb]
                        #print m[xb - 2, yb]
                    elif trial <= dirr_m[2]: #right
                        #print 'RIGHT'
                        #print m[xb,yb]
                        #index_m[dot][0] = xb + 2
                        m[xb + 2, yb] = 1
                        m[xb,yb] = 0
                        #print m[xb,yb]
                        #print m[xb + 2, yb]
                    elif trial <= dirr_m[3]: #down
                        #print 'DOWN'
                        #print m[xb,yb]
                        #index_m[dot][1] = yb - 2
                        m[xb, yb - 2] = 1
                        m[xb,yb] = 0
                        #print m[xb,yb]
                       # print m[xb, yb - 2]
                    else: #>dirr[3] #up
                        #print 'UP'
                        #print m[xb,yb]
                        #index_m[dot][1] = yb + 2
                        m[xb, yb + 2] = 1
                        m[xb,yb] = 0
                        #print m[xb,yb]
                        #print m[xb, yb + 2]
                    for ec_i in range(0,len(matrix_tip)):
                        if (xb,yb) in matrix_tip[ec_i]:
                            index_mn.append([xb,yb])
        
        '''
        index_mo = index_m[:]
        #print '#Numbers of m', len(index_m)
        for dot in range(0,len(index_mo)):
            xb = index_mo[dot][0]
            yb = index_mo[dot][1]
            if not [xb,yb] in index_mn:
                dirr = movement_dir(x_pos = xb, y_pos = yb, cc = p_o, #ff = fake,
                                      tep = tp, h1 = h2, R_min = r_min, error = Error,
                                      d_n1 = d_m, ki_n1 = ki_m, al_n1 = al_m, #ro1 = ro_m, 
                                      n_x = Nx, n_y = Ny, Matrix_tip = matrix_tip, Index_m = index_m, n_dir = False)
                dirr_m = [dirr[0],dirr[0]+dirr[1],dirr[0]+dirr[1]+dirr[2],dirr[0]+dirr[1]+dirr[2]+dirr[3],1]
                #print dirr
                trial = random.uniform(0,1)
                if trial <= dirr_m[0]: #stay
                    lop = 1
                    #print 'STAY'
                    #do nothing
                elif trial <= dirr_m[1]: #left
                    #print 'LEFT'
                    #print m[xb,yb]
                    index_m[dot][0] = xb - 2
                    m[xb - 2, yb] = 1
                    m[xb,yb] = 0
                    #print m[xb,yb]
                    #print m[xb - 2, yb]
                elif trial <= dirr_m[2]: #right
                    #print 'RIGHT'
                    #print m[xb,yb]
                    index_m[dot][0] = xb + 2
                    m[xb + 2, yb] = 1
                    m[xb,yb] = 0
                    #print m[xb,yb]
                    #print m[xb + 2, yb]
                elif trial <= dirr_m[3]: #down
                    #print 'DOWN'
                    #print m[xb,yb]
                    index_m[dot][1] = yb - 2
                    m[xb, yb - 2] = 1
                    m[xb,yb] = 0
                    #print m[xb,yb]
                   # print m[xb, yb - 2]
                else: #>dirr[3] #up
                    #print 'UP'
                    #print m[xb,yb]
                    index_m[dot][1] = yb + 2
                    m[xb, yb + 2] = 1
                    m[xb,yb] = 0
                    #print m[xb,yb]
                    #print m[xb, yb + 2]
                for ec_i in range(0,len(matrix_tip)):
                    if (index_m[dot][0],index_m[dot][1]) in matrix_tip[ec_i]:
                        index_mn.append(index_m[dot])
        '''
	'''m movement no index_m
    if not mic == 0 or not kappa == 0:
        m_o = m[:]
        for yb in range(1,Ny,2):
            for xb in range(1,Nx,2):
                if m_o[xb,yb] == 1:
                    dirr_m = movement_dir(x_pos = xb, y_pos = yb, cc = p_o, ff = fake,
                                          tep = tp, h1 = h2, R_min = r_min, error = Error,
                                          d_n1 = d_m, ki_n1 = ki_m, al_n1 = al_m, ro1 = ro_m, 
                                          n_x = Nx, n_y = Ny, Matrix_tip = matrix_tip, n_dir = False)
                    dirr_m = [dirr_m[0],dirr_m[0]+dirr_m[1],dirr_m[0]+dirr_m[1]+dirr_m[2],dirr_m[0]+dirr_m[1]+dirr_m[2]+dirr_m[3],1]
                    trial = random.uniform(0,1)
                    if trial <= dirr_m[0]: #stay
                        lop = 1
                        #do nothing
                    elif trial <= dirr_m[1]: #left
                        #print 'LEFT'
                        newx = xb - 2
                        m[newx, yb] = 1
                        m[xb,yb] = 0
                    elif trial <= dirr_m[2]: #right
                        #print 'RIGHT'
                        newx = xb + 2
                        m[newx, yb] = 1
                        m[xb,yb] = 0
                    elif trial <= dirr_m[3]: #down
                        #print 'DOWN'
                        newy = yb - 2
                        m[xb, newy] = 1
                        m[xb,yb] = 0
                    else: #>dirr[3] #up
                        #print 'UP'
                        newy = yb + 2
                        m[xb, newy] = 1
                        m[xb,yb] = 0
    m movement no index_m'''
                
    ty = tp
    gg = [matrix_tip, list_tip_movement, life_time_tip, stop_iter, sp_stop, n, c, f, ty, p, m, index_mn]
    
    return gg
    