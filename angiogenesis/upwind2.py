'''Domain'''
from twisted.test.test_amp import WTF
X = 1
T = 0.1

h_half = 0.2/2
h = 0.2
dt = 0.0001

Nx = int(X/h_half)
Nt = int(T/dt)

'''Initial Condition'''
import numpy
import math

p = numpy.zeros((Nx+1, Nt+1))
w = numpy.zeros((Nx+1, Nt+1))
f = numpy.zeros((Nx+1, Nt+1))
for i in range(1,Nx+1,2):
#     p[i,0] = (math.sin((math.pi)*i*h))**2
    p[i,0] = 0
p[int(Nx/2),0] = 100

'''constant'''
a = -1



# for x in range(0,Nx+1,2): 
#     print x
# for x in range(1,Nx-1,2): 
#     print x
# quit()
'''filling the node'''
#Nx+5 = 25
for t in range(Nt):
    #fill W
    for x in range(0,Nx+1,2):#x = 0,2,4,..., 14
        if x==0:
            w[x,t+1] = w[x,t] + dt*p[x+1,t]      
        elif x==Nx:
            w[x,t+1] = w[x,t] + dt*p[x-1,t]
        else:
            w[x,t+1] = w[x,t] + 1/2*dt*(p[x-1,t]+p[x+1,t])
    #fill P
    f[0,t] = 0
    f[Nx,t] = 0
    for x in range(2,Nx,2):#x = 2,4,6,8
         #cek dir
         q_l = a/h*(w[x,t]-w[x-2,t])
         q_r = a/h*(w[x+2,t]-w[x,t])
         b_l = max(0,q_l)
         b_r = max(0,-q_r)
         f[x,t] = (p[x+1,t]-p[x-1,t])/h - b_l*p[x-1,t] + b_r*p[x+1,t]
         p[x-1,t+1] = p[x-1,t] + dt/h*(f[x,t]-f[x-2,t])

for t in range(Nt):
    for x in range(Nx+1):
        if p[x,t]<0:
            print 'neg'
# for i, j in enumerate(range(1,Nx,2)):
#     print i,j

sol = numpy.zeros((Nx/2, Nt+1))
for t in range(Nt+1):
    for i, j in enumerate(range(1,Nx,2)):
        sol[i,t] = p[j,t]

'''Draw solution'''
qx = []
wx = []
wt = []
for t in range(Nt+1):
    for x in range(5):
        wt.append(t*dt)
qx.append(h_half)
for x in range(1, 5,):
    qx.append(qx[x-1]+h)     
for t in range(Nt+1):
    for i in range(5):
        wx.append(qx[i])
    
sol1 = []
for t in range(Nt+1):
    for x in range(5):
        sol1.append(sol[x,t])
print len(wx)
print wx
print len(wt)
print len(sol1) 


import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from matplotlib.mlab import griddata
xx = np.arange(0, X, h_half)
tt = np.arange(0, T, dt)
xx, tt = np.meshgrid(xx, tt)
ZZ = griddata(wx, wt, sol1, xx, tt)
from mpl_toolkits.mplot3d import Axes3D
fig1 = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(xx, tt, ZZ, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
plt.show()  

# print p[:,0]
# print p[:,20]
# print p[:,40]
# print p[:,60]
# print p[:,80]