from dirrection_of_movement import movement_dir #2.2.1
import random
import numpy
from random import randint
from collections import OrderedDict
import math as m #r

def set_list_prob(dirr): #2.2.(1)
    line_1 = range(1,10001)
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
    return list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4

def move_left(sol,set,nom,xb,yb,list_prob_0,list_prob_1): #2.2.(2).(1)
    tipp = 'left'
    xpos_new = xb - 2
    ypos_new = yb                    
    sol['matrix_tip'][nom].append([xpos_new,ypos_new])
    sol['list_tip_movement'][nom] = tipp
    for i in list_prob_1:
        list_prob_0.append(i)
    list_prob_1 =[]   
    
    '''Checking Anastomosis'''
    sol = anastomosis(sol,set,xpos_new,ypos_new,nom, xb, yb)

    return sol, list_prob_0, list_prob_1, tipp

def move_right(sol,set,nom,xb,yb,list_prob_0,list_prob_2): #2.2.(2).(2) 
    tipp = 'right'
    xpos_new = xb + 2
    ypos_new = yb
    sol['matrix_tip'][nom].append([xpos_new,ypos_new]) 
    sol['list_tip_movement'][nom] = tipp
    for i in list_prob_2:
        list_prob_0.append(i)
    list_prob_2 =[]
    
    '''Checking Anastomosis'''
    sol = anastomosis(sol,set,xpos_new,ypos_new,nom, xb, yb)
    
    return sol, list_prob_0, list_prob_2, tipp

def move_down(sol,set,nom,xb,yb,list_prob_0,list_prob_3): #2.2.(2).(3)
    tipp = 'down'
    xpos_new = xb
    ypos_new = yb - 2
    sol['matrix_tip'][nom].append([xpos_new,ypos_new]) 
    sol['list_tip_movement'][nom] = tipp
    for i in list_prob_3:
        list_prob_0.append(i)
    list_prob_3 =[]
    
    '''Checking Anastomosis'''
    sol = anastomosis(sol,set,xpos_new,ypos_new,nom, xb, yb)

    return sol, list_prob_0, list_prob_3, tipp

def move_up(sol,set,nom,xb,yb,list_prob_0,list_prob_4): #2.2.(2).(4)
    tipp = 'up'
    xpos_new = xb
    ypos_new = yb + 2
    sol['matrix_tip'][nom].append([xpos_new,ypos_new])
    sol['list_tip_movement'][nom] = tipp
    for i in list_prob_4:
        list_prob_0.append(i)
    list_prob_4 =[]
    
    '''Checking Anastomosis'''
    sol = anastomosis(sol,set,xpos_new,ypos_new,nom, xb, yb)
    
    return sol, list_prob_0, list_prob_4, tipp

def movement(sol,set,nom,xb,yb,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4, branch): #2.2.(2)
    tes = randint(1,10000)
    if branch == False:
        if tes in list_prob_0:
            tipp = 'stay'
        else:
            if tes in list_prob_1:                
                sol, list_prob_0, list_prob_1, tipp = move_left(sol,set,nom,xb,yb,list_prob_0,list_prob_1) #2.2.(2).(1)
            elif tes in list_prob_2:   
                sol, list_prob_0, list_prob_2, tipp = move_right(sol,set,nom,xb,yb,list_prob_0,list_prob_2) #2.2.(2).(2)    
            elif tes in list_prob_3: 
                sol, list_prob_0, list_prob_3, tipp = move_down(sol,set,nom,xb,yb,list_prob_0,list_prob_3) #2.2.(2).(3)   
            elif tes in list_prob_4:
                sol, list_prob_0, list_prob_4, tipp = move_up(sol,set,nom,xb,yb,list_prob_0,list_prob_4) #2.2.(2).(4)
    else:
        tipp = 'stay'
        while tipp == 'stay':
#             print 'haiyaaa'
            tes = randint(1,10000)
            if tes in list_prob_0:
                tipp = 'stay'
            else:
                if tes in list_prob_1:                
                    sol, list_prob_0, list_prob_1, tipp = move_left(sol,set,nom,xb,yb,list_prob_0,list_prob_1) #2.2.(2).(1)
                elif tes in list_prob_2:   
                    sol, list_prob_0, list_prob_2, tipp = move_right(sol,set,nom,xb,yb,list_prob_0,list_prob_2) #2.2.(2).(2)    
                elif tes in list_prob_3: 
                    sol, list_prob_0, list_prob_3, tipp = move_down(sol,set,nom,xb,yb,list_prob_0,list_prob_3) #2.2.(2).(3)   
                elif tes in list_prob_4:
                    sol, list_prob_0, list_prob_4, tipp = move_up(sol,set,nom,xb,yb,list_prob_0,list_prob_4) #2.2.(2).(4)
                
    return sol,tipp,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4 

def anastomosis(sol,set,xpos_new,ypos_new, nom, xb, yb, backward = False, sellooping = False):
    if [xpos_new,ypos_new] in sol['tip_cell']: #ANASTOMOSIS TIP TO TIP
#         print 'YEYYYYYY'
        sol['sp_stop'].append(nom)
        sol['n'][xb,yb] = 0
        sol['stalk'][xb,yb] = 1
        if [xb,yb] in sol['tip_cell']:
            sol['tip_cell'].remove([xb,yb])
    
    elif sol['stalk'][xpos_new,ypos_new] == 1: #Check ANASTOMOSIS TIP TO BRANCH
        '''Check if it is backward movement on its track'''
        if [xpos_new,ypos_new] == sol['matrix_tip'][nom][len(sol['matrix_tip'][nom])-2]:
#             print 'anasback1'
#             print set['k']
#             print sol['backward']
            if sol['bw'] == 0:
                sol['backward'][set['k']] = [[xpos_new,ypos_new]]
            else:
                sol['backward'][set['k']].append([xpos_new,ypos_new])
            sol['bw'] += 1
            backward = True
            sol['n'][xb,yb] = 1
            sol['matrix_tip'][nom].pop()
            if not [xb,yb] in sol['tip_cell']:
                    sol['tip_cell'].append([xb,yb])
        '''Check if self looping'''
        i = 0
        while i < len(sol['matrix_tip'][nom])-1:
#             print 'hmmmm'
            if [xpos_new,ypos_new] == sol['matrix_tip'][nom][i]:
#                 print 'self looping'
                sellooping = True
                if [xb,yb] in sol['tip_cell']: #kalo branching, xb yb sudah diremove dr sprout branch sblmny. jadi gak perlu remove lagi
                    sol['tip_cell'].remove([xb,yb])
                sol['tip_cell'].append([xpos_new,ypos_new])
                sol['n'][xpos_new,ypos_new] = 1
                sol['n'][xb,yb] = 0
                sol['stalk'][xb,yb] = 1
            i += 1
                
        '''Check if it is backward movement on tip-tip anastomosis track'''
        for i in sol['sp_stop']:
            nol = 0
            j = 0
            while j< len(sol['matrix_tip'][i])-1 and nol == 0:
#                 print 'uuuuu'
                if [xpos_new,ypos_new] == sol['matrix_tip'][i][j]:
#                     print 'anasback2'
                    nol = 1
                    if sol['bw'] == 0:
                        sol['backward'][set['k']] = [[xpos_new,ypos_new]]
                    else:
                        sol['backward'][set['k']].append([xpos_new,ypos_new])
                    sol['bw'] += 1
                    backward = True
                    sol['n'][xb,yb] = 1
                    sol['matrix_tip'][i].pop()
                    if not [xb,yb] in sol['tip_cell']:
                        sol['tip_cell'].append([xb,yb])
                elif j == len(sol['matrix_tip'][i])-2:
                    nol = 5
                j += 1
        if backward == False and sellooping == False: #Anastomosis to sprout!
            sol['sp_stop'].append(nom)
            sol['stalk'][xpos_new,ypos_new] = 1
            sol['stalk'][xb,yb] = 1
            sol['n'][xb,yb] = 0
            if [xb,yb] in sol['tip_cell']:
                sol['tip_cell'].remove([xb,yb])
    else:
#         print 'elsee'
        if [xb,yb] in sol['tip_cell']: #kalo branching, xb yb sudah diremove dr sprout branch sblmny. jadi gak perlu remove lagi
            sol['tip_cell'].remove([xb,yb])
        sol['tip_cell'].append([xpos_new,ypos_new])
        sol['n'][xpos_new,ypos_new] = 1
        sol['n'][xb,yb] = 0
        sol['stalk'][xb,yb] = 1
    return sol

def prob_by_c(sol,xb,yb): #2.2.(4)
    line = range(1,11)
    if sol['c'][xb+1,yb+1] >= 0 and sol['c'][xb+1,yb+1] < 0.25:
        list_prob = [20]
    elif sol['c'][xb+1,yb+1] >= 0.25 and sol['c'][xb+1,yb+1] < 0.45:
        prob_weight = 3
        list_prob = random.sample(line, prob_weight) 
    elif sol['c'][xb+1,yb+1] >= 0.45 and sol['c'][xb+1,yb+1] < 0.6:
        prob_weight = 4
        list_prob = random.sample(line, prob_weight)   
    elif sol['c'][xb+1,yb+1] >= 0.6 and sol['c'][xb+1,yb+1] < 0.7:
        prob_weight = 5
        list_prob = random.sample(line, prob_weight)  
    elif sol['c'][xb+1,yb+1] >= 0.7:
        list_prob = line
    return list_prob

def hybrid_tech(coef, set, sol): #2.2
    n_sp = len(sol['matrix_tip']) #to save original number of tips before branching
    n_o = numpy.copy(sol['n']) #to save the value of 'n' at time step k (we are calculating at time step k+1)
    vn_o = [] #to record tip cell position
    sol['bw'] = 0
    for nom in range(0,n_sp): #dicek setiap tip
        if not nom in sol['sp_stop']: #kalo dia sudah anastomosis, gak perlu branching dan move lg.
            xb = sol['matrix_tip'][nom][-1][0] #get x position of last tip position
            yb = sol['matrix_tip'][nom][-1][1] #get y position of last tip position
            vn_o.append([xb,yb])
            
            dirr, probb = movement_dir(coef, set, sol, xb, yb) #2.2.1 => go to direction_of_movement.py
        
            if dirr[1] == 0 and dirr[2] == 0 and dirr[3] == 0 and dirr[4] == 0: #checking if there is space for tip cell to move
                sol['sp_stop'].append(nom)
                sol['tip_cell'].remove([xb,yb])
                sol['n'][xb,yb] = 0
            else:
                '''Making list of prob'''
                list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4 = set_list_prob(dirr) #2.2.(1)
                                           
                '''The Movement And Tip-Tip Anastomosis Checking'''
                branch = False
                sol,tipp,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4 = movement(sol,set,nom,xb,yb,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4, branch) #2.2.(2)
                
                '''2.1 Branching Decision'''
                PP = 'test'
                if tipp == 'stay' and PP == 'test': #not able to branch, PP untuk pertama kali 
                    sol['life_time_tip'][nom] += set['dt']
                else: #there is possibility to branch
                    if dirr.count(0) >= 3: #no space to move
                        sol['life_time_tip'][nom] += set['dt']
                    else: #there is possibility to branch
                        if sol['life_time_tip'][nom] < coef['T_branch']: #not able to branch
                            sol['life_time_tip'][nom] += set['dt']
#                             sol['life_mit'][nom] += set['dt']
                        else: #there is possibility to branch
#                             Probability of Branching using c 
                            list_prob = range(1,11) #prob_by_c(sol,xb,yb) #2.2.(4)TESSSSS
                            tes = randint(1,10)
                            if not tes in list_prob: #not able to branch
                                sol['life_time_tip'][nom] += set['dt']
                            else: #BRANCHING!
                                sol['life_time_tip'][nom] = 0
                                sol['matrix_tip'].append([[xb,yb]])
                                sol['life_time_tip'].append(0)
                                sol['list_tip_movement'].append('start')
                                '''The Movement from branching'''
                                branch = True
                                nom = len(sol['matrix_tip'])-1
                                sol,tipp,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4 = movement(sol,set,nom,xb,yb,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4, branch) #2.2.(5)
    
#     print 'Tip cell position:', vn_o
#     print 'Velocity Vector stalk on [3,201]: [',sol['Vb_x'][3,201],',',sol['Vb_y'][3,201],']'
    return sol, n_o