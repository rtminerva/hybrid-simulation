import random
from random import randint
from dirrection_of_movement import movement_dir
import numpy

def hybrid_tech_m(coef, set, sol):
    mo = sol['m'][:]
    nom = 0
    
    '''Identify The fartest tip from center'''
    '''
    distance = []
    for tip in sol['tip_cell']:
        r_f = numpy.sqrt((tip[0]*set['Hh']-set['O_x'])**2 + (tip[1]*set['Hh']-set['O_y'])**2)
        distance.append(r_f)
    far = max(distance) + 0.4
    '''
    far = 100
    for cell in sol['cell_m']:
        xb = cell[0]
        yb = cell[1]
        r_f = numpy.sqrt((xb*set['Hh']-set['O_x'])**2 + (yb*set['Hh']-set['O_y'])**2)
        if r_f <= far:
            line_1 = range(1,10001)
        
            dirr, space = movement_dir(coef, set, sol, xb, yb, nom, n_dir = False)
            
            if dirr[1] == 0 and dirr[2] == 0 and dirr[3] == 0 and dirr[4] == 0:
                lop = 1
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
                
                #print 'selesai bikin line'
                nx = xb
                ny = yb
                tes = randint(1,10000) #select integer number randomly between 1 and 100000
                if tes in list_prob_1:
                    if (xb - 2, yb) not in sol['tip_cell']:
                        nx = xb - 2
                        ny = yb
                        sol['m'][xb - 2, yb] = 1
                        sol['m'][xb,yb] = 0
                elif tes in list_prob_2:   
                    if (xb + 2, yb) not in sol['tip_cell']:
                        nx = xb + 2
                        ny = yb
                        sol['m'][xb + 2, yb] = 1
                        sol['m'][xb,yb] = 0
                elif tes in list_prob_3: 
                    if (xb, yb - 2) not in sol['tip_cell']:
                        nx = xb
                        ny = yb - 2
                        sol['m'][xb, yb - 2] = 1
                        sol['m'][xb,yb] = 0
                elif tes in list_prob_4: 
                    if (xb, yb + 2) not in sol['tip_cell']:
                        nx = xb
                        ny = yb + 2
                        sol['m'][xb, yb + 2] = 1
                        sol['m'][xb,yb] = 0
                if sol['n'][nx,ny] == 1:
                    if [xb,yb] in sol['index_mn']:
                        sol['index_mn'].remove([xb,yb])
                    sol['index_mn'].append([nx,ny])
                #for ec_i in range(0,len(sol['matrix_tip'])):
                #    if (nx,ny) in sol['matrix_tip'][ec_i]:
                #        sol['index_mn'].append([nx,ny])
    return sol