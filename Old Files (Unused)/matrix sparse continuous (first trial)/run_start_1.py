import start_1 as disc
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
h = 0.01
ty = 0.001
the = 0.5
roo = 0 #c2 profile

Nt = 100000
t = 0
k = 0
T = 2
X = 1
Y = 1
hh = h/2
Nx = int(X/hh)
Ny = int(Y/hh)

g = [0, 0, 0, 0, 0, 0, 0, 0, 0, ty]
surf = 0
while t <= T and k < Nt:
    start1 = timer()
    k += 1
    t += ty
    '''Discrete Code'''
    g = disc.discrete_1_iter(iter = k, h2 = h, ro = roo,
                             n = g[6], c = g[7], f = g[8], tp = g[9],
                             matrix_tip = g[0], list_last_movement = g[1], 
                             list_tip_movement = g[2], life_time_tip = g[3],
                             stop_iter = g[4], sp_stop = g[5])
      
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
X = 1
Y = 1
hh = h/2 
fig2 = plt.figure(2)
plt.xlim(hh,X-hh)#X-hh
plt.ylim(hh,Y-hh)#
ax = fig2.add_subplot(111)
plot_all = []
for i in range(0,len(g[0])):
    x_p = []
    y_p = []
    for j in range(0,len(g[0][i])):
        x_p.append(g[0][i][j][0]*hh)
        y_p.append(g[0][i][j][1]*hh)
    globals()['plo%s' % i] = ax.plot(x_p, y_p, 'b')
fig2.show()   
del g
'''Plot Hybrid'''
raw_input()
# plt.show(block=True)

