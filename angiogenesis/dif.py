'''Domain'''
from duplicity.path import Path
X=1
Y=1
T=50

dx=0.1
dy=0.1
dt=0.01

Nx=int(X/dx)
Ny=int(Y/dy)
Nt=int(T/dt)


'''Initial condition ijk'''
import numpy
import math

#initial n
nw = []
wx = []
wy = []
n = numpy.zeros((Nx+1,Ny+1,Nt+1))
for j in range(Ny+1):
    for i in range(Nx+1):
        n[i,j,0] = math.exp(-(j*dy)**2/0.001)*(math.sin(6*(math.pi)*i*dx))**2
        nw.append(n[i,j,0])
        wx.append(j*dx)
        wy.append(i*dy)
#print n[:,Ny,0]
#node filling
##constant
D = 0.00035
for it in range(Nt):
    for iy in range(Ny+1):
        ##filling node boundary
        if (iy==0):#boundary bawah
            for ix in range(Nx+1): 
                if (ix==0):#pojok kiri bawah
                    n[ix,iy,it+1] = n[ix,iy,it] + dt*D/dx**2*(-4*n[ix,iy,it]+2*n[ix+1,iy,it]+2*n[ix,iy+1,it])
                elif (ix==Nx):#pojok kanan bawah
                    n[ix,iy,it+1] = n[ix,iy,it] + dt*D/dx**2*(-4*n[ix,iy,it]+2*n[ix-1,iy,it]+2*n[ix,iy+1,it])
                else:#selain pojokan namun dibawah
                    n[ix,iy,it+1] = n[ix,iy,it] + dt*D/dx**2*(-4*n[ix,iy,it]+n[ix+1,iy,it]+n[ix-1,iy,it]+2*n[ix,iy+1,it])
        elif (iy==Ny):#boundary atas
            for ix in range(Nx+1):
                if (ix==0):#pojok kiri atas
                    n[ix,iy,it+1] = n[ix,iy,it] + dt*D/dx**2*(-4*n[ix,iy,it]+2*n[ix+1,iy,it]+2*n[ix,iy-1,it])
                elif (ix==Nx):#pojok kanan atas
                    n[ix,iy,it+1] = n[ix,iy,it] + dt*D/dx**2*(-4*n[ix,iy,it]+2*n[ix-1,iy,it]+2*n[ix,iy-1,it])
                else:#selain pojokan namun diatas
                    n[ix,iy,it+1] = n[ix,iy,it] + dt*D/dx**2*(-4*n[ix,iy,it]+n[ix+1,iy,it]+n[ix-1,iy,it]+2*n[ix,iy-1,it])
        else:#selain boundary atas bawah
            for ix in range(Nx+1):
                if (ix==0):#selain boundary atas bawah namun dipinggiran kiri
                    n[ix,iy,it+1] = n[ix,iy,it] + dt*D/dx**2*(-4*n[ix,iy,it]+2*n[ix+1,iy,it]+n[ix,iy+1,it]+n[ix,iy-1,it])
                elif (ix==Nx):#selain boundary atas bawah namun dipinggiran kanan
                    n[ix,iy,it+1] = n[ix,iy,it] + dt*D/dx**2*(-4*n[ix,iy,it]+2*n[ix-1,iy,it]+n[ix,iy+1,it]+n[ix,iy-1,it])
                else:#tengah2 selain boundary
                    n[ix,iy,it+1] = n[ix,iy,it] + dt*D/dx**2*(-4*n[ix,iy,it]+n[ix+1,iy,it]+n[ix-1,iy,it]+n[ix,iy+1,it]+n[ix,iy-1,it])
for u1 in range(Nt+1):
    for u2 in range(Ny+1):
        for u3 in range(Nx+1):
            if n[u3,u2,u1]<0:
                print 'negative value'
                print u3, u2, u1
                quit()
nw1 = []
for j in range(Ny+1):
    for i in range(Nx+1):
        nw1.append(n[i,j,Nt])
        
print len(wx)
print len(wy)
print len(nw1) 
quit()
                
'''FIGURE'''
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from matplotlib.mlab import griddata
xx = np.arange(0, (X+dx), dx)
yy = np.arange(0, (Y+dy), dy)
xx, yy = np.meshgrid(xx, yy)
ZZ = griddata(wx, wy, nw, xx, yy)
ZZsol = griddata(wx, wy, nw1, xx, yy)
from mpl_toolkits.mplot3d import Axes3D

fig1 = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(xx, yy, ZZ, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
plt.show()    

fig1 = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(xx, yy, ZZsol, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
plt.show()  