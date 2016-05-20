import random
import numpy

def init_m(coef,set,sol):
    if set['initial_m'] == 'rectangular_1_tip':
        y = set['Ny']/2 + 5
        x = 5
        if y % 2 == 0:
            y += 1
        sol['m'][x,y] = 1
    elif set['initial_m'] == 'rectangular_tip':
        '''Randomly spotted in domain'''
        for tt in range(0,250):
            idx_m_1 = random.sample(range(1,set['Nx'],2),7)
            idx_m_2 = random.sample(range(1,set['Ny'],2),7)
            for id in range(0,len(idx_m_1)):
                if not sol['m'][idx_m_1[id], idx_m_2[id]] == 1 and not sol['n'][idx_m_1[id], idx_m_2[id]] == 1:
                    sol['m'][idx_m_1[id], idx_m_2[id]] = 1
        del idx_m_1
        del idx_m_2
    elif set['initial_m'] == 'retina_1_tip':
        sol['m'][187,213] = 1
    elif set['initial_m'] == 'retina_tip':
        '''Randomly spotted in domain'''
        for tt in range(0,250):
            idx_m_1 = random.sample(range(1,set['Nx'],2),100)
            idx_m_2 = random.sample(range(1,set['Ny'],2),100)
            for id in range(0,len(idx_m_1)):
                r_f = numpy.sqrt((idx_m_1[id]*set['Hh']-set['O_x'])**2 + (idx_m_2[id]*set['Hh']-set['O_y'])**2)
                if not sol['m'][idx_m_1[id], idx_m_2[id]] == 1 and not sol['n'][idx_m_1[id], idx_m_2[id]] == 1  and r_f > set['R_min']:
                    sol['m'][idx_m_1[id], idx_m_2[id]] = 1
        del idx_m_1
        del idx_m_2
    return sol