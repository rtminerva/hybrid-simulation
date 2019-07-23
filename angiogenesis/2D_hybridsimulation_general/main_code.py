from teshybrid import hybrid_tech #Ref.4.1
from solve_con import system_2d #Ref.4.2
from timeit import default_timer as timer

def boolean_1_iter(coef, set, sol): #Ref.4                                                   
    start1 = timer()
    '''2. Branching and Movement'''
    sol = hybrid_tech(coef, set, sol) #Ref.4.1  
    start2 = timer()
    '''Solving c'''
    sol = system_2d(coef, set, sol) #Ref.4.2
    start3 = timer()            
    print 'Hybrid for n time', start2-start1
    print 'Solving c time', start3-start2
    return sol