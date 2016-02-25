#import continuous_run as cont

def movement_dir(x_pos = 0, y_pos = 0, cc = 0, ff = 0,
                 tep = 0, h1 = 0, R_min = 0, error = 0,
                 d_n1 = 0, ki_n1 = 0, al_n1 = 0, ro1 = 0,
                 n_x = 0, n_y = 0, Matrix_tip = 0):

    la = tep/(h1**2)
    h2 = h1/2

    vvx = 0.5/h1*(cc[x_pos+1,y_pos+1]-cc[x_pos-1,y_pos+1]+cc[x_pos+1,y_pos-1]-cc[x_pos-1,y_pos-1])
    vvy = 0.5/h1*(cc[x_pos+1,y_pos+1]+cc[x_pos-1,y_pos+1]-cc[x_pos+1,y_pos-1]-cc[x_pos-1,y_pos-1])
    
    wwx = 0.5/h1*(ff[x_pos+1,y_pos+1]-ff[x_pos-1,y_pos+1]+ff[x_pos+1,y_pos-1]-ff[x_pos-1,y_pos-1])
    wwy = 0.5/h1*(ff[x_pos+1,y_pos+1]+ff[x_pos-1,y_pos+1]-ff[x_pos+1,y_pos-1]-ff[x_pos-1,y_pos-1])
    
    vvx_p = max(0,vvx)
    vvx_n = max(0,-vvx)
    vvy_p = max(0,vvy)
    vvy_n = max(0,-vvy)
    
    wwx_p = max(0,wwx)
    wwx_n = max(0,-wwx)
    wwy_p = max(0,wwy)
    wwy_n = max(0,-wwy)
    
    P_1 = la*d_n1+la*h1*ki_n1/(1+al_n1*cc[x_pos-1,y_pos+1])*vvx_n + la*h1*ro1*wwx_n
    P_2 = la*d_n1+la*h1*ki_n1/(1+al_n1*cc[x_pos+1,y_pos+1])*vvx_p + la*h1*ro1*wwx_p
    
    P_3 = la*d_n1+la*h1*ki_n1/(1+al_n1*cc[x_pos+1,y_pos-1])*vvy_n + la*h1*ro1*wwy_n
    P_4 = la*d_n1+la*h1*ki_n1/(1+al_n1*cc[x_pos+1,y_pos+1])*vvy_p + la*h1*ro1*wwy_p
    
    if P_1 < 0 or P_2 < 0 or P_3 < 0 or P_4 < 0:
        print 'ADA P yang Negative'
    
    '''Boundary on the inner circle'''
    O_x = n_x/2*h2
    O_y = n_y/2*h2
    r_f = (x_pos*h2-O_x)**2 + (y_pos*h2-O_y)**2
    Pos = (x_pos,y_pos)
    
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
    '''Using Non-reflection Boundary'''
            
    P_0 = 1-(P_1+P_2+P_3+P_4)
    R_0 = P_0
    R_1 = P_0+P_1
    R_2 = P_0+P_1+P_2
    R_3 = P_0+P_1+P_2+P_3
    R_4 = 1
    
    prob_range = [R_0,R_1,R_2,R_3,R_4]
    print 'probability P', P_0, ',',P_1,',',P_2,',',P_3,',',P_4
    return prob_range;

def discrete_1_iter(iter = 0, hh = 0, Nx = 0, Ny = 0,
                    r_min = 0, r_max = 0,
                    ro = 0, d_n = 0, d_c = 0, ki_n = 0, al_n = 0, nu = 0, be = 0, ga = 0,
                    matrix_tip = 0, list_last_movement = 0, 
                    list_tip_movement = 0, life_time_tip = 0,
                    stop_iter = 0, sp_stop = 0,
                    n = 0, c = 0, f = 0, tp = 0,
                    t_branch = 0,
                    Error = 0):

    import numpy
    import random
    from random import randint
    h2 = 2*hh
    O_x = Nx/2*hh
    O_y = Ny/2*hh
    
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
        list_last_movement = []
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
                    list_last_movement.append('start') #last tip movement
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
                    list_last_movement.append('start') #last tip movement
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
                    list_last_movement.append('start') #last tip movement
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
                    list_last_movement.append('start') #last tip movement
                    list_tip_movement.append('start') #movement tip
                    life_time_tip.append(0) #lifetime
                    u = 10
            else:
                u = 2           
            x += u
         
        print 'initial tips:', matrix_tip
        '''Initial Tips'''

    '''1. Anastomosis''' #not yet
    sp_new_stop =[]
    for noms in range(0,len(matrix_tip)):         
        if not noms in sp_stop:
#            '''1.1 Checking if looping itself'''
#            if not globals()['tip%s' % noms] == 'stay':
#                gg = globals()['sp%s' % noms][:]
#                gg.pop()
##                gg = list(set(gg))    
#                if len(gg) > 0: #mencegah start masuk ke bagian ini
#                    if globals()['sp%s' % noms][-1] in gg:
#                        sp_new_stop.append(noms)
#                        print 'looping itself for tip number', noms
#                        print 'looping to position', globals()['sp%s' % noms][-1]
#                #kalau < = 0, artinya baru start iterasi
#            #kalau 'stay', artinya aman. do nothing. done looping itself
            '''1.2 Checking if hit another sprout'''
            if noms in sp_new_stop or len(matrix_tip) == 1: #kalau sudah looping itself, gak usah cek hit others lg.
                pass
            elif not list_last_movement[noms] == 'stay':
                #making list of others
                other_tips = range(0,len(matrix_tip))
                other_tips.remove(noms)
                for i in other_tips:
                    if matrix_tip[noms][-1] in matrix_tip[i]:
                        sp_new_stop.append(noms)
                        print 'anastomosis for tip number ', noms, ' to tip number ', i 
                        print 'anastomosis at position', matrix_tip[noms][-1]
                    #kalau gak hit, do nothing
    '''1.3 Checking if two tips meet at one point'''
    if len(sp_new_stop) >= 2:
        pair = [(0,0)]
        for j in sp_new_stop:
            other_tips = []
            for uu in sp_new_stop:
                other_tips.append(uu)
            other_tips.remove(j)
            for i in other_tips:
                if matrix_tip[j][-1] == matrix_tip[i][-1]:
                    jjj = (j,i)
                    if reversed(jjj) in pair:
                        lop = 1
                    else:
                        pair.append((j,i))
        pair.remove((0,0))
        if len(pair) >= 1:
            for j in range(1,len(pair)):
                if not pair[j][0] in sp_new_stop:
                    sp_new_stop.remove(pair[j][0])         
    sp_stop.extend(sp_new_stop)
    sp_stop = list(set(sp_stop))
    for noms in range(0,len(matrix_tip)):
        if not noms in sp_stop:
            for i in range(0,len(matrix_tip[noms])):
                if matrix_tip[noms][i][1] == Nx-1:
                    sp_stop.append(noms)
    for i in sp_stop:
        list_last_movement[i] = 'stop'
    print 'check 1'
    
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
                dirr = movement_dir(x_pos = xb, y_pos = yb, cc = c, ff = f, 
                                    tep = tp, h1 = h2, R_min = r_min, error = Error,
                                    d_n1 = d_n, ki_n1 = ki_n, al_n1 = al_n, ro1 = ro,
                                    n_x = Nx, n_y = Ny, Matrix_tip = matrix_tip)
                print 'check 2'

                '''2.1 Branching Decision''' 
                if life_time_tip[nom] >= t_branch: #being able to branch by life time               
                    #probabilty of branching
#                    print 'NILAI C', c[xb+1,yb+1]
                    if c[xb+1,yb+1] >= 0 and c[xb+1,yb+1] < 0.1:
                        prob_weight = 2 # set the number to select here.
                        list_prob = random.sample(line, prob_weight) #list of selected numbers from line
                    elif c[xb+1,yb+1] >= 0.1 and c[xb+1,yb+1] < 0.2:
                        prob_weight = 3 # set the number to select here.
                        list_prob = random.sample(line, prob_weight)   
                    elif c[xb+1,yb+1] >= 0.2 and c[xb+1,yb+1] < 0.3:
                        prob_weight = 4 # set the number to select here.
                        list_prob = random.sample(line, prob_weight)  
                    elif c[xb+1,yb+1] >= 0.3: #do branching
                        list_prob = line
                    else: #no branching or in the condition: c[xb+1,yb+1,k+1] < 0.3
                        list_prob = [20]
                else: #not branchable
                    list_prob = [20]
                #apakah branching? meaning masuk dalam probability of branching?
                tes = randint(1,10) #select integer number randomly between 1 and 10
                print 'check 3'
                if tes in list_prob:#do branching
                    '''2.1.1 Branching tip's movement: 1st tip movement: nom tip'''
                    '''2.1.1.1 Checking no back and stay movement'''
                    no1_back = list_tip_movement[nom]
                    no_back = list_tip_movement[nom]
                    while no_back == list_tip_movement[nom]:
                        trial = random.uniform(0,1)
                        if trial <= dirr[0]: #stay
                            no_back = list_tip_movement[nom] #karna branching, dia harus move
                        elif trial <= dirr[1]: #left
                            no_back = 'right'
                        elif trial <= dirr[2]: #right
                            no_back = 'left'
                        elif trial <= dirr[3]: #down
                            no_back = 'up'
                        else: #>dirr[3] #up
                            no_back = 'down'
                    #movement 1st tip
                    if no_back == 'right':
                        tip_1 = 'left'
                        xpos_new = matrix_tip[nom][-1][0] - 2
                        ypos_new = matrix_tip[nom][-1][1]
                        matrix_tip[nom].append((xpos_new,ypos_new))
                    elif no_back == 'left':
                        tip_1 = 'right'
                        xpos_new = matrix_tip[nom][-1][0] + 2
                        ypos_new = matrix_tip[nom][-1][1]
                        matrix_tip[nom].append((xpos_new,ypos_new))
                    elif no_back == 'up':
                        tip_1 = 'down'
                        xpos_new = matrix_tip[nom][-1][0]
                        ypos_new = matrix_tip[nom][-1][1] - 2
                        matrix_tip[nom].append((xpos_new,ypos_new))
                    else:
                        tip_1 = 'up'
                        xpos_new = matrix_tip[nom][-1][0]
                        ypos_new = matrix_tip[nom][-1][1] + 2
                        matrix_tip[nom].append((xpos_new,ypos_new))
                    n[xpos_new,ypos_new] = 1
                    
                    '''2.1 Branhcing'''
                    print 'check 4'
                    matrix_tip.append([(xb,yb)])
                    #waktunya diriset
                    life_time_tip.append(0)
                    life_time_tip[nom] = 0
                    
                    '''2.1.2 Branching tip's movement: 2nd tip movement : num_sp tip'''
                    '''2.1.2.1 Checking no back, tip 1, stay movement'''
                    #ada no1_back
                    #ada tip_1
                    dom = tip_1
                    while no1_back == list_tip_movement[nom] or dom == tip_1:
                        trial = random.uniform(0,1)
                        if trial <= dirr[0]:
                            dom = tip_1
                        elif trial <= dirr[1]:
                            dom = 'left'
                            no1_back = 'right'
                        elif trial <= dirr[2]:
                            dom = 'right'
                            no1_back = 'left'
                        elif trial <= dirr[3]:
                            dom = 'down'
                            no1_back = 'up'
                        else: #>dirr[3]
                            dom = 'up'
                            no1_back = 'down'
                    print 'check 5'
                    #movement 2nd tip
                    if dom == 'left':
                        xpos_new = matrix_tip[-1][-1][0] - 2
                        ypos_new = matrix_tip[-1][-1][1]
                        matrix_tip[-1].append((xpos_new,ypos_new))
                    elif dom == 'right':
                        xpos_new = matrix_tip[-1][-1][0] + 2
                        ypos_new = matrix_tip[-1][-1][1]
                        matrix_tip[-1].append((xpos_new,ypos_new))
                    elif dom == 'down':
                        xpos_new = matrix_tip[-1][-1][0]
                        ypos_new = matrix_tip[-1][-1][1] - 2
                        matrix_tip[-1].append((xpos_new,ypos_new))
                    else: #dom == 'up'
                        xpos_new = matrix_tip[-1][-1][0]
                        ypos_new = matrix_tip[-1][-1][1] + 2
                        matrix_tip[-1].append((xpos_new,ypos_new))
                    
                    n[xpos_new,ypos_new] = 1
                    
                    '''2.1.3 Renewal Some Vars'''
                    if not dom == 'stay':
                        list_tip_movement.append(dom)
                    if not tip_1 == 'stay':
                        list_tip_movement[nom] = tip_1
                    list_last_movement.append(dom)
                    list_last_movement[nom] = tip_1   
#                    life_time_tip[-1] = tp
                    
                else: #no branching
                    print 'check 6,no branch'
                    '''2.2 No Branching'''
                    '''Movement only'''
                    '''2.2.1 Checking no back movement'''
                    life_time_tip[nom] += tp
                    no_back = list_tip_movement[nom]
                    while no_back == list_tip_movement[nom]:
                        trial = random.uniform(0,1)
                        if trial <= dirr[0]: #stay
                            no_back = 'pro' #stay
                        elif trial <= dirr[1]: #left
                            no_back = 'right'
                        elif trial <= dirr[2]: #right
                            no_back = 'left'
                        elif trial <= dirr[3]: #down
                            no_back = 'up'
                        else: #>dirr[3] #up
                            no_back = 'down'
                    print 'check 7,no branch'
                    if no_back == 'pro':
                        tipp = 'stay'
#                        globals()['sp%s' % nom].append(globals()['sp%s' % nom][-1])
                    elif no_back == 'right':
                        tipp = 'left'
                        xpos_new = matrix_tip[nom][-1][0] - 2
                        ypos_new = matrix_tip[nom][-1][1]
                        matrix_tip[nom].append((xpos_new,ypos_new))
                        n[xpos_new,ypos_new] = 1
                    elif no_back == 'left':
                        tipp = 'right'
                        xpos_new = matrix_tip[nom][-1][0] + 2
                        ypos_new = matrix_tip[nom][-1][1]
                        matrix_tip[nom].append((xpos_new,ypos_new)) 
                        n[xpos_new,ypos_new] = 1
                    elif no_back == 'up':
                        tipp = 'down'
                        xpos_new = matrix_tip[nom][-1][0]
                        ypos_new = matrix_tip[nom][-1][1] - 2
                        matrix_tip[nom].append((xpos_new,ypos_new)) 
                        n[xpos_new,ypos_new] = 1
                    else:
                        tipp = 'up'
                        xpos_new = matrix_tip[nom][-1][0]
                        ypos_new = matrix_tip[nom][-1][1] + 2
                        matrix_tip[nom].append((xpos_new,ypos_new))
                        n[xpos_new,ypos_new] = 1
                    print 'check 8,no branch'    
                    '''2.2.2 Renewal Some Vars'''
                    if not tipp == 'stay':
                        list_tip_movement[nom] = tipp
                    list_last_movement[nom] = tipp  
    for i in range(0, len(matrix_tip)):
        print 'tip',i,':',matrix_tip[i]
#         print 'life time tip',i+1,':', life_time_tip[i]   
#         print 'last tip movement of tip',i+1,':', list_last_movement[i]      
    print 'List Stop Tips:', sp_stop
    print 'Total Tips:', len(matrix_tip)
    print 'Total Stop Tips:', len(sp_stop)    
    '''***BRANCHING/PY END***'''
    c_o = c
    f_o = f
    
    '''Solve c, f, p at sub lattice'''
    h3 = h2 
    for y in range(0,Ny+1,2):
        for x in range(0,Nx+1,2):
            r_f = (x*hh-O_x)**2 + (y*hh-O_y)**2
            n_bool = 0
            if r_f <= (r_min**2 + Error + hh):
                if x >= matrix_tip[2][0][0] and y >= matrix_tip[0][0][1]: #area 1
                    if n[x+1,y+1] == 1 or n[x-1,y+1] == 1 or n[x+1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool) + d_c*tp/h3**2*(c_o[x+2,y]+c_o[x,y+2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
                elif x < matrix_tip[2][0][0] and y > matrix_tip[0][0][1]: #area 2
                    if n[x-1,y+1] == 1 or n[x+1,y+1] == 1 or n[x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x-2,y]+c_o[x,y+2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
                elif x <= matrix_tip[2][0][0] and y <= matrix_tip[0][0][1]: #area 3
                    if n[x+1,y-1] == 1 or n[x-1,y+1] == 1 or n[x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x-2,y]+c_o[x,y-2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
                elif x > matrix_tip[2][0][0] and y < matrix_tip[0][0][1]: #area 4
                    if n[x+1,y+1] == 1 or n[x-1,y-1] == 1 or n[x+1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x+2,y]+c_o[x,y-2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
            elif y == 0:
                if x == 0:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n[1,1])+ d_c*tp/h3**2*(c_o[x+2,y]+c_o[x,y+2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n[1,1] - tp*ga*f_o[x,y]*n[1,1]
                elif x == Nx:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n[Nx-1,1])+ d_c*tp/h3**2*(c_o[x-2,y]+c_o[x,y+2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n[Nx-1,1] - tp*ga*f_o[x,y]*n[Nx-1,1]
                else:
                    if n[x+1,1] == 1 or n[x-1,1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]-3*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
            elif y == Ny:
                if x == 0:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n[1,Ny-1])+ d_c*tp/h3**2*(c_o[x+2,y]+c_o[x,y-2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n[1,Ny-1]
                elif x == Nx:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n[Nx-1,Ny-1])+ d_c*tp/h3**2*(c_o[x-2,y]+c_o[x,y-2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n[Nx-1,Ny-1]
                else:
                    if n[x+1,Ny-1] == 1 or n[x-1,Ny-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y-2]-3*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
            else:
                if x == 0:
                    if n[x+1,y+1] == 1 or n[x+1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x+2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
                elif x == Nx:
                    if n[x-1,y+1] == 1 or n[x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
                else:
                    if n[x+1,y+1] == 1 or n[x-1,y+1] == 1 or n[x+1,y-1] == 1 or n[x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-4*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool

    ty = tp
    gg = [matrix_tip, list_last_movement, list_tip_movement, life_time_tip, stop_iter, sp_stop, n, c, f, ty]
    
    return gg
    