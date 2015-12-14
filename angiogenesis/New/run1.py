import continuous_run as cont
import matrix_code_gauss as gauss
import discrete_run as disc
import numpy
from timeit import default_timer as timer 
import time
import matplotlib.pyplot as plt 
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

h = 0.005
X = 1
Y = 1
hh = h/2
Nx = int(X/hh)
Ny = int(Y/hh)
   
x_main_axis = numpy.arange(hh, X, h)
y_main_axis = numpy.arange(hh, Y, h)
x_main_axis, y_main_axis = numpy.meshgrid(x_main_axis, y_main_axis)

# x_sub_axis = numpy.arange(0, X+hh, h)
# y_sub_axis = numpy.arange(0, Y+hh, h)
# x_sub_axis, y_sub_axis = numpy.meshgrid(x_sub_axis, y_sub_axis)
Untuk Plot'''

Nt = 10000
t = 0
k = 0
T = 1.27
r = [0, 0, 0, 0, 0, 0, 0.001]
g = [0, 0, 0, 0, 0, 0]
surf = 0
while t <= T and k < Nt:
    start1 = timer()
    k += 1    
    '''Continuous Code'''
    r = cont.contiuous_1_iter(iter = k, 
                              n_o = r[0], c_o = r[1], f_o = r[2], 
                              n = r[3], c = r[4], f = r[5], 
                              tp = r[6])
    t += r[6]
    print 'TIME AT',t
    start2 = timer()
    
    '''Discrete Code'''
    g = disc.discrete_1_iter(iter = k,
                             n = r[3], c = r[4], f = r[5],
                             matrix_tip = g[0], list_last_movement = g[1], 
                             list_tip_movement = g[2], life_time_tip = g[3],
                             stop_iter = g[4], sp_stop = g[5])
      
    start3 = timer()
     
    if g[4] == 100000:
        k == Nt
    
    '''Plot Continuous real time
    if k % 100 == 0 or k == 1: #k==11:
        print 'masuk draw'
        
        n_sol = numpy.zeros((Nx/2, Ny/2))
        for j, y in enumerate(range(1,Ny,2)):
            for i, x in enumerate(range(1,Nx,2)):
                n_sol[i,j] = r[3][x,y]  
        start3 = timer()
        n_sol_time = start3-start2
        print 'process time for n_sol:', n_sol_time
 
#         del surf
        surf = ax.plot_surface(x_main_axis, y_main_axis, n_sol, rstride=1, cstride=1, cmap=cm.coolwarm,
                linewidth=0, antialiased=False)
        start4 = timer()
        surf_time = start4-start3
        print 'process time for making surf:', surf_time
        plt.draw()
        start5 = timer()
        draw_time = start5-start4
        print 'process time for drawing:', draw_time
#         time.sleep(0.01)
    Plot Continuous real time'''
    print 'Time Step Size:', r[6]
    print 'process time of Cont:', start2-start1
    print 'process time of Disc:', start3-start2
    print 'total ime of processing:', time.clock()
    print '***************************************************'
    print

print '*************DONE*****************'


h = 0.005
X = 1
Y = 1
hh = h/2 
fig = plt.figure()
plt.xlim(hh,X-hh)#X-hh
plt.ylim(hh,Y-hh)#
ax = fig.add_subplot(111)
plot_all = []
for i in range(0,len(g[0])):
    x_p = []
    y_p = []
    for j in range(0,len(g[0][i])):
        x_p.append(g[0][i][j][0]*hh)
        y_p.append(g[0][i][j][1]*hh)
    globals()['plo%s' % i] = ax.plot(x_p, y_p, 'b')
plt.show()   
 
plt.show(block=True)

