import random
from dirrection_of_movement import movement_dir

def hybrid_tech_m(coef, set, sol):
    mo = sol['m'][:]
    nom = 0
    for yb in range(1,set['Ny'],2):
        for xb in range(1,set['Nx'],2):
            #print mo[xb,yb]
            if mo[xb,yb] == 1: #and not [xb,yb] in sol['sol['index_mn']']:
                dirr = movement_dir(coef, set, sol, xb, yb, nom, n_dir = False)
            
                dirr_m = [dirr[0],dirr[0]+dirr[1],dirr[0]+dirr[1]+dirr[2],dirr[0]+dirr[1]+dirr[2]+dirr[3],1]
                #print dirr
                keep = True
                dire = 'f'
                while keep == True:
                    trial = random.uniform(0,1)
                    if trial <= dirr_m[0]: #stay
                        dire = 'stay'
                        keep = False
                    elif trial <= dirr_m[1]: #left
                        if (xb - 2, yb) not in sol['tip_cell']:
                            keep = False
                            dire = 'left'
                            trial = 100
                            sol['m'][xb - 2, yb] = 1
                            sol['m'][xb,yb] = 0
                    elif trial <= dirr_m[2]: #right
                        if (xb + 2, yb) not in sol['tip_cell']:
                            keep = False
                            dire = 'right'
                            trial = 100
                        sol['m'][xb + 2, yb] = 1
                        sol['m'][xb,yb] = 0
                    elif trial <= dirr_m[3]: #down
                        if (xb, yb - 2) not in sol['tip_cell']:
                            keep = False
                            dire = 'down'
                            trial = 100
                        sol['m'][xb, yb - 2] = 1
                        sol['m'][xb,yb] = 0
                    elif trial <= dirr_m[4]: #>dirr[3] #up
                        if (xb, yb + 2) not in sol['tip_cell']:
                            keep = False
                            dire = 'up'
                            trial = 100
                        sol['m'][xb, yb + 2] = 1
                        sol['m'][xb,yb] = 0
                
                
                if dire == 'left': #stay
                    sol['m'][xb - 2, yb] = 1
                    sol['m'][xb,yb] = 0
                elif dire == 'right': #right
                    sol['m'][xb + 2, yb] = 1
                    sol['m'][xb,yb] = 0
                elif dire == 'down': #down
                    sol['m'][xb, yb - 2] = 1
                    sol['m'][xb,yb] = 0
                elif dire == 'up': #>dirr[3] #up
                    sol['m'][xb, yb + 2] = 1
                    sol['m'][xb,yb] = 0
                
                for ec_i in range(0,len(sol['matrix_tip'])):
                    if (xb,yb) in sol['matrix_tip'][ec_i]:
                        sol['index_mn'].append([xb,yb])
    return sol