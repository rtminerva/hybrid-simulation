#import continuous_run as cont
from sympy.physics.quantum.tests.test_sho1d import N_rep

def movement_dir(r_pos = 0, p_pos = 0, cc = 0, ff = 0, 
                 tep = 0, d_r1 = 0, d_p1 = 0, d_n1 = 0, ki_n1 = 0, al_n1 = 0, ro1 = 0, r_len1 = 0, p_len1 = 0):
    la_r = tep/((2*d_r1)**2)
    la_p = tep/((2*d_p1)**2)
    
    '''MUST FIX THIS!'''
    if p_pos == p_len1-1: # on periodic boundary  
        pp_pos = 0
        vvr = 0.5/(2*d_r1)*(cc[r_pos+1,p_pos-1]+cc[r_pos+1,pp_pos]-cc[r_pos-1,p_pos-1]-cc[r_pos-1,pp_pos])
        vvp = 0.5/(2*d_p1)*(cc[r_pos+1,p_pos-1]-cc[r_pos+1,pp_pos]+cc[r_pos-1,p_pos-1]-cc[r_pos-1,pp_pos])
        
        wwr = 0.5/(2*d_r1)*(ff[r_pos+1,p_pos-1]+ff[r_pos+1,pp_pos]-ff[r_pos-1,p_pos-1]-ff[r_pos-1,pp_pos])
        wwp = 0.5/(2*d_p1)*(ff[r_pos+1,p_pos-1]-ff[r_pos+1,pp_pos]+ff[r_pos-1,p_pos-1]-ff[r_pos-1,pp_pos])    
    else:         
        vvr = 0.5/(2*d_r1)*(cc[r_pos+1,p_pos-1]+cc[r_pos+1,p_pos+1]-cc[r_pos-1,p_pos-1]-cc[r_pos-1,p_pos+1])
        vvp = 0.5/(2*d_p1)*(cc[r_pos+1,p_pos-1]-cc[r_pos+1,p_pos+1]+cc[r_pos-1,p_pos-1]-cc[r_pos-1,p_pos+1])
        
        wwr = 0.5/(2*d_r1)*(ff[r_pos+1,p_pos-1]+ff[r_pos+1,p_pos+1]-ff[r_pos-1,p_pos-1]-ff[r_pos-1,p_pos+1])
        wwp = 0.5/(2*d_p1)*(ff[r_pos+1,p_pos-1]-ff[r_pos+1,p_pos+1]+ff[r_pos-1,p_pos-1]-ff[r_pos-1,p_pos+1])
    
    vvr_p = max(0,vvr)
    vvr_n = max(0,-vvr)
    vvp_p = max(0,vvp)
    vvp_n = max(0,-vvp)
    
    wwr_p = max(0,wwr)
    wwr_n = max(0,-wwr)
    wwp_p = max(0,wwp)
    wwp_n = max(0,-wwp)
    
    P_1 = la_r*d_n1+la_r*(2*d_r1)*ki_n1/(1+al_n1*cc[r_pos-1,p_pos+1])*vvr_n + la_r*(2*d_r1)*ro1*wwr_n
    P_2 = la_r*d_n1+la_r*(2*d_r1)*ki_n1/(1+al_n1*cc[r_pos+1,p_pos+1])*vvr_p + la_r*(2*d_r1)*ro1*wwr_p
    
    P_3 = la_p*d_n1+la_p*(2*d_p1)*ki_n1/(1+al_n1*cc[r_pos+1,p_pos-1])*vvp_n + la_p*(2*d_p1)*ro1*wwp_n
    P_4 = la_p*d_n1+la_p*(2*d_p1)*ki_n1/(1+al_n1*cc[r_pos-1,p_pos-1])*vvp_p + la_p*(2*d_p1)*ro1*wwp_p
            
    '''Using Non-reflection Boundary'''
    if r_pos == 1: # in the smallest circle
        P_1 = 0  
    elif r_pos == r_len1-1: #in the mas circle
        P_2 = 0
    '''Using Non-reflection Boundary'''
            
    P_0 = 1-(P_1+P_2+P_3+P_4)
    R_0 = P_0
    R_1 = P_0+P_1
    R_2 = P_0+P_1+P_2
    R_3 = P_0+P_1+P_2+P_3
    R_4 = 1
    
    prob_range = [R_0,R_1,R_2,R_3,R_4]
    #print 'probability P', P_0, ',',P_1,',',P_2,',',P_3,',',P_4
    return prob_range;



def discrete_1_iter(iter = 0, n_r = 0, n_p = 0, r_min = 0, r_max = 0,
                    ro = 0, d_n = 0, d_c = 0, ki_n = 0, al_n = 0, nu = 0, be = 0, ga = 0,
                    matrix_tip = 0, list_last_movement = 0, 
                    list_tip_movement = 0, life_time_tip = 0,
                    stop_iter = 0, sp_stop = 0,
                    n = 0, c = 0, f = 0, tp = 0,
                    t_branch = 0.25, number_of_tip = 6):

    import numpy as np
    import random
    from random import randint
    
    '''Mesh Grid'''
    r = np.linspace(r_min, r_max, n_r)
    p = np.linspace(0, 2*np.pi, n_p)
    d_r = (r_max - r_min)/n_r
    d_p = 2*np.pi/n_p
    r_len = len(r)-1
    p_len = len(p)-1
    R, P = np.meshgrid(r, p)
    
    '''Initial Condition'''
    if iter == 1:     
        c = np.zeros((r_len+1,p_len+1))
        f = np.zeros((r_len+1,p_len+1))
        for rr in range(0,r_len+1,2):
            for pp in range(0,p_len+1,2):
                c[rr,pp] = 1-0.45*np.exp(-(r_min+rr*d_r)**2/0.45)
                f[rr,pp] = 1-0.45*np.exp(-(r_max-r_min+rr*d_r)**2/0.45)
        matrix_tip = []
        list_last_movement = []
        list_tip_movement = []
        life_time_tip = []
        sp_stop = []
                        
        '''Initial Tips'''
        n = np.zeros((r_len+1,p_len+1))
        index_tip = [pp for pp in range(5,p_len,20)]
        for i,y in enumerate(index_tip):
            matrix_tip.append([(1,y)]) #real time position
            n[1,y] = 1
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
                if matrix_tip[noms][i][1] == r_len-1:
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
                r_b = matrix_tip[nom][-1][0] #get x position of last tip position
                p_b = matrix_tip[nom][-1][1] #get y position of last tip position
                #print 'xb,yb', xb,',',yb
                dirr = movement_dir(r_pos = r_b, p_pos = p_b, cc = c, ff = f, 
                                    tep = tp, d_r1 = d_r, d_p1 = d_p, 
                                    d_n1 = d_n, ki_n1 = ki_n, al_n1 = al_n, ro1 = ro, r_len1 = r_len, p_len1 = p_len) # get list of prob_range

                '''2.1 Branching Decision''' 
                if life_time_tip[nom] >= t_branch: #being able to branch by life time               
                    #probabilty of branching
#                    print 'NILAI C', c[xb+1,yb+1]
                    if c[r_b+1,p_b-1] >= 0.3 and c[r_b+1,p_b-1] < 0.5:
                        prob_weight = 2 # set the number to select here.
                        list_prob = random.sample(line, prob_weight) #list of selected numbers from line
                    elif c[r_b+1,p_b-1] >= 0.5 and c[r_b+1,p_b-1] < 0.7:
                        prob_weight = 3 # set the number to select here.
                        list_prob = random.sample(line, prob_weight)   
                    elif c[r_b+1,p_b-1] >= 0.7 and c[r_b+1,p_b-1] < 0.8:
                        prob_weight = 4 # set the number to select here.
                        list_prob = random.sample(line, prob_weight)  
                    elif c[r_b+1,p_b-1] >= 0.8: #do branching
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
                        xpos_new = matrix_tip[nom][-1][0] -2
                        ypos_new = matrix_tip[nom][-1][1] 
                        matrix_tip[nom].append((xpos_new,ypos_new))
                    elif no_back == 'left':
                        tip_1 = 'right'
                        xpos_new = matrix_tip[nom][-1][0] +2
                        ypos_new = matrix_tip[nom][-1][1] 
                        matrix_tip[nom].append((xpos_new,ypos_new))
                    elif no_back == 'up':
                        tip_1 = 'down'
                        if matrix_tip[nom][-1][1] == 1:
                            xpos_new = matrix_tip[nom][-1][0] 
                            ypos_new = p_len-1
                        else:
                            xpos_new = matrix_tip[nom][-1][0] 
                            ypos_new = matrix_tip[nom][-1][1] -2
                        matrix_tip[nom].append((xpos_new,ypos_new))
                    else:
                        tip_1 = 'up'
                        if matrix_tip[nom][-1][1] == p_len-1:
                            xpos_new = matrix_tip[nom][-1][0] 
                            ypos_new = 1
                        else:
                            xpos_new = matrix_tip[nom][-1][0] 
                            ypos_new = matrix_tip[nom][-1][1] +2
                        matrix_tip[nom].append((xpos_new,ypos_new))
                    n[xpos_new,ypos_new] = 1
                    
                    '''2.1 Branhcing'''
                    
                    matrix_tip.append([(r_b,p_b)])
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
                        xpos_new = matrix_tip[-1][-1][0] -2
                        ypos_new = matrix_tip[-1][-1][1] 
                        matrix_tip[-1].append((xpos_new,ypos_new))
                    elif dom == 'right':
                        xpos_new = matrix_tip[-1][-1][0] +2
                        ypos_new = matrix_tip[-1][-1][1] 
                        matrix_tip[-1].append((xpos_new,ypos_new))
                    elif dom == 'down':
                        if matrix_tip[-1][-1][1] == 1:
                            xpos_new = matrix_tip[-1][-1][0]
                            ypos_new = p_len-1
                        else:
                            xpos_new = matrix_tip[-1][-1][0] 
                            ypos_new = matrix_tip[-1][-1][1] -2
                        matrix_tip[-1].append((xpos_new,ypos_new))
                    else: #dom == 'up'
                        if matrix_tip[-1][-1][1] == p_len-1:
                            xpos_new = matrix_tip[-1][-1][0] 
                            ypos_new = 1
                        else:
                            xpos_new = matrix_tip[-1][-1][0] 
                            ypos_new = matrix_tip[-1][-1][1] +2    
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
                        xpos_new = matrix_tip[nom][-1][0] -2
                        ypos_new = matrix_tip[nom][-1][1] 
                        matrix_tip[nom].append((xpos_new,ypos_new))
                        n[xpos_new,ypos_new] = 1
                    elif no_back == 'left':
                        tipp = 'right'
                        xpos_new = matrix_tip[nom][-1][0] +2
                        ypos_new = matrix_tip[nom][-1][1] 
                        matrix_tip[nom].append((xpos_new,ypos_new)) 
                        n[xpos_new,ypos_new] = 1
                    elif no_back == 'up':
                        tipp = 'down'
                        if matrix_tip[nom][-1][1] == 1:
                            xpos_new = matrix_tip[nom][-1][0] 
                            ypos_new = p_len-1
                        else:
                            xpos_new = matrix_tip[nom][-1][0] 
                            ypos_new = matrix_tip[nom][-1][1] -2
                        matrix_tip[nom].append((xpos_new,ypos_new)) 
                        n[xpos_new,ypos_new] = 1
                    else:
                        tipp = 'up'
                        if matrix_tip[nom][-1][1] == p_len-1:
                            xpos_new = matrix_tip[nom][-1][0] 
                            ypos_new = 1
                        else:
                            xpos_new = matrix_tip[nom][-1][0] 
                            ypos_new = matrix_tip[nom][-1][1] +2
                        matrix_tip[nom].append((xpos_new,ypos_new))
                        n[xpos_new,ypos_new] = 1
                        
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
    
    '''Solve c, f at sub lattice'''
    for rr in range(0,r_len+1,2):
        for pp in range(0,p_len+1,2):
            if rr == 0: #in the smallest circle
                if pp == p_len or pp == 0: #in the periodic boundary
                    p_pp1 = 1
                    p_pp2 = p_len - 1
                    if n[rr+1,p_pp1] == 1 or n[rr+1,p_pp2] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[rr,pp] = c_o[rr,pp]*(1 - tp*nu*n_bool) 
                    f[rr,pp] = f_o[rr,pp]+ tp*(be-ga*f_o[rr,pp])*n_bool                 
                else:
                    p_pp1 = pp + 1
                    p_pp2 = pp - 1
                    if n[rr+1,p_pp1] == 1 or n[rr+1,p_pp2] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[rr,pp] = c_o[rr,pp]*(1 - tp*nu*n_bool) 
                    f[rr,pp] = f_o[rr,pp]+ tp*(be-ga*f_o[rr,pp])*n_bool        
            elif rr == r_len: #in the biggest circle
                if pp == p_len or pp == 0: #in the periodic boundary
                    p_pp1 = 1
                    p_pp2 = p_len - 1
                    if n[rr-1,p_pp1] == 1 or n[rr-1,p_pp2] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[rr,pp] = c_o[rr,pp]*(1 - tp*nu*n_bool) 
                    f[rr,pp] = f_o[rr,pp]+ tp*(be-ga*f_o[rr,pp])*n_bool   
                else:
                    p_pp1 = pp + 1
                    p_pp2 = pp - 1
                    if n[rr-1,p_pp1] == 1 or n[rr-1,p_pp2] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[rr,pp] = c_o[rr,pp]*(1 - tp*nu*n_bool) 
                    f[rr,pp] = f_o[rr,pp]+ tp*(be-ga*f_o[rr,pp])*n_bool
            else:
                if pp == p_len or pp == 0: #in the periodic boundary
                    p_pp1 = 1
                    p_pp2 = p_len - 1
                    if n[rr+1,p_pp1] == 1 or n[rr+1,p_pp2] == 1 or n[rr-1,p_pp1] == 1 or n[rr-1,p_pp2] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[rr,pp] = c_o[rr,pp]*(1 - tp*nu*n_bool) 
                    f[rr,pp] = f_o[rr,pp]+ tp*(be-ga*f_o[rr,pp])*n_bool 
                else:
                    p_pp1 = pp + 1
                    p_pp2 = pp - 1
                    if n[rr+1,p_pp1] == 1 or n[rr+1,p_pp2] == 1 or n[rr-1,p_pp1] == 1 or n[rr-1,p_pp2] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[rr,pp] = c_o[rr,pp]*(1 - tp*nu*n_bool) 
                    f[rr,pp] = f_o[rr,pp]+ tp*(be-ga*f_o[rr,pp])*n_bool    
    
    gg = [matrix_tip, list_last_movement, list_tip_movement, life_time_tip, stop_iter, sp_stop, n, c, f, tp]
    
    return gg
    