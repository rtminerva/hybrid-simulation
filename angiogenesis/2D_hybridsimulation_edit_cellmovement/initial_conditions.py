from init_2d import init_2d_ #Ref.2.1
from init_tip_2d import init_tip_2d_ #Ref.2.2

import numpy
import random
from random import randint

def initial_prof(coef, set, sol): #Ref.2
    ##For continuous function
    sol = init_2d_(coef,set,sol) #Ref.2.1
    ##For discrete function
    sol = init_tip_2d_(coef,set,sol) #Ref.2.2
    #print 'initial tips:', sol['matrix_tip']
    return sol