X=1
T=1

h=0.2
hh=h/2
tau=0.1

Nx=int(X/hh)
Nt=100
'''Initial Condition'''
import numpy
import math

print 'Nx =',Nx
print 'Node =', range(0,Nx+1)
print 'point p=', range(1,Nx,2)
print 'point w=', range(0,Nx+1,2)
# h*=-1
# print h

p = numpy.zeros((Nx+1, Nt))
w = numpy.zeros((Nx+1, Nt))
f = numpy.zeros((Nx+1, Nt))
qx = []
for x in range(1, Nx/2+1):
    qx.append(0)
for i in range(1,Nx,2):
#     p[i,0] = (math.sin((math.pi)*i*h))**2
    p[i,0] = 0
p[int(Nx/2),0] = 100

qx[2] = p[int(Nx/2),0]

'''constant'''
a = -1

'''Filling The Node'''
t=0
it = 1
ddt =[]
ddt.append(0)
wt=[]
for x in range(1, Nx/2+1):
    wt.append(0)

wx = []
wx.append(hh)
for x in range(1, Nx/2):
    wx.append(wx[x-1]+h)

while t<=T and it <= Nt:
    it = it+1
    '''to determine step size of time'''
    bmax = 0
    for x in range(0,Nx,2):
        q_l = a/h*(w[x+2,t]-w[x,t])
        if abs(q_l) >bmax:
            bmax = q_l
    tau1 = h**2/(2+2*h*bmax)
    if tau1 < tau:
        t_o = t #t lama
        t += tau1
    else:
        t_o = t
        t += tau
    dt = t-t_o
    ddt.append(dt)
    wt.append(t)
    for x in range(1, Nx/2):
        wt.append(t)
    wx.append(hh)
    for x in range(1, Nx/2):
        wx.append(wx[x-1]+h)
    '''to solve w'''
    for x in range(0,Nx+1,2):#x = 0,2,4,..., 14
        if x==0:
            w[x,t] = w[x,t_o] + dt*p[x+1,t_o]      
        elif x==Nx:
            w[x,t] = w[x,t_o] + dt*p[x-1,t_o]
        else:
            w[x,t] = w[x,t_o] + 1/2*dt*(p[x-1,t_o]+p[x+1,t_o])
    '''to solve p'''
    f[0,t] = 0
    f[Nx,t] = 0
    for x in range(1,Nx-1,2):#x = 1,3,5,7,9
         #cek dir
         k_l = a/h*(w[x+1,t_o]-w[x-1,t_o])
         k_r = a/h*(w[x+3,t_o]-w[x+1,t_o])
         b_l = max(0,k_l)
         b_r = max(0,-k_r)
         f[x,t_o] = (p[x+2,t_o]-p[x,t_o])/h - b_l*p[x,t_o] + b_r*p[x+2,t_o]
         p[x,t] = p[x,t_o] + dt/h*(f[x,t_o]-f[x-1,t_o])
         qx.append(p[x,t])
    #calculate at right boundary
    k_l = a/h*(w[9+1,t_o]-w[9-1,t_o])
    k_r = a/h*(w[9+1,t_o]-w[9+1,t_o]) #point 12 = 10
    b_l = max(0,k_l)
    b_r = max(0,-k_r)
    f[9,t_o] = (p[9,t_o]-p[9,t_o])/h - b_l*p[9,t_o] + b_r*p[9,t_o] #point 11 = 9
    p[9,t] = p[9,t_o] + dt/h*(f[9,t_o]-f[9-1,t_o])
    qx.append(p[9,t])
    print 'p(:,',t,') = ',p[:,t]
print 't=',t
for t in range(Nt):
    for x in range(Nx):
        if p[x,t]<0:
            print 'neg'
#         else:
#             print 'all'

# sol = numpy.zeros((Nx/2, Nt))
# for t in range(Nt):
#     for i, j in enumerate(range(1,Nx,2)):
#         sol[i,t] = p[j,t]
        
'''Draw solution'''
print 'length of wx =', len(wx)
print 'length of wt =', len(wt)
print 'length of qx =', len(qx)
print 'ddt =', ddt
print 'length of ddt =', len(ddt)


# import matplotlib.pyplot as plt
# from matplotlib import cm
# import numpy as np
# from matplotlib.mlab import griddata
# xx = np.arange(hh, X, h) #list
# tt = np.asarray(ddt)#np.arange(0, (T+dt), dt) #list
# xx, tt = np.meshgrid(xx, tt)
# ZZ = griddata(wx, wt, qx, xx, tt)
# from mpl_toolkits.mplot3d import Axes3D
# fig1 = plt.figure()
# ax = plt.axes(projection='3d')
# ax.plot_surface(xx, tt, ZZ, rstride=1, cstride=1, cmap=cm.coolwarm)
# plt.show()  

#linewidth=0, antialiased=False