import random
from random import randint
import math

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



a = n[1,:,0][:]
m = max(a)
idr = [i for i, j in enumerate(a) if j == m]
print idr

