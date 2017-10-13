from init_1d import init_1d_ #2.1.1
from init_2d import init_2d_ #2.1.1

import numpy
import random
from random import randint

def initial_prof(coef, set, sol):
    if set['Dimension'] == '1D':
        sol = init_1d_(coef,set,sol) #2.1.1
    elif set['Dimension'] == '2D':
        sol = init_2d_(coef,set,sol) #2.1.1
    return sol