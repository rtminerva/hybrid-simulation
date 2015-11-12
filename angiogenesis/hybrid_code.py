from ac_model_new import *


def discrete_code():
    '''1. Anastomosis''' #not yet
    
    sp_new_stop =[]
    for noms in range(1,num_sp+1):         
        if not noms in sp_stop:
            '''1.1 Checking if looping itself'''
            if not globals()['tip%s' % noms] == 'stay':
                gg = globals()['sp%s' % noms][:]
                gg.pop()
                gg = list(set(gg))    
                if len(gg) > 0: #mencegah start masuk ke bagian ini
                    if globals()['sp%s' % noms][-1] in gg:
                        sp_new_stop.append(noms)
                        print 'looping itself for tip number', noms
                        print 'looping to position', globals()['sp%s' % noms][-1]
                #kalau < = 0, artinya baru start iterasi
            #kalau 'stay', artinya aman. do nothing. done looping itself
            '''1.2 Checking if hit another sprout'''
            if noms in sp_new_stop or num_sp == 1: #kalau sudah looping itself, gak usah cek hit others lg.
                lop = 1
            else:
                #making list of others
                other_tips = range(1,num_sp+1)
                other_tips.remove(noms)
                for i in other_tips:
                    if globals()['sp%s' % noms][-1] in globals()['sp%s' % i]:
                        sp_new_stop.append(noms)
                        print 'anastomosis for tip number ', noms, ' to tip number ', i 
                        print 'anastomosis at position', globals()['sp%s' % noms][-1]
                    #kalau gak hit, do nothing
    
    '''1.3 Checking if two tips meet at one point'''
    if len(sp_new_stop) >= 2 or num_sp > 1:
        pair = [(0,0)]
        for j in sp_new_stop:
            other_tips = sp_new_stop[:]
            other_tips.remove(j)
            for i in other_tips:
                if globals()['sp%s' % j][-1] == globals()['sp%s' % i][-1]:
                    jjj = (j,i)
                    if reversed(jjj) in pair:
                        lop = 1
                    else:
                        pair.append((j,i))
        if len(pair) > 1:
            for j in range(1,len(pair)):             
                sp_new_stop.remove(pair[j][0])         
    sp_stop.extend(sp_new_stop)
    sp_stop = list(set(sp_stop))

    '''2. Branching and Movement'''        
    if len(sp_stop) == num_sp:
        k = 100000 #sp_stop harus dicek di setiap movement and branching. karena sudah tidak bergerak lagi yang ada di list ini.
        print 'all looping itself or anastomosis'
    else:    
        ##branching decision and action. Also movement   
        line = range(1,11) #for Pb
        n_sp = num_sp #to save original number of tips before branching
        
        for nom in range(1,n_sp+1): #dicek setiap tip
            if nom in sp_stop: #kalo dia sudah anastomosis, gak perlu branching dan move lg.
                print 'no_moving for tip', nom
            else:
                xb = globals()['sp%s' % nom][-1][0] #get x position of last tip position
                yb = globals()['sp%s' % nom][-1][1] #get y position of last tip position
                #print 'xb,yb', xb,',',yb
                dirr = movement_dir() # get list of prob_range
                
                '''2.1 Branching Decision''' 
                if globals()['tsp%s' % nom] >= t_branch: #being able to branch by life time               
                    #probabilty of branching
                    if c[xb+1,yb+1,k+1] >= 0.3 and c[xb+1,yb+1,k+1] < 0.5:
                        prob_weight = 2 # set the number to select here.
                        list_prob = random.sample(line, prob_weight) #list of selected numbers from line
                    elif c[xb+1,yb+1,k+1] >= 0.5 and c[xb+1,yb+1,k+1] < 0.7:
                        prob_weight = 3 # set the number to select here.
                        list_prob = random.sample(line, prob_weight)   
                    elif c[xb+1,yb+1,k+1] >= 0.7 and c[xb+1,yb+1,k+1] < 0.8:
                        prob_weight = 4 # set the number to select here.
                        list_prob = random.sample(line, prob_weight)  
                    elif c[xb+1,yb+1,k+1] >= 0.8: #do branching
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
                    no1_back = globals()['move%s' % nom]
                    no_back = globals()['move%s' % nom]
                    while no_back == globals()['move%s' % nom]:
                        trial = random.uniform(0,1)
                        if trial <= dirr[0]: #stay
                            no_back = globals()['move%s' % nom] #karna branching, dia harus move
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
                        xpos_new = globals()['sp%s' % nom][-1][0] - 2
                        ypos_new = globals()['sp%s' % nom][-1][1]
                        globals()['sp%s' % nom].append((xpos_new,ypos_new))
                    elif no_back == 'left':
                        tip_1 = 'right'
                        xpos_new = globals()['sp%s' % nom][-1][0] + 2
                        ypos_new = globals()['sp%s' % nom][-1][1]
                        globals()['sp%s' % nom].append((xpos_new,ypos_new))
                    elif no_back == 'up':
                        tip_1 = 'down'
                        xpos_new = globals()['sp%s' % nom][-1][0]
                        ypos_new = globals()['sp%s' % nom][-1][1] - 2
                        globals()['sp%s' % nom].append((xpos_new,ypos_new))
                    else:
                        tip_1 = 'up'
                        xpos_new = globals()['sp%s' % nom][-1][0]
                        ypos_new = globals()['sp%s' % nom][-1][1] + 2
                        globals()['sp%s' % nom].append((xpos_new,ypos_new))
                    
                    '''2.1 Branhcing'''
                    num_sp += 1
                    globals()['sp%s' % num_sp] = [(xb,yb)]
                    globals()['ps%s' % num_sp] = []
                    #waktunya diriset
                    globals()['tsp%s' % num_sp] = 0
                    globals()['tsp%s' % nom] = 0
                    
                    '''2.1.2 Branching tip's movement: 2nd tip movement : num_sp tip'''
                    '''2.1.2.1 Checking no back, tip 1, stay movement'''
                    #ada no1_back
                    #ada tip_1
                    dom = tip_1
                    while no1_back == globals()['tip%s' % nom] or dom == tip_1:
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
                        xpos_new = globals()['sp%s' % num_sp][-1][0] - 2
                        ypos_new = globals()['sp%s' % num_sp][-1][1]
                        globals()['sp%s' % num_sp].append((xpos_new,ypos_new))
                    elif dom == 'right':
                        xpos_new = globals()['sp%s' % num_sp][-1][0] + 2
                        ypos_new = globals()['sp%s' % num_sp][-1][1]
                        globals()['sp%s' % num_sp].append((xpos_new,ypos_new))
                    elif dom == 'down':
                        xpos_new = globals()['sp%s' % num_sp][-1][0]
                        ypos_new = globals()['sp%s' % num_sp][-1][1] - 2
                        globals()['sp%s' % num_sp].append((xpos_new,ypos_new))
                    else: #dom == 'up'
                        xpos_new = globals()['sp%s' % num_sp][-1][0]
                        ypos_new = globals()['sp%s' % num_sp][-1][1] + 2
                        globals()['sp%s' % num_sp].append((xpos_new,ypos_new))
                    
                    '''2.1.3 Renewal Some Vars'''
                    if not dom == 'stay':
                        globals()['move%s' % num_sp] = dom
                    if not tip_1 == 'stay':
                        globals()['move%s' % nom] = tip_1
                    globals()['tip%s' % num_sp] = dom
                    globals()['tip%s' % nom] = tip_1   
                else: #no branching
                    '''2.2 No Branching'''
                    '''Movement only'''
                    '''2.2.1 Checking no back movement'''
                    globals()['tsp%s' % nom] += tp
                    no_back = globals()['move%s' % nom]
                    while no_back == globals()['move%s' % nom]:
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
                        globals()['sp%s' % nom].append(globals()['sp%s' % nom][-1])
                    elif no_back == 'right':
                        tipp = 'left'
                        xpos_new = globals()['sp%s' % nom][-1][0] - 2
                        ypos_new = globals()['sp%s' % nom][-1][1]
                        globals()['sp%s' % nom].append((xpos_new,ypos_new)) 
                    elif no_back == 'left':
                        tipp = 'right'
                        xpos_new = globals()['sp%s' % nom][-1][0] + 2
                        ypos_new = globals()['sp%s' % nom][-1][1]
                        globals()['sp%s' % nom].append((xpos_new,ypos_new)) 
                    elif no_back == 'up':
                        tipp = 'down'
                        xpos_new = globals()['sp%s' % nom][-1][0]
                        ypos_new = globals()['sp%s' % nom][-1][1] - 2
                        globals()['sp%s' % nom].append((xpos_new,ypos_new)) 
                    else:
                        tipp = 'up'
                        xpos_new = globals()['sp%s' % nom][-1][0]
                        ypos_new = globals()['sp%s' % nom][-1][1] + 2
                        globals()['sp%s' % nom].append((xpos_new,ypos_new))
                        
                    '''2.2.2 Renewal Some Vars'''
                    if not tipp == 'stay':
                        globals()['move%s' % nom] = tipp
                    globals()['tip%s' % nom] = tipp  
    print        
    print '*****START HERE FOR TIME STEP', t, '*****'
    print 'Total Tip:',num_sp
    print 'sp_stop list:', sp_stop
    for i in range(1,num_sp+1):
        print 'TIP', i, ':',globals()['sp%s' % i]
        print 'last movement tip', globals()['tip%s' % i]
    print '*****END*****'
    print
    return k;
    