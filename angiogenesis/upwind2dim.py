'''Domain'''
from twisted.test.test_amp import WTF
from PyQt4.QtGui import QX11EmbedContainer
X = 1
Y = 1
T = 10

h_half = 0.2/2
h = 0.2
dt = 1

Nx = int(X/h_half)
Ny = int(Y/h_half)
Nt = int(T/dt)

'''Initial Condition'''
import numpy
import math

p = numpy.zeros((Nx+5, Ny+5, Nt+1))
w = numpy.zeros((Nx+5, Ny+5, Nt+1))
f1 = numpy.zeros((Nx+5, Ny+5, Nt+1))
f2 = numpy.zeros((Nx+5, Ny+5, Nt+1))
# for i in range(1,Nx+5,2):
#     for j in range(1,Ny+5,2):
#         p[i,j,0] = 0
        #p[i,0] = (math.sin((math.pi)*i*h))**2
p[int(Nx/2+2),int(Ny/2+2),0] = 100

'''constant'''
a = -1

'''filling the node'''
#Nx+5 = 25
for t in range(Nt):
    #fill W (done)
    for y in range(0,Ny+5,2):#x = 0,2,4,..., 14
        if y==0:#lower boundary
            for x in range(0,Nx+5,2):
                if x==0:#down left corner
                    w[x,y,t+1] = w[x,y,t] + dt*p[x+1,y+1,t]
                elif x==Nx+4:#down right corner
                    w[x,y,t+1] = w[x,y,t] + dt*p[x-1,y+1,t]
                else:
                    w[x,y,t+1] = w[x,y,t] + 1/2*dt*(p[x+1,y+1,t]+p[x-1,y+1,t])
        elif y==Ny+4:#upper boundary
            for x in range(0,Nx+5,2):
                if x==0:#up left corner
                    w[x,y,t+1] = w[x,y,t] + dt*p[x+1,y-1,t]
                elif x==Nx+4:#up right corner
                    w[x,y,t+1] = w[x,y,t] + dt*p[x-1,y-1,t]
                else:
                    w[x,y,t+1] = w[x,y,t] + 1/2*dt*(p[x+1,y-1,t]+p[x-1,y-1,t])
        else:#other than lower and upper boundary
            for x in range(0,Nx+5,2):
                if x==0:#left boundary
                    w[x,y,t+1] = w[x,y,t] + 1/2*dt*(p[x+1,y-1,t]+p[x+1,y+1,t])
                elif x==Nx+4:#right boundary
                    w[x,y,t+1] = w[x,y,t] + 1/2*dt*(p[x-1,y-1,t]+p[x-1,y+1,t])
                else:
                    w[x,y,t+1] = w[x,y,t] + 1/4*dt*(p[x-1,y-1,t]+p[x+1,y-1,t]+p[x+1,y+1,t]+p[x-1,y+1,t])
    #fill P
    f1[0,y,t] = 0
    f1[Nx+4,y,t] = 0
    f2[x,0,t] = 0
    f2[x,Ny+4,t] = 0
    for y in range(2,Ny+3,2):#y = 2,4,6,8,10,12
        for x in range(2,Nx+3,2):#x = 1,3,5,7
            #cek dir
            qx_l = a/h*(w[x,y,t]-w[x-2,y,t]) 
            qx_r = a/h*(w[x+2,y,t]-w[x,y,t])
            bx_l = max(0,qx_l)
            bx_r = max(0,-qx_r)
            
            qy_d = a/h*(w[x,y,t]-w[x,y-2,t]) 
            qy_u = a/h*(w[x,y+2,t]-w[x,y,t])
            by_d = max(0,qy_d)
            by_u = max(0,-qy_u)
            
            f1[x,y,t] = (p[x+1,y-1,t]-p[x-1,y-1,t]+p[x+1,y+1,t]-p[x-1,y+1,t])/(2*h) - bx_l*(p[x-1,y-1,t]+p[x-1,y+1,t])/2 + bx_r*(p[x+1,y-1,t]+p[x+1,y+1,t])
            f2[x,y,t] = (p[x-1,y+1,t]-p[x-1,y-1,t]+p[x+1,y+1,t]-p[x+1,y-1,t])/(2*h) - by_d*(p[x-1,y-1,t]+p[x+1,y-1,t])/2 + by_u*(p[x-1,y+1,t]+p[x+1,y+1,t])
            
            p[x-1,y-1,t+1] = p[x-1,y-1,t] + dt/(2*h)*(f1[x,y,t]-f1[x-2,y,t]+f1[x,y-2,t]-f1[x-2,y-2,t])+dt/(2*h)*(f2[x,y,t]-f2[x,y-2,t]+f2[x-2,y,t]-f2[x-2,y-2,t])
        if x==Nx+3:#right side of black nodes
            x=Nx+2
            p[x+1,y-1,t+1] = p[x+1,y-1,t] + dt/(2*h)*(f1[x+2,y,t]-f1[x,y,t]+f1[x+2,y-2,t]-f1[x,y-2,t])+dt/(2*h)*(f2[x+2,y,t]-f2[x,y,t]+f2[x+2,y-2,t]-f2[x,y-2,t])
    if y==Ny+3:
        for x in range(1,Nx+4,2):
            p[x,y,t+1] = p[x,y,t] + dt/(2*h)*(f1[x+1,y+1,t]-f1[x-1,y+1,t]+f1[x+1,y-1,t]-f1[x-1,y-1,t])+dt/(2*h)*(f2[x+1,y+1,t]-f2[x+1,y-1,t]+f2[x-1,y+1,t]-f2[x-1,y-1,t])

for t in range(Nt):
    for y in range(Nx+5):
        for x in range(Nx+5):
            if p[x,y,t]<0:
                print 'neg'
        