import random
import numpy

def init_m(coef,set,sol):
    if set['initial_prof'] == 'test_1_tip':
        sol['m'][187,213] = 1
    else:
        '''Randomly spotted in domain'''
        for tt in range(0,250):
            idx_m_1 = random.sample(range(1,440,2),100)
            idx_m_2 = random.sample(range(1,440,2),100)
            for id in range(0,len(idx_m_1)):
                r_f = numpy.sqrt((idx_m_1[id]*set['Hh']-set['O_x'])**2 + (idx_m_2[id]*set['Hh']-set['O_y'])**2)
                if not sol['m'][idx_m_1[id], idx_m_2[id]] == 1 and not sol['n'][idx_m_1[id], idx_m_2[id]] == 1  and r_f > set['R_min']:
                    sol['m'][idx_m_1[id], idx_m_2[id]] = 1
                    #sol['cell_m'].append([idx_m_1[id], idx_m_2[id]])
        del idx_m_1
        del idx_m_2
    return sol