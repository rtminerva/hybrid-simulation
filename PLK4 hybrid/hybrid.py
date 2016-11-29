from dirrection_of_movement import movement_dir #2.2.1
import random
import numpy
from random import randint
from collections import OrderedDict

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
    for i in list_prob_1:
        list_prob_0.append(i)
    list_prob_1 =[]    
    return sol, tipp, list_prob_0, list_prob_1

def move_right(sol,nom,xb,yb,list_prob_0,list_prob_2): #2.2.(2).(2)
    tipp = 'right' 
    xpos_new = xb + 2
    ypos_new = yb
    sol['matrix_tip'][nom].append([xpos_new,ypos_new]) 
    for i in list_prob_2:
        list_prob_0.append(i)
    list_prob_2 =[]
    #sol['tip_cell'].remove([xb,yb])
    return sol, tipp, list_prob_0, list_prob_2

def move_down(sol,nom,xb,yb,list_prob_0,list_prob_3): #2.2.(2).(3)
    tipp = 'down'
    xpos_new = xb
    ypos_new = yb - 2
    sol['matrix_tip'][nom].append([xpos_new,ypos_new]) 
    for i in list_prob_3:
        list_prob_0.append(i)
    list_prob_3 =[]
    #sol['tip_cell'].remove([xb,yb])
    return sol, tipp, list_prob_0, list_prob_3

def move_up(sol,nom,xb,yb,list_prob_0,list_prob_4): #2.2.(2).(4)
    tipp = 'up'
    xpos_new = xb
    ypos_new = yb + 2
    sol['matrix_tip'][nom].append([xpos_new,ypos_new])
    for i in list_prob_4:
        list_prob_0.append(i)
    list_prob_4 =[]
    #sol['tip_cell'].remove([xb,yb])
    return sol, tipp, list_prob_0, list_prob_4

def movement(sol,nom,xb,yb,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4): #2.2.(2)
    tes = randint(1,10000)
    if tes in list_prob_0:
        tipp = 'stay'
    elif tes in list_prob_1:
        sol['jum_X4'][xb,yb] -=1
        sol['jum_X4'][xb-2,yb] +=1
        sol, tipp, list_prob_0, list_prob_1 = move_left(sol,nom,xb,yb,list_prob_0,list_prob_1) #2.2.(2).(1)
    elif tes in list_prob_2: 
        sol['jum_X4'][xb,yb] -=1
        sol['jum_X4'][xb+2,yb] +=1  
        sol, tipp, list_prob_0, list_prob_2 = move_right(sol,nom,xb,yb,list_prob_0,list_prob_2) #2.2.(2).(2)    
    elif tes in list_prob_3: 
        sol['jum_X4'][xb,yb] -=1
        sol['jum_X4'][xb,yb-2] +=1
        sol, tipp, list_prob_0, list_prob_3 = move_down(sol,nom,xb,yb,list_prob_0,list_prob_3) #2.2.(2).(3)   
    elif tes in list_prob_4:
        sol['jum_X4'][xb,yb] -=1 
        sol['jum_X4'][xb,yb+2] +=1
        sol, tipp, list_prob_0, list_prob_4 = move_up(sol,nom,xb,yb,list_prob_0,list_prob_4) #2.2.(2).(4)
    return sol,tipp

def absorbed_f(sol,set,nom):
    if sol['matrix_tip'][nom][-1][0] == set['Nx']-1 and sol['matrix_tip'][nom][-1][1] == set['Ny']-1:
        sol['matrix_tip_die'].append(sol['matrix_tip'][nom])
        sol['matrix_tip'].pop(nom)
        sol['jum_X4'][sol['matrix_tip'][nom][-1][0],sol['matrix_tip'][nom][-1][1]] -= 1
        abs = 'yes'
        sol['num_of_absorbed'] += 1
    else:
        abs = 'no'
    return sol, abs

def hybrid_tech_c(coef, set, sol): #2.2
    n_sp = len(sol['matrix_tip']) #to save original number of tips before branching
    sol['tip_cell'] = []
    for nom in range(0,n_sp): #dicek setiap element
        xb = sol['matrix_tip'][nom][-1][0] #get x position of last tip position
        yb = sol['matrix_tip'][nom][-1][1] #get y position of last tip position
        
        dirr= movement_dir(coef, set, sol, xb, yb, nom) #2.2.1 ok
    
        '''Making list of prob'''
        list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4 = set_list_prob(dirr) #2.2.(1)
                        
        '''The Movement'''
        sol,tipp = movement(sol,nom,xb,yb,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4) #2.2.(2)
        
        '''Checking if X4 is absorbed'''
        if not tipp == 'stay':
            sol, abs = absorbed_f(sol,set,nom)
        else:
            abs = 'no'
        if abs == 'no':
            sol['tip_cell'].append(sol['matrix_tip'][nom][-1])
    return sol