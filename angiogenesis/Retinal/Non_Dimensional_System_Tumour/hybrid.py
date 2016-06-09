import random
from random import randint
from dirrection_of_movement import movement_dir

def set_list_prob(dirr):
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

def anastomosis_tip_tip(sol,nom):
    for e,tep in enumerate(range(0,len(sol['matrix_tip']))):
        if not tep == nom:
            #jj = len(sol['matrix_tip'][tep])-2
            if sol['matrix_tip'][nom][-1] == sol['matrix_tip'][tep][-1]:
                sol['sp_stop'].append(nom)
                if [sol['matrix_tip'][nom][-1][0],sol['matrix_tip'][nom][-1][1]] in sol['tip_cell']:
                    sol['tip_cell'].remove([sol['matrix_tip'][nom][-1][0],sol['matrix_tip'][nom][-1][1]])
                
            #elif sol['matrix_tip'][nom][-1] == sol['matrix_tip'][tep][jj] and sol['matrix_tip'][tep][-1] == (xb,yb):
    return sol

def anastomosis_tip_branch(sol,nom,xb,yb,ml,mr,md,mu,tip_l,tip_r,tip_d,tip_u):
    lx = xb - 2
    rx = xb + 2
    dy = yb - 2
    uy = yb + 2
    for e,tep in enumerate(range(0,len(sol['matrix_tip']))):
        if not tep == nom:
            if (lx,yb) in sol['matrix_tip'][tep]:
                ml = 'stop'
                if (lx,yb) == sol['matrix_tip'][tep][-1]:
                    tip_l = e
            if (rx,yb) in sol['matrix_tip'][tep]:
                mr = 'stop'
                if (rx,yb) == sol['matrix_tip'][tep][-1]:
                    tip_r = e
            if (xb,dy) in sol['matrix_tip'][tep]:
                md = 'stop'
                if (xb,dy) == sol['matrix_tip'][tep][-1]:
                    tip_d = e
            if (xb,uy) in sol['matrix_tip'][tep]:
                mu = 'stop'
                if (xb,uy) == sol['matrix_tip'][tep][-1]:
                    tip_u = e
    return ml, mr, md, mu, tip_l, tip_r, tip_d, tip_u

def move_left(sol,nom,xb,yb,list_prob_0,list_prob_1,ml,tip_l):
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
            if str(tip_l) in sol['pp']:
                sol['pp'][tip_l][0] = 'right'
            else:
                sol['pp'][tip_l] = ['right','a','a','a']
        else:
            if [xb,yb] in sol['tip_cell']:
                sol['tip_cell'].remove([xb,yb])
    else:
        if [xb,yb] in sol['tip_cell']:
            sol['tip_cell'].remove([xb,yb])
        sol['tip_cell'].append([xpos_new,ypos_new])
    return sol, list_prob_0, list_prob_1, tipp

def move_right(sol,nom,xb,yb,list_prob_0,list_prob_2,mr,tip_r):
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
            if str(tip_r) in sol['pp']:
                sol['pp'][tip_r][1] = 'left'
            else:
                sol['pp'][tip_r] = ['a','left','a','a']
        else:
            if [xb,yb] in sol['tip_cell']:
                sol['tip_cell'].remove([xb,yb])       
    else:
        if [xb,yb] in sol['tip_cell']:
            sol['tip_cell'].remove([xb,yb])
        sol['tip_cell'].append([xpos_new,ypos_new])
    return sol, list_prob_0, list_prob_2, tipp

def move_down(sol,nom,xb,yb,list_prob_0,list_prob_3,md,tip_d):
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
            if str(tip_d) in sol['pp']:
                sol['pp'][tip_d][2] = 'up'
            else:
                sol['pp'][tip_d] = ['a','a','up','a']
        else:
            if [xb,yb] in sol['tip_cell']:
                sol['tip_cell'].remove([xb,yb])
    else:
        if [xb,yb] in sol['tip_cell']:
            sol['tip_cell'].remove([xb,yb])
        sol['tip_cell'].append([xpos_new,ypos_new])
    return sol, list_prob_0, list_prob_3, tipp

def move_up(sol,nom,xb,yb,list_prob_0,list_prob_4,mu,tip_u):
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
            if str(tip_u) in sol['pp']:
                sol['pp'][tip_u][3] = 'down'
            else:
                sol['pp'][tip_u] = ['a','a','a','down']
        else:
            if [xb,yb] in sol['tip_cell']:
                sol['tip_cell'].remove([xb,yb])
    else:
        if [xb,yb] in sol['tip_cell']:
            sol['tip_cell'].remove([xb,yb])
        sol['tip_cell'].append([xpos_new,ypos_new])
    return sol, list_prob_0, list_prob_4, tipp

def movement(sol,nom,xb,yb,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4,ml,mr,md,mu,tip_l,tip_r,tip_d,tip_u):
    if nom in sol['pp']:
        tipp = 'stay'
        oo = 0
        while tipp == 'stay' and oo < 1000:
            oo +=1
            tes = randint(1,10000)
            if tes in list_prob_0:
                tipp = 'stay'
            elif tes in list_prob_1:
                sol, list_prob_0, list_prob_1, tipp = move_left(sol,nom,xb,yb,list_prob_0,list_prob_1,ml,tip_l)
            elif tes in list_prob_2:   
                sol, list_prob_0, list_prob_2, tipp = move_right(sol,nom,xb,yb,list_prob_0,list_prob_2,mr,tip_r)    
            elif tes in list_prob_3: 
                sol, list_prob_0, list_prob_3, tipp = move_down(sol,nom,xb,yb,list_prob_0,list_prob_3,md,tip_d)   
            elif tes in list_prob_4: 
                sol, list_prob_0, list_prob_4, tipp = move_up(sol,nom,xb,yb,list_prob_0,list_prob_4,mu,tip_u)
    else:
        tes = randint(1,10000)
        if tes in list_prob_0:
            tipp = 'stay'
        elif tes in list_prob_1:
            sol, list_prob_0, list_prob_1, tipp = move_left(sol,nom,xb,yb,list_prob_0,list_prob_1,ml,tip_l)
        elif tes in list_prob_2:   
            sol, list_prob_0, list_prob_2, tipp = move_right(sol,nom,xb,yb,list_prob_0,list_prob_2,mr,tip_r)    
        elif tes in list_prob_3: 
            sol, list_prob_0, list_prob_3, tipp = move_down(sol,nom,xb,yb,list_prob_0,list_prob_3,md,tip_d)   
        elif tes in list_prob_4: 
            sol, list_prob_0, list_prob_4, tipp = move_up(sol,nom,xb,yb,list_prob_0,list_prob_4,mu,tip_u)
    return sol,tipp,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4 

def prob_by_c(sol,xb,yb):
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

def move_left_branch(sol,xb,yb,list_prob_0,list_prob_1,ml,tip_l):
    tipp = 'left'
    xpos_new = sol['matrix_tip'][-1][-1][0] - 2
    ypos_new = sol['matrix_tip'][-1][-1][1]                    
    sol['matrix_tip'][-1].append((xpos_new,ypos_new))
    sol['n'][xpos_new,ypos_new] = 1
    sol['list_tip_movement'][-1] = tipp
    if ml == 'stop':
        sol['sp_stop'].append(len(sol['matrix_tip'])-1)
        if tip_l>=0:
            sol['pp'][tip_l][0] = 'right'
    else:
        sol['tip_cell'].append([xpos_new,ypos_new])
    return sol, tipp

def move_right_branch(sol,xb,yb,list_prob_0,list_prob_2,mr,tip_r):
    tipp = 'right'
    xpos_new = sol['matrix_tip'][-1][-1][0] + 2
    ypos_new = sol['matrix_tip'][-1][-1][1]
    sol['matrix_tip'][-1].append((xpos_new,ypos_new)) 
    sol['n'][xpos_new,ypos_new] = 1
    sol['list_tip_movement'][-1] = tipp
    if mr == 'stop':
        sol['sp_stop'].append(len(sol['matrix_tip'])-1)
        if tip_r>=0:
            sol['pp'][tip_r][1] = 'left'
    else:
        sol['tip_cell'].append([xpos_new,ypos_new])
    return sol, tipp

def move_down_branch(sol,xb,yb,list_prob_0,list_prob_3,md,tip_d):
    tipp = 'down'
    xpos_new = sol['matrix_tip'][-1][-1][0]
    ypos_new = sol['matrix_tip'][-1][-1][1] - 2
    sol['matrix_tip'][-1].append((xpos_new,ypos_new)) 
    sol['n'][xpos_new,ypos_new] = 1
    sol['list_tip_movement'][-1] = tipp
    if md == 'stop':
        sol['sp_stop'].append(len(sol['matrix_tip'])-1)
        if tip_d>=0:
            sol['pp'][tip_d][2] = 'up'
    else:
        sol['tip_cell'].append([xpos_new,ypos_new])
    return sol, tipp

def move_up_branch(sol,xb,yb,list_prob_0,list_prob_4,mu,tip_u):
    tipp = 'up'
    xpos_new = sol['matrix_tip'][-1][-1][0]
    ypos_new = sol['matrix_tip'][-1][-1][1] + 2
    sol['matrix_tip'][-1].append((xpos_new,ypos_new))
    sol['n'][xpos_new,ypos_new] = 1
    sol['list_tip_movement'][-1] = tipp
    if mu == 'stop':
        sol['sp_stop'].append(len(sol['matrix_tip'])-1)
        if tip_u>=0:
            sol['pp'][tip_u][3] = 'down'
    else:
        sol['tip_cell'].append([xpos_new,ypos_new])
    return sol, tipp

def movement_branch(tipp,sol,xb,yb,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4,ml,mr,md,mu,tip_l,tip_r,tip_d,tip_u):
    tes = randint(1,10000)
    if tes in list_prob_0:
        tipp = 'stay'
    elif tes in list_prob_1:
        sol, tipp = move_left_branch(sol,xb,yb,list_prob_0,list_prob_1,ml,tip_l)
    elif tes in list_prob_2:   
        sol, tipp = move_right_branch(sol,xb,yb,list_prob_0,list_prob_2,mr,tip_r)
    elif tes in list_prob_3: 
        sol, tipp = move_down_branch(sol,xb,yb,list_prob_0,list_prob_3,md,tip_d)
    elif tes in list_prob_4: 
        sol, tipp = move_up_branch(sol,xb,yb,list_prob_0,list_prob_4,mu,tip_u)
    return sol, tipp

def hybrid_tech_c(coef, set, sol):
    n_sp = len(sol['matrix_tip']) #to save original number of tips before branching
    
    for nom in range(0,n_sp): #dicek setiap tip
        if not nom in sol['sp_stop']: #kalo dia sudah anastomosis, gak perlu branching dan move lg.
            xb = sol['matrix_tip'][nom][-1][0] #get x position of last tip position
            yb = sol['matrix_tip'][nom][-1][1] #get y position of last tip position

            dirr= movement_dir(coef, set, sol, xb, yb, nom)
            
            if dirr[1] == 0 and dirr[2] == 0 and dirr[3] == 0 and dirr[4] == 0:
                sol['sp_stop'].append(nom)
                sol['tip_cell'].remove([xb,yb])
                
            else:
                '''Making list of prob'''
                list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4 = set_list_prob(dirr)
                
                '''Checking Space for n #if meet vessel'''
                ml = 'f'
                mr = 'f'
                md = 'f'
                mu = 'f'
                tip_l = -1
                tip_r = -1
                tip_d = -1
                tip_u = -1
                
                '''
                ml, mr, md, mu, tip_l, tip_r, tip_d, tip_u = anastomosis_tip_branch(sol,nom,xb,yb,ml,mr,md,mu,tip_l,tip_r,tip_d,tip_u)
                sol['pp'] ={}
                ml = 'f'
                mr = 'f'
                md = 'f'
                mu = 'f'
                
                tip_l = -1
                tip_r = -1
                tip_d = -1
                tip_u = -1
                '''
                
                '''The Movement'''
                sol,tipp,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4 = movement(sol,nom,xb,yb,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4,ml,mr,md,mu,tip_l,tip_r,tip_d,tip_u)
                
                '''Test Anastomosis tip-tip if move'''
                if not tipp == 'stay':
                    sol=anastomosis_tip_tip(sol,nom)
                
                '''2.1 Branching Decision'''
                if tipp == 'stay': #not able to branch
                    sol['life_time_tip'][nom] += set['dt']
                else: #there is possibility to branch
                    cek = str(nom)
                    if dirr.count(0) >= 3: #no space to move
                        sol['life_time_tip'][nom] += set['dt']
                        if cek in sol['pp']:
                            sol['pp'].pop('cek')
                    else: #there is possibility to branch
                        if sol['life_time_tip'][nom] < coef['T_branch']: #not able to branch
                            sol['life_time_tip'][nom] += set['dt']
                            if cek in sol['pp']:
                                sol['pp'].pop('cek')
                        else: #there is possibility to branch
                            '''Probability of Branching using c'''   
                            list_prob = prob_by_c(sol,xb,yb)
                            tes = randint(1,10)
                            if not tes in list_prob: #not able to branch
                                sol['life_time_tip'][nom] += set['dt']
                                if cek in sol['pp']:
                                    sol['pp'].pop('cek')
                            else: #BRANCHING!
                                sol['life_time_tip'][nom] = 0
                                sol['matrix_tip'].append([(xb,yb)])
                                sol['life_time_tip'].append(0)
                                sol['list_tip_movement'].append('start')
                                tipp = 'stay'
                                if cek in sol['pp']:
                                    sol['pp'].pop('cek')
                                '''The Movement from branching'''
                                while tipp == 'stay':
                                    sol, tipp = movement_branch(tipp,sol,xb,yb,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4,ml,mr,md,mu,tip_l,tip_r,tip_d,tip_u)
                                
                                '''Check Anastomosis'''
                                sol=anastomosis_tip_tip(sol,len(sol['matrix_tip'])-1)
    return sol