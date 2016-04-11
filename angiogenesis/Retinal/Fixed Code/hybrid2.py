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
                trial = random.uniform(0,1)
                if trial <= dirr_sol['m'][0]: #stay
                    lop = 1
                    #print 'STAY'
                    #do nothing
                elif trial <= dirr_sol['m'][1]: #left
                    #print 'LEFT'
                    #print sol['m'][xb,yb]
                    #index_sol['m'][dot][0] = xb - 2
                    sol['m'][xb - 2, yb] = 1
                    sol['m'][xb,yb] = 0
                    #print sol['m'][xb,yb]
                    #print sol['m'][xb - 2, yb]
                elif trial <= dirr_sol['m'][2]: #right
                    #print 'RIGHT'
                    #print sol['m'][xb,yb]
                    #index_sol['m'][dot][0] = xb + 2
                    sol['m'][xb + 2, yb] = 1
                    sol['m'][xb,yb] = 0
                    #print sol['m'][xb,yb]
                    #print sol['m'][xb + 2, yb]
                elif trial <= dirr_sol['m'][3]: #down
                    #print 'DOWN'
                    #print sol['m'][xb,yb]
                    #index_sol['m'][dot][1] = yb - 2
                    sol['m'][xb, yb - 2] = 1
                    sol['m'][xb,yb] = 0
                    #print sol['m'][xb,yb]
                   # print sol['m'][xb, yb - 2]
                else: #>dirr[3] #up
                    #print 'UP'
                    #print sol['m'][xb,yb]
                    #index_sol['m'][dot][1] = yb + 2
                    sol['m'][xb, yb + 2] = 1
                    sol['m'][xb,yb] = 0
                    #print sol['m'][xb,yb]
                    #print sol['m'][xb, yb + 2]
                for ec_i in range(0,len(matrix_tip)):
                    if (xb,yb) in matrix_tip[ec_i]:
                        sol['index_mn'].append([xb,yb])
    return sol