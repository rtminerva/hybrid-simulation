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
            dirr, space = movement_dir(coef, set, sol, xb, yb, nom, n_dir = True)
            
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
                
                '''Checking if new position hits any existing vessel'''
                if not tipp == 'stay':
                    if tipp == 'left' and space[0] == 'stop':
                        sol['sp_stop'].append(nom)
                    elif tipp == 'right' and space[1] == 'stop':
                        sol['sp_stop'].append(nom)
                    elif tipp == 'down' and space[2] == 'stop':
                        sol['sp_stop'].append(nom)
                    elif tipp == 'up' and space[3] == 'stop':
                        sol['sp_stop'].append(nom)
                
                '''Checking m space and calculating number of EC'''
                if not coef['Mic'] == 0 or not coef['Kappa'] == 0:
                    if not tipp == 'stay' and set['t'] > set['tm']:  
                        #calculate number of EC
                        #sol['number_ec'] += 1
                                     
                        #Kalau di posisi n baru ada m, m nya dibuang
                        if sol['m'][xpos_new,ypos_new] == 1:
                            sol['m'][xpos_new,ypos_new] == 0
                            #sol['cell_m'].remove([xpos_new,ypos_new])
                        
                '''2.1 Branching Decision'''
                if tipp == 'stay':
                    sol['life_time_tip'][nom] += sol['tp']
                else:
                    if dirr.count(0) >= 3:
                        sol['life_time_tip'][nom] += sol['tp']
                    else:
                        if sol['life_time_tip'][nom] < coef['T_branch']: 
                            sol['life_time_tip'][nom] += sol['tp']
                        else: #being able to branch by life time              
                            #probabilty of branching
        #                    print 'NILAI C', c[xb+1,yb+1]
                            if sol['c'][xb+1,yb+1] >= 0 and sol['c'][xb+1,yb+1] < 0.1:
                                prob_weight = 7 # set the number to select here.
                                list_prob = random.sample(line, prob_weight) #list of selected numbers from line
                            elif sol['c'][xb+1,yb+1] >= 0.1 and sol['c'][xb+1,yb+1] < 0.2:
                                prob_weight = 8 # set the number to select here.
                                list_prob = random.sample(line, prob_weight)   
                            elif sol['c'][xb+1,yb+1] >= 0.2 and sol['c'][xb+1,yb+1] < 0.3:
                                prob_weight = 9 # set the number to select here.
                                list_prob = random.sample(line, prob_weight)  
                            elif sol['c'][xb+1,yb+1] >= 0.3: #do branching
                                list_prob = line
                            #apakah branching? meaning masuk dalam probability of branching?
                            tes = randint(1,10) #select integer number randomly between 1 and 10
                            #print 'check 3'
                            if not tes in list_prob:
                                sol['life_time_tip'][nom] += sol['tp']
                            else: #do branching
                                '''2.1 Branhcing'''
                                sol['life_time_tip'][nom] = 0
                                sol['matrix_tip'].append([(xb,yb)])
                                sol['life_time_tip'].append(0)
                                sol['list_tip_movement'].append('start')
        
                                while tipp == 'stay':
                                    tes = randint(1,100000) #select integer number randomly between 1 and 100000
                                    if tes in list_prob_0:
                                        tipp = 'stay'
                                    elif tes in list_prob_1:
                                        tipp = 'left'
                                        xpos_new = sol['matrix_tip'][-1][-1][0] - 2
                                        ypos_new = sol['matrix_tip'][-1][-1][1]                    
                                        sol['matrix_tip'][-1].append((xpos_new,ypos_new))
                                        sol['n'][xpos_new,ypos_new] = 1
                                        sol['list_tip_movement'][-1] = tipp
                                    elif tes in list_prob_2:   
                                        tipp = 'right'
                                        xpos_new = sol['matrix_tip'][-1][-1][0] + 2
                                        ypos_new = sol['matrix_tip'][-1][-1][1]
                                        sol['matrix_tip'][-1].append((xpos_new,ypos_new)) 
                                        sol['n'][xpos_new,ypos_new] = 1
                                        sol['list_tip_movement'][-1] = tipp
                                    elif tes in list_prob_3: 
                                        tipp = 'down'
                                        xpos_new = sol['matrix_tip'][-1][-1][0]
                                        ypos_new = sol['matrix_tip'][-1][-1][1] - 2
                                        sol['matrix_tip'][-1].append((xpos_new,ypos_new)) 
                                        sol['n'][xpos_new,ypos_new] = 1
                                        sol['list_tip_movement'][-1] = tipp
                                    elif tes in list_prob_4: 
                                        tipp = 'up'
                                        xpos_new = sol['matrix_tip'][-1][-1][0]
                                        ypos_new = sol['matrix_tip'][-1][-1][1] + 2
                                        sol['matrix_tip'][-1].append((xpos_new,ypos_new))
                                        sol['n'][xpos_new,ypos_new] = 1
                                        sol['list_tip_movement'][-1] = tipp
                                
                                '''Checking if new position hits any existing vessel'''
                                if tipp == 'left' and space[0] == 'stop':
                                    sol['sp_stop'].append(len(sol['matrix_tip'])-1)
                                elif tipp == 'right' and space[1] == 'stop':
                                    sol['sp_stop'].append(len(sol['matrix_tip'])-1)
                                elif tipp == 'down' and space[2] == 'stop':
                                    sol['sp_stop'].append(len(sol['matrix_tip'])-1)
                                elif tipp == 'up' and space[3] == 'stop':
                                    sol['sp_stop'].append(len(sol['matrix_tip'])-1)
                                
                                '''Checking m space and calculating number of EC'''
                                if not coef['Mic'] == 0 or not coef['Kappa'] == 0: 
                                    #calculate number of EC
                                    #sol['number_ec'] += 1
                                    #Kalau di posisi n baru ada m, m nya dibuang
                                    if set['t'] > set['tm']:
                                        if sol['m'][xpos_new,ypos_new] == 1:
                                            sol['m'][xpos_new,ypos_new] == 0
                                           # sol['cell_m'].remove([xpos_new,ypos_new])
        
    return sol