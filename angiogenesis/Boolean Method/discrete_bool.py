#import continuous_run as cont

def movement_dir(h1 = 0.005,d = 0.00035,ki = 0.38,al = 0.6,ro1 = 0,
                 tep = 0.001, X = 1,Y = 1,
                 x_pos = 0, y_pos = 0, cc = 0, ff = 0):
    la = tep/(h1**2)
    hh = h1/2
    Nx = int(X/hh)
    Ny = int(Y/hh)
    
    
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
    
    P_1 = la*d+la*h1*ki/(1+al*0.5*(cc[x_pos-1,y_pos+1]+cc[x_pos-1,y_pos-1]))*vvx_n + la*h1*ro1*wwx_n
    P_2 = la*d+la*h1*ki/(1+al*0.5*(cc[x_pos+1,y_pos+1]+cc[x_pos+1,y_pos-1]))*vvx_p + la*h1*ro1*wwx_p
    
    P_3 = la*d+la*h1*ki/(1+al*0.5*(cc[x_pos+1,y_pos+1]+cc[x_pos-1,y_pos+1]))*vvy_n + la*h1*ro1*wwy_n
    P_4 = la*d+la*h1*ki/(1+al*0.5*(cc[x_pos+1,y_pos-1]+cc[x_pos-1,y_pos-1]))*vvy_p + la*h1*ro1*wwy_p
    
    
    '''Boundary'''
#     '''Using reflection on the boundary'''
#     if y_pos == 1: #batas bawah
#         P_4 +=P_3
#         if x_pos == 1: #pojok kiri bawah
#             P_2 += P_1
#             P_1 = 0
#             P_3 = 0
#         elif x_pos == Nx-1: #pojok kanan bawah
#             P_1 += P_2
#             P_2 = 0
#             P_3 = 0
#         else: #batas bawah selain pojok
#             P_3 = 0
#     elif y_pos == Ny-1: #batas atas
#         P_3 += P_4
#         if x_pos == 1: #pojok kiri atas
#             P_2 += P_1
#             P_1 = 0
#             P_4 = 0
#         elif x_pos == Nx-1: #pojok kanan atas
#             P_1 += P_2
#             P_2 = 0
#             P_4 = 0
#         else: #batas atas selain pojok
#             P_4 = 0
#     else: #selain batas bawah dan atas
#         if x_pos == 1: #batas kiri selain pojok
#             P_2 += P_1
#             P_1 = 0
#         elif x_pos == Nx-1: #batas kanan selain pojok
#             P_1 += P_2
#             P_2 = 0
#         #selain batas2, tetap pada nilai P_1 ~ P_4 awal saja
#     '''Using reflection on the boundary'''
            
    '''Using Non-reflection Boundary'''
    if y_pos == 1: #batas bawah
        P_3 = 0
        if x_pos == 1: #pojok kiri bawah
            P_1 = 0
        elif x_pos == Nx-1: #pojok kanan bawah
            P_2 = 0
    elif y_pos == Ny-1: #batas atas
        P_4 = 0
        if x_pos == 1: #pojok kiri atas
            P_1 = 0
        elif x_pos == Nx-1: #pojok kanan atas
            P_2 = 0
    else: #selain batas bawah dan atas
        if x_pos == 1: #batas kiri selain pojok
            P_1 = 0
        elif x_pos == Nx-1: #batas kanan selain pojok
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
#    print 'probability P', P_0, ',',P_1,',',P_2,',',P_3,',',P_4
    return prob_range;



def discrete_1_iter(d = 0.00035,ki = 0.38,al = 0.6,ro = 0,
                     nu = 0.1,be = 0.05,ga = 0.1,e = 0.45,X = 1,Y = 1,
                     h2 = 0.005,tp = 0.001,iter = 0, number_of_tip = 6,
                     n = 0, c = 0, f = 0,
                     matrix_tip = 0, list_last_movement = 0, 
                     list_tip_movement = 0, life_time_tip = 0,
                     stop_iter = 0, sp_stop = 0, t_branch = 0.25):
    import numpy
    import math as m
    import random
    from random import randint
    hh = h2/2
    Nx = int(X/hh)
    Ny = int(Y/hh)
    
    if iter == 1:     
        c = numpy.zeros((Nx+1,Ny+1))
        f = numpy.zeros((Nx+1,Ny+1))
        c_prof_2 = False
        if c_prof_2 == True:
            viu = (m.sqrt(5)-0.1)/(m.sqrt(5)-1)
            for y in range(0,Ny+1,2):
                for x in range(0,Nx+1,2):
                    r_c = m.sqrt((x*hh-1)**2+(y*hh-0.5)**2)
                    if r_c >= 0.1:
                        c[x,y] = (viu-r_c)**2/(viu-0.1)**2
                    elif r_c>=0 and r_c<0.1:
                        c[x,y] = 1
                    f[x,y] = 0.75*m.exp(-(x*hh)**2/e)
        else:
            for y in range(0,Ny+1,2):
                for x in range(0,Nx+1,2):
                    c[x,y] = m.exp(-(1-x*hh)**2/e)
                    f[x,y] = 0.75*m.exp(-(x*hh)**2/e)
               
        matrix_tip = []
        list_last_movement = []
        list_tip_movement = []
        life_time_tip = []
        sp_stop = []
        n = numpy.zeros((Nx+1,Ny+1))
        for y in range(1,Ny,2):
            for x in range(1,Nx,2):
#                 n[x,y] = m.exp(-(x*hh)**2/0.001)*(m.sin(number_of_tip*m.pi*y*hh))**2
                n[x,y] = m.exp(-(x*hh)**2/0.001)*(m.sin(number_of_tip*m.pi*y*hh))**2
                
        '''Initial Tips'''
        split = int(Nx/number_of_tip)
        aw = 0
        index_tip = []
        for i in range(1,number_of_tip+1):
            jj = i*split
            ar = []
            for u in range(aw,jj+1):
                ar.append(n[1,u])
            m = max(ar)
            for i in range(0,len(ar)):
                if len(index_tip)>0:
                    tess = i+aw-index_tip[-1]
                    if ar[i] == m and tess>2:
                        index_tip.append(i+aw)
                else:
                    if ar[i] == m:
                        index_tip.append(i+aw)
            aw = jj+1
        print 'Initial Tip:', index_tip
        n = numpy.zeros((Nx+1,Ny+1))
        for i,y in enumerate(index_tip):
            matrix_tip.append([(1,y)]) #real time position
            n[i,y] = 1
            list_last_movement.append('start') #last tip movement
            list_tip_movement.append('start') #movement tip
            life_time_tip.append(0) #lifetime
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
                dirr = movement_dir(x_pos = xb, y_pos = yb, cc = c, ff = f, tep = tp, h1 = h2, ro1 = ro) # get list of prob_range
                
                '''2.1 Branching Decision''' 
                if life_time_tip[nom] >= t_branch: #being able to branch by life time               
                    #probabilty of branching
#                    print 'NILAI C', c[xb+1,yb+1]
                    if c[xb+1,yb+1] >= 0.3 and c[xb+1,yb+1] < 0.5:
                        prob_weight = 2 # set the number to select here.
                        list_prob = random.sample(line, prob_weight) #list of selected numbers from line
                    elif c[xb+1,yb+1] >= 0.5 and c[xb+1,yb+1] < 0.7:
                        prob_weight = 3 # set the number to select here.
                        list_prob = random.sample(line, prob_weight)   
                    elif c[xb+1,yb+1] >= 0.7 and c[xb+1,yb+1] < 0.8:
                        prob_weight = 4 # set the number to select here.
                        list_prob = random.sample(line, prob_weight)  
                    elif c[xb+1,yb+1] >= 0.8: #do branching
                        list_prob = line
                    else: #no branching or in the condition: c[xb+1,yb+1,k+1] < 0.3
                        list_prob = [20]
                else: #not branchable
                    list_prob = [20]
                #apakah branching? meaning masuk dalam probability of branching?
                tes = randint(1,10) #select integer number randomly between 1 and 10
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
                        
                    '''2.2.2 Renewal Some Vars'''
                    if not tipp == 'stay':
                        list_tip_movement[nom] = tipp
                    list_last_movement[nom] = tipp  
    for i in range(0, len(matrix_tip)):
        print 'tip',i+1,':',matrix_tip[i]
#         print 'life time tip',i+1,':', life_time_tip[i]   
#         print 'last tip movement of tip',i+1,':', list_last_movement[i]      
    print 'List Stop Tips:', sp_stop
    print 'Total Tips:', len(matrix_tip)
    print 'Total Stop Tips:', len(sp_stop)    
    '''***BRANCHING/PY END***'''
    c_o = c
    f_o = f
    
    '''Solve c, f at sub lattice'''
    for y in range(0,Ny+1,2):
        for x in range(0,Nx+1,2):
            if y == 0:
                if x == 0:
                    c[x,y] = c_o[x+2,y] - c_o[x,y] + c_o[x,y+2] - c_o[x,y] + c_o[x,y]*(1 - tp*nu*n[1,1])
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*n[1,1]
                elif x == Nx:
                    c[x,y] = c_o[x-2,y] - c_o[x,y] + c_o[x,y+2] - c_o[x,y] + c_o[x,y]*(1 - tp*nu*n[Nx-1,1])
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*n[Nx-1,1]
                else:
                    if n[x+1,1] == 1 or n[x-1,1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x+2,y] - 2*c_o[x,y] + c_o[x-2,y] + c_o[x,y+2] - c_o[x,y] + c_o[x,y]*(1 - tp*nu*n_bool)
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*n_bool
            elif y == Ny:
                if x == 0:
                    c[x,y] = c_o[x+2,y] - c_o[x,y] + c_o[x,y-2] - c_o[x,y] + c_o[x,y]*(1 - tp*nu*n[1,Ny-1])
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*n[1,Ny-1]
                elif x == Nx:
                    c[x,y] = c_o[x-2,y] - c_o[x,y] + c_o[x,y-2] - c_o[x,y] + c_o[x,y]*(1 - tp*nu*n[Nx-1,Ny-1])
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*n[Nx-1,Ny-1]
                else:
                    if n[x+1,Ny-1] == 1 or n[x-1,Ny-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x+2,y] - 2*c_o[x,y] + 2*c_o[x,y-2] - c_o[x,y]  + c_o[x-2,y] + c_o[x,y]*(1 - tp*nu*n_bool)
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*n_bool
            else:
                if x == 0:
                    if n[x+1,y+1] == 1 or n[x+1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = 2*c_o[x+2,y]-2*c_o[x,y] + c[x,y+2] - c[x,y] + c[x,y-2] + c_o[x,y]*(1 - tp*nu*n_bool)
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*n_bool
                elif x == Nx:
                    if n[x-1,y+1] == 1 or n[x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = 2*c_o[x-2,y]-2*c_o[x,y] + c[x,y+2] - c[x,y] + c[x,y-2] + c_o[x,y]*(1 - tp*nu*n_bool)
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*n_bool
                else:
                    if n[x+1,y+1] == 1 or n[x-1,y+1] == 1 or n[x+1,y-1] == 1 or n[x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x+2,y] - 2*c_o[x,y] + c[x,y+2] - c[x,y] + c[x,y-2] + c_o[x-2,y] + c_o[x,y]*(1 - tp*nu*n_bool)
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*n_bool
    
    
    gg = [matrix_tip, list_last_movement, list_tip_movement, life_time_tip, stop_iter, sp_stop, n, c, f, 0.001]
    
    return gg
    