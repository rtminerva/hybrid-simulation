import code_no_mural as disc
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

D_c = 0.005
Nu = 0.1

Beta = 0.05
Gama = 0.1

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
error = 0.01

T_branch = 0.078 #

g = [0, 0, 0, 0, 0, 0, 0, 0, dt]
surf = 0
while t <= T and k < Nt:
    start1 = timer()
    k += 1
    t += dt
    '''Discrete Code'''
    g = disc.discrete_1_iter(iter = k, hh = Hh, Nx = nx, Ny = ny,
                             r_min = R_min, r_max = R_max,
                             ro = Ro, d_n = D_n, d_c = D_c, ki_n = Ki_n, al_n = Al_n, nu = Nu, be = Beta, ga = Gama, 
                             matrix_tip = g[0],  
                             list_tip_movement = g[1], life_time_tip = g[2],
                             stop_iter = g[3], sp_stop = g[4],
                             n = g[5], c = g[6], f = g[7], tp = g[8],
                             Error = error,
                             t_branch = T_branch)
      
    start2 = timer()
     
    if g[3] >=10000:
        k = g[3]
    print 'at Time', t
    print 'NILAI C, F MAX', g[6].max(), ',', g[7].max()
    print 'process time of Hybrid:', start2-start1
    print 'total time of processing:', time.clock()
    print '***************************************************'
    print
    
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

