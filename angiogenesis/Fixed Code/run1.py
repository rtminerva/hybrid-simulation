import matrix_sparse_continuous_Q as sprQ
import discrete_run as disc
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
h = 0.005
the = 0.5
roo = 0 #c2 profile

Nt = 100000
t = 0
k = 0
T = 1
X = 1
Y = 1
hh = h/2
Nx = int(X/hh)
Ny = int(Y/hh)

r = [0, 0, 0, 0.001]
#r = [0,0,0,0,0,0.001]
g = [0, 0, 0, 0, 0, 0]
surf = 0
while t <= T and k < Nt:
    start1 = timer()
    k += 1
    '''Continuous Code by Sparse Matrix'''
    r = sprQ.continuous_sparse_matrix_1_iter(iter = k, hh = Hh, teta = the, ro = roo,
                                            n = r[0], c = r[1], f = r[2], 
                                            tp = r[3])
#    r = sprlil.continuous_sparse_matrix_1_iter(iter = k, h3 = h, teta = the, ro = roo,
#                                            n = r[0], c = r[1], f = r[2], 
#                                            tp = r[3])
    
#    '''Continuous Code by Matrix Using Gauss Method to Solve SPL'''
#     r = gauss.continuous_matrix_1_iter(iter = k, 
#                                        n_o = r[0], c_o = r[1], f_o = r[2], 
#                                        n = r[3], c = r[4], f = r[5], 
#                                        tp = r[6])
        
#     '''Continuous Code by Non-Matix'''
#         r = cont.contiuous_1_iter(iter = k, 
#                                   c_o = r[0], f_o = r[1], 
#                                   n = r[2], c = r[3], f = r[4], 
#                                   tp = r[5])

        
    t += r[3]
    print 'TIME AT',t
    start2 = timer()
    
    '''Discrete Code'''
    g = disc.discrete_1_iter(iter = k, h2 = h, ro = roo,
                             n = r[0], c = r[1], f = r[2], tp = r[3],
                             matrix_tip = g[0], list_last_movement = g[1], 
                             list_tip_movement = g[2], life_time_tip = g[3],
                             stop_iter = g[4], sp_stop = g[5])
      
    start3 = timer()
     
    if g[4] >=10000:
        k = g[4]
    print 'NILAI N, C, F MAX', r[0].max(), ',', r[1].max(), ',', r[2].max() 
    print 'Time Step Size:', r[3]
    print 'process time of Cont:', start2-start1
    print 'process time of Disc:', start3-start2
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

'''Plot Continuous'''
fig1 = plt.figure(1)
ax = fig1.gca(projection='3d')
ax.set_zlim(-0.1, 1)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
plt.xlabel('X axis')
plt.ylabel('Y axis')

x_main_axis = numpy.arange(hh, X, h)
y_main_axis = numpy.arange(hh, Y, h)
x_main_axis, y_main_axis = numpy.meshgrid(x_main_axis, y_main_axis)

n_sol = numpy.zeros((Nx/2, Ny/2))
for j, y in enumerate(range(1,Ny,2)):
    for i, x in enumerate(range(1,Nx,2)):
        n_sol[i,j] = r[0][x,y]
surf = ax.plot_surface(x_main_axis, y_main_axis, n_sol, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False, label = 'n(x,y) profile')
fig1.colorbar(surf, shrink=0.5, aspect=5)
fig1.show()
'''Plot Continuous'''
del r

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

