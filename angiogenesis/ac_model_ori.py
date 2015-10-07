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

tau = 0.01

'''Partition'''
X = 1
Y = 1
T = 1

h = 0.1
hh = h/2

Nx = int(X/hh)
Ny = int(Y/hh)
Nt = 200

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
for x in range(1,Nx,2):
    n[x,1,0] = (math.sin((math.pi)*x*h))**2


'''Filling Node'''
#choice of time increment
t = 0
time = []
time.append(0)
k = 0
while t <= T:
    '''to determine step size of time'''
    v1=[]
    w1=[]
    
    c1 = c[:,:,k].max()
    for y in range(2,Ny+1,2):
        for x in range(2,Nx+1,2):
            v1x = (c[x,y,k]-c[x-2,y,k])/h
            v1y = (c[x,y,k]-c[x,y-2,k])/h
            v1.append(max(v1x,v1y))
            w1x = (f[x,y,k]-f[x-2,y,k])/h
            w1y = (f[x,y,k]-f[x,y-2,k])/h
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
            #left dir
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
    k += 1
print k 
for t in range(k+1):
   for y in range(Ny+1):
        for x in range(Nx+1):
           if c[x,y,t] < 0:
                print x,y,t,'neg'
print "finished"        