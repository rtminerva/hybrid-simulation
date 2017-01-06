from dirrection_of_movement import movement_dir #2.2.1
import random
import numpy
from random import randint
from collections import OrderedDict
import math as m

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

def move_left(sol,nom,xb,yb,list_prob_0,list_prob_1): #2.2.(2).(1)
    tipp = 'left'
    xpos_new = xb - 2
    ypos_new = yb                    
    sol['matrix_tip'][nom].append([xpos_new,ypos_new])
    sol['list_tip_movement'][nom] = tipp
    for i in list_prob_1:
        list_prob_0.append(i)
    list_prob_1 =[]   
#     if sol['n'][xb-2,yb] == 1: #ANASTOMOSIS TO TIP
#         #print 'HERELeft', xb-2,yb
#         sol['sp_stop'].append(nom)
#         sol['loc_anas_tt'].append([xb-2,yb])
#         if not [xb-2,yb] in sol['PP']:
#             sol['pp'][(xb-2,yb)] = 'left'
#     
#     elif sol['b'][xpos_new,ypos_new] == 1: #ANASTOMOSIS TIP TO BRANCH 
#         for e, i in enumerate(sol['matrix_tip']):
#             if e != nom:
#                 for k in range(len(i)):
#                     if [xpos_new,ypos_new] != i[-1] and [xpos_new,ypos_new] == i[k]:
#                         sol['sp_stop'].append(nom)
#                         sol['loc_anas_tb'].append([xpos_new,ypos_new])        
#     else: 
    sol['tip_cell'].append([xpos_new,ypos_new])
    sol['n'][xpos_new,ypos_new] = 1
    return sol, list_prob_0, list_prob_1, tipp

def move_right(sol,nom,xb,yb,list_prob_0,list_prob_2): #2.2.(2).(2) 
    tipp = 'right'
    xpos_new = xb + 2
    ypos_new = yb
    sol['matrix_tip'][nom].append([xpos_new,ypos_new]) 
    sol['list_tip_movement'][nom] = tipp
    for i in list_prob_2:
        list_prob_0.append(i)
    list_prob_2 =[]
#     if sol['n'][xb+2,yb] == 1: #ANASTOMOSIS TIP TO TIP
#         #print 'HEREright', xb+2,yb
#         sol['sp_stop'].append(nom)
#         sol['loc_anas_tt'].append([xb+2,yb])
#         if not [xb+2,yb] in sol['PP']:
#             sol['pp'][(xb+2,yb)] = 'right'
#             sol['PP'].append([xb+2,yb])
#     elif sol['b'][xpos_new,ypos_new] == 1: #ANASTOMOSIS TIP TO BRANCH 
#         for e, i in enumerate(sol['matrix_tip']):
#             if e != nom:
#                 for k, pos in enumerate(i):
#                     if [xpos_new,ypos_new] != pos[-1] and [xpos_new,ypos_new] == pos[k]:
#                         sol['sp_stop'].append(nom)
#                         sol['loc_anas_tb'].append([xpos_new,ypos_new])  
#     else: 
    sol['tip_cell'].append([xpos_new,ypos_new])
    sol['n'][xpos_new,ypos_new] = 1
    return sol, list_prob_0, list_prob_2, tipp

def move_down(sol,nom,xb,yb,list_prob_0,list_prob_3): #2.2.(2).(3)
    tipp = 'down'
    xpos_new = xb
    ypos_new = yb - 2
    sol['matrix_tip'][nom].append([xpos_new,ypos_new]) 
    sol['list_tip_movement'][nom] = tipp
    for i in list_prob_3:
        list_prob_0.append(i)
    list_prob_3 =[]
#     if sol['n'][xb,yb-2] == 1: #ANASTOMOSIS TIP TO TIP
#         #print 'HEREdown', xb,yb-2
#         sol['sp_stop'].append(nom)
#         sol['loc_anas_tt'].append([xb,yb-2])
#         if not [xb,yb-2] in sol['PP']:
#             sol['pp'][(xb,yb-2)] = 'down'
#             sol['PP'].append([xb,yb-2])
#     elif sol['b'][xpos_new,ypos_new] == 1: #ANASTOMOSIS TIP TO BRANCH 
#         for e, i in enumerate(sol['matrix_tip']):
#             if e != nom:
#                 for k, pos in enumerate(i):
#                     if [xpos_new,ypos_new] != pos[-1] and [xpos_new,ypos_new] == pos[k]:
#                         sol['sp_stop'].append(nom)
#                         sol['loc_anas_tb'].append([xpos_new,ypos_new]) 
#     else: 
    sol['tip_cell'].append([xpos_new,ypos_new])
    sol['n'][xpos_new,ypos_new] = 1
    return sol, list_prob_0, list_prob_3, tipp

def move_up(sol,nom,xb,yb,list_prob_0,list_prob_4): #2.2.(2).(4)
    tipp = 'up'
    xpos_new = xb
    ypos_new = yb + 2
    sol['matrix_tip'][nom].append([xpos_new,ypos_new])
    sol['list_tip_movement'][nom] = tipp
    for i in list_prob_4:
        list_prob_0.append(i)
    list_prob_4 =[]
#     if sol['n'][xb,yb+2] == 1: #ANASTOMOSIS TIP TO TIP
#         #print 'HEREup',xb,yb+2
#         sol['sp_stop'].append(nom)
#         sol['loc_anas_tt'].append([xb,yb+2])
#         if not [xb,yb+2] in sol['PP']:
#             sol['pp'][(xb,yb+2)] = 'up'
#             sol['PP'].append([xb,yb+2])
#     elif sol['b'][xpos_new,ypos_new] == 1: #ANASTOMOSIS TIP TO BRANCH 
#         for e, i in enumerate(sol['matrix_tip']):
#             if e != nom:
#                 for k, pos in enumerate(i):
#                     if [xpos_new,ypos_new] != pos[-1] and [xpos_new,ypos_new] == pos[k]:
#                         sol['sp_stop'].append(nom)
#                         sol['loc_anas_tb'].append([xpos_new,ypos_new])   
#     else: 
    sol['tip_cell'].append([xpos_new,ypos_new])
    sol['n'][xpos_new,ypos_new] = 1
    return sol, list_prob_0, list_prob_4, tipp

def movement(sol,nom,xb,yb,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4): #2.2.(2)
    tes = randint(1,10000)
    if tes in list_prob_0:
        tipp = 'stay'
    elif tes in list_prob_1:
        if [xb,yb] in sol['tip_cell']: 
            sol['tip_cell'].remove([xb,yb])
        sol['n'][xb,yb] = 0
        sol, list_prob_0, list_prob_1, tipp = move_left(sol,nom,xb,yb,list_prob_0,list_prob_1) #2.2.(2).(1)
    elif tes in list_prob_2:   
        if [xb,yb] in sol['tip_cell']: 
            sol['tip_cell'].remove([xb,yb])
        sol['n'][xb,yb] = 0
        sol, list_prob_0, list_prob_2, tipp = move_right(sol,nom,xb,yb,list_prob_0,list_prob_2) #2.2.(2).(2)    
    elif tes in list_prob_3: 
        if [xb,yb] in sol['tip_cell']: 
            sol['tip_cell'].remove([xb,yb])
        sol['n'][xb,yb] = 0
        sol, list_prob_0, list_prob_3, tipp = move_down(sol,nom,xb,yb,list_prob_0,list_prob_3) #2.2.(2).(3)   
    elif tes in list_prob_4: 
        if [xb,yb] in sol['tip_cell']: 
            sol['tip_cell'].remove([xb,yb])
        sol['n'][xb,yb] = 0
        sol, list_prob_0, list_prob_4, tipp = move_up(sol,nom,xb,yb,list_prob_0,list_prob_4) #2.2.(2).(4)
    return sol,tipp,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4 

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

def move_left_branch(sol,nom,xb,yb,list_prob_0,list_prob_1): #2.2.(5).(1)
    tipp = 'left'
    xpos_new = xb - 2
    ypos_new = yb                    
    sol['matrix_tip'][-1].append([xpos_new,ypos_new])
    sol['list_tip_movement'][-1] = tipp   
    if sol['n'][xb-2,yb] == 1: #ANASTOMOSIS TIP TO TIP
        sol['sp_stop'].append(len(sol['matrix_tip'])-1)
        sol['loc_anas_tt'].append([xb-2,yb])
        if not [xb-2,yb] in sol['PP']:
            sol['pp'][(xb-2,yb)] = 'left'
            sol['PP'].append([xb-2,yb])
    elif sol['b'][xpos_new,ypos_new] == 1: #ANASTOMOSIS TIP TO BRANCH 
        for e, i in enumerate(sol['matrix_tip']):
            if e != nom:
                for k, pos in enumerate(i):
                    if [xpos_new,ypos_new] != pos[-1] and [xpos_new,ypos_new] == pos[k]:
                        sol['sp_stop'].append(nom)
                        sol['loc_anas_tb'].append([xpos_new,ypos_new]) 
    else: 
        sol['tip_cell'].append([xpos_new,ypos_new])
        sol['n'][xpos_new,ypos_new] = 1
    return sol, tipp
    
def move_right_branch(sol,nom,xb,yb,list_prob_0,list_prob_2): #2.2.(5).(2)
    tipp = 'right'
    xpos_new = xb + 2
    ypos_new = yb                    
    sol['matrix_tip'][-1].append([xpos_new,ypos_new])
    sol['list_tip_movement'][-1] = tipp   
    if sol['n'][xb+2,yb] == 1: #ANASTOMOSIS TIP TO TIP
        sol['sp_stop'].append(len(sol['matrix_tip'])-1)
        sol['loc_anas_tt'].append([xb+2,yb])
        if not [xb+2,yb] in sol['PP']:
            sol['pp'][(xb+2,yb)] = 'right'
            sol['PP'].append([xb+2,yb])
    elif sol['b'][xpos_new,ypos_new] == 1: #ANASTOMOSIS TIP TO BRANCH 
        for e, i in enumerate(sol['matrix_tip']):
            if e != nom:
                for k, pos in enumerate(i):
                    if [xpos_new,ypos_new] != pos[-1] and [xpos_new,ypos_new] == pos[k]:
                        sol['sp_stop'].append(nom)
                        sol['loc_anas_tb'].append([xpos_new,ypos_new]) 
    else: 
        sol['tip_cell'].append([xpos_new,ypos_new])
        sol['n'][xpos_new,ypos_new] = 1
    return sol, tipp

def move_down_branch(sol,nom,xb,yb,list_prob_0,list_prob_3): #2.2.(5).(3)
    tipp = 'down'
    xpos_new = xb
    ypos_new = yb - 2                    
    sol['matrix_tip'][-1].append([xpos_new,ypos_new])
    sol['list_tip_movement'][-1] = tipp   
    if sol['n'][xb,yb-2] == 1: #ANASTOMOSIS TIP TO TIP
        sol['sp_stop'].append(len(sol['matrix_tip'])-1)
        sol['loc_anas_tt'].append([xb,yb-2])
        if not [xb,yb-2] in sol['PP']:
            sol['pp'][(xb,yb-2)] = 'down'
            sol['PP'].append([xb,yb-2])
    elif sol['b'][xpos_new,ypos_new] == 1: #ANASTOMOSIS TIP TO BRANCH 
        for e, i in enumerate(sol['matrix_tip']):
            if e != nom:
                for k, pos in enumerate(i):
                    if [xpos_new,ypos_new] != pos[-1] and [xpos_new,ypos_new] == pos[k]:
                        sol['sp_stop'].append(nom)
                        sol['loc_anas_tb'].append([xpos_new,ypos_new])  
    else: 
        sol['tip_cell'].append([xpos_new,ypos_new])
        sol['n'][xpos_new,ypos_new] = 1
    return sol, tipp

def move_up_branch(sol,nom,xb,yb,list_prob_0,list_prob_4): #2.2.(5).(4)
    tipp = 'up'
    xpos_new = xb
    ypos_new = yb + 2                    
    sol['matrix_tip'][-1].append([xpos_new,ypos_new])
    sol['list_tip_movement'][-1] = tipp   
    if sol['n'][xb,yb+2] == 1: #ANASTOMOSIS TIP TO TIP
        sol['sp_stop'].append(len(sol['matrix_tip'])-1)
        sol['loc_anas_tt'].append([xb,yb+2])
        if not [xb,yb+2] in sol['PP']:
            sol['pp'][(xb,yb+2)] = 'up'
            sol['PP'].append([xb,yb+2])
    elif sol['b'][xpos_new,ypos_new] == 1: #ANASTOMOSIS TIP TO BRANCH 
        for e, i in enumerate(sol['matrix_tip']):
            if e != nom:
                for k, pos in enumerate(i):
                    if [xpos_new,ypos_new] != pos[-1] and [xpos_new,ypos_new] == pos[k]:
                        sol['sp_stop'].append(nom)
                        sol['loc_anas_tb'].append([xpos_new,ypos_new])  
    else: 
        sol['tip_cell'].append([xpos_new,ypos_new])
        sol['n'][xpos_new,ypos_new] = 1
    return sol, tipp

def movement_branch(tipp,sol,nom,xb,yb,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4): #2.2.(5)
    tes = randint(1,10000)
    if tes in list_prob_0:
        tipp = 'stay'
    elif tes in list_prob_1:
        sol, tipp = move_left_branch(sol,nom,xb,yb,list_prob_0,list_prob_1) #2.2.(5).(1)
    elif tes in list_prob_2:   
        sol, tipp = move_right_branch(sol,nom,xb,yb,list_prob_0,list_prob_2) #2.2.(5).(2)
    elif tes in list_prob_3:
        sol, tipp = move_down_branch(sol,nom,xb,yb,list_prob_0,list_prob_3) #2.2.(5).(3)
    elif tes in list_prob_4: 
        sol, tipp = move_up_branch(sol,nom,xb,yb,list_prob_0,list_prob_4) #2.2.(5).(4)
    return sol, tipp

def hybrid_tech(coef, set, sol): #2.2
    n_sp = len(sol['matrix_tip']) #to save original number of tips before branching
    n_o = numpy.copy(sol['n'])
    vn_o = []
    for nom in range(0,n_sp): #dicek setiap tip
        if not nom in sol['sp_stop']: #kalo dia sudah anastomosis, gak perlu branching dan move lg.
            xb = sol['matrix_tip'][nom][-1][0] #get x position of last tip position
            yb = sol['matrix_tip'][nom][-1][1] #get y position of last tip position
            vn_o.append([xb,yb])
            
            dirr= movement_dir(coef, set, sol, xb, yb, nom) #2.2.1 ok
            
            if dirr[1] == 0 and dirr[2] == 0 and dirr[3] == 0 and dirr[4] == 0: #if no space
                sol['sp_stop'].append(nom)
                sol['tip_cell'].remove([xb,yb])
                sol['n'][xb,yb] = 0
            else:
                '''Making list of prob'''
                list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4 = set_list_prob(dirr) #2.2.(1)
                                
                '''The Movement'''
                sol,tipp,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4 = movement(sol,nom,xb,yb,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4) #2.2.(2)
                
                '''2.1 Branching Decision
                PP = 'test'
                if tipp == 'stay' and PP == 'test': #not able to branch, PP untuk pertama kali 
                    sol['life_time_tip'][nom] += set['dt']
                    sol['life_mit'][nom] += set['dt']
                else: #there is possibility to branch
                    #print 'YAYAYA1'
                    if movi == True:
                        sol['PP'].remove([xb,yb])
                        sol['pp'].pop((xb,yb))
                    if dirr.count(0) >= 3: #no space to move
                        sol['life_time_tip'][nom] += set['dt']
                        sol['life_mit'][nom] += set['dt']
                    else: #there is possibility to branch
                        #print 'YAYAYA2'
                        #print sol['life_time_tip'][nom]
                        if sol['life_time_tip'][nom] < coef['T_branch']: #not able to branch
                            sol['life_time_tip'][nom] += set['dt']
                            sol['life_mit'][nom] += set['dt']
                        else: #there is possibility to branch
                            #print 'YAYAYA3'
#                             Probability of Branching using c  
                            list_prob = range(1,11)#prob_by_c(sol,xb,yb) #2.2.(4)
                            tes = randint(1,10)
                            if not tes in list_prob: #not able to branch
                                sol['life_time_tip'][nom] += set['dt']
                                sol['life_mit'][nom] += set['dt']
                            else: #BRANCHING!
                                #print 'YAYAYA4'
                                sol['life_time_tip'][nom] = 0
                                sol['life_mit'][nom] += set['dt']
                                sol['matrix_tip'].append([(xb,yb)])
                                sol['life_time_tip'].append(0)
                                sol['life_mit'].append(0)
                                sol['list_tip_movement'].append('start')
                                tipp = 'stay'
#                                 The Movement from branching
                                while tipp == 'stay':
                                    sol, tipp = movement_branch(tipp,sol,nom,xb,yb,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4) #2.2.(5)
                    '''
    '''Vector Velocity of stalk (Vb)'''
    for y in range(1,set['Ny'],2):
        for x in range(1,set['Nx'],2):
            vb_x = 0
            vb_y = 0
            for ind, vec in enumerate(vn_o):
                if x == vec[0] and y == vec[1]:
                    leave = 22
                else:
                    s = m.sqrt((x-vec[0])**2+(y-vec[1])**2)
                    if s <= 50:
                        h_s = 0.5 + coef['m1']*(s-2)
                    elif s <= 100:
                        h_s = 0.2 + coef['m2']*(s-50)
                    elif s <= 200:
                        h_s = 1 + coef['m3']*(s-100)
                    else:
                        h_s = 0
                    vb_x += (vec[0]-x)*h_s/s
                    vb_y += (vec[1]-y)*h_s/s
            sol['Vb_x'][x,y] = vb_x
            sol['Vb_y'][x,y] = vb_y
#     print 'Tip cell position:', vn_o
#     print 'Velocity Vector stalk on [3,201]: [',sol['Vb_x'][3,201],',',sol['Vb_y'][3,201],']'
    return sol, n_o