import random
from random import randint

'''Definition of Functions'''
def nonbranch_movement_dir(x_pos,y_pos):
    la = tp/(h**2)
    
    '''for x part'''
    vx[x_pos,y_pos,k] = 0.5/h*(c[x_pos+1,y_pos+1,k]-c[x_pos-1,y_pos+1,k]+c[x_pos+1,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
    wx[x_pos,y_pos,k] = 0.5/h*(f[x_pos+1,y_pos+1,k]-f[x_pos-1,y_pos+1,k]+f[x_pos+1,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
    #right dir
    vxl = max(0,vx[x_pos,y_pos,k])
    wxl = max(0,wx[x_pos,y_pos,k])
    #left dir
    vxr = max(0,-vx[x_pos,y_pos,k])
    wxr = max(0,-wx[x_pos,y_pos,k])
    
    '''for y part'''
    vy[x_pos,y_pos,k] = 0.5/h*(c[x_pos+1,y_pos+1,k]+c[x_pos-1,y_pos+1,k]-c[x_pos+1,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
    wy[x_pos,y_pos,k] = 0.5/h*(f[x_pos+1,y_pos+1,k]+f[x_pos-1,y_pos+1,k]-f[x_pos+1,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
    #up dir
    vyl = max(0,vy[x_pos,y_pos,k])
    wyl = max(0,wy[x_pos,y_pos,k]) 
    #down dir
    vyr = max(0,-vy[x_pos,y_pos,k])
    wyr = max(0,-wy[x_pos,y_pos,k])
    
    ##start executing P_0 ~ P_4
    P_1 = la*d+la*h*ki/(1+al*c[x_pos-1,y_pos+1,k])*vxr + la*h*ro*wxr
    P_2 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos+1,k])*vxl + la*h*ro*wxl
    P_3 = la*d+la*h*ki/(1+al*c[x_pos+1,y_pos-1,k])*vyr + la*h*ro*wyr
    P_4 = la*d+la*h*ki/(1+al*c[x_pos-1,y_pos-1,k])*vyl + la*h*ro*wyl
    if y_pos == 1: #batas bawah
        if x_pos == 1: #pojok kiri bawah
            P_1 = 0
            P_3 = 0
        elif x_pos == Nx-1: #pojok kanan bawah
            P_2 = 0
            P_3 = 0
        else: #batas bawah selain pojok
            P_3 = 0
    elif y_pos == Ny-1: #batas atas
        if x_pos == 1: #pojok kiri atas
            P_1 = 0
            P_4 = 0
        elif x_pos == Nx-1: #pojok kanan atas
            P_2 = 0
            P_4 = 0
        else: #batas atas selain pojok
            P_4 = 0
    else: #selain batas bawah dan atas
        if x_pos == 1: #batas kiri selain pojok
            P_1 = 0
        elif x_pos == Nx-1: #batas kanan selain pojok
            P_2 = 0
        #selain batas2, tetap pada nilai P_1 ~ P_4 awal saja
    P_0 = 1 -(P_1+P_2+P_3+P_4)                
    falls = random.uniform(0,1)
    if falls <= P_0:
        dirr = ('stay')
    elif falls <= (P_0+P_1):
        dirr = ('left')
    elif falls <= (P_0+P_1+P_2):
        dirr = ('right')
    elif falls <= (P_0+P_1+P_2+P_3):
        dirr = ('down')
    elif falls <= 1:
        diff = ('up')    
    return dirr;


'''Parameter'''
d = 0.00035
ki = 0.38
al = 0.6
ro = 0#0.3
nu = 0.1
be = 0#0.05
ga = 0#0.1

ef = 0.45
ec = 0.45
#k = (5**0.5-0.1)/(5**0.5-1)

tau = 0.001

'''Partition'''
X = 1
Y = 1
T = 2

h = 0.05
hh = h/2

Nx = int(X/hh)
Ny = int(Y/hh)
Nt = 10

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

'''Branching'''
t_branch = 0.25

'''Initial Condition'''
#p[i,0] = (math.sin((math.pi)*i*h))**2
for y in range(0,Ny+1,2):
    for x in range(0,Nx+1,2):
        f[x,y,0] = 0.75* math.exp(-(x*hh)**2/ef)
        c[x,y,0] = math.exp(-(1-x*hh)**2/ec)
for y in range(1,Ny,2):
    for x in range(1,Nx,2):
        n[x,y,0] = math.exp(-(x*hh)**2/0.001)*(math.sin(2*math.pi*y*hh))**2
#         n[x,y,0] = math.exp(-(x*hh)**2/0.1)*(math.sin((math.pi)*y*hh))**2
#for x in range(1,Nx,2):
#    n[x,1,0] = (math.sin((math.pi)*x*h))**2
'''Initial Sprout'''
##find max tip
m = n[:,:,0].max()
index_tip = []
print m
for y in range(1,Ny,2):
    for x in range(1,Nx,2):
        if n[x,y,0] == m:
            print "index max y position at", y
            index_tip.append(y)
##initial tip
print index_tip
num_sp = 0
for y in index_tip:
    num_sp += 1
    globals()['sp%s' % num_sp] = [(1,y)]
    globals()['tsp%s' % num_sp] = 0
#for nom in range(1,num_sp+1):
#    print globals()['sp%s' % nom]
#    print globals()['tsp%s' % nom]
#print globals()['sp%s' % nom][-1][1]


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
    n1 = n[:,:,k].max()
    for y in range(2,Ny+1,2):
        for x in range(0,Nx,2):
            v1x = 1/(2*h)*(c[x+2,y,k]-c[x,y,k]+c[x+2,y-2,k]-c[x,y-2,k])
            v1y = 1/(2*h)*(c[x+2,y,k]-c[x+2,y-2,k]+c[x,y,k]-c[x,y-2,k])
            v1.append(max(v1x,v1y))
            w1x = 1/(2*h)*(f[x+2,y,k]-f[x,y,k]+f[x+2,y-2,k]-f[x,y-2,k])
            w1y = 1/(2*h)*(f[x+2,y,k]-f[x+2,y-2,k]+f[x,y,k]-f[x,y-2,k])
            w1.append(max(w1x,w1y))
    vv1 = max(v1)
    ww1 = max(w1)
    tau1 = h**2/(4*(d+h*ki*vv1/(1+al*c1)+h*ro*ww1))
    tau2 = 1/(nu*n1)
    tau1 = min(tau1,tau2)
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
            
            Fx[x,y,k] = -d*(n[x+1,y-1,k]-n[x-1,y-1,k]) + ki/(1+al*c[x,y,k])*(n[x-1,y-1,k]*vxl-n[x+1,y-1,k]*vxr) + ro*(n[x-1,y-1,k]*wxl-n[x+1,y-1,k]*wxr)
            Fy[x,y,k] = -d*(n[x-1,y+1,k]-n[x-1,y-1,k]) + ki/(1+al*c[x,y,k])*(n[x-1,y-1,k]*vyl-n[x+1,y-1,k]*vyr) + ro*(n[x-1,y-1,k]*wyl-n[x+1,y-1,k]*wyr)
            
#             Fx[x,y,k] = -d*0.5*(n[x+1,y+1,k]-n[x-1,y+1,k]+n[x+1,y-1,k]-n[x-1,y-1,k]) + ki/(1+al*c[x,y,k])*(n[x-1,y-1,k]*vxl-n[x+1,y-1,k]*vxr) + ro*(n[x-1,y-1,k]*wxl-n[x+1,y-1,k]*wxr)
#             Fy[x,y,k] = -d*0.5*(n[x+1,y+1,k]+n[x-1,y+1,k]-n[x+1,y-1,k]-n[x-1,y-1,k]) + ki/(1+al*c[x,y,k])*(n[x-1,y-1,k]*vyl-n[x+1,y-1,k]*vyr) + ro*(n[x-1,y-1,k]*wyl-n[x+1,y-1,k]*wyr)
            
    for y in range(1,Ny,2): #at main lattice
        for x in range(1,Nx,2): #at main lattice
            n[x,y,k+1] = n[x,y,k] - tp/h*(Fx[x+1,y+1,k]-Fx[x-1,y+1,k]+Fy[x+1,y+1,k]-Fy[x+1,y-1,k])
            #tp*0.5/h*(Fx[x+1,y+1,k]-Fx[x-1,y+1,k]+Fx[x+1,y-1,k]-Fx[x-1,y-1,k] + Fy[x+1,y+1,k]+Fx[x-1,y+1,k]-Fx[x+1,y-1,k]-Fx[x-1,y-1,k])
    
    '''Discrete Problem'''
    ##anastomosis
    sp_stop = [] #to record unbranchable tips
    for noms in range(1,num_sp+1): #to compare same tips
        for nums in range(noms+1, num_sp+1):
            if globals()['sp%s' % noms][-1] == globals()['sp%s' % nums][-1]: #comparison
                sp_stop.append(noms)
    #sp_stop harus dicek di setiap movement and branching. karena sudah tidak bergerak lagi yang ada di list ini.
    
    ##branching decision and action. Also movement   
    line = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    n_sp = num_sp #to save original number of tips before branching
    for nom in range(1,n_sp+1): #dicek setiap tip
        if nom in sp_stop: #kalo dia sudah anastomosis, gak perlu branching lg
            lop = 1
        else:
            xb = globals()['sp%s' % nom][-1][0] #get x position of last tip position
            yb = globals()['sp%s' % nom][-1][1] #get y position of last tip position
            if globals()['tsp%s' % nom] >= t_branch: #being able to branch by life time
                #probabilty of branching
                rec_tip = [] #to record pasangan tip yg melakukan brancing
                if c[xb+1,yb+1,k+1] >= 0.3 and c[xb+1,yb+1,k+1] < 0.5:
                    prob_weight = 2 # set the number to select here.
                    list_prob = random.sample(line, prob_weight)
                    tes = randint(1,10)
                    if tes in list_prob:#do branching
                        num_sp += 1
                        globals()['sp%s' % num_sp] = globals()['sp%s' % nom][-1]
                        globals()['tsp%s' % num_sp] = 0
                        globals()['tsp%s' % nom] = 0
                        rec_tip.append((nom,num_sp))
                        #movement
                        
                        
                        
                elif c[xb+1,yb+1,k+1] >= 0.5 and c[xb+1,yb+1,k+1] < 0.7:
                    prob_weight = 3 # set the number to select here.
                    list_prob = random.sample(line, prob_weight)
                    tes = randint(1,10)
                    if tes in list_prob:#do branching
                        num_sp += 1
                        globals()['sp%s' % num_sp] = globals()['sp%s' % nom][-1]
                        globals()['tsp%s' % num_sp] = 0
                        globals()['tsp%s' % nom] = 0
                        rec_tip.append((nom,num_sp))
                        
                elif c[xb+1,yb+1,k+1] >= 0.7 and c[xb+1,yb+1,k+1] < 0.8:
                    prob_weight = 4 # set the number to select here.
                    list_prob = random.sample(line, prob_weight)
                    tes = randint(1,10)
                    if tes in list_prob:#do branching
                        num_sp += 1
                        globals()['sp%s' % num_sp] = globals()['sp%s' % nom][-1]
                        globals()['tsp%s' % num_sp] = 0
                        globals()['tsp%s' % nom] = 0
                        rec_tip.append((nom,num_sp))
                        
                elif c[xb+1,yb+1,k+1] >= 0.8: #do branching
                    num_sp += 1
                    globals()['sp%s' % num_sp] = globals()['sp%s' % nom][-1]
                    globals()['tsp%s' % num_sp] = 0
                    globals()['tsp%s' % nom] = 0
                    rec_tip.append((nom,num_sp)) 
            #else: no branching or in the condition: c[xb+1,yb+1,k+1] < 0.3 orsp nya < t_branch
            
            dirr = nonbranch_movement_dir(xb,yb)
                
                
    
    
    
    
    
    k += 1
print 'time end : ',t
print 'number of iteration : ',k 
for t in range(k+1):
   for y in range(Ny+1):
        for x in range(Nx+1):
           if n[x,y,t] < 0:
                print x,y,t,'neg'

'''Plot Result'''
l =2000
print 'at time', time[l]
time_plot = time[l]
x_main_axis = numpy.arange(hh, X, h)
y_main_axis = numpy.arange(hh, Y, h)
x_main_axis, y_main_axis = numpy.meshgrid(x_main_axis, y_main_axis)

x_sub_axis = numpy.arange(0, X+hh, h)
y_sub_axis = numpy.arange(0, Y+hh, h)
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

# surf = ax.plot_surface(x_sub_axis, y_sub_axis, c_sol, rstride=1, cstride=1, cmap=cm.coolwarm,
#         linewidth=0, antialiased=False)

ax.set_zlim(-0.1, 1.01)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()


        

