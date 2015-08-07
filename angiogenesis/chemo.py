'''Domain'''
from duplicity.path import Path
X=1
Y=1
T=100
import numpy
old_settings = numpy.seterr(all='ignore')

dx=0.01
dy=0.01
dt=1

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
for i in range(Ny+1):
    n[0,i,0] = 1
    nw.append(n[0,i,0])
#for j in range(Ny+1):
#    for i in range(Nx+1):
#        n[i,j,0] = math.exp(-(j*dy)**2/0.001)*(math.sin(6*(math.pi)*i*dx))**2
#        nw.append(n[i,j,0])
#        wx.append(j*dx)
#        wy.append(i*dy)
#print n[:,Ny,0]
#initial c
c = numpy.zeros((Nx+1,Ny+1,Nt+1))
for i in range(Ny+1):
    for j in range(Nx+1):
        wx.append(j*dx)
        wy.append(i*dy)
        c[j,i,0] = math.exp(-(X-dx*j)**2/0.45)
        #c[j,i,0] = math.exp(-((X-dx*j)**2+(Y-dy*i)**2)/0.45)
        cw.append(c[j,i,0])


al = 0.6
ki = 0.38
nu = 0.1

for it in range(Nt):
    for iy in range(Ny+1):
        ##filling node boundary
        if (iy==0):#boundary bawah
            for ix in range(Nx+1):
                c[ix,iy,it+1] = c[ix,iy,it]*(1-dt*nu*n[ix,iy,it])
                P_3 = dt*D/dx**2 - dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix,iy+1,it]-c[ix,iy,it]))
                P_4 = dt*D/dx**2 + dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix,iy+1,it]-c[ix,iy,it]))
                if (ix==0):#pojok kiri bawah
                    P_1 = dt*D/dx**2 - dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix+1,iy,it]-c[ix,iy,it]))
                    P_2 = dt*D/dx**2 + dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix+1,iy,it]-c[ix,iy,it]))
                    P_0 = 1-4*dt*D/dx**2 + dt*al*ki*c[ix,iy,it]/(4*dx**2*(1+al*c[ix,iy,it]))*((c[ix+1,iy,it]-c[ix,iy,it])**2+(c[ix,iy+1,it]-c[ix,iy,it])**2) - dt*ki*c[ix,iy,it]/dx**2*(c[ix+1,iy,it]+c[ix,iy,it]-4*c[ix,iy,it]+c[ix,iy+1,it]+c[ix,iy,it]) - dt*ro/dx**2*(f[ix+1,iy,it]+f[ix,iy,it]-4*f[ix,iy,it]+f[ix,iy+1,it]+f[ix,iy,it])
                    n[ix,iy,it+1] = P_0*n[ix,iy,it] + P_1*n[ix+1,iy,it] + P_2*n[ix,iy,it] + P_3*n[ix,iy+1,it] + P_4*n[ix,iy,it]
                elif (ix==Nx):#pojok kanan bawah
                    P_1 = dt*D/dx**2 - dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix,iy,it]-c[ix-1,iy,it])+ro*(f[ix,iy,it]-f[ix-1,iy,it]))
                    P_2 = dt*D/dx**2 + dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix,iy,it]-c[ix-1,iy,it])+ro*(f[ix,iy,it]-f[ix-1,iy,it]))
                    P_0 = 1-4*dt*D/dx**2 + dt*al*ki*c[ix,iy,it]/(4*dx**2*(1+al*c[ix,iy,it]))*((c[ix,iy,it]-c[ix-1,iy,it])**2+(c[ix,iy+1,it]-c[ix,iy,it])**2) - dt*ki*c[ix,iy,it]/dx**2*(c[ix,iy,it]+c[ix-1,iy,it]-4*c[ix,iy,it]+c[ix,iy+1,it]+c[ix,iy,it]) - dt*ro/dx**2*(f[ix,iy,it]+f[ix-1,iy,it]-4*f[ix,iy,it]+f[ix,iy+1,it]+f[ix,iy,it])
                    n[ix,iy,it+1] = P_0*n[ix,iy,it] + P_1*n[ix,iy,it] + P_2*n[ix-1,iy,it] + P_3*n[ix,iy+1,it] + P_4*n[ix,iy,it]
                else:#selain pojokan namun dibawah
                    P_1 = dt*D/dx**2 - dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix+1,iy,it]-c[ix-1,iy,it])+ro*(f[ix+1,iy,it]-f[ix-1,iy,it]))
                    P_2 = dt*D/dx**2 + dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix+1,iy,it]-c[ix-1,iy,it])+ro*(f[ix+1,iy,it]-f[ix-1,iy,it]))
                    P_0 = 1-4*dt*D/dx**2 + dt*al*ki*c[ix,iy,it]/(4*dx**2*(1+al*c[ix,iy,it]))*((c[ix+1,iy,it]-c[ix-1,iy,it])**2+(c[ix,iy+1,it]-c[ix,iy,it])**2) - dt*ki*c[ix,iy,it]/dx**2*(c[ix+1,iy,it]+c[ix-1,iy,it]-4*c[ix,iy,it]+c[ix,iy+1,it]+c[ix,iy,it]) - dt*ro/dx**2*(f[ix+1,iy,it]+f[ix-1,iy,it]-4*f[ix,iy,it]+f[ix,iy+1,it]+f[ix,iy,it])
                    n[ix,iy,it+1] = P_0*n[ix,iy,it] + P_1*n[ix+1,iy,it] + P_2*n[ix-1,iy,it] + P_3*n[ix,iy+1,it] + P_4*n[ix,iy-1,it]
        elif (iy==Ny):#boundary atas
            for ix in range(Nx+1):
                f[ix,iy,it+1] = f[ix,iy,it]*(1-dt*ga*n[ix,iy,it])+dt*be*n[ix,iy,it]
                c[ix,iy,it+1] = c[ix,iy,it]*(1-dt*nu*n[ix,iy,it])
                P_3 = dt*D/dx**2 - dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix,iy,it]-c[ix,iy-1,it])+ro*(f[ix,iy,it]-f[ix,iy-1,it]))
                P_4 = dt*D/dx**2 + dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix,iy,it]-c[ix,iy-1,it])+ro*(f[ix,iy,it]-f[ix,iy-1,it]))
                if (ix==0):#pojok kiri atas
                    P_1 = dt*D/dx**2 - dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix+1,iy,it]-c[ix,iy,it])+ro*(f[ix+1,iy,it]-f[ix,iy,it]))
                    P_2 = dt*D/dx**2 + dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix+1,iy,it]-c[ix,iy,it])+ro*(f[ix+1,iy,it]-f[ix,iy,it]))
                    P_0 = 1-4*dt*D/dx**2 + dt*al*ki*c[ix,iy,it]/(4*dx**2*(1+al*c[ix,iy,it]))*((c[ix+1,iy,it]-c[ix,iy,it])**2+(c[ix,iy,it]-c[ix,iy-1,it])**2) - dt*ki*c[ix,iy,it]/dx**2*(c[ix+1,iy,it]+c[ix,iy,it]-4*c[ix,iy,it]+c[ix,iy,it]+c[ix,iy-1,it]) - dt*ro/dx**2*(f[ix+1,iy,it]+f[ix,iy,it]-4*f[ix,iy,it]+f[ix,iy,it]+f[ix,iy-1,it])
                    n[ix,iy,it+1] = P_0*n[ix,iy,it] + P_1*n[ix+1,iy,it] + P_2*n[ix,iy,it] + P_3*n[ix,iy,it] + P_4*n[ix,iy-1,it]
                elif (ix==Nx):#pojok kanan atas
                    P_1 = dt*D/dx**2 - dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix,iy,it]-c[ix-1,iy,it])+ro*(f[ix,iy,it]-f[ix-1,iy,it]))
                    P_2 = dt*D/dx**2 + dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix,iy,it]-c[ix-1,iy,it])+ro*(f[ix,iy,it]-f[ix-1,iy,it]))
                    P_0 = 1-4*dt*D/dx**2 + dt*al*ki*c[ix,iy,it]/(4*dx**2*(1+al*c[ix,iy,it]))*((c[ix,iy,it]-c[ix-1,iy,it])**2+(c[ix,iy,it]-c[ix,iy-1,it])**2) - dt*ki*c[ix,iy,it]/dx**2*(c[ix,iy,it]+c[ix-1,iy,it]-4*c[ix,iy,it]+c[ix,iy,it]+c[ix,iy-1,it]) - dt*ro/dx**2*(f[ix,iy,it]+f[ix-1,iy,it]-4*f[ix,iy,it]+f[ix,iy,it]+f[ix,iy-1,it])
                    n[ix,iy,it+1] = P_0*n[ix,iy,it] + P_1*n[ix,iy,it] + P_2*n[ix-1,iy,it] + P_3*n[ix,iy,it] + P_4*n[ix,iy-1,it]
                else:#selain pojokan namun diatas
                    P_1 = dt*D/dx**2 - dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix+1,iy,it]-c[ix-1,iy,it])+ro*(f[ix+1,iy,it]-f[ix-1,iy,it]))
                    P_2 = dt*D/dx**2 + dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix+1,iy,it]-c[ix-1,iy,it])+ro*(f[ix+1,iy,it]-f[ix-1,iy,it]))
                    P_0 = 1-4*dt*D/dx**2 + dt*al*ki*c[ix,iy,it]/(4*dx**2*(1+al*c[ix,iy,it]))*((c[ix+1,iy,it]-c[ix-1,iy,it])**2+(c[ix,iy,it]-c[ix,iy-1,it])**2) - dt*ki*c[ix,iy,it]/dx**2*(c[ix+1,iy,it]+c[ix-1,iy,it]-4*c[ix,iy,it]+c[ix,iy,it]+c[ix,iy-1,it]) - dt*ro/dx**2*(f[ix+1,iy,it]+f[ix-1,iy,it]-4*f[ix,iy,it]+f[ix,iy,it]+f[ix,iy-1,it])
                    n[ix,iy,it+1] = P_0*n[ix,iy,it] + P_1*n[ix+1,iy,it] + P_2*n[ix-1,iy,it] + P_3*n[ix,iy,it] + P_4*n[ix,iy-1,it]
        else:#selain boundary atas bawah
            for ix in range(Nx+1):
                f[ix,iy,it+1] = f[ix,iy,it]*(1-dt*ga*n[ix,iy,it])+dt*be*n[ix,iy,it]
                c[ix,iy,it+1] = c[ix,iy,it]*(1-dt*nu*n[ix,iy,it])
                P_3 = dt*D/dx**2 - dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix,iy+1,it]-c[ix,iy-1,it])+ro*(f[ix,iy+1,it]-f[ix,iy-1,it]))
                P_4 = dt*D/dx**2 + dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix,iy+1,it]-c[ix,iy-1,it])+ro*(f[ix,iy+1,it]-f[ix,iy-1,it]))
                if (ix==0):#selain boundary atas bawah namun dipinggiran kiri
                    P_1 = dt*D/dx**2 - dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix+1,iy,it]-c[ix,iy,it])+ro*(f[ix+1,iy,it]-f[ix,iy,it]))
                    P_2 = dt*D/dx**2 + dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix+1,iy,it]-c[ix,iy,it])+ro*(f[ix+1,iy,it]-f[ix,iy,it]))
                    P_0 = 1-4*dt*D/dx**2 + dt*al*ki*c[ix,iy,it]/(4*dx**2*(1+al*c[ix,iy,it]))*((c[ix+1,iy,it]-c[ix,iy,it])**2+(c[ix,iy+1,it]-c[ix,iy-1,it])**2) - dt*ki*c[ix,iy,it]/dx**2*(c[ix+1,iy,it]+c[ix,iy,it]-4*c[ix,iy,it]+c[ix,iy+1,it]+c[ix,iy-1,it]) - dt*ro/dx**2*(f[ix+1,iy,it]+f[ix,iy,it]-4*f[ix,iy,it]+f[ix,iy+1,it]+f[ix,iy-1,it])
                    n[ix,iy,it+1] = P_0*n[ix,iy,it] + P_1*n[ix+1,iy,it] + P_2*n[ix,iy,it] + P_3*n[ix,iy+1,it] + P_4*n[ix,iy-1,it] 
                elif (ix==Nx):#selain boundary atas bawah namun dipinggiran kanan
                    P_1 = dt*D/dx**2 - dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix,iy,it]-c[ix-1,iy,it])+ro*(f[ix,iy,it]-f[ix-1,iy,it]))
                    P_2 = dt*D/dx**2 + dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix,iy,it]-c[ix-1,iy,it])+ro*(f[ix,iy,it]-f[ix-1,iy,it]))
                    P_0 = 1-4*dt*D/dx**2 + dt*al*ki*c[ix,iy,it]/(4*dx**2*(1+al*c[ix,iy,it]))*((c[ix,iy,it]-c[ix-1,iy,it])**2+(c[ix,iy+1,it]-c[ix,iy-1,it])**2) - dt*ki*c[ix,iy,it]/dx**2*(c[ix,iy,it]+c[ix-1,iy,it]-4*c[ix,iy,it]+c[ix,iy+1,it]+c[ix,iy-1,it]) - dt*ro/dx**2*(f[ix,iy,it]+f[ix-1,iy,it]-4*f[ix,iy,it]+f[ix,iy+1,it]+f[ix,iy-1,it])
                    n[ix,iy,it+1] = P_0*n[ix,iy,it] + P_1*n[ix,iy,it] + P_2*n[ix-1,iy,it] + P_3*n[ix,iy+1,it] + P_4*n[ix,iy-1,it] 
                else:#tengah2 selain boundary
                    P_1 = dt*D/dx**2 - dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix+1,iy,it]-c[ix-1,iy,it])+ro*(f[ix+1,iy,it]-f[ix-1,iy,it]))
                    P_2 = dt*D/dx**2 + dt/(4*dx**2)*(ki*c[ix,iy,it]*(c[ix+1,iy,it]-c[ix-1,iy,it])+ro*(f[ix+1,iy,it]-f[ix-1,iy,it]))
                    P_0 = 1-4*dt*D/dx**2 + dt*al*ki*c[ix,iy,it]/(4*dx**2*(1+al*c[ix,iy,it]))*((c[ix+1,iy,it]-c[ix-1,iy,it])**2+(c[ix,iy+1,it]-c[ix,iy-1,it])**2) - dt*ki*c[ix,iy,it]/dx**2*(c[ix+1,iy,it]+c[ix-1,iy,it]-4*c[ix,iy,it]+c[ix,iy+1,it]+c[ix,iy-1,it]) - dt*ro/dx**2*(f[ix+1,iy,it]+f[ix-1,iy,it]-4*f[ix,iy,it]+f[ix,iy+1,it]+f[ix,iy-1,it])
                    n[ix,iy,it+1] = P_0*n[ix,iy,it] + P_1*n[ix+1,iy,it] + P_2*n[ix-1,iy,it] + P_3*n[ix,iy+1,it] + P_4*n[ix,iy-1,it]

for u1 in range(Nt+1):
    for u2 in range(Ny+1):
        for u3 in range(Nx+1):
            if n[u3,u2,u1]<0:
                #print 'negative value'
                #print u3, u2, u1
                #quit()
                break;
