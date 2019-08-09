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
#     '''Adding cell in the tip cell path'''     
#     if set['k'] % 50 == 0:
#         y = set['Ny']/2 
#         if y % 2 == 0:
#             y += 1  
#         sol['n'][1,y] = 1
#         sol['matrix_tip'].append([[1,y]])
#         sol['list_tip_movement'].append('start') #movement tip
#         sol['life_time_tip'].append(0) #lifetime
               
    print 'Hybrid for n time', start2-start1
    print 'Solving c time', start3-start2
    return sol