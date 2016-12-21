from init_2d import init_2d_ #2.1.1
from init_tip_2d import init_tip_2d_ #2.1.2

import numpy
import random
from random import randint

def initial_prof(coef, set, sol):
    ##For continuous function
    sol = init_2d_(coef,set,sol) #2.1.1
    ##For discrete function
    sol = init_tip_2d_(coef,set,sol) #2.1.2
    if set['con'] == False:
        print 'initial tips:', sol['matrix_tip']
        if set['parent'] == 'two':
            print 'initial tips2:', sol['matrix_tip_2']
    return sol