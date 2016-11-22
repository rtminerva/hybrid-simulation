from init_2d import init_2d_ #2.1.1
from init_tip_2d import init_tip_2d_ #2.1.2

import numpy
import random
from random import randint
#from init_3d import init_3d_
#from init_tip_3d import init_tip_3d_
#from init_tip_3d_n import init_tip_3d_n_

def initial_prof(coef, set, sol):
    if set['layout'] == '2D':
        if set['con'] == True:
            sol = init_2d_(coef,set,sol) #2.1.1
        else:
            sol = init_2d_(coef,set,sol) #2.1.1
            #sol = init_tip_2d_(coef,set,sol) #2.1.2
    if set['layout'] == '3D':
        sol = init_3d_(coef,set,sol)
        #sol = init_tip_3d_(coef,set,sol)
        sol = init_tip_3d_n_(coef,set,sol)
    return sol