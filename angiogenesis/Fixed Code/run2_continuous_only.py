import continuous_run as cont
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

h = 0.005
X = 1
Y = 1
hh = h/2
Nx = int(X/hh)
Ny = int(Y/hh)

Untuk Plot'''
h = 0.005
roo = 0

Nt = 10000
t = 0
k = 0
T = 0.1
X = 1
Y = 1
hh = h/2
Nx = int(X/hh)
Ny = int(Y/hh)

#r = [0, 0, 0, 0.001]
r = [0,0,0,0.001]
surf = 0
while t <= T and k < Nt:
    start1 = timer()
    k += 1
    '''Continuous Code by Sparse Matrix'''

        
    '''Continuous Code by Non-Matix'''
    r = cont.contiuous_1_iter(iter = k, 
                              n = r[0], c = r[1], f = r[2], 
                              tp = r[3])

        
    t += r[3]
    print 'TIME AT',t
    print 'NILAI N, C, F MAX', r[0].max(), ',', r[1].max(), ',', r[2].max() 
    print 'Time Step Size:', r[3]
    print 'total time of processing:', time.clock()
    print '***************************************************'
    print
   
    
print '*************DONE*****************'

'''Plot Continuous'''
fig1 = plt.figure(1)
ax = fig1.gca(projection='3d')
ax.set_zlim(-0.1, 1)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

x_main_axis = numpy.arange(hh, X, h)
y_main_axis = numpy.arange(hh, Y, h)
x_main_axis, y_main_axis = numpy.meshgrid(x_main_axis, y_main_axis)

n_sol = numpy.zeros((Nx/2, Ny/2))
for j, y in enumerate(range(1,Ny,2)):
    for i, x in enumerate(range(1,Nx,2)):
        n_sol[i,j] = r[0][x,y]
surf = ax.plot_surface(x_main_axis, y_main_axis, n_sol, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
fig1.colorbar(surf, shrink=0.5, aspect=5)
fig1.show()
'''Plot Continuous'''
del r
raw_input()