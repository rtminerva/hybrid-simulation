'''Parameter'''
d = 0.00035
ki = 0.38
al = 0.6
ro = 0.3
nu = 0.1
be = 0.05
ga = 0.1

ef = 0.45
ec = 0.45
#k = (5**0.5-0.1)/(5**0.5-1)

tau = 0.1

'''Partition'''
X = 1
Y = 1
T = 10

h = 0.05
hh = h/2

Nx = int(X/hh)
Ny = int(Y/hh)
Nt =1000

print 'Nx =',Nx
print 'Node =', range(0,Nx+1)
print 'point n,v,w=', range(1,Nx,2)
print 'point F,c,f=', range(0,Nx+1,2)


'''Define Variable'''
import numpy
import math

n = numpy.zeros((Nx+1, Ny+1, Nt+1))
c = numpy.zeros((Nx+1, Ny+1, Nt+1))
f = numpy.zeros((Nx+1, Ny+1, Nt+1))

Fx = numpy.zeros((Nx+1, Ny+1, Nt+1))
vx = numpy.zeros((Nx+1, Ny+1, Nt+1))
wx = numpy.zeros((Nx+1, Ny+1, Nt+1))

Fy = numpy.zeros((Nx+1, Ny+1, Nt+1))
vy = numpy.zeros((Nx+1, Ny+1, Nt+1))
wy = numpy.zeros((Nx+1, Ny+1, Nt+1))

'''Initial Condition'''
#p[i,0] = (math.sin((math.pi)*i*h))**2
for y in range(0,Ny+1,2):
    for x in range(0,Nx+1,2):
        f[x,y,0] = 0.75* math.exp(-(x*h)**2/ef)
        c[x,y,0] = math.exp(-(1-x*h)**2/ec)
for y in range(5,Ny-4,2):
    for x in range(1,Nx,2):
        n[x,y,0] = math.exp(-(x*h)**2/0.1)*(math.sin((math.pi)*y*h))**2
#for x in range(1,Nx,2):
#    n[x,1,0] = (math.sin((math.pi)*x*h))**2


'''Filling Node'''
#choice of time increment
t = 0
k = 0
time = []
time.append(0)
while t <= T and k < Nt:
    '''to determine step size of time'''
    v1=[]
    w1=[]
    
    c1 = c[:,:,k].max()
    for y in range(2,Ny+1,2):
        for x in range(0,Nx,2):
            v1x = 1/(2*h)*c[x+2,y,k]-c[x,y,k]+c[x+2,y-2,k]-c[x,y-2,k]
            v1y = 1/(2*h)*c[x+2,y,k]-c[x+2,y-2,k]+c[x,y,k]-c[x,y-2,k]
            v1.append(max(v1x,v1y))
            w1x = 1/(2*h)*f[x+2,y,k]-f[x,y,k]+f[x+2,y-2,k]-f[x,y-2,k]
            w1y = 1/(2*h)*f[x+2,y,k]-f[x+2,y-2,k]+f[x,y,k]-f[x,y-2,k]
            w1.append(max(w1x,w1y))
    vv1 = max(v1)
    ww1 = max(w1)
    tau1 = h**2/(4*(d+h*ki*vv1/(1+al*c1)+h*ro*ww1))
    if tau1 < tau:
        tp = tau1
    else:
        tp = tau
    t += tp
    time.append(t)
    '''solve c, f at sublattice'''
    for y in range(0,Ny+1,2):
        for x in range(0,Nx+1,2):
            if y == 0:
                if x == 0:
                    c[x,y,k+1] = c[x,y,k]*(1 - tp*nu*n[1,1,k])
                    f[x,y,k+1] = f[x,y,k]+ tp*(be-ga*f[x,y,k])*n[1,1,k]
                elif x == Nx:
                    c[x,y,k+1] = c[x,y,k]*(1 - tp*nu*n[Nx-1,1,k])
                    f[x,y,k+1] = f[x,y,k]+ tp*(be-ga*f[x,y,k])*n[Nx-1,1,k]
                else:
                    c[x,y,k+1] = c[x,y,k]*(1 - tp*nu*0.5*(n[x+1,1,k]+n[x-1,1,k]))
                    f[x,y,k+1] = f[x,y,k]+ tp*(be-ga*f[x,y,k])*0.5*(n[x+1,1,k]+n[x-1,1,k])
            elif y == Ny:
                if x == 0:
                    c[x,y,k+1] = c[x,y,k]*(1 - tp*nu*n[1,Ny-1,k])
                    f[x,y,k+1] = f[x,y,k]+ tp*(be-ga*f[x,y,k])*n[1,Ny-1,k]
                elif x == Nx:
                    c[x,y,k+1] = c[x,y,k]*(1 - tp*nu*n[Nx-1,Ny-1,k])
                    f[x,y,k+1] = f[x,y,k]+ tp*(be-ga*f[x,y,k])*n[Nx-1,Ny-1,k]
                else:
                    c[x,y,k+1] = c[x,y,k]*(1 - tp*nu*0.5*(n[x+1,Ny-1,k]+n[x-1,Ny-1,k]))
                    f[x,y,k+1] = f[x,y,k]+ tp*(be-ga*f[x,y,k])*0.5*(n[x+1,Ny-1,k]+n[x-1,Ny-1,k])
            else:
                if x == 0:
                    c[x,y,k+1] = c[x,y,k]*(1 - tp*nu*0.5*(n[x+1,y+1,k]+n[x+1,y-1,k]))
                    f[x,y,k+1] = f[x,y,k]+ tp*(be-ga*f[x,y,k])*0.5*(n[x+1,y+1,k]+n[x+1,y-1,k])
                elif x == Nx:
                    c[x,y,k+1] = c[x,y,k]*(1 - tp*nu*0.5*(n[x-1,y+1,k]+n[x-1,y-1,k]))
                    f[x,y,k+1] = f[x,y,k]+ tp*(be-ga*f[x,y,k])*0.5*(n[x-1,y+1,k]+n[x-1,y-1,k])
                else:
                    c[x,y,k+1] = c[x,y,k]*(1 - tp*nu*0.25*(n[x+1,y+1,k]+n[x-1,y+1,k]+n[x+1,y-1,k]+n[x-1,y-1,k]))
                    f[x,y,k+1] = f[x,y,k]+ tp*(be-ga*f[x,y,k])*0.25*(n[x+1,y+1,k]+n[x-1,y+1,k]+n[x+1,y-1,k]+n[x-1,y-1,k])
    '''solve for n at main lattice'''
    Fx[0,:,k] = 0
    Fx[Nx,:,k] = 0
    Fx[:,0,k] = 0
    Fx[:,Ny,k] = 0
    
    Fy[0,:,k] = 0
    Fy[Nx,:,k] = 0
    Fy[:,0,k] = 0
    Fy[:,Ny,k] = 0
    for y in range(2,Ny,2): #at sub lattice
        for x in range(2,Nx,2): #at sub lattice
            '''for x part'''
            #left dir
            vx[x-1,y-1,k] = 0.5/h*(c[x,y,k]-c[x-2,y,k]+c[x,y-2,k]-c[x-2,y-2,k])
            wx[x-1,y-1,k] = 0.5/h*(f[x,y,k]-f[x-2,y,k]+f[x,y-2,k]-f[x-2,y-2,k])
            vxl = max(0,vx[x-1,y-1,k])
            wxl = max(0,wx[x-1,y-1,k])
            
            #right dir
            vx[x+1,y-1,k] = 0.5/h*(c[x+2,y,k]-c[x,y,k]+c[x+2,y-2,k]-c[x,y-2,k])
            wx[x+1,y-1,k] = 0.5/h*(f[x+2,y,k]-f[x,y,k]+f[x+2,y-2,k]-f[x,y-2,k])
            vxr = max(0,-vx[x+1,y-1,k])
            wxr = max(0,-wx[x+1,y-1,k])
            
            '''for y part'''
            #down dir
            vy[x-1,y-1,k] = 0.5/h*(c[x,y,k]+c[x-2,y,k]-c[x,y-2,k]-c[x-2,y-2,k])
            wy[x-1,y-1,k] = 0.5/h*(f[x,y,k]+f[x-2,y,k]-f[x,y-2,k]-f[x-2,y-2,k])
            vyl = max(0,vy[x-1,y-1,k])
            wyl = max(0,wy[x-1,y-1,k])
            
            #up dir
            vy[x-1,y+1,k] = 0.5/h*(c[x,y+2,k]-c[x,y,k]+c[x-2,y+2,k]-c[x-2,y,k])
            wy[x-1,y+1,k] = 0.5/h*(f[x,y+2,k]-f[x,y,k]+f[x-2,y+2,k]-f[x-2,y,k])
            vyr = max(0,-vy[x-1,y+1,k])
            wyr = max(0,-wy[x-1,y+1,k])
            
            Fx[x,y,k] = -d*0.5*(n[x+1,y+1,k]-n[x-1,y+1,k]+n[x+1,y-1,k]-n[x-1,y-1,k]) + ki/(1+al*c[x,y,k])*(n[x-1,y-1,k]*vxl-n[x+1,y-1,k]*vxr) + ro*(n[x-1,y-1,k]*wxl-n[x+1,y-1,k]*wxr)
            Fy[x,y,k] = -d*0.5*(n[x+1,y+1,k]+n[x-1,y+1,k]-n[x+1,y-1,k]-n[x-1,y-1,k]) + ki/(1+al*c[x,y,k])*(n[x-1,y-1,k]*vyl-n[x+1,y-1,k]*vyr) + ro*(n[x-1,y-1,k]*wyl-n[x+1,y-1,k]*wyr)
            
    for y in range(1,Ny,2): #at main lattice
        for x in range(1,Nx,2): #at main lattice
            n[x,y,k+1] = n[x,y,k] - tp/h*(Fx[x+1,y+1,k]-Fx[x-1,y+1,k]+Fy[x+1,y+1,k]-Fy[x+1,y-1,k])
            #tp*0.5/h*(Fx[x+1,y+1,k]-Fx[x-1,y+1,k]+Fx[x+1,y-1,k]-Fx[x-1,y-1,k] + Fy[x+1,y+1,k]+Fx[x-1,y+1,k]-Fx[x+1,y-1,k]-Fx[x-1,y-1,k])
    k += 1
print 'time end : ',t
print 'number of iteration : ',k 
for t in range(k+1):
   for y in range(Ny+1):
        for x in range(Nx+1):
           if n[x,y,t] < 0:
                print x,y,t,'neg'

'''Plot Result'''
l = 500
time_plot = time[l]
x_main_axis = numpy.arange(hh, X, h)
y_main_axis = numpy.arange(hh, Y, h)
x_main_axis, y_main_axis = numpy.meshgrid(x_main_axis, y_main_axis)

x_sub_axis = numpy.arange(0, X+hh, h)
y_sub_axis = numpy.arange(hh, Y+hh, h)
x_sub_axis, y_sub_axis = numpy.meshgrid(x_sub_axis, y_sub_axis)

c_sol = numpy.zeros((Nx/2+1, Ny/2+1))
f_sol = numpy.zeros((Nx/2+1, Ny/2+1))
n_sol = numpy.zeros((Nx/2, Ny/2))

for j, y in enumerate(range(0,Ny+1,2)):
    for i, x in enumerate(range(0,Nx+1,2)):
        c_sol[i,j] = c[x,y,l]
        f_sol[i,j] = f[x,y,l]       
        
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
ax.set_zlim(-0.1, 1.01)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()


        

