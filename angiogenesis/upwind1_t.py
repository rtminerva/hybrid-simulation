X=1
T=1

h=0.2
hh=h/2
tau=0.01

Nx=int(X/hh)
Nt=10
'''Initial Condition'''
import numpy
import math

print 'Nx=',Nx
print 'Node=', range(0,Nx+1)
print 'point p=', range(1,Nx,2)
print 'point w=', range(0,Nx+1,2)
h*=-1
print h
quit()

p = numpy.zeros((Nx, Nt))
w = numpy.zeros((Nx, Nt))
f = numpy.zeros((Nx, Nt))
for i in range(1,Nx,2):
#     p[i,0] = (math.sin((math.pi)*i*h))**2
    p[i,0] = 0
p[int(Nx/2),0] = 100
print p[:,0]

'''constant'''
a = -1

'''Filling The Node'''
t=0
while t<=T:
    '''to determine step size of time'''
    bmax = 0
    for x in range(0,Nx+1,2):
        q_l = a/h*(w[x+2,t]-w[x,t])
        if q_l < 0:
            q_l *= -1
        if q_l > bmax:
            bmax = q_l
    tau1 = h^2/(2+2*h*bmax)
    if tau1 < tau:
        t_o = t #t lama
        t += tau1
    else:
        t_o = t
        t += tau
    '''to solve w'''
    for x in range(0,Nx+1,2):#x = 0,2,4,..., 14
        if x==0:
            w[x,t] = w[x,t_o] + dt*p[x+1,t_o]      
        elif x==Nx:
            w[x,t] = w[x,t_o] + dt*p[x-1,t_o]
        else:
            w[x,t] = w[x,t_o] + 1/2*dt*(p[x-1,t_o]+p[x+1,t_o])
    '''to solve p'''
    