import numpy
import random
from random import randint
from dirrection_of_movement import movement_dir


def hybrid_tech_c(coef, set, sol):
    ##branching decision and action. Also movement   
    line = range(1,11) #for Pb
    n_sp = len(sol['matrix_tip']) #to save original number of tips before branching
    
    for nom in range(0,n_sp): #dicek setiap tip
        if not nom in sol['sp_stop']: #kalo dia sudah anastomosis, gak perlu branching dan move lg.
            xb = sol['matrix_tip'][nom][-1][0] #get x position of last tip position
            yb = sol['matrix_tip'][nom][-1][1] #get y position of last tip position
            #print 'xb,yb', xb,',',yb
            dirr = movement_dir(coef, set, sol, xb, yb, nom, n_dir = True)
    
            dirr1 = [dirr[0],dirr[0]+dirr[1],dirr[0]+dirr[1]+dirr[2],dirr[0]+dirr[1]+dirr[2]+dirr[3],1]
                     
            no_back = sol['list_tip_movement'][nom]
            
            k = 0
            while no_back == sol['list_tip_movement'][nom]:
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
                xpos_new = sol['matrix_tip'][nom][-1][0] - 2
                ypos_new = sol['matrix_tip'][nom][-1][1]
                sol['matrix_tip'][nom].append((xpos_new,ypos_new))
                sol['n'][xpos_new,ypos_new] = 1
                sol['list_tip_movement'][nom] = tipp
            elif no_back == 'left':
                tipp = 'right'
                xpos_new = sol['matrix_tip'][nom][-1][0] + 2
                ypos_new = sol['matrix_tip'][nom][-1][1]
                sol['matrix_tip'][nom].append((xpos_new,ypos_new)) 
                sol['n'][xpos_new,ypos_new] = 1
                sol['list_tip_movement'][nom] = tipp
            elif no_back == 'up':
                tipp = 'down'
                xpos_new = sol['matrix_tip'][nom][-1][0]
                ypos_new = sol['matrix_tip'][nom][-1][1] - 2
                sol['matrix_tip'][nom].append((xpos_new,ypos_new)) 
                sol['n'][xpos_new,ypos_new] = 1
                sol['list_tip_movement'][nom] = tipp
            else:
                tipp = 'up'
                xpos_new = sol['matrix_tip'][nom][-1][0]
                ypos_new = sol['matrix_tip'][nom][-1][1] + 2
                sol['matrix_tip'][nom].append((xpos_new,ypos_new))
                sol['n'][xpos_new,ypos_new] = 1
                sol['list_tip_movement'][nom] = tipp
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
                if sol['life_time_tip'][nom] >= coef['T_branch']: #being able to branch by life time               
                    #probabilty of branching
#                    print 'NILAI C', c[xb+1,yb+1]
                    if sol['c'][xb+1,yb+1] >= 0 and sol['c'][xb+1,yb+1] < 0.1:
                        prob_weight = 7 # set the number to select here.
                        list_prob = random.sample(line, prob_weight) #list of selected numbers from line
                    elif sol['c'][xb+1,yb+1] >= 0.05 and sol['c'][xb+1,yb+1] < 0.2:
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
                    if tes in list_prob:#do branching
                        '''2.1 Branhcing'''
                        sol['life_time_tip'][nom] = 0
                        
                        sol['matrix_tip'].append([(xb,yb)])
                        sol['life_time_tip'].append(0)
                        sol['list_tip_movement'].append('start')

                        dom = tipp #other movement
                        no_back = sol['list_tip_movement'][-1]
             #           print 'check 2'
                        k = 0
                        while no_back == sol['list_tip_movement'][-1] or dom == tipp:
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
                            xpos_new = sol['matrix_tip'][-1][-1][0] - 2
                            ypos_new = sol['matrix_tip'][-1][-1][1]
                            sol['matrix_tip'][nom].append((xpos_new,ypos_new))
                            sol['n'][xpos_new,ypos_new] = 1
                            sol['list_tip_movement'][-1] = tipp
                        elif no_back == 'left':
                            tipp = 'right'
                            xpos_new = sol['matrix_tip'][-1][-1][0] + 2
                            ypos_new = sol['matrix_tip'][-1][-1][1]
                            sol['matrix_tip'][nom].append((xpos_new,ypos_new)) 
                            sol['n'][xpos_new,ypos_new] = 1
                            sol['list_tip_movement'][-1] = tipp
                        elif no_back == 'up':
                            tipp = 'down'
                            xpos_new = sol['matrix_tip'][-1][-1][0]
                            ypos_new = sol['matrix_tip'][-1][-1][1] - 2
                            sol['matrix_tip'][nom].append((xpos_new,ypos_new)) 
                            sol['n'][xpos_new,ypos_new] = 1
                            sol['list_tip_movement'][-1] = tipp
                        else:
                            tipp = 'up'
                            xpos_new = sol['matrix_tip'][-1][-1][0]
                            ypos_new = sol['matrix_tip'][-1][-1][1] + 2
                            sol['matrix_tip'][nom].append((xpos_new,ypos_new))
                            sol['n'][xpos_new,ypos_new] = 1
                            sol['list_tip_movement'][-1] = tipp
                        if not tipp == 'stay':
                            if dirr[5] == 'stop' and tipp == 'left':
                                sp_stop.append(len(sol['matrix_tip'])-1)
                            if dirr[6] == 'stop' and tipp == 'right':
                                sp_stop.append(len(sol['matrix_tip'])-1)
                            if dirr[7] == 'stop' and tipp == 'down':
                                sp_stop.append(len(sol['matrix_tip'])-1)
                            if dirr[8] == 'stop' and tipp == 'up':
                                sp_stop.append(len(sol['matrix_tip'])-1)
                    else:
                        sol['life_time_tip'][nom] += tp    
                else: 
                    sol['life_time_tip'][nom] += tp       
            else:
                sol['life_time_tip'][nom] += tp
    return sol