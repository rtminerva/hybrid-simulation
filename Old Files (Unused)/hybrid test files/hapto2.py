'''Domain'''
from duplicity.path import Path
X=10
Y=10
T=1
import numpy
old_settings = numpy.seterr(all='ignore')

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
fw = []
wx = []
wy = []
n = numpy.zeros((Nx+1,Ny+1,Nt+1))
for i in range(Nx+1):
    n[i,0,0] = 1
    nw.append(n[i,0,0])
#for j in range(Ny+1):
#    for i in range(Nx+1):
#        n[i,j,0] = math.exp(-(j*dy)**2/0.001)*(math.sin(6*(math.pi)*i*dx))**2
#        nw.append(n[i,j,0])
#        wx.append(j*dx)
#        wy.append(i*dy)
#print n[:,Ny,0]
#initial f

f = numpy.zeros((Nx+1,Ny+1,Nt+1))
for i in range(Ny+1):
    for j in range(Nx+1):
        wx.append(j*dx)
        wy.append(i*dy)
        f[j,i,0] = math.exp(-(dy*i)**2/0.35)
        fw.append(f[j,i,0])
        
ro = 1#0.34
ga = 1#0.1
be = 1#0.05

for it in range(Nt):
    for iy in range(Ny+1):
        ##filling node boundary
        if (iy==0):#boundary bawah
            for ix in range(Nx+1):
                f[ix,iy,it+1] = f[ix,iy,it]*(1-dt*ga*n[ix,iy,it])+dt*be*n[ix,iy,it]
                P_3 = 0
                P_4 = 0
                P_1 = 0
                P_2 = 0
                if (ix==0):#pojok kiri bawah
                    P_0 = 1- dt*ro/dx**2*(2*f[ix+1,iy,it]-4*f[ix,iy,it]+2*f[ix,iy+1,it])
                    n[ix,iy,it+1] = P_0*n[ix,iy,it] + P_1*n[ix+1,iy,it] + P_2*n[ix,iy,it] + P_3*n[ix,iy+1,it] + P_4*n[ix,iy,it]
                elif (ix==Nx):#pojok kanan bawah
                    P_0 = 1- dt*ro/dx**2*(2*f[ix-1,iy,it]-4*f[ix,iy,it]+2*f[ix,iy+1,it])
                    n[ix,iy,it+1] = P_0*n[ix,iy,it] + P_1*n[ix,iy,it] + P_2*n[ix-1,iy,it] + P_3*n[ix,iy+1,it] + P_4*n[ix,iy,it]
                else:#selain pojokan namun dibawah
                    P_0 = 1- dt*ro/dx**2*(f[ix+1,iy,it]+f[ix-1,iy,it]-4*f[ix,iy,it]+2*f[ix,iy+1,it])
                    n[ix,iy,it+1] = P_0*n[ix,iy,it] + P_1*n[ix+1,iy,it] + P_2*n[ix-1,iy,it] + P_3*n[ix,iy+1,it] + P_4*n[ix,iy-1,it]
        elif (iy==Ny):#boundary atas
            for ix in range(Nx+1):
                f[ix,iy,it+1] = f[ix,iy,it]*(1-dt*ga*n[ix,iy,it])+dt*be*n[ix,iy,it]
                P_3 = 0
                P_4 = 0
                P_1 = 0
                P_2 = 0
                if (ix==0):#pojok kiri atas
                    P_0 = 1- dt*ro/dx**2*(2*f[ix+1,iy,it]-4*f[ix,iy,it]+2*f[ix,iy-1,it])
                    n[ix,iy,it+1] = P_0*n[ix,iy,it] + P_1*n[ix+1,iy,it] + P_2*n[ix,iy,it] + P_3*n[ix,iy,it] + P_4*n[ix,iy-1,it]
                elif (ix==Nx):#pojok kanan atas
                    P_0 = 1- dt*ro/dx**2*(2*f[ix-1,iy,it]-4*f[ix,iy,it]+2*f[ix,iy-1,it])
                    n[ix,iy,it+1] = P_0*n[ix,iy,it] + P_1*n[ix,iy,it] + P_2*n[ix-1,iy,it] + P_3*n[ix,iy,it] + P_4*n[ix,iy-1,it]
                else:#selain pojokan namun diatas
                    P_0 = 1- dt*ro/dx**2*(f[ix+1,iy,it]+f[ix-1,iy,it]-4*f[ix,iy,it]+2*f[ix,iy-1,it])
                    n[ix,iy,it+1] = P_0*n[ix,iy,it] + P_1*n[ix+1,iy,it] + P_2*n[ix-1,iy,it] + P_3*n[ix,iy,it] + P_4*n[ix,iy-1,it]
        else:#selain boundary atas bawah
            for ix in range(Nx+1):
                f[ix,iy,it+1] = f[ix,iy,it]*(1-dt*ga*n[ix,iy,it])+dt*be*n[ix,iy,it]
                P_3 = - dt/(4*dx**2)*(ro*(f[ix,iy+1,it]-f[ix,iy-1,it]))
                P_4 = dt/(4*dx**2)*(ro*(f[ix,iy+1,it]-f[ix,iy-1,it]))
                if (ix==0):#selain boundary atas bawah namun dipinggiran kiri
                    P_1 = 0
                    P_2 = 0
                    P_0 = 1- dt*ro/dx**2*(2*f[ix+1,iy,it]-4*f[ix,iy,it]+f[ix,iy+1,it]+f[ix,iy-1,it])
                    n[ix,iy,it+1] = P_0*n[ix,iy,it] + P_1*n[ix+1,iy,it] + P_2*n[ix,iy,it] + P_3*n[ix,iy+1,it] + P_4*n[ix,iy-1,it]
                elif (ix==Nx):#selain boundary atas bawah namun dipinggiran kanan
                    P_1 = 0
                    P_2 = 0
                    P_0 = 1- dt*ro/dx**2*(2*f[ix-1,iy,it]-4*f[ix,iy,it]+f[ix,iy+1,it]+f[ix,iy-1,it])
                    n[ix,iy,it+1] = P_0*n[ix,iy,it] + P_1*n[ix,iy,it] + P_2*n[ix-1,iy,it] + P_3*n[ix,iy+1,it] + P_4*n[ix,iy-1,it] 
                else:#tengah2 selain boundary
                    P_1 = - dt/(4*dx**2)*(ro*(f[ix+1,iy,it]-f[ix-1,iy,it]))
                    P_2 = dt/(4*dx**2)*(ro*(f[ix+1,iy,it]-f[ix-1,iy,it]))
                    P_0 = 1- dt*ro/dx**2*(f[ix+1,iy,it]+f[ix-1,iy,it]-4*f[ix,iy,it]+f[ix,iy+1,it]+f[ix,iy-1,it])
                    n[ix,iy,it+1] = P_0*n[ix,iy,it] + P_1*n[ix+1,iy,it] + P_2*n[ix-1,iy,it] + P_3*n[ix,iy+1,it] + P_4*n[ix,iy-1,it]
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

'''FIGURE'''
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from matplotlib.mlab import griddata
xx = np.arange(0, (X+dx), dx)
yy = np.arange(0, (Y+dy), dy)
xx, yy = np.meshgrid(xx, yy)
Z2 = griddata(wx, wy, fw, xx, yy)
#ZZ = griddata(wx, wy, nw, xx, yy)
ZZsol = griddata(wx, wy, nw1, xx, yy)
from mpl_toolkits.mplot3d import Axes3D

fig1 = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(xx, yy, ZZsol, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
plt.show()  