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

def anas_tip(sol,xpos_new,ypos_new, nom, xb, yb):
    '''Detect which pair tip-tip that fuse'''
    i = 0
    found = False
    while i < len(sol['matrix_tip']) and found == False:
        if [xpos_new,ypos_new] == sol['matrix_tip'][i][-1] and i != nom:
            found = True
        else:
            i +=1
#     print found
    '''Stop moving for tip i or nom'''
    if found == True:
        if nom < i:
            sol['tip_tip_anas'].append([i, nom])
            if not i in sol['sp_stop']:
                sol['sp_stop'].append(i)
                sol['cause'][i] = 'tip to tip'
        elif nom > i:
            sol['tip_tip_anas'].append([nom, i])
            if not nom in sol['sp_stop']:
                sol['sp_stop'].append(nom)
                sol['cause'][nom] = 'tip to tip'
    return sol

def anastomosis(sol,set,xpos_new,ypos_new, nom, xb, yb, back_and_loop = False):    
    if sol['n'][xpos_new,ypos_new] == 1: # in sol['tip_cell']: #ANASTOMOSIS TIP TO TIP
#         print 'anas tip to tip'
        sol['matrix_tip'][nom].append([xpos_new,ypos_new])
        if [xb,yb] in sol['tip_cell']:
            sol['tip_cell'].remove([xb,yb])
        sol['n'][xb,yb] = 0
        sol['stalk'][xb,yb] = 1
        sol = anas_tip(sol,xpos_new,ypos_new, nom, xb, yb)
                
    elif sol['stalk'][xpos_new,ypos_new] == 1: #Check ANASTOMOSIS TIP TO BRANCH
        '''Check if it is backward movement on its track'''
        if [xpos_new,ypos_new] == sol['matrix_tip'][nom][len(sol['matrix_tip'][nom])-2]:
            '''no record new position on matrix sol'''
            '''Record Backward List'''
            sol['backward_list'].append([xpos_new,ypos_new])
            back_and_loop = True
             
        '''Check if self looping'''
        i = 0
        while i < len(sol['matrix_tip'][nom])-3 and back_and_loop == False:
            if [xpos_new,ypos_new] == sol['matrix_tip'][nom][i]:
                sol['matrix_tip'][nom].append([xpos_new,ypos_new])
                if [xb,yb] in sol['tip_cell']:
                    sol['tip_cell'].remove([xb,yb])
                if not [xpos_new,ypos_new] in sol['tip_cell']:
                    sol['tip_cell'].append([xpos_new,ypos_new])
                back_and_loop = True
                sol['n'][xb,yb] = 0
                sol['stalk'][xb,yb] = 1
                sol['n'][xpos_new,ypos_new] = 1
            else:
                i += 1
                  
        '''Check if it is backward movement on tip-tip anastomosis track'''
        for k in sol['tip_tip_anas']:
            if nom == k[0]:
                if [xpos_new,ypos_new] == sol['matrix_tip'][k[1]][len(sol['matrix_tip'][k[1]])-2]:
                    sol['backward_list'].append([xpos_new,ypos_new])
                    back_and_loop = True
          
        if back_and_loop == False: #Anastomosis to sprout!
            sol['matrix_tip'][nom].append([xpos_new,ypos_new])
            if [xb,yb] in sol['tip_cell']:
                sol['tip_cell'].remove([xb,yb])
            if not nom in sol['sp_stop']:
                sol['sp_stop'].append(nom)
                sol['cause'][nom] = 'tip to sprout'
            sol['stalk'][xpos_new,ypos_new] = 1
            sol['stalk'][xb,yb] = 1
            sol['n'][xb,yb] = 0
    else: #No anastomosis and backward movement
        for k in sol['tip_tip_anas']:
            if nom == k[0] or nom == k[1]:
                sol['tip_tip_anas'].remove(k) #karena sudah move
        sol['matrix_tip'][nom].append([xpos_new,ypos_new])
#         print [xb,yb]
        if [xb,yb] in sol['tip_cell']:
            sol['tip_cell'].remove([xb,yb])
        if not [xpos_new,ypos_new] in sol['tip_cell']:
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

def hybrid_tech(coef, set, sol): #2.23
    n_sp = len(sol['matrix_tip']) #to save original number of tips before branching
    n_o = numpy.copy(sol['n']) #to save the value of 'n' at time step k (we are calculating at time step k+1)
#     sol['vn_o'] = [] #to record tip cell position
#     sol['bw'] = 0 #to detect backward list
    sol['backward_list'] = [] #backward list
       
    for nom in range(0,n_sp): #dicek setiap tip
        if not nom in sol['sp_stop']: #kalo dia sudah anastomosis, gak perlu branching dan move lg.
            xb = sol['matrix_tip'][nom][-1][0] #get x position of last tip position
            yb = sol['matrix_tip'][nom][-1][1] #get y position of last tip position
            
            dirr, probb = movement_dir(coef, set, sol, xb, yb) #2.2.1 => go to direction_of_movement.py
        
            if dirr[1] == 0 and dirr[2] == 0 and dirr[3] == 0 and dirr[4] == 0: #checking if there is space for tip cell to move
                if not nom in sol['sp_stop']:
                    sol['sp_stop'].append(nom)
                    sol['cause'][nom] = 'no space'
                if [xb,yb] in sol['tip_cell']:
                    sol['tip_cell'].remove([xb,yb])
                sol['n'][xb,yb] = 0
                sol['stalk'][xb,yb] = 1
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
                        else: #there is possibility to branch
#                             Probability of Branching using c
                            list_prob = prob_by_c(sol,xb,yb) #range(1,11) #2.2.(4)
                            tes = randint(1,10)
                            if not tes in list_prob: #not able to branch
                                sol['life_time_tip'][nom] += set['dt']
                            else: #BRANCHING!
                                sol['life_time_tip'][nom] = 0
                                sol['matrix_tip'].append([[xb,yb]])
                                sol['life_time_tip'].append(0)
                                '''The Movement from branching'''
                                branch = True
                                nom = len(sol['matrix_tip'])-1
                                sol,tipp,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4 = movement(sol,set,nom,xb,yb,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4, branch) #2.2.(5)
    if len(sol['backward_list']) > 0:
        sol['backward_count'].append(set['k'])

#     '''Create tip cell area'''    
#     for tip in sol['tip_cell']:
#         sol['tip_cell_area'].append([tip[0]-2,tip[1]])
#         sol['tip_cell_area'].append([tip[0]+2,tip[1]])
#         sol['tip_cell_area'].append([tip[0],tip[1]-2])
#         sol['tip_cell_area'].append([tip[0],tip[1]+2])
#         sol['tip_cell_area'].append([tip[0]-2,tip[1]+2])
#         sol['tip_cell_area'].append([tip[0]+2,tip[1]+2])
#         sol['tip_cell_area'].append([tip[0]+2,tip[1]-2])
#         sol['tip_cell_area'].append([tip[0]-2,tip[1]-2])
    
    
    sol['tip_cell_area'] = []
    for i in sol['tip_cell']:
        sol['tip_cell_area'].append([i[0]+1, i[1]+1])
        sol['tip_cell_area'].append([i[0]+1, i[1]-1])
        sol['tip_cell_area'].append([i[0]-1, i[1]+1])
        sol['tip_cell_area'].append([i[0]-1, i[1]-1])

    '''Record New Tip Cell'''
#     sol['tip_cell'] = []
#     for nom in range(0,len(sol['matrix_tip'])): #dicek setiap tip
#         if not nom in sol['sp_stop']: #record only active sprout
#             sol['tip_cell'].append([sol['matrix_tip'][nom][-1][0],sol['matrix_tip'][nom][-1][1]])
    return sol