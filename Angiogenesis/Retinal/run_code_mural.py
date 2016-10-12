import code_mural as disc
import code_mural_continuous as cont
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
Ro = 0.16
D_n = 0.00018
Ki_n = 0.4
Al_n = 0.6

D_c = 0.005 #
Nu = 0.1

Beta = 0.05
Gama = 0.1

D_m = 0.00018 #
Ki_m = 0.4 #
Al_m = 0.6 #

A_p = 0.1 #
B_p = 0.1 #
Dl = 0.05 #


Kappa = 0 #0.1 #
Mic = 0 #0.1 #

T_branch = 0.078 #

the = 0.75


'''Spatial and Temporal Meshes Number'''
h = 0.02
X = 4.4
Y = 4.4
Hh = h/2
nx = int(X/Hh)
ny = int(Y/Hh)

R_min = 0.52/2
R_max = X
Nt = 100000

'''Setting up '''
t = 0
k = 0
T = 0.5
dt = 0.001
error = 0.008

g = [0, 0, 0, 0, 0, 0, 0]
r = [0, 0, 0, 0, dt]
surf = 0
while t <= T and k < Nt:
    start1 = timer()
    k += 1
    '''Discrete Code'''
    g = disc.discrete_1_iter(iter = k, hh = Hh, Nx = nx, Ny = ny,
                             r_min = R_min, r_max = R_max,
                             ro = Ro, d_n = D_n, ki_n = Ki_n, al_n = Al_n,
                             t_branch = T_branch,
                             matrix_tip = g[0], list_last_movement = g[1], 
                             list_tip_movement = g[2], life_time_tip = g[3],
                             stop_iter = g[4], sp_stop = g[5],
                             n = g[6], tp = r[4], c= r[0], f =r[1], m = r[2],
                             Error = error,
                             kappa = Kappa, mic = Mic)
    if k ==1:
        tip_init = []
        for i in g[0]:
            tip_init.append(i[0])
    r = cont.continuous_sparse_matrix_1_iter(teta = the,
                                             c = r[0], f = r[1], m = r[2], p = r[3], tp = r[4], n = g[6],
                                             iter = k, hh = Hh, Nx = nx, Ny = ny,
                                             r_min = R_min, r_max = R_max,
                                             d_c = D_c, nu = Nu,
                                             be = Beta, ga = Gama, 
                                             d_m = D_m, ki_m = Ki_m, al_m = Al_m,
                                             a_p = A_p, b_p = B_p, dl = Dl,
                                             Error = error, init_tip = tip_init)
    

    start2 = timer()
     
    if g[4] >=10000:
        k = g[4]
    print 'at Time', t
    print 'NILAI C, F, M, P MAX', r[0].max(), ',', r[1].max() , ',', r[2].max(), ',', r[3].max()
    print 'process time of Hybrid:', start2-start1
    print 'total time of processing:', time.clock()
    print '***************************************************'
    print
    t += r[4]
print '*************DONE*****************'

'''Plot Continuous
fig1 = plt.figure(1)
ax = fig1.gca(projection='3d')
ax.set_zlim(-0.1, 1)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

x_main_axis = numpy.arange(0, X+Hh, h)
y_main_axis = numpy.arange(0, Y+Hh, h)
x_main_axis, y_main_axis = numpy.meshgrid(x_main_axis, y_main_axis)

c_sol = numpy.zeros((nx/2+1, ny/2+1))
for j, y in enumerate(range(0,ny+1,2)):
    for i, x in enumerate(range(0,nx+1,2)):
        c_sol[i,j] = g[8][x,y]
surf = ax.plot_surface(x_main_axis, y_main_axis, c_sol, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
fig1.colorbar(surf, shrink=0.5, aspect=5)
fig1.show()
Plot Continuous'''


'''Plot Hybrid'''
fig2 = plt.figure(2)
O_x = nx/2*Hh
O_y = ny/2*Hh
plt.xlim(Hh,X-Hh)#X-hh
plt.ylim(Hh,Y-Hh)#
ax = fig2.add_subplot(111)
#an = numpy.linspace(0, 2*numpy.pi, 100)
#plt.plot((R_min)*numpy.cos(an)+O_x, (R_min)*numpy.sin(an)+O_y, color ='black')
for i in range(0,len(g[0])):
    x_p = []
    y_p = []
    for j in range(0,len(g[0][i])):
        x_p.append(g[0][i][j][0]*Hh)
        y_p.append(g[0][i][j][1]*Hh)
    globals()['plo%s' % i] = ax.plot(x_p, y_p, 'b')
fig2.show()   

'''Plot Hybrid'''
raw_input()
# plt.show(block=True)

