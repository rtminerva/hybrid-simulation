import tip_cell as disc
import numpy
from timeit import default_timer as timer 
import time

import matplotlib.pyplot as plt 
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
# import discrete_run as disc

'''Untuk Plot
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D


plt.ion() #interactively
plt.show()
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_zlim(-0.1, 1.2)

Untuk Plot'''


'''Coefficients'''
Ro = 0.0125
D_n = 0.00018
D_c = 0.005
Ki_n = 0.4
Al_n = 0.6
Nu = 0.1
Beta = 1.5
Gama = 0.1

'''Spatial and Temporal Meshes Number'''
R_min = 0.5
R_max = 1
N_r = 201
N_p = 201 #odd number
Nt = 100000

'''Setting up '''
t = 0
k = 0
T = 1
dt = 0.001

g = [0, 0, 0, 0, 0, 0, 0, 0, 0, dt]
surf = 0
while t <= T and k < Nt:
    start1 = timer()
    k += 1
    t += 0.001
    '''Discrete Code'''
    g = disc.discrete_1_iter(iter = k, n_r = N_r, n_p = N_p, r_min = R_min, r_max = R_max,
                             ro = Ro, d_n = D_n, d_c = D_c, ki_n = Ki_n, al_n = Al_n, nu = Nu, be = Beta, ga = Gama,
                             matrix_tip = g[0], list_last_movement = g[1], 
                             list_tip_movement = g[2], life_time_tip = g[3],
                             stop_iter = g[4], sp_stop = g[5],
                             n = g[6], c = g[7], f = g[8], tp = g[9])
      
    start2 = timer()
     
    if g[4] >=10000:
        k = g[4]
    print 'at Time', t
    print 'NILAI C, F MAX', g[7].max(), ',', g[8].max() 
    print 'process time of Hybrid:', start2-start1
    print 'total time of processing:', time.clock()
    print '***************************************************'
    print
    
#    '''Plot Hybrid'''
#    fig2 = plt.figure(2)
#    plt.ion()
#    plt.show()
#    plt.xlim(hh,X-hh)#X-hh
#    plt.ylim(hh,Y-hh)#
#    ax = fig2.add_subplot(111)
#    plot_all = []
#    for i in range(0,len(g[0])):
#        x_p = g[0][i][-1][0]*hh
#        y_p = g[0][i][-1][1]*hh
#        ax.scatter(x_p, y_p, edgecolors='none')
#        plt.draw()
#        time.sleep(0.05)
#    '''Plot Hybrid'''
    
    
print '*************DONE*****************'

'''Plot Hybrid'''

#ax.plot(theta_matrix, radius_matrix, color='g', ls='none', marker='.')

#plt.xlim(hh,X-hh)#X-hh
#plt.ylim(hh,Y-hh)#
d_r = (R_max - R_min)/N_r
d_p = 2*numpy.pi/N_p

ax = plt.subplot(111, polar=True)
for i in range(0,len(g[0])):
    R_p = []
    P_p = []
    for j in range(0,len(g[0][i])):
        R_p.append(g[0][i][j][0]*d_r)
        P_p.append(g[0][i][j][1]*d_p)
    globals()['plo%s' % i] = ax.plot(P_p, R_p, 'b')
plt.show()   
'''Plot Hybrid'''

