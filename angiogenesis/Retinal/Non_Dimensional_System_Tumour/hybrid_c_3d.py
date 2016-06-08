import random
from random import randint
from dirrection_of_movement_3d import movement_dir_3d

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
    if dirr[5] == 0:
        list_prob_5 = []
    else:
        list_prob_5 = random.sample(line_1, dirr[5])
        for i in list_prob_5:
            line_1.remove(i)
    if dirr[6] == 0:
        list_prob_6 = []
    else:
        list_prob_6 = random.sample(line_1, dirr[6])
        for i in list_prob_6:
            line_1.remove(i)
    list_prob_0 = line_1
    return list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4,list_prob_5,list_prob_6

def anastomosis_tip_tip(sol,nom,set):
    for e,tep in enumerate(range(0,len(sol['matrix_tip']))):
        if not tep == nom:
            #jj = len(sol['matrix_tip'][tep])-2
            if sol['matrix_tip'][nom][-1] == sol['matrix_tip'][tep][-1]:
                sol['sp_stop'].append(nom)
                if [sol['matrix_tip'][nom][-1][0],sol['matrix_tip'][nom][-1][1],sol['matrix_tip'][nom][-1][2]] in sol['tip_cell']:
                    sol['tip_cell'].remove([sol['matrix_tip'][nom][-1][0],sol['matrix_tip'][nom][-1][1],sol['matrix_tip'][nom][-1][2]])
                
            #elif sol['matrix_tip'][nom][-1] == sol['matrix_tip'][tep][jj] and sol['matrix_tip'][tep][-1] == (xb,yb):
    if set['parent'] == 'two':
        for tep in range(0,len(sol['matrix_tip_2'])):
            if sol['matrix_tip'][nom][-1] == sol['matrix_tip_2'][tep][-1]:
                sol['sp_stop'].append(nom)
                if [sol['matrix_tip'][nom][-1][0],sol['matrix_tip'][nom][-1][1],sol['matrix_tip'][nom][-1][2]] in sol['tip_cell']:
                    sol['tip_cell'].remove([sol['matrix_tip'][nom][-1][0],sol['matrix_tip'][nom][-1][1],sol['matrix_tip'][nom][-1][2]])
    return sol

def anastomosis_tip_branch(sol,nom,xb,yb,zb,ml,mr,md,mu,mzd,mzu,tip_l,tip_r,tip_d,tip_u,tip_zd,tip_zu):
    lx = xb - 2
    rx = xb + 2
    dy = yb - 2
    uy = yb + 2
    dz = zb - 2
    uz = zb + 2
    for e,tep in enumerate(range(0,len(sol['matrix_tip']))):
        if not tep == nom:
            if (lx,yb,zb) in sol['matrix_tip'][tep]:
                ml = 'stop'
                if [lx,yb,zb] in sol['matrix_tip'][tep][-1]:
                    tip_l = e
            if (rx,yb,zb) in sol['matrix_tip'][tep]:
                mr = 'stop'
                if [rx,yb,zb] in sol['matrix_tip'][tep][-1]:
                    tip_r = e
                    
            if (xb,dy,zb) in sol['matrix_tip'][tep]:
                md = 'stop'
                if [xb,dy,zb] in sol['matrix_tip'][tep][-1]:
                    tip_d = e
            if (xb,uy,zb) in sol['matrix_tip'][tep]:
                mu = 'stop'
                if [xb,uy,zb] in sol['matrix_tip'][tep][-1]:
                    tip_u = e
                    
            if (xb,yb,dz) in sol['matrix_tip'][tep]:
                mzd = 'stop'
                if [xb,yb,dz] in sol['matrix_tip'][tep][-1]:
                    tip_zd = e
            if (xb,yb,uz) in sol['matrix_tip'][tep]:
                mzu = 'stop'
                if [xb,yb,dz] in sol['matrix_tip'][tep][-1]:
                    tip_zu = e
    return ml,mr,md,mu,mzd,mzu,tip_l,tip_r,tip_d,tip_u,tip_zd,tip_zu

def move_left(sol,nom,xb,yb,zb,list_prob_0,list_prob_1,ml,tip_l):
    tipp = 'left'
    xpos_new = sol['matrix_tip'][nom][-1][0] - 2
    ypos_new = sol['matrix_tip'][nom][-1][1]   
    zpos_new = sol['matrix_tip'][nom][-1][2]                 
    sol['matrix_tip'][nom].append((xpos_new,ypos_new,zpos_new))
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
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
                sol['pp'][tip_l] = ['right','a','a','a','a','a']
        else:
            if [xb,yb,zb] in sol['tip_cell']:
                sol['tip_cell'].remove([xb,yb,zb])
    else:
        if [xb,yb,zb] in sol['tip_cell']:
            sol['tip_cell'].remove([xb,yb,zb])
        sol['tip_cell'].append([xpos_new,ypos_new,zpos_new])
    return sol, list_prob_0, list_prob_1, tipp

def move_right(sol,nom,xb,yb,zb,list_prob_0,list_prob_2,mr,tip_r):
    tipp = 'right'
    xpos_new = sol['matrix_tip'][nom][-1][0] + 2
    ypos_new = sol['matrix_tip'][nom][-1][1]
    zpos_new = sol['matrix_tip'][nom][-1][2]
    sol['matrix_tip'][nom].append((xpos_new,ypos_new,zpos_new)) 
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
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
                sol['pp'][tip_r] = ['a','left','a','a','a','a']    
        else:
            if [xb,yb,zb] in sol['tip_cell']:
                sol['tip_cell'].remove([xb,yb,zb])   
    else:
        if [xb,yb,zb] in sol['tip_cell']:
            sol['tip_cell'].remove([xb,yb,zb])
        sol['tip_cell'].append([xpos_new,ypos_new,zpos_new])
    return sol, list_prob_0, list_prob_2, tipp

def move_down(sol,nom,xb,yb,zb,list_prob_0,list_prob_3,md,tip_d):
    tipp = 'down'
    xpos_new = sol['matrix_tip'][nom][-1][0]
    ypos_new = sol['matrix_tip'][nom][-1][1] - 2
    zpos_new = sol['matrix_tip'][nom][-1][2]
    sol['matrix_tip'][nom].append((xpos_new,ypos_new,zpos_new)) 
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
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
                sol['pp'][tip_d] = ['a','a','up','a','a','a']
        else:
            if [xb,yb,zb] in sol['tip_cell']:
                sol['tip_cell'].remove([xb,yb,zb])
    else:
        if [xb,yb,zb] in sol['tip_cell']:
            sol['tip_cell'].remove([xb,yb,zb])
        sol['tip_cell'].append([xpos_new,ypos_new,zpos_new])
    return sol, list_prob_0, list_prob_3, tipp

def move_up(sol,nom,xb,yb,zb,list_prob_0,list_prob_4,mu,tip_u):
    tipp = 'up'
    xpos_new = sol['matrix_tip'][nom][-1][0]
    ypos_new = sol['matrix_tip'][nom][-1][1] + 2
    zpos_new = sol['matrix_tip'][nom][-1][2]
    sol['matrix_tip'][nom].append((xpos_new,ypos_new,zpos_new))
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
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
                sol['pp'][tip_u] = ['a','a','a','down','a','a']
        else:
            if [xb,yb,zb] in sol['tip_cell']:
                sol['tip_cell'].remove([xb,yb,zb])
    else:
        if [xb,yb,zb] in sol['tip_cell']:
            sol['tip_cell'].remove([xb,yb,zb])
        sol['tip_cell'].append([xpos_new,ypos_new,zpos_new])
    return sol, list_prob_0, list_prob_4, tipp

def move_zdown(sol,nom,xb,yb,zb,list_prob_0,list_prob_5,mzd,tip_zd):
    tipp = 'down'
    xpos_new = sol['matrix_tip'][nom][-1][0]
    ypos_new = sol['matrix_tip'][nom][-1][1]
    zpos_new = sol['matrix_tip'][nom][-1][2] - 2
    sol['matrix_tip'][nom].append((xpos_new,ypos_new,zpos_new)) 
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
    sol['list_tip_movement'][nom] = tipp
    for i in list_prob_5:
        list_prob_0.append(i)
    list_prob_5 =[]
    if mzd == 'stop':
        sol['sp_stop'].append(nom)
        if tip_zd>=0:
            if str(tip_zd) in sol['pp']:
                sol['pp'][tip_zd][4] = 'up'
            else:
                sol['pp'][tip_zd] = ['a','a','a','a','up','a']
        else:
            if [xb,yb,zb] in sol['tip_cell']:
                sol['tip_cell'].remove([xb,yb,zb])
    else:
        if [xb,yb,zb] in sol['tip_cell']:
            sol['tip_cell'].remove([xb,yb,zb])
        sol['tip_cell'].append([xpos_new,ypos_new,zpos_new])
    return sol, list_prob_0, list_prob_5, tipp

def move_zup(sol,nom,xb,yb,zb,list_prob_0,list_prob_6,mzu,tip_zu):
    tipp = 'up'
    xpos_new = sol['matrix_tip'][nom][-1][0]
    ypos_new = sol['matrix_tip'][nom][-1][1] 
    zpos_new = sol['matrix_tip'][nom][-1][2] + 2
    sol['matrix_tip'][nom].append((xpos_new,ypos_new,zpos_new))
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
    sol['list_tip_movement'][nom] = tipp
    for i in list_prob_6:
        list_prob_0.append(i)
    list_prob_6 =[]
    if mzu == 'stop':
        sol['sp_stop'].append(nom)
        if tip_zu>=0:
            if str(tip_zu) in sol['pp']:
                sol['pp'][tip_zu][5] = 'down'
            else:
                sol['pp'][tip_zu] = ['a','a','a','a','a','down']
        else:
            if [xb,yb,zb] in sol['tip_cell']:
                sol['tip_cell'].remove([xb,yb,zb])
    else:
        if [xb,yb,zb] in sol['tip_cell']:
            sol['tip_cell'].remove([xb,yb,zb])
        sol['tip_cell'].append([xpos_new,ypos_new,zpos_new])
    return sol, list_prob_0, list_prob_6, tipp

def movement(sol,nom,xb,yb,zb,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4,list_prob_5,list_prob_6,ml,mr,md,mu,mzd,mzu,tip_l,tip_r,tip_d,tip_u,tip_zd,tip_zu):
    if nom in sol['pp']:
        tipp = 'stay'
        oo = 0
        while tipp == 'stay' and oo < 1000:
            oo +=1
            tes = randint(1,10000)
            if tes in list_prob_0:
                tipp = 'stay'
            elif tes in list_prob_1:
                sol, list_prob_0, list_prob_1, tipp = move_left(sol,nom,xb,yb,zb,list_prob_0,list_prob_1,ml,tip_l)
            elif tes in list_prob_2:   
                sol, list_prob_0, list_prob_2, tipp = move_right(sol,nom,xb,yb,zb,list_prob_0,list_prob_2,mr,tip_r)    
            elif tes in list_prob_3: 
                sol, list_prob_0, list_prob_3, tipp = move_down(sol,nom,xb,yb,zb,list_prob_0,list_prob_3,md,tip_d)   
            elif tes in list_prob_4: 
                sol, list_prob_0, list_prob_4, tipp = move_up(sol,nom,xb,yb,zb,list_prob_0,list_prob_4,mu,tip_u)
            elif tes in list_prob_5: 
                sol, list_prob_0, list_prob_5, tipp = move_zdown(sol,nom,xb,yb,zb,list_prob_0,list_prob_5,mzd,tip_zd)   
            elif tes in list_prob_6: 
                sol, list_prob_0, list_prob_6, tipp = move_zup(sol,nom,xb,yb,zb,list_prob_0,list_prob_6,mzu,tip_zu)
    else:
        tes = randint(1,10000)
        if tes in list_prob_0:
            tipp = 'stay'
        elif tes in list_prob_1:
            sol, list_prob_0, list_prob_1, tipp = move_left(sol,nom,xb,yb,zb,list_prob_0,list_prob_1,ml,tip_l)
        elif tes in list_prob_2:   
            sol, list_prob_0, list_prob_2, tipp = move_right(sol,nom,xb,yb,zb,list_prob_0,list_prob_2,mr,tip_r)    
        elif tes in list_prob_3: 
            sol, list_prob_0, list_prob_3, tipp = move_down(sol,nom,xb,yb,zb,list_prob_0,list_prob_3,md,tip_d)   
        elif tes in list_prob_4: 
            sol, list_prob_0, list_prob_4, tipp = move_up(sol,nom,xb,yb,zb,list_prob_0,list_prob_4,mu,tip_u)
        elif tes in list_prob_5: 
            sol, list_prob_0, list_prob_5, tipp = move_zdown(sol,nom,xb,yb,zb,list_prob_0,list_prob_5,mzd,tip_zd)   
        elif tes in list_prob_6: 
            sol, list_prob_0, list_prob_6, tipp = move_zup(sol,nom,xb,yb,zb,list_prob_0,list_prob_6,mzu,tip_zu)
    return sol,tipp,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4,list_prob_5,list_prob_6

def prob_by_c(sol,xb,yb,zb):
    line = range(1,11)
    if sol['c'][xb+1,yb+1,zb+1] >= 0 and sol['c'][xb+1,yb+1,zb+1] < 0.25:
        list_prob = [20]
    elif sol['c'][xb+1,yb+1,zb+1] >= 0.25 and sol['c'][xb+1,yb+1,zb+1] < 0.45:
        prob_weight = 3
        list_prob = random.sample(line, prob_weight) 
    elif sol['c'][xb+1,yb+1,zb+1] >= 0.45 and sol['c'][xb+1,yb+1,zb+1] < 0.6:
        prob_weight = 4
        list_prob = random.sample(line, prob_weight)   
    elif sol['c'][xb+1,yb+1,zb+1] >= 0.6 and sol['c'][xb+1,yb+1,zb+1] < 0.7:
        prob_weight = 5
        list_prob = random.sample(line, prob_weight)  
    elif sol['c'][xb+1,yb+1,zb+1] >= 0.7:
        list_prob = line
    return list_prob

def move_left_branch(sol,xb,yb,zb,list_prob_0,list_prob_1,ml,tip_l):
    tipp = 'left'
    xpos_new = sol['matrix_tip'][-1][-1][0] - 2
    ypos_new = sol['matrix_tip'][-1][-1][1]   
    zpos_new = sol['matrix_tip'][-1][-1][2]                 
    sol['matrix_tip'][nom].append((xpos_new,ypos_new,zpos_new))
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
    sol['list_tip_movement'][-1] = tipp
    if ml == 'stop':
        sol['sp_stop'].append(len(sol['matrix_tip']))
        if tip_l>=0:
            sol['pp'][tip_l][0] = 'right'
    else:
        sol['tip_cell'].append([xpos_new,ypos_new,zpos_new])
    return sol, tipp

def move_right_branch(sol,xb,yb,zb,list_prob_0,list_prob_2,mr,tip_r):
    tipp = 'right'
    xpos_new = sol['matrix_tip'][-1][-1][0] + 2
    ypos_new = sol['matrix_tip'][-1][-1][1]
    zpos_new = sol['matrix_tip'][-1][-1][2]
    sol['matrix_tip'][-1].append((xpos_new,ypos_new,zpos_new)) 
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
    sol['list_tip_movement'][-1] = tipp
    if mr == 'stop':
        sol['sp_stop'].append(len(sol['matrix_tip']))
        if tip_r>=0:
            sol['pp'][tip_r][1] = 'left'
    else:
        sol['tip_cell'].append([xpos_new,ypos_new,zpos_new])
    return sol, tipp

def move_down_branch(sol,xb,yb,zb,list_prob_0,list_prob_3,md,tip_d):
    tipp = 'down'
    xpos_new = sol['matrix_tip'][-1][-1][0]
    ypos_new = sol['matrix_tip'][-1][-1][1] - 2
    zpos_new = sol['matrix_tip'][-1][-1][2]
    sol['matrix_tip'][-1].append((xpos_new,ypos_new,zpos_new)) 
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
    sol['list_tip_movement'][-1] = tipp
    if md == 'stop':
        sol['sp_stop'].append(len(sol['matrix_tip']))
        if tip_d>=0:
            sol['pp'][tip_d][2] = 'up'
    else:
        sol['tip_cell'].append([xpos_new,ypos_new,zpos_new])
    return sol, tipp

def move_up_branch(sol,xb,yb,list_prob_0,list_prob_4,mu,tip_u):
    tipp = 'up'
    xpos_new = sol['matrix_tip'][-1][-1][0]
    ypos_new = sol['matrix_tip'][-1][-1][1] + 2
    zpos_new = sol['matrix_tip'][-1][-1][2]
    sol['matrix_tip'][-1].append((xpos_new,ypos_new,zpos_new))
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
    sol['list_tip_movement'][-1] = tipp
    if mu == 'stop':
        sol['sp_stop'].append(len(sol['matrix_tip']))
        if tip_u>=0:
            sol['pp'][tip_u][3] = 'down'
    else:
        sol['tip_cell'].append([xpos_new,ypos_new,zpos_new])
    return sol, tipp

def move_zdown_branch(sol,xb,yb,zb,list_prob_0,list_prob_5,mzd,tip_zd):
    tipp = 'down'
    xpos_new = sol['matrix_tip'][-1][-1][0]
    ypos_new = sol['matrix_tip'][-1][-1][1] 
    zpos_new = sol['matrix_tip'][-1][-1][2] -2
    sol['matrix_tip'][-1].append((xpos_new,ypos_new,zpos_new)) 
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
    sol['list_tip_movement'][-1] = tipp
    if mzd == 'stop':
        sol['sp_stop'].append(len(sol['matrix_tip']))
        if tip_zd>=0:
            sol['pp'][tip_zd][4] = 'up'
    else:
        sol['tip_cell'].append([xpos_new,ypos_new,zpos_new])
    return sol, tipp

def move_zup_branch(sol,xb,yb,list_prob_0,list_prob_6,mzu,tip_zu):
    tipp = 'up'
    xpos_new = sol['matrix_tip'][-1][-1][0]
    ypos_new = sol['matrix_tip'][-1][-1][1]
    zpos_new = sol['matrix_tip'][-1][-1][2] + 2
    sol['matrix_tip'][-1].append((xpos_new,ypos_new,zpos_new))
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
    sol['list_tip_movement'][-1] = tipp
    if mzu == 'stop':
        sol['sp_stop'].append(len(sol['matrix_tip']))
        if tip_zu>=0:
            sol['pp'][tip_zu][5] = 'down'
    else:
        sol['tip_cell'].append([xpos_new,ypos_new,zpos_new])
    return sol, tipp

def move_left_branch_2(sol,xb,yb,zb,list_prob_0,list_prob_1,ml,tip_l):
    tipp = 'left'
    xpos_new = sol['matrix_tip_2'][-1][-1][0] - 2
    ypos_new = sol['matrix_tip_2'][-1][-1][1]   
    zpos_new = sol['matrix_tip_2'][-1][-1][2]                 
    sol['matrix_tip_2'][nom].append((xpos_new,ypos_new,zpos_new))
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
    sol['list_tip_movement_2'][-1] = tipp
    if ml == 'stop':
        sol['sp_stop_2'].append(len(sol['matrix_tip_2']))
        if tip_l>=0:
            sol['pp_2'][tip_l][0] = 'right'
    else:
        sol['tip_cell_2'].append([xpos_new,ypos_new,zpos_new])
    return sol, tipp

def move_right_branch_2(sol,xb,yb,zb,list_prob_0,list_prob_2,mr,tip_r):
    tipp = 'right'
    xpos_new = sol['matrix_tip_2'][-1][-1][0] + 2
    ypos_new = sol['matrix_tip_2'][-1][-1][1]
    zpos_new = sol['matrix_tip_2'][-1][-1][2]
    sol['matrix_tip_2'][-1].append((xpos_new,ypos_new,zpos_new)) 
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
    sol['list_tip_movement_2'][-1] = tipp
    if mr == 'stop':
        sol['sp_stop_2'].append(len(sol['matrix_tip_2']))
        if tip_r>=0:
            sol['pp_2'][tip_r][1] = 'left'
    else:
        sol['tip_cell_2'].append([xpos_new,ypos_new,zpos_new])
    return sol, tipp

def move_down_branch_2(sol,xb,yb,zb,list_prob_0,list_prob_3,md,tip_d):
    tipp = 'down'
    xpos_new = sol['matrix_tip_2'][-1][-1][0]
    ypos_new = sol['matrix_tip_2'][-1][-1][1] - 2
    zpos_new = sol['matrix_tip_2'][-1][-1][2]
    sol['matrix_tip_2'][-1].append((xpos_new,ypos_new,zpos_new)) 
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
    sol['list_tip_movement_2'][-1] = tipp
    if md == 'stop':
        sol['sp_stop_2'].append(len(sol['matrix_tip_2']))
        if tip_d>=0:
            sol['pp_2'][tip_d][2] = 'up'
    else:
        sol['tip_cell_2'].append([xpos_new,ypos_new,zpos_new])
    return sol, tipp

def move_up_branch_2(sol,xb,yb,list_prob_0,list_prob_4,mu,tip_u):
    tipp = 'up'
    xpos_new = sol['matrix_tip_2'][-1][-1][0]
    ypos_new = sol['matrix_tip_2'][-1][-1][1] + 2
    zpos_new = sol['matrix_tip_2'][-1][-1][2]
    sol['matrix_tip_2'][-1].append((xpos_new,ypos_new,zpos_new))
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
    sol['list_tip_movement_2'][-1] = tipp
    if mu == 'stop':
        sol['sp_stop_2'].append(len(sol['matrix_tip_2']))
        if tip_u>=0:
            sol['pp_2'][tip_u][3] = 'down'
    else:
        sol['tip_cell_2'].append([xpos_new,ypos_new,zpos_new])
    return sol, tipp

def move_zdown_branch_2(sol,xb,yb,zb,list_prob_0,list_prob_5,mzd,tip_zd):
    tipp = 'down'
    xpos_new = sol['matrix_tip_2'][-1][-1][0]
    ypos_new = sol['matrix_tip_2'][-1][-1][1] 
    zpos_new = sol['matrix_tip_2'][-1][-1][2] -2
    sol['matrix_tip_2'][-1].append((xpos_new,ypos_new,zpos_new)) 
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
    sol['list_tip_movement_2'][-1] = tipp
    if mzd == 'stop':
        sol['sp_stop_2'].append(len(sol['matrix_tip_2']))
        if tip_zd>=0:
            sol['pp_2'][tip_zd][4] = 'up'
    else:
        sol['tip_cell_2'].append([xpos_new,ypos_new,zpos_new])
    return sol, tipp

def move_zup_branch_2(sol,xb,yb,list_prob_0,list_prob_6,mzu,tip_zu):
    tipp = 'up'
    xpos_new = sol['matrix_tip_2'][-1][-1][0]
    ypos_new = sol['matrix_tip_2'][-1][-1][1]
    zpos_new = sol['matrix_tip_2'][-1][-1][2] + 2
    sol['matrix_tip_2'][-1].append((xpos_new,ypos_new,zpos_new))
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
    sol['list_tip_movement_2'][-1] = tipp
    if mzu == 'stop':
        sol['sp_stop_2'].append(len(sol['matrix_tip_2']))
        if tip_zu>=0:
            sol['pp_2'][tip_zu][5] = 'down'
    else:
        sol['tip_cell_2'].append([xpos_new,ypos_new,zpos_new])
    return sol, tipp

def movement_branch(tipp,sol,xb,yb,zb,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4,list_prob_5,list_prob_6,ml,mr,md,mu,mzd,mzu,tip_l,tip_r,tip_d,tip_u,tip_zd,tip_zu):
    if set['parent'] == 'two':
        tes = randint(1,10000)
        if tes in list_prob_0:
            tipp = 'stay'
        elif tes in list_prob_1:
            sol, tipp = move_left_branch_2(sol,xb,yb,zb,list_prob_0,list_prob_1,ml,tip_l)
        elif tes in list_prob_2:   
            sol, tipp = move_right_branch_2(sol,xb,yb,zb,list_prob_0,list_prob_2,mr,tip_r)
        elif tes in list_prob_3: 
            sol, tipp = move_down_branch_2(sol,xb,yb,zb,list_prob_0,list_prob_3,md,tip_d)
        elif tes in list_prob_4: 
            sol, tipp = move_up_branch_2(sol,xb,yb,zb,list_prob_0,list_prob_4,mu,tip_u)
        elif tes in list_prob_5: 
            sol, tipp = move_zdown_branch_2(sol,nom,xb,yb,zb,list_prob_0,list_prob_5,mzd,tip_zd)   
        elif tes in list_prob_6: 
            sol, tipp = move_zup_branch_2(sol,nom,xb,yb,zb,list_prob_0,list_prob_6,mzu,tip_zu)
    else:
        tes = randint(1,10000)
        if tes in list_prob_0:
            tipp = 'stay'
        elif tes in list_prob_1:
            sol, tipp = move_left_branch(sol,xb,yb,zb,list_prob_0,list_prob_1,ml,tip_l)
        elif tes in list_prob_2:   
            sol, tipp = move_right_branch(sol,xb,yb,zb,list_prob_0,list_prob_2,mr,tip_r)
        elif tes in list_prob_3: 
            sol, tipp = move_down_branch(sol,xb,yb,zb,list_prob_0,list_prob_3,md,tip_d)
        elif tes in list_prob_4: 
            sol, tipp = move_up_branch(sol,xb,yb,zb,list_prob_0,list_prob_4,mu,tip_u)
        elif tes in list_prob_5: 
            sol, tipp = move_zdown_branch(sol,nom,xb,yb,zb,list_prob_0,list_prob_5,mzd,tip_zd)   
        elif tes in list_prob_6: 
            sol, tipp = move_zup_branch(sol,nom,xb,yb,zb,list_prob_0,list_prob_6,mzu,tip_zu)
    return sol, tipp

def anastomosis_tip_tip_2(sol,nom,set):
    for e,tep in enumerate(range(0,len(sol['matrix_tip_2']))):
        if not tep == nom:
            #jj = len(sol['matrix_tip_2'][tep])-2
            if sol['matrix_tip_2'][nom][-1] == sol['matrix_tip_2'][tep][-1]:
                sol['sp_stop_2'].append(nom)
                if [sol['matrix_tip_2'][nom][-1][0],sol['matrix_tip_2'][nom][-1][1],sol['matrix_tip_2'][nom][-1][2]] in sol['tip_cell_2']:
                    sol['tip_cell_2'].remove([sol['matrix_tip_2'][nom][-1][0],sol['matrix_tip_2'][nom][-1][1]],sol['matrix_tip_2'][nom][-1][2])
                
            #elif sol['matrix_tip_2'][nom][-1] == sol['matrix_tip_2'][tep][jj] and sol['matrix_tip_2'][tep][-1] == (xb,yb):
    if set['parent'] == 'two':
        for tep in range(0,len(sol['matrix_tip'])):
            if sol['matrix_tip_2'][nom][-1] == sol['matrix_tip'][tep][-1]:
                sol['sp_stop_2'].append(nom)
                if [sol['matrix_tip_2'][nom][-1][0],sol['matrix_tip_2'][nom][-1][1],sol['matrix_tip_2'][nom][-1][2]] in sol['tip_cell_2']:
                    sol['tip_cell_2'].remove([sol['matrix_tip_2'][nom][-1][0],sol['matrix_tip_2'][nom][-1][1]],sol['matrix_tip_2'][nom][-1][2])
    return sol

def move_left_2(sol,nom,xb,yb,zb,list_prob_0,list_prob_1,ml,tip_l):
    tipp = 'left'
    xpos_new = sol['matrix_tip_2'][nom][-1][0] - 2
    ypos_new = sol['matrix_tip_2'][nom][-1][1]   
    zpos_new = sol['matrix_tip_2'][nom][-1][2]                 
    sol['matrix_tip_2'][nom].append((xpos_new,ypos_new,zpos_new))
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
    sol['list_tip_movement_2'][nom] = tipp
    for i in list_prob_1:
        list_prob_0.append(i)
    list_prob_1 =[]
    if ml == 'stop':
        sol['sp_stop_2'].append(nom)
        if tip_l>=0:
            if str(tip_l) in sol['pp_2']:
                sol['pp_2'][tip_l][0] = 'right'
            else:
                sol['pp_2'][tip_l] = ['right','a','a','a','a','a']
        else:
            if [xb,yb,zb] in sol['tip_cell_2']:
                sol['tip_cell_2'].remove([xb,yb,zb])
    else:
        if [xb,yb,zb] in sol['tip_cell_2']:
            sol['tip_cell_2'].remove([xb,yb,zb])
        sol['tip_cell_2'].append([xpos_new,ypos_new,zpos_new])
    return sol, list_prob_0, list_prob_1, tipp

def move_right_2(sol,nom,xb,yb,zb,list_prob_0,list_prob_2,mr,tip_r):
    tipp = 'right'
    xpos_new = sol['matrix_tip_2'][nom][-1][0] + 2
    ypos_new = sol['matrix_tip_2'][nom][-1][1]
    zpos_new = sol['matrix_tip_2'][nom][-1][2]
    sol['matrix_tip_2'][nom].append((xpos_new,ypos_new,zpos_new)) 
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
    sol['list_tip_movement_2'][nom] = tipp
    for i in list_prob_2:
        list_prob_0.append(i)
    list_prob_2 =[]
    if mr == 'stop':
        sol['sp_stop_2'].append(nom)
        if tip_r>=0:
            if str(tip_r) in sol['pp_2']:
                sol['pp_2'][tip_r][1] = 'left'
            else:
                sol['pp_2'][tip_r] = ['a','left','a','a','a','a']    
        else:
            if [xb,yb,zb] in sol['tip_cell_2']:
                sol['tip_cell_2'].remove([xb,yb,zb])   
    else:
        if [xb,yb,zb] in sol['tip_cell_2']:
            sol['tip_cell_2'].remove([xb,yb,zb])
        sol['tip_cell_2'].append([xpos_new,ypos_new,zpos_new])
    return sol, list_prob_0, list_prob_2, tipp

def move_down_2(sol,nom,xb,yb,zb,list_prob_0,list_prob_3,md,tip_d):
    tipp = 'down'
    xpos_new = sol['matrix_tip_2'][nom][-1][0]
    ypos_new = sol['matrix_tip_2'][nom][-1][1] - 2
    zpos_new = sol['matrix_tip_2'][nom][-1][2]
    sol['matrix_tip_2'][nom].append((xpos_new,ypos_new,zpos_new)) 
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
    sol['list_tip_movement_2'][nom] = tipp
    for i in list_prob_3:
        list_prob_0.append(i)
    list_prob_3 =[]
    if md == 'stop':
        sol['sp_stop_2'].append(nom)
        if tip_d>=0:
            if str(tip_d) in sol['pp_2']:
                sol['pp_2'][tip_d][2] = 'up'
            else:
                sol['pp_2'][tip_d] = ['a','a','up','a','a','a']
        else:
            if [xb,yb,zb] in sol['tip_cell_2']:
                sol['tip_cell_2'].remove([xb,yb,zb])
    else:
        if [xb,yb,zb] in sol['tip_cell_2']:
            sol['tip_cell_2'].remove([xb,yb,zb])
        sol['tip_cell_2'].append([xpos_new,ypos_new,zpos_new])
    return sol, list_prob_0, list_prob_3, tipp

def move_up_2(sol,nom,xb,yb,zb,list_prob_0,list_prob_4,mu,tip_u):
    tipp = 'up'
    xpos_new = sol['matrix_tip_2'][nom][-1][0]
    ypos_new = sol['matrix_tip_2'][nom][-1][1] + 2
    zpos_new = sol['matrix_tip_2'][nom][-1][2]
    sol['matrix_tip_2'][nom].append((xpos_new,ypos_new,zpos_new))
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
    sol['list_tip_movement_2'][nom] = tipp
    for i in list_prob_4:
        list_prob_0.append(i)
    list_prob_4 =[]
    if mu == 'stop':
        sol['sp_stop_2'].append(nom)
        if tip_u>=0:
            if str(tip_u) in sol['pp_2']:
                sol['pp_2'][tip_u][3] = 'down'
            else:
                sol['pp_2'][tip_u] = ['a','a','a','down','a','a']
        else:
            if [xb,yb,zb] in sol['tip_cell_2']:
                sol['tip_cell_2'].remove([xb,yb,zb])
    else:
        if [xb,yb,zb] in sol['tip_cell_2']:
            sol['tip_cell_2'].remove([xb,yb,zb])
        sol['tip_cell_2'].append([xpos_new,ypos_new,zpos_new])
    return sol, list_prob_0, list_prob_4, tipp

def move_zdown_2(sol,nom,xb,yb,zb,list_prob_0,list_prob_5,mzd,tip_zd):
    tipp = 'down'
    xpos_new = sol['matrix_tip_2'][nom][-1][0]
    ypos_new = sol['matrix_tip_2'][nom][-1][1]
    zpos_new = sol['matrix_tip_2'][nom][-1][2] - 2
    sol['matrix_tip_2'][nom].append((xpos_new,ypos_new,zpos_new)) 
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
    sol['list_tip_movement_2'][nom] = tipp
    for i in list_prob_5:
        list_prob_0.append(i)
    list_prob_5 =[]
    if mzd == 'stop':
        sol['sp_stop_2'].append(nom)
        if tip_zd>=0:
            if str(tip_zd) in sol['pp_2']:
                sol['pp_2'][tip_zd][4] = 'up'
            else:
                sol['pp_2'][tip_zd] = ['a','a','a','a','up','a']
        else:
            if [xb,yb,zb] in sol['tip_cell_2']:
                sol['tip_cell_2'].remove([xb,yb,zb])
    else:
        if [xb,yb,zb] in sol['tip_cell_2']:
            sol['tip_cell_2'].remove([xb,yb,zb])
        sol['tip_cell_2'].append([xpos_new,ypos_new,zpos_new])
    return sol, list_prob_0, list_prob_5, tipp

def move_zup_2(sol,nom,xb,yb,zb,list_prob_0,list_prob_6,mzu,tip_zu):
    tipp = 'up'
    xpos_new = sol['matrix_tip_2'][nom][-1][0]
    ypos_new = sol['matrix_tip_2'][nom][-1][1] 
    zpos_new = sol['matrix_tip_2'][nom][-1][2] + 2
    sol['matrix_tip_2'][nom].append((xpos_new,ypos_new,zpos_new))
    sol['n'][xpos_new,ypos_new,zpos_new] = 1
    sol['list_tip_movement_2'][nom] = tipp
    for i in list_prob_6:
        list_prob_0.append(i)
    list_prob_6 =[]
    if mzu == 'stop':
        sol['sp_stop_2'].append(nom)
        if tip_zu>=0:
            if str(tip_zu) in sol['pp_2']:
                sol['pp_2'][tip_zu][5] = 'down'
            else:
                sol['pp_2'][tip_zu] = ['a','a','a','a','a','down']
        else:
            if [xb,yb,zb] in sol['tip_cell_2']:
                sol['tip_cell_2'].remove([xb,yb,zb])
    else:
        if [xb,yb,zb] in sol['tip_cell_2']:
            sol['tip_cell_2'].remove([xb,yb,zb])
        sol['tip_cell_2'].append([xpos_new,ypos_new,zpos_new])
    return sol, list_prob_0, list_prob_6, tipp

def movement_2(sol,nom,xb,yb,zb,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4,list_prob_5,list_prob_6,ml,mr,md,mu,mzd,mzu,tip_l,tip_r,tip_d,tip_u,tip_zd,tip_zu):
    if nom in sol['pp_2']:
        tipp = 'stay'
        oo = 0
        while tipp == 'stay' and oo < 1000:
            oo +=1
            tes = randint(1,10000)
            if tes in list_prob_0:
                tipp = 'stay'
            elif tes in list_prob_1:
                sol, list_prob_0, list_prob_1, tipp = move_left_2(sol,nom,xb,yb,zb,list_prob_0,list_prob_1,ml,tip_l)
            elif tes in list_prob_2:   
                sol, list_prob_0, list_prob_2, tipp = move_right_2(sol,nom,xb,yb,zb,list_prob_0,list_prob_2,mr,tip_r)    
            elif tes in list_prob_3: 
                sol, list_prob_0, list_prob_3, tipp = move_down_2(sol,nom,xb,yb,zb,list_prob_0,list_prob_3,md,tip_d)   
            elif tes in list_prob_4: 
                sol, list_prob_0, list_prob_4, tipp = move_up_2(sol,nom,xb,yb,zb,list_prob_0,list_prob_4,mu,tip_u)
            elif tes in list_prob_5: 
                sol, list_prob_0, list_prob_5, tipp = move_zdown_2(sol,nom,xb,yb,zb,list_prob_0,list_prob_5,mzd,tip_zd)   
            elif tes in list_prob_6: 
                sol, list_prob_0, list_prob_6, tipp = move_zup_2(sol,nom,xb,yb,zb,list_prob_0,list_prob_6,mzu,tip_zu)
    else:
        tes = randint(1,10000)
        if tes in list_prob_0:
            tipp = 'stay'
        elif tes in list_prob_1:
            sol, list_prob_0, list_prob_1, tipp = move_left_2(sol,nom,xb,yb,zb,list_prob_0,list_prob_1,ml,tip_l)
        elif tes in list_prob_2:   
            sol, list_prob_0, list_prob_2, tipp = move_right_2(sol,nom,xb,yb,zb,list_prob_0,list_prob_2,mr,tip_r)    
        elif tes in list_prob_3: 
            sol, list_prob_0, list_prob_3, tipp = move_down_2(sol,nom,xb,yb,zb,list_prob_0,list_prob_3,md,tip_d)   
        elif tes in list_prob_4: 
            sol, list_prob_0, list_prob_4, tipp = move_up_2(sol,nom,xb,yb,zb,list_prob_0,list_prob_4,mu,tip_u)
        elif tes in list_prob_5: 
            sol, list_prob_0, list_prob_5, tipp = move_zdown_2(sol,nom,xb,yb,zb,list_prob_0,list_prob_5,mzd,tip_zd)   
        elif tes in list_prob_6: 
            sol, list_prob_0, list_prob_6, tipp = move_zup_2(sol,nom,xb,yb,zb,list_prob_0,list_prob_6,mzu,tip_zu)
    return sol,tipp,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4,list_prob_5,list_prob_6

def hybrid_tech_c_3d(coef, set, sol):
    n_sp = len(sol['matrix_tip']) #to save original number of tips before branching
    for nom in range(0,n_sp): #dicek setiap tip
        if not nom in sol['sp_stop']: #kalo dia sudah anastomosis, gak perlu branching dan move lg.
            xb = sol['matrix_tip'][nom][-1][0] #get x position of last tip position
            yb = sol['matrix_tip'][nom][-1][1] #get y position of last tip position
            zb = sol['matrix_tip'][nom][-1][2]
            dirr= movement_dir_3d(coef, set, sol, xb, yb, zb, nom)
            
            if dirr[1] == 0 and dirr[2] == 0 and dirr[3] == 0 and dirr[4] == 0 and dirr[5] == 0 and dirr[6] == 0:
                sol['sp_stop'].append(nom)
            else:
                '''Making list of prob'''
                list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4,list_prob_5,list_prob_6 = set_list_prob(dirr)
                '''Checking Space for n #if meet vessel'''
                ml = 'f'
                mr = 'f'
                md = 'f'
                mu = 'f'
                mzd = 'f'
                mzu = 'f'
                tip_l = -1
                tip_r = -1
                tip_d = -1
                tip_u = -1
                tip_zd = -1
                tip_zu = -1
                '''
                ml,mr,md,mu,mzd,mzu,tip_l,tip_r,tip_d,tip_u,tip_zd,tip_zu = anastomosis_tip_branch(sol,nom,xb,yb,zb,ml,mr,md,mu,mzd,mzu,tip_l,tip_r,tip_d,tip_u,tip_zd,tip_zu)
                ml = 'f'
                mr = 'f'
                md = 'f'
                mu = 'f'
                mzd = 'f'
                mzu = 'f'
                tip_l = -1
                tip_r = -1
                tip_d = -1
                tip_u = -1
                tip_zd = -1
                tip_zu = -1
                '''
                '''The Movement'''
                sol,tipp,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4,list_prob_5,list_prob_6 = movement(sol,nom,xb,yb,zb,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4,list_prob_5,list_prob_6,ml,mr,md,mu,mzd,mzu,tip_l,tip_r,tip_d,tip_u,tip_zd,tip_zu)
                
                '''Test Anastomosis tip-tip if move'''
                if not tipp == 'stay':
                    sol=anastomosis_tip_tip(sol,nom,set)
                
                '''2.1 Branching Decision'''
                if tipp == 'stay': #not able to branch
                    sol['life_time_tip'][nom] += set['dt']
                else: #there is possibility to branch
                    cek = str(nom)
                    if dirr.count(0) >= 5: #no space to move
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
                            list_prob = prob_by_c(sol,xb,yb,zb)
                            tes = randint(1,10)
                            if not tes in list_prob: #not able to branch
                                sol['life_time_tip'][nom] += set['dt']
                                if cek in sol['pp']:
                                    sol['pp'].pop('cek')
                            else: #BRANCHING!
                                sol['life_time_tip'][nom] = 0
                                sol['matrix_tip'].append([(xb,yb,zb)])
                                sol['life_time_tip'].append(0)
                                sol['list_tip_movement'].append('start')
                                tipp = 'stay'
                                if cek in sol['pp']:
                                    sol['pp'].pop('cek')
                                '''The Movement from branching'''
                                while tipp == 'stay':
                                    sol, tipp = movement_branch(tipp,sol,xb,yb,zb,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4,list_prob_5,list_prob_6,ml,mr,md,mu,mzd,mzu,tip_l,tip_r,tip_d,tip_u,tip_zd,tip_zd)                          
    
                                '''Check Anastomosis'''
                                sol=anastomosis_tip_tip(sol,len(sol['matrix_tip'])-1,set)
    if set['parent'] == 'two':
        n_sp = len(sol['matrix_tip_2']) #to save original number of tips before branching
        for nom in range(0,n_sp): #dicek setiap tip
            if not nom in sol['sp_stop_2']: #kalo dia sudah anastomosis, gak perlu branching dan move lg.
                xb = sol['matrix_tip_2'][nom][-1][0] #get x position of last tip position
                yb = sol['matrix_tip_2'][nom][-1][1] #get y position of last tip position
                zb = sol['matrix_tip_2'][nom][-1][2]
                dirr= movement_dir_3d(coef, set, sol, xb, yb, zb, nom)
                
                if dirr[1] == 0 and dirr[2] == 0 and dirr[3] == 0 and dirr[4] == 0 and dirr[5] == 0 and dirr[6] == 0:
                    sol['sp_stop_2'].append(nom)
                else:
                    '''Making list of prob'''
                    list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4,list_prob_5,list_prob_6 = set_list_prob(dirr)
                    '''Checking Space for n #if meet vessel'''
                    ml = 'f'
                    mr = 'f'
                    md = 'f'
                    mu = 'f'
                    mzd = 'f'
                    mzu = 'f'
                    tip_l = -1
                    tip_r = -1
                    tip_d = -1
                    tip_u = -1
                    tip_zd = -1
                    tip_zu = -1
                    '''
                    ml,mr,md,mu,mzd,mzu,tip_l,tip_r,tip_d,tip_u,tip_zd,tip_zu = anastomosis_tip_branch_2(sol,nom,xb,yb,zb,ml,mr,md,mu,mzd,mzu,tip_l,tip_r,tip_d,tip_u,tip_zd,tip_zu)
                    ml = 'f'
                    mr = 'f'
                    md = 'f'
                    mu = 'f'
                    mzd = 'f'
                    mzu = 'f'
                    tip_l = -1
                    tip_r = -1
                    tip_d = -1
                    tip_u = -1
                    tip_zd = -1
                    tip_zu = -1
                    '''
                    '''The Movement'''
                    sol,tipp,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4,list_prob_5,list_prob_6 = movement_2(sol,nom,xb,yb,zb,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4,list_prob_5,list_prob_6,ml,mr,md,mu,mzd,mzu,tip_l,tip_r,tip_d,tip_u,tip_zd,tip_zu)
                    
                    '''Test Anastomosis tip-tip if move'''
                    if not tipp == 'stay':
                        sol=anastomosis_tip_tip_2(sol,nom,set)
                    
                    '''2.1 Branching Decision'''
                    if tipp == 'stay': #not able to branch
                        sol['life_time_tip_2'][nom] += set['dt']
                    else: #there is possibility to branch
                        cek = str(nom)
                        if dirr.count(0) >= 5: #no space to move
                            sol['life_time_tip_2'][nom] += set['dt']
                            if cek in sol['pp_2']:
                                sol['pp_2'].pop('cek')
                        else: #there is possibility to branch
                            if sol['life_time_tip_2'][nom] < coef['T_branch']: #not able to branch
                                sol['life_time_tip_2'][nom] += set['dt']
                                if cek in sol['pp_2']:
                                    sol['pp_2'].pop('cek')
                            else: #there is possibility to branch
                                '''Probability of Branching using c'''   
                                list_prob = prob_by_c(sol,xb,yb,zb)
                                tes = randint(1,10)
                                if not tes in list_prob: #not able to branch
                                    sol['life_time_tip_2'][nom] += set['dt']
                                    if cek in sol['pp_2']:
                                        sol['pp_2'].pop('cek')
                                else: #BRANCHING!
                                    sol['life_time_tip_2'][nom] = 0
                                    sol['matrix_tip_2'].append([(xb,yb,zb)])
                                    sol['life_time_tip_2'].append(0)
                                    sol['list_tip_movement_2'].append('start')
                                    tipp = 'stay'
                                    if cek in sol['pp_2']:
                                        sol['pp_2'].pop('cek')
                                    '''The Movement from branching'''
                                    while tipp == 'stay':
                                        sol, tipp = movement_branch(tipp,sol,xb,yb,zb,list_prob_0,list_prob_1,list_prob_2,list_prob_3,list_prob_4,list_prob_5,list_prob_6,ml,mr,md,mu,mzd,mzu,tip_l,tip_r,tip_d,tip_u,tip_zd,tip_zd)                          
        
                                    '''Check Anastomosis'''
                                    sol=anastomosis_tip_tip_2(sol,len(sol['matrix_tip_2'])-1,set)
    
    
    return sol