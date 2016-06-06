import random
from random import randint
from dirrection_of_movement import movement_dir

def hybrid_tech_c(coef, set, sol):
    ##branching decision and action. Also movement   
    line = range(1,11) #for Pb
    n_sp = len(sol['matrix_tip']) #to save original number of tips before branching
    
    for nom in range(0,n_sp): #dicek setiap tip
        if not nom in sol['sp_stop']: #kalo dia sudah anastomosis, gak perlu branching dan move lg.
            line_1 = range(1,10001)
            xb = sol['matrix_tip'][nom][-1][0] #get x position of last tip position
            yb = sol['matrix_tip'][nom][-1][1] #get y position of last tip position
            #print 'xb,yb', xb,',',yb
            dirr= movement_dir(coef, set, sol, xb, yb, nom)
            
            if dirr[1] == 0 and dirr[2] == 0 and dirr[3] == 0 and dirr[4] == 0:
                sol['sp_stop'].append(nom)
            else:
                if dirr[1] == 0:
                    list_prob_1 = []
                else:
                    list_prob_1 = random.sample(line_1, dirr[1])
                    for i in list_prob_1:
                        line_1.remove(i)
                
                if dirr[2] == 0:
                    list_prob_2 = []
                else:
                    list_prob_2 = random.sample(line_1, dirr[2])
                    for i in list_prob_2:
                        line_1.remove(i)
                
                if dirr[3] == 0:
                    list_prob_3 = []
                else:   
                    list_prob_3 = random.sample(line_1, dirr[3])
                    for i in list_prob_3:
                        line_1.remove(i)
                
                if dirr[4] == 0:
                    list_prob_4 = []
                else:
                    list_prob_4 = random.sample(line_1, dirr[4])
                    for i in list_prob_4:
                        line_1.remove(i)
                
                list_prob_0 = line_1
                #print 'corret:', len(list_prob_0), len(list_prob_1), len(list_prob_2), len(list_prob_3), len(list_prob_4)
                
                '''Checking Space for n #if meet vessel'''
                ml = 'f'
                mr = 'f'
                md = 'f'
                mu = 'f'
            
                lx = xb - 2
                rx = xb + 2
                dy = yb - 2
                uy = yb + 2
                
                tip_l = -1
                tip_r = -1
                tip_d = -1
                tip_u = -1
                
                for e,tep in enumerate(range(0,len(sol['matrix_tip']))):
                    if not tep == nom:
                        if (lx,yb) in sol['matrix_tip'][tep]:
                            ml = 'stop'
                            if [lx,yb] in sol['tip_cell'] and tip_l<0:
                                al = 'in'
                                tip_l = e
                                #sol['pp'][e] = 'start'
                        if (rx,yb) in sol['matrix_tip'][tep]:
                            mr = 'stop'
                            if [rx,yb] in sol['tip_cell'] and tip_r<0:
                                al = 'in'
                                tip_r = e
                                #sol['pp'][e] = 'start'
                        if (xb,dy) in sol['matrix_tip'][tep]:
                            md = 'stop'
                            if [xb,dy] in sol['tip_cell'] and tip_u<0:
                                al = 'in'
                                tip_d = e
                                #sol['pp'][e] = 'start'
                        if (xb,uy) in sol['matrix_tip'][tep]:
                            mu = 'stop'
                            if [xb,uy] in sol['tip_cell'] and tip_u<0:
                                al = 'in'
                                tip_u = e
                                #sol['pp'][e] = 'start'
                '''Checking Space for n #if meet vessel'''
            
                tes = randint(1,10000) #select integer number randomly between 1 and 100000
                if tes in list_prob_0:
                    tipp = 'stay'
                elif tes in list_prob_1:
                    tipp = 'left'
                    xpos_new = sol['matrix_tip'][nom][-1][0] - 2
                    ypos_new = sol['matrix_tip'][nom][-1][1]                    
                    sol['matrix_tip'][nom].append((xpos_new,ypos_new))
                    sol['n'][xpos_new,ypos_new] = 1
                    sol['list_tip_movement'][nom] = tipp
                    for i in list_prob_1:
                        list_prob_0.append(i)
                    list_prob_1 =[]
                    if ml == 'stop':
                        sol['sp_stop'].append(nom)
                        if tip_l>=0:
                            sol['pp'][tip_l] = ['right','a','a','a']
                elif tes in list_prob_2:   
                    tipp = 'right'
                    xpos_new = sol['matrix_tip'][nom][-1][0] + 2
                    ypos_new = sol['matrix_tip'][nom][-1][1]
                    sol['matrix_tip'][nom].append((xpos_new,ypos_new)) 
                    sol['n'][xpos_new,ypos_new] = 1
                    sol['list_tip_movement'][nom] = tipp
                    for i in list_prob_2:
                        list_prob_0.append(i)
                    list_prob_2 =[]
                    if mr == 'stop':
                        sol['sp_stop'].append(nom)
                        if tip_r>=0:
                            sol['pp'][tip_r] = ['a','left','a','a']
                elif tes in list_prob_3: 
                    tipp = 'down'
                    xpos_new = sol['matrix_tip'][nom][-1][0]
                    ypos_new = sol['matrix_tip'][nom][-1][1] - 2
                    sol['matrix_tip'][nom].append((xpos_new,ypos_new)) 
                    sol['n'][xpos_new,ypos_new] = 1
                    sol['list_tip_movement'][nom] = tipp
                    for i in list_prob_3:
                        list_prob_0.append(i)
                    list_prob_3 =[]
                    if md == 'stop':
                        sol['sp_stop'].append(nom)
                        if tip_d>=0:
                            sol['pp'][tip_d] = ['a','a','up','a']
                elif tes in list_prob_4: 
                    tipp = 'up'
                    xpos_new = sol['matrix_tip'][nom][-1][0]
                    ypos_new = sol['matrix_tip'][nom][-1][1] + 2
                    sol['matrix_tip'][nom].append((xpos_new,ypos_new))
                    sol['n'][xpos_new,ypos_new] = 1
                    sol['list_tip_movement'][nom] = tipp
                    for i in list_prob_4:
                        list_prob_0.append(i)
                    list_prob_4 =[]
                    if mu == 'stop':
                        sol['sp_stop'].append(nom)
                        if tip_u>=0:
                            sol['pp'][tip_u] = ['a','a','a','down']
                
                '''2.1 Branching Decision'''
                if tipp == 'stay':
                    sol['life_time_tip'][nom] += set['dt']
                else:
                    cek = str(nom)
                    if dirr.count(0) >= 3:
                        sol['life_time_tip'][nom] += set['dt']
                        if cek in sol['pp']:
                            sol['pp'].pop('cek')
                    else:
                        if sol['life_time_tip'][nom] < coef['T_branch']: 
                            sol['life_time_tip'][nom] += set['dt']
                            if cek in sol['pp']:
                                sol['pp'].pop('cek')
                        else: #being able to branch by life time              
                            #probabilty of branching
        #                    print 'NILAI C', c[xb+1,yb+1]
                            if sol['c'][xb+1,yb+1] >= 0 and sol['c'][xb+1,yb+1] < 0.25:
                                list_prob = [20]
                            elif sol['c'][xb+1,yb+1] >= 0.25 and sol['c'][xb+1,yb+1] < 0.45:
                                prob_weight = 3 # set the number to select here.
                                list_prob = random.sample(line, prob_weight) #list of selected numbers from line
                            elif sol['c'][xb+1,yb+1] >= 0.45 and sol['c'][xb+1,yb+1] < 0.6:
                                prob_weight = 4 # set the number to select here.
                                list_prob = random.sample(line, prob_weight)   
                            elif sol['c'][xb+1,yb+1] >= 0.6 and sol['c'][xb+1,yb+1] < 0.7:
                                prob_weight = 5 # set the number to select here.
                                list_prob = random.sample(line, prob_weight)  
                            elif sol['c'][xb+1,yb+1] >= 0.7: #do branching
                                list_prob = line
                            tes = randint(1,10) #select integer number randomly between 1 and 10
                            #print 'check 3'
                            if not tes in list_prob:
                                sol['life_time_tip'][nom] += set['dt']
                                if cek in sol['pp']:
                                    sol['pp'].pop('cek')
                            else: #do branching
                                '''2.1 Branhcing'''
                                sol['life_time_tip'][nom] = 0
                                sol['matrix_tip'].append([(xb,yb)])
                                sol['life_time_tip'].append(0)
                                sol['list_tip_movement'].append('start')
                                tipp = 'stay'
                                if cek in sol['pp']:
                                    sol['pp'].pop('cek')
                                while tipp == 'stay':
                                    tes = randint(1,10000) #select integer number randomly between 1 and 100000
                                    if tes in list_prob_0:
                                        tipp = 'stay'
                                    elif tes in list_prob_1:
                                        tipp = 'left'
                                        xpos_new = sol['matrix_tip'][-1][-1][0] - 2
                                        ypos_new = sol['matrix_tip'][-1][-1][1]                    
                                        sol['matrix_tip'][-1].append((xpos_new,ypos_new))
                                        sol['n'][xpos_new,ypos_new] = 1
                                        sol['list_tip_movement'][-1] = tipp
                                        if ml == 'stop':
                                            sol['sp_stop'].append(nom)
                                            if tip_l>=0:
                                                sol['pp'][tip_l][0] = 'right'
                                    elif tes in list_prob_2:   
                                        tipp = 'right'
                                        xpos_new = sol['matrix_tip'][-1][-1][0] + 2
                                        ypos_new = sol['matrix_tip'][-1][-1][1]
                                        sol['matrix_tip'][-1].append((xpos_new,ypos_new)) 
                                        sol['n'][xpos_new,ypos_new] = 1
                                        sol['list_tip_movement'][-1] = tipp
                                        if mr == 'stop':
                                            sol['sp_stop'].append(nom)
                                            if tip_r>=0:
                                                sol['pp'][tip_r][1] = 'left'
                                    elif tes in list_prob_3: 
                                        tipp = 'down'
                                        xpos_new = sol['matrix_tip'][-1][-1][0]
                                        ypos_new = sol['matrix_tip'][-1][-1][1] - 2
                                        sol['matrix_tip'][-1].append((xpos_new,ypos_new)) 
                                        sol['n'][xpos_new,ypos_new] = 1
                                        sol['list_tip_movement'][-1] = tipp
                                        if md == 'stop':
                                            sol['sp_stop'].append(nom)
                                            if tip_d>=0:
                                                sol['pp'][tip_d][2] = 'up'
                                    elif tes in list_prob_4: 
                                        tipp = 'up'
                                        xpos_new = sol['matrix_tip'][-1][-1][0]
                                        ypos_new = sol['matrix_tip'][-1][-1][1] + 2
                                        sol['matrix_tip'][-1].append((xpos_new,ypos_new))
                                        sol['n'][xpos_new,ypos_new] = 1
                                        sol['list_tip_movement'][-1] = tipp
                                        if mu == 'stop':
                                            sol['sp_stop'].append(nom)
                                            if tip_u>=0:
                                                sol['pp'][tip_u][3] = 'down'
    return sol