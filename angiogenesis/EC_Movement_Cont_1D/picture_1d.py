import matplotlib.pyplot as plt 
import numpy
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

'''
def pic_1d(coef,set,sol):
    c_sol = numpy.zeros(set['Nx']/2+1) #to save values at time step k (we are calculating at time step k+1)
    n_sol = numpy.zeros(set['Nx']/2) #to save values at time step k (we are calculating at time step k+1)
    b_sol = numpy.zeros(set['Nx']/2) #to save values at time step k (we are calculating at time step k+1)
    
    id = 0
    for ind, v in enumerate(sol['c']):
        if ind % 2 == 0:
            c_sol[id] = sol['c'][ind]
            id += 1
    id = 0
    for ind, v in enumerate(sol['n']):
        if ind % 2 != 0:
            n_sol[id] = sol['n'][ind]
            id += 1
    id = 0
    for ind, v in enumerate(sol['b']):
        if ind % 2 != 0:
            b_sol[id] = sol['b'][ind]
            id += 1        

    Blood Vessel Growth (TIP and STALK)
    plt.figure(1)
    axes = plt.gca()
    axes.set_xlim([0,1])
    axes.set_ylim([0,1.2])
    plt.title('%s%f' % ('t=',set['t']))
    x_main_axis = numpy.arange(set['Hh'], coef['X'], set['h'])
    x_sub_axis = numpy.arange(0, coef['X']+set['Hh'], set['h'])
    plt.plot(x_main_axis, n_sol, x_main_axis, b_sol, x_sub_axis, c_sol) 
    flag = 'N&S=%s' % str(sol['stEC']) 
    plt.savefig("%s.png" % flag)
    plt.close()
    sol['stEC'] +=1 
'''
def pic_1d(coef,set,sol):
    c_sol = numpy.zeros(set['Nx']/2+1) #to save values at time step k (we are calculating at time step k+1)
    n_sol = numpy.zeros(set['Nx']/2)
    b_sol = numpy.zeros(set['Nx']/2)
    
    id = 0
    for ind, v in enumerate(sol['c']):
        if ind % 2 == 0:
            c_sol[id] = sol['c'][ind]
            id += 1
    id = 0
    for ind, v in enumerate(sol['n']):
        if ind % 2 != 0:
            n_sol[id] = sol['n'][ind]
            id += 1
    id = 0
    for ind, v in enumerate(sol['b']):
        if ind % 2 != 0:
            b_sol[id] = sol['b'][ind]
            id += 1
    
    if set['k'] == 0:
        sol['n_0'] = n_sol
        sol['b_0'] = b_sol
        sol['c_0'] = c_sol
            
    if set['k'] == 2000:
        sol['n_2'] = n_sol
        sol['b_2'] = b_sol
        sol['c_2'] = c_sol
    
    if set['k'] == 4000:
        sol['n_4'] = n_sol
        sol['b_4'] = b_sol
        sol['c_4'] = c_sol
        
    if set['k'] == 6000:
        sol['n_6'] = n_sol
        sol['b_6'] = b_sol
        sol['c_6'] = c_sol
        if set['vegf_dep'] == 6:
            sol['n_00'] = numpy.zeros(set['Nx']/2)
            sol['b_00'] = numpy.zeros(set['Nx']/2)
            sol['n_00'] = n_sol
            sol['b_00'] = b_sol
        elif set['vegf_dep'] == 5:
            sol['n_22'] = numpy.zeros(set['Nx']/2)
            sol['b_22'] = numpy.zeros(set['Nx']/2)
            sol['n_22'] = n_sol
            sol['b_22'] = b_sol
        elif set['vegf_dep'] == 4:
            sol['n_44'] = numpy.zeros(set['Nx']/2)
            sol['b_44'] = numpy.zeros(set['Nx']/2)
            sol['n_44'] = n_sol
            sol['b_44'] = b_sol
        elif set['vegf_dep'] == 3:
            sol['n_66'] = numpy.zeros(set['Nx']/2)
            sol['b_66'] = numpy.zeros(set['Nx']/2)
            sol['n_66'] = n_sol
            sol['b_66'] = b_sol
        elif set['vegf_dep'] == 2:
            sol['n_88'] = numpy.zeros(set['Nx']/2)
            sol['b_88'] = numpy.zeros(set['Nx']/2)
            sol['n_88'] = n_sol
            sol['b_88'] = b_sol
        elif set['vegf_dep'] == 1:
            sol['n_1010'] = numpy.zeros(set['Nx']/2)
            sol['b_1010'] = numpy.zeros(set['Nx']/2)
            sol['n_1010'] = n_sol
            sol['b_1010'] = b_sol
        
    if set['k'] == 8000:
        sol['n_8'] = n_sol
        sol['b_8'] = b_sol
        sol['c_8'] = c_sol       
    

    '''Model extension'''
    if set['Model'] == 'extension': 
        p_sol = numpy.zeros(set['Nx']/2+1)
        e_sol = numpy.zeros(set['Nx']/2)
        a1_sol = numpy.zeros(set['Nx']/2)
        a2_sol = numpy.zeros(set['Nx']/2)
        r1_sol = numpy.zeros(set['Nx']/2)
        r2_sol = numpy.zeros(set['Nx']/2)
        m_sol = numpy.zeros(set['Nx']/2)
        ma_sol = numpy.zeros(set['Nx']/2)
        
        id = 0
        for ind, v in enumerate(sol['p']):
            if ind % 2 == 0:
                p_sol[id] = sol['p'][ind]
                id += 1
        id = 0
        for ind, v in enumerate(sol['e']):
            if ind % 2 != 0:
                e_sol[id] = sol['e'][ind]
                id += 1
        id = 0
        for ind, v in enumerate(sol['a1']):
            if ind % 2 != 0:
                a1_sol[id] = sol['a1'][ind]
                id += 1
        id = 0
        for ind, v in enumerate(sol['a2']):
            if ind % 2 != 0:
                a2_sol[id] = sol['a2'][ind]
                id += 1
        id = 0
        for ind, v in enumerate(sol['r1']):
            if ind % 2 != 0:
                r1_sol[id] = sol['r1'][ind]
                id += 1
        id = 0
        for ind, v in enumerate(sol['r2']):
            if ind % 2 != 0:
                r2_sol[id] = sol['r2'][ind]
                id += 1
        id = 0
        for ind, v in enumerate(sol['m']):
            if ind % 2 != 0:
                m_sol[id] = sol['m'][ind]
                id += 1
        id = 0
        for ind, v in enumerate(sol['ma']):
            if ind % 2 != 0:
                ma_sol[id] = sol['ma'][ind]
                id += 1
        '''Blood Vessel Growth (TIP and STALK)'''
        plt.figure(1)
        axes = plt.gca()
        axes.set_xlim([0,1])
        axes.set_ylim([0,1.5])
        plt.title('%s%f' % ('Tip, Stalk, VEGF at t=',set['t']))
        x_main_axis = numpy.arange(set['Hh'], coef['X'], set['h'])
        x_sub_axis = numpy.arange(0, coef['X']+set['Hh'], set['h'])
        plt.plot(x_main_axis, n_sol, 'b', x_main_axis, b_sol, 'g', x_sub_axis, c_sol, 'r', x_main_axis, m_sol, 'g--', x_main_axis, ma_sol, 'g^') 
        flag = 'A=%s' % str(sol['stEC']) 
        plt.savefig("%s.png" % flag)
        plt.close()
        sol['stEC'] +=1 
        
        plt.figure(2)
        axes = plt.gca()
        axes.set_xlim([0,1])
        axes.set_ylim([0,1.5])
        plt.title('%s%f' % ('PDGF-B, Tie2, Ang1, Ang2, Mural, Attached-Mural at t=',set['t']))
        plt.plot(x_sub_axis, p_sol, 'bs', x_main_axis, e_sol, 'g', x_main_axis, a1_sol, 'r', x_main_axis, a2_sol, 'b', x_main_axis, m_sol, 'g--', x_main_axis, ma_sol, 'g^') 
        flag = 'B=%s' % str(sol['stEC_1']) 
        plt.savefig("%s.png" % flag)
        plt.close()
        sol['stEC_1'] +=1 
        
        plt.figure(3)
        axes = plt.gca()
        axes.set_xlim([0,1])
        axes.set_ylim([0,1.5])
        plt.title('%s%f' % ('Ang1-Tie2, Ang2-Tie2 at t=',set['t']))
        plt.plot(x_main_axis, r1_sol, 'r', x_main_axis, r2_sol, 'b') 
        flag = 'C=%s' % str(sol['stEC_2']) 
        plt.savefig("%s.png" % flag)
        plt.close()
        sol['stEC_2'] +=1
        
    else:
#         '''Blood Vessel Growth (TIP and STALK)'''
#         plt.figure(1)
#         axes = plt.gca()
#         axes.set_xlim([0,1])
#         axes.set_ylim([0,1.2])
#         plt.title('%s%f' % ('t=',set['t']))
#         x_main_axis = numpy.arange(set['Hh'], coef['X'], set['h'])
#         x_sub_axis = numpy.arange(0, coef['X']+set['Hh'], set['h'])
#         plt.plot(x_main_axis, n_sol, ':', color = 'k', label = 'Tip cell')
#         plt.plot(x_main_axis, b_sol, '-.', color = 'k', label = 'Stalk cell')
#         plt.plot(x_sub_axis, c_sol, '-', color = 'k', label = 'VEGF') 
#         plt.xlim([0,1])
#         plt.ylim([0,1.2])
#         plt.legend()
#         plt.xlabel('x (position)')
#         plt.ylabel('density')
#         flag = 'N&S&C=%s' % str(sol['stEC']) 
#         plt.savefig("%s.png" % flag)
#         plt.close()
#         sol['stEC'] +=1 
#             
#         plt.figure(2)
#         axes = plt.gca()
#         axes.set_xlim([0,1])
#         axes.set_ylim([0,1.2])
#         plt.title('%s%f' % ('t=',set['t']))
#         x_main_axis = numpy.arange(set['Hh'], coef['X'], set['h'])
#         x_sub_axis = numpy.arange(0, coef['X']+set['Hh'], set['h'])
#         plt.plot(x_main_axis, n_sol, ':', color = 'k', label = 'Tip cell')
#         plt.plot(x_sub_axis, c_sol, '-', color = 'k', label = 'VEGF') 
#         plt.xlim([0,1])
#         plt.ylim([0,1.2])
#         plt.legend()
#         plt.xlabel('x (position)')
#         plt.ylabel('density')
#         flag = 'N&C=%s' % str(sol['stEC_1']) 
#         plt.savefig("%s.png" % flag)
#         plt.close()
#         sol['stEC_1'] +=1 
#             
#         plt.figure(3)
#         axes = plt.gca()
#         axes.set_xlim([0,1])
#         axes.set_ylim([0,1.2])
#         plt.title('%s%f' % ('t=',set['t']))
#         x_main_axis = numpy.arange(set['Hh'], coef['X'], set['h'])
#         x_sub_axis = numpy.arange(0, coef['X']+set['Hh'], set['h'])
#         plt.plot(x_main_axis, n_sol, ':', color = 'k', label = 'Tip cell')
#         plt.plot(x_main_axis, b_sol, '-.', color = 'k', label = 'Stalk cell') 
#         plt.xlim([0,1])
#         plt.ylim([0,1.2])
#         plt.legend()
#         plt.xlabel('x (position)')
#         plt.ylabel('density')
#         flag = 'N&S=%s' % str(sol['stEC_2']) 
#         plt.savefig("%s.png" % flag)
#         plt.close()
#         sol['stEC_2'] +=1 
        
        if set['k'] == 8000:
#             plt.figure(4)
#             axes = plt.gca()
#             axes.set_xlim([0,1])
#             axes.set_ylim([0,1.2])
#             plt.title('Tip cell Density')
#             x_main_axis = numpy.arange(set['Hh'], coef['X'], set['h'])
#             x_sub_axis = numpy.arange(0, coef['X']+set['Hh'], set['h'])
# #             plt.plot(x_main_axis, sol['n_0'], ':', x_main_axis, sol['n_2'], ':', x_main_axis, sol['n_4'], ':', x_main_axis, sol['n_6'], ':', x_main_axis, sol['n_8'], ':', color = 'k') 
#             plt.plot(x_main_axis, sol['n_0'], label = 't=0')
#             plt.plot(x_main_axis, sol['n_2'], label = 't=2')
#             plt.plot(x_main_axis, sol['n_4'], label = 't=4')
#             plt.plot(x_main_axis, sol['n_6'], label = 't=6')
#             plt.plot(x_main_axis, sol['n_8'], label = 't=8') 
#             plt.xlim([0,1])
#             plt.ylim([0,1.2])
#             plt.legend()
#             plt.xlabel('x (position)')
#             plt.ylabel('density')
#             flag = 'N_time'
#             plt.savefig("%s.png" % flag)
#             plt.close()
#               
#             plt.figure(5)
#             axes = plt.gca()
#             axes.set_xlim([0,1])
#             axes.set_ylim([0,1.2])
#             plt.title('Stalk cell Density')
#             x_main_axis = numpy.arange(set['Hh'], coef['X'], set['h'])
#             x_sub_axis = numpy.arange(0, coef['X']+set['Hh'], set['h'])
# #             plt.plot(x_main_axis, sol['b_0'], '-.', x_main_axis, sol['b_2'], '-.', x_main_axis, sol['b_4'], '-.', x_main_axis, sol['b_6'], '-.', x_main_axis, sol['b_8'], '-.', color = 'k') 
#             plt.plot(x_main_axis, sol['b_0'], label = 't=0')
#             plt.plot(x_main_axis, sol['b_2'], label = 't=2')
#             plt.plot(x_main_axis, sol['b_4'], label = 't=4')
#             plt.plot(x_main_axis, sol['b_6'], label = 't=6')
#             plt.plot(x_main_axis, sol['b_8'], label = 't=8') 
#             plt.xlim([0,1])
#             plt.ylim([0,1.2])
#             plt.legend()
#             plt.xlabel('x (position)')
#             plt.ylabel('density')
#             flag = 'S_time'
#             plt.savefig("%s.png" % flag)
#             plt.close()
#               
#             plt.figure(6)
#             axes = plt.gca()
#             axes.set_xlim([0,1])
#             axes.set_ylim([0,1.2])
#             plt.title('VEGF Density')
#             x_main_axis = numpy.arange(set['Hh'], coef['X'], set['h'])
#             x_sub_axis = numpy.arange(0, coef['X']+set['Hh'], set['h'])
# #             plt.plot(x_sub_axis, sol['c_0'], '-', x_sub_axis, sol['c_2'], '-', x_sub_axis, sol['c_4'], '-', x_sub_axis, sol['c_6'], '-', x_sub_axis, sol['c_8'], '-', color = 'k') 
#             plt.plot(x_sub_axis, sol['c_0'], label = 't=0')
#             plt.plot(x_sub_axis, sol['c_2'], label = 't=2')
#             plt.plot(x_sub_axis, sol['c_4'], label = 't=4')
#             plt.plot(x_sub_axis, sol['c_6'], label = 't=6')
#             plt.plot(x_sub_axis, sol['c_8'], label = 't=8') 
#             plt.xlim([0,1])
#             plt.ylim([0,1.2])
#             plt. legend()
#             plt.xlabel('x (position)')
#             plt.ylabel('density')
#             flag = 'C_time'
#             plt.savefig("%s.png" % flag)
#             plt.close()
        
            if set['vegf_dep'] == 1:
                plt.figure(7)
                axes = plt.gca()
                axes.set_xlim([0,1])
                axes.set_ylim([0,1.2])
                plt.title('Tip Density at t=6')
                x_main_axis = numpy.arange(set['Hh'], coef['X'], set['h'])
                x_sub_axis = numpy.arange(0, coef['X']+set['Hh'], set['h'])
    #             plt.plot(x_sub_axis, sol['c_0'], '-', x_sub_axis, sol['c_2'], '-', x_sub_axis, sol['c_4'], '-', x_sub_axis, sol['c_6'], '-', x_sub_axis, sol['c_8'], '-', color = 'k') 
                plt.plot(x_main_axis, sol['n_00'], label = 'VEGF=0')
                plt.plot(x_main_axis, sol['n_22'], label = 'VEGF=0.2')
                plt.plot(x_main_axis, sol['n_44'], label = 'VEGF=0.4')
                plt.plot(x_main_axis, sol['n_66'], label = 'VEGF=0.6')
                plt.plot(x_main_axis, sol['n_88'], label = 'VEGF=0.8')
                plt.plot(x_main_axis, sol['n_1010'], label = 'VEGF=1')
                plt.xlim([0,1])
                plt.ylim([0,1.2])
                plt. legend()
                plt.xlabel('x (position)')
                plt.ylabel('density')
                flag = 'n_vegf'
                plt.savefig("%s.png" % flag)
                plt.close()
                
                plt.figure(8)
                axes = plt.gca()
                axes.set_xlim([0,1])
                axes.set_ylim([0,1.2])
                plt.title('Stalk Density at t=6')
                x_main_axis = numpy.arange(set['Hh'], coef['X'], set['h'])
                x_sub_axis = numpy.arange(0, coef['X']+set['Hh'], set['h'])
    #             plt.plot(x_sub_axis, sol['c_0'], '-', x_sub_axis, sol['c_2'], '-', x_sub_axis, sol['c_4'], '-', x_sub_axis, sol['c_6'], '-', x_sub_axis, sol['c_8'], '-', color = 'k') 
                plt.plot(x_main_axis, sol['b_00'], label = 'VEGF=0')
                plt.plot(x_main_axis, sol['b_22'], label = 'VEGF=0.2')
                plt.plot(x_main_axis, sol['b_44'], label = 'VEGF=0.4')
                plt.plot(x_main_axis, sol['b_66'], label = 'VEGF=0.6')
                plt.plot(x_main_axis, sol['b_88'], label = 'VEGF=0.8')
                plt.plot(x_main_axis, sol['b_1010'], label = 'VEGF=1')
                plt.xlim([0,1])
                plt.ylim([0,1.2])
                plt. legend()
                plt.xlabel('x (position)')
                plt.ylabel('density')
                flag = 'b_vegf'
                plt.savefig("%s.png" % flag)
                plt.close()
           
        
    return