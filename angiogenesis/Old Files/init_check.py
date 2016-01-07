import random
from random import randint
import math

'''Parameter'''
d = 0.00035
ki = 0.38
al = 0.6
ro = 0.3 #0
nu = 0.1
be = 0.05
ga = 0.1

ef = 0.45
ec = 0.45
#k = (5**0.5-0.1)/(5**0.5-1)
tau = 0.001


'''Partition'''
X = 1
Y = 1
T = 1

h = 0.005  
hh = h/2

Nx = int(X/hh)
Ny = int(Y/hh)
Nt = 10000

print 'Nx =',Nx
print 'Node =', range(0,Nx+1)
print 'point n,v,w=', range(1,Nx,2)
print 'point F,c,f=', range(0,Nx+1,2)


'''Define Variable'''
import numpy
import math

n = numpy.zeros((Nx+1, Ny+1, Nt+1))

'''Initial Condition'''
#p[i,0] = (math.sin((math.pi)*i*h))**2
for y in range(1,Ny,2):
    for x in range(1,Nx,2):
        tipss = 6
        n[x,y,0] = math.exp(-(x*hh)**2/0.001)*(math.sin(tipss*math.pi*y*hh))**2
split = int(Nx/tipss)
aw = 0
index_tip = []
for i in range(1,tipss+1):
    jj = i*split
    print jj
    a = []
    for u in range(aw,jj+1):
        a.append(n[1,u,0])
    m = max(a)
    for i in range(0,len(a)):
        if len(index_tip)>0:
            tess = i+aw-index_tip[-1]
            if a[i] == m and tess>2:
                index_tip.append(i+aw)
        else:
            if a[i] == m:
                index_tip.append(i+aw)
    aw = jj+1
print index_tip
for i in range(0,len(index_tip)):
    print n[1,index_tip[i],0]

'''Plot Result'''
l =0
x_main_axis = numpy.arange(hh, X, h)
y_main_axis = numpy.arange(hh, Y, h)
x_main_axis, y_main_axis = numpy.meshgrid(x_main_axis, y_main_axis)

x_sub_axis = numpy.arange(0, X+hh, h)
y_sub_axis = numpy.arange(0, Y+hh, h)
x_sub_axis, y_sub_axis = numpy.meshgrid(x_sub_axis, y_sub_axis)

n_sol = numpy.zeros((Nx/2, Ny/2))      
        
for j, y in enumerate(range(1,Ny,2)):
    for i, x in enumerate(range(1,Nx,2)):
        n_sol[i,j] = n[x,y,l]
        
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x_main_axis, y_main_axis, n_sol, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
# surf = ax.plot_surface(x_sub_axis, y_sub_axis, c_sol, rstride=1, cstride=1, cmap=cm.coolwarm,
#         linewidth=0, antialiased=False)
ax.set_zlim(-0.1, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()