import random
from random import randint
import math
from samba.dcerpc.security import dom_sid

'''Branching'''
t_branch = 0.25
sp_stop = [] #to record unbranchable tips

'''Initial Sprout'''
index_tip = [73,133]
len_init_tip = len(index_tip)
print index_tip
num_sp = 0
for y in index_tip:
    num_sp += 1 
    globals()['sp%s' % num_sp] = [(1,y)] #real time position
    globals()['tip%s' % num_sp] = 'start' #last tip movement
    globals()['move%s' % num_sp] = 'start'
    globals()['tsp%s' % num_sp] = 0 #lifetime

def movement_dir():
    la = tp/(h**2)
    x_pos = xb
    y_pos = yb
    vvx = 0.5/h*(c[x_pos+1,y_pos+1,k]-c[x_pos-1,y_pos+1,k]+c[x_pos+1,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
    vvy = 0.5/h*(c[x_pos+1,y_pos+1,k]+c[x_pos-1,y_pos+1,k]-c[x_pos+1,y_pos-1,k]-c[x_pos-1,y_pos-1,k])
    
    wwx = 0.5/h*(f[x_pos+1,y_pos+1,k]-f[x_pos-1,y_pos+1,k]+f[x_pos+1,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
    wwy = 0.5/h*(f[x_pos+1,y_pos+1,k]+f[x_pos-1,y_pos+1,k]-f[x_pos+1,y_pos-1,k]-f[x_pos-1,y_pos-1,k])
    
    vvx_p = max(0,vvx)
    vvx_n = max(0,-vvx)
    vvy_p = max(0,vvy)
    vvy_n = max(0,-vvy)
    
    wwx_p = max(0,wwx)
    wwx_n = max(0,-wwx)
    wwy_p = max(0,wwy)
    wwy_n = max(0,-wwy)
    
    
    P_1 = la*d+la*h*ki/(1+al*0.5*(c[x_pos-1,y_pos+1,k]+c[x_pos-1,y_pos-1,k]))*vvx_n + la*h*ro*wwx_n
    P_2 = la*d+la*h*ki/(1+al*0.5*(c[x_pos+1,y_pos+1,k]+c[x_pos+1,y_pos-1,k]))*vvx_p + la*h*ro*wwx_p
    
    P_3 = la*d+la*h*ki/(1+al*0.5*(c[x_pos+1,y_pos+1,k]+c[x_pos-1,y_pos+1,k]))*vvy_n + la*h*ro*wwy_n
    P_4 = la*d+la*h*ki/(1+al*0.5*(c[x_pos+1,y_pos-1,k]+c[x_pos-1,y_pos-1,k]))*vvy_p + la*h*ro*wwy_p

    '''Boundary'''
    if y_pos == 1: #batas bawah
        P_4 +=P_3
        if x_pos == 1: #pojok kiri bawah
            P_2 += P_1
            P_1 = 0
            P_3 = 0
        elif x_pos == Nx-1: #pojok kanan bawah
            P_1 += P_2
            P_2 = 0
            P_3 = 0
        else: #batas bawah selain pojok
            P_3 = 0
    elif y_pos == Ny-1: #batas atas
        P_3 += P_4
        if x_pos == 1: #pojok kiri atas
            P_2 += P_1
            P_1 = 0
            P_4 = 0
        elif x_pos == Nx-1: #pojok kanan atas
            P_1 += P_2
            P_2 = 0
            P_4 = 0
        else: #batas atas selain pojok
            P_4 = 0
    else: #selain batas bawah dan atas
        if x_pos == 1: #batas kiri selain pojok
            P_2 += P_1
            P_1 = 0
        elif x_pos == Nx-1: #batas kanan selain pojok
            P_1 += P_2
            P_2 = 0
        #selain batas2, tetap pada nilai P_1 ~ P_4 awal saja
                
    
#     '''tes saja'''
#     P_1 = 0.15# P_1#*100
#     P_2 = 0.15#P_2#*100
#     P_3 = 0.15#P_3#*100
#     P_4 = 0.15#P_4#*100
#     if y_pos == 1: #batas bawah
#         if x_pos == 1: #pojok kiri bawah
#             P_1 = 0
#             P_3 = 0
#         elif x_pos == Nx-1: #pojok kanan bawah
#             P_2 = 0
#             P_3 = 0
#         else: #batas bawah selain pojok
#             P_3 = 0
#     elif y_pos == Ny-1: #batas atas
#         if x_pos == 1: #pojok kiri atas
#             P_1 = 0
#             P_4 = 0
#         elif x_pos == Nx-1: #pojok kanan atas
#             P_2 = 0
#             P_4 = 0
#         else: #batas atas selain pojok
#             P_4 = 0
#     else: #selain batas bawah dan atas
#         if x_pos == 1: #batas kiri selain pojok
#             P_1 = 0
#         elif x_pos == Nx-1: #batas kanan selain pojok
#             P_2 = 0
#         #selain batas2, tetap pada nilai P_1 ~ P_4 awal saja
#         else:
#             lop = 1
#     '''tes saja'''
    
    P_0 = 1-(P_1+P_2+P_3+P_4)
    R_0 = P_0
    R_1 = P_0+P_1
    R_2 = P_0+P_1+P_2
    R_3 = P_0+P_1+P_2+P_3
    R_4 = 1
    
    prob_range = [R_0,R_1,R_2,R_3,R_4]
    print P_0, ',',P_1,',',P_2,',',P_3,',',P_4
    return prob_range;

'''Parameter'''
d = 0.00035
ki = 0.38
al = 0.6
ro = 0#0.3
nu = 0.1
be = 0.05
ga = 0.1

ef = 0.45
ec = 0.45
#k = (5**0.5-0.1)/(5**0.5-1)
tau = 0.001


'''Partition'''
X = 1
Y = 1
T = 5

h = 0.01
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
        f[x,y,0] = 0.75* math.exp(-(x*hh)**2/ef)
        c[x,y,0] = math.exp(-(1-x*hh)**2/ec)
for y in range(1,Ny,2):
    for x in range(1,Nx,2):
        tipss = 2
        n[x,y,0] = math.exp(-(x*hh)**2/0.001)*(math.sin(tipss*math.pi*y*hh))**2

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
                        
    for y in range(1,Ny,2): #at main lattice
        for x in range(1,Nx,2): #at main lattice
            n[x,y,k+1] = n[x,y,k] - tp/h*(Fx[x+1,y+1,k]-Fx[x-1,y+1,k]+Fy[x+1,y+1,k]-Fy[x+1,y-1,k])
            
    '''***PUT BRANCHING.PY HERE***'''
     
    '''1. Anastomosis''' #not yet
    
    sp_new_stop =[]
    for noms in range(1,num_sp+1):         
        if not noms in sp_stop:
            '''1.1 Checking if looping itself'''
            if not globals()['tip%s' % noms] == 'stay':
                gg = globals()['sp%s' % noms][:]
                gg.pop()
                gg = list(set(gg))    
                if len(gg) > 0: #mencegah start masuk ke bagian ini
                    if globals()['sp%s' % noms][-1] in gg:
                        sp_new_stop.append(noms)
                        print 'looping itself for tip number', noms
                        print 'looping to position', globals()['sp%s' % noms][-1]
                #kalau < = 0, artinya baru start iterasi
            #kalau 'stay', artinya aman. do nothing. done looping itself
            '''1.2 Checking if hit another sprout'''
            if noms in sp_new_stop or num_sp == 1: #kalau sudah looping itself, gak usah cek hit others lg.
                lop = 1
            else:
                #making list of others
                other_tips = range(1,num_sp+1)
                other_tips.remove(noms)
                for i in other_tips:
                    if globals()['sp%s' % noms][-1] in globals()['sp%s' % i]:
                        sp_new_stop.append(noms)
                        print 'anastomosis for tip number ', noms, ' to tip number ', i 
                        print 'anastomosis at position', globals()['sp%s' % noms][-1]
                    #kalau gak hit, do nothing
    
    '''1.3 Checking if two tips meet at one point'''
    if len(sp_new_stop) >= 2:
        pair = [(0,0)]
        for j in sp_new_stop:
            other_tips = sp_new_stop[:]
            other_tips.remove(j)
            for i in other_tips:
                if globals()['sp%s' % j][-1] == globals()['sp%s' % i][-1]:
                    jjj = (j,i)
                    if reversed(jjj) in pair:
                        lop = 1
                    else:
                        pair.append((j,i))
        if len(pair) > 1:
            for j in range(1,len(pair)):             
                sp_new_stop.remove(pair[j][0])         
    sp_stop.extend(sp_new_stop)
    sp_stop = list(set(sp_stop))
    for i in sp_stop:
        globals()['tip%s' % i] = 'stop'

    '''2. Branching and Movement'''        
    if len(sp_stop) == num_sp:
        k = 100000 #sp_stop harus dicek di setiap movement and branching. karena sudah tidak bergerak lagi yang ada di list ini.
        print 'all looping itself or anastomosis'
    else:    
        ##branching decision and action. Also movement   
        line = range(1,11) #for Pb
        n_sp = num_sp #to save original number of tips before branching
        
        for nom in range(1,n_sp+1): #dicek setiap tip
            if nom in sp_stop: #kalo dia sudah anastomosis, gak perlu branching dan move lg.
                print 'no_moving for tip', nom
            else:
                xb = globals()['sp%s' % nom][-1][0] #get x position of last tip position
                yb = globals()['sp%s' % nom][-1][1] #get y position of last tip position
                #print 'xb,yb', xb,',',yb
                dirr = movement_dir() # get list of prob_range
                
                '''2.1 Branching Decision''' 
                if globals()['tsp%s' % nom] >= t_branch: #being able to branch by life time               
                    #probabilty of branching
                    if c[xb+1,yb+1,k+1] >= 0.3 and c[xb+1,yb+1,k+1] < 0.5:
                        prob_weight = 2 # set the number to select here.
                        list_prob = random.sample(line, prob_weight) #list of selected numbers from line
                    elif c[xb+1,yb+1,k+1] >= 0.5 and c[xb+1,yb+1,k+1] < 0.7:
                        prob_weight = 3 # set the number to select here.
                        list_prob = random.sample(line, prob_weight)   
                    elif c[xb+1,yb+1,k+1] >= 0.7 and c[xb+1,yb+1,k+1] < 0.8:
                        prob_weight = 4 # set the number to select here.
                        list_prob = random.sample(line, prob_weight)  
                    elif c[xb+1,yb+1,k+1] >= 0.8: #do branching
                        list_prob = line
                    else: #no branching or in the condition: c[xb+1,yb+1,k+1] < 0.3
                        list_prob = [20]
                else: #not branchable
                    list_prob = [20]
                #apakah branching? meaning masuk dalam probability of branching?
                tes = randint(1,10) #select integer number randomly between 1 and 10
                if tes in list_prob:#do branching
                    '''2.1.1 Branching tip's movement: 1st tip movement: nom tip'''
                    '''2.1.1.1 Checking no back and stay movement'''
                    no1_back = globals()['move%s' % nom]
                    no_back = globals()['move%s' % nom]
                    while no_back == globals()['move%s' % nom]:
                        trial = random.uniform(0,1)
                        if trial <= dirr[0]: #stay
                            no_back = globals()['move%s' % nom] #karna branching, dia harus move
                        elif trial <= dirr[1]: #left
                            no_back = 'right'
                        elif trial <= dirr[2]: #right
                            no_back = 'left'
                        elif trial <= dirr[3]: #down
                            no_back = 'up'
                        else: #>dirr[3] #up
                            no_back = 'down'
                    #movement 1st tip
                    if no_back == 'right':
                        tip_1 = 'left'
                        xpos_new = globals()['sp%s' % nom][-1][0] - 2
                        ypos_new = globals()['sp%s' % nom][-1][1]
                        globals()['sp%s' % nom].append((xpos_new,ypos_new))
                    elif no_back == 'left':
                        tip_1 = 'right'
                        xpos_new = globals()['sp%s' % nom][-1][0] + 2
                        ypos_new = globals()['sp%s' % nom][-1][1]
                        globals()['sp%s' % nom].append((xpos_new,ypos_new))
                    elif no_back == 'up':
                        tip_1 = 'down'
                        xpos_new = globals()['sp%s' % nom][-1][0]
                        ypos_new = globals()['sp%s' % nom][-1][1] - 2
                        globals()['sp%s' % nom].append((xpos_new,ypos_new))
                    else:
                        tip_1 = 'up'
                        xpos_new = globals()['sp%s' % nom][-1][0]
                        ypos_new = globals()['sp%s' % nom][-1][1] + 2
                        globals()['sp%s' % nom].append((xpos_new,ypos_new))
                    
                    '''2.1 Branhcing'''
                    num_sp += 1
                    globals()['sp%s' % num_sp] = [(xb,yb)]
                    globals()['ps%s' % num_sp] = []
                    #waktunya diriset
                    globals()['tsp%s' % num_sp] = 0
                    globals()['tsp%s' % nom] = 0
                    
                    '''2.1.2 Branching tip's movement: 2nd tip movement : num_sp tip'''
                    '''2.1.2.1 Checking no back, tip 1, stay movement'''
                    #ada no1_back
                    #ada tip_1
                    dom = tip_1
                    while no1_back == globals()['tip%s' % nom] or dom == tip_1:
                        trial = random.uniform(0,1)
                        if trial <= dirr[0]:
                            dom = tip_1
                        elif trial <= dirr[1]:
                            dom = 'left'
                            no1_back = 'right'
                        elif trial <= dirr[2]:
                            dom = 'right'
                            no1_back = 'left'
                        elif trial <= dirr[3]:
                            dom = 'down'
                            no1_back = 'up'
                        else: #>dirr[3]
                            dom = 'up'
                            no1_back = 'down'
                    #movement 2nd tip
                    if dom == 'left':
                        xpos_new = globals()['sp%s' % num_sp][-1][0] - 2
                        ypos_new = globals()['sp%s' % num_sp][-1][1]
                        globals()['sp%s' % num_sp].append((xpos_new,ypos_new))
                    elif dom == 'right':
                        xpos_new = globals()['sp%s' % num_sp][-1][0] + 2
                        ypos_new = globals()['sp%s' % num_sp][-1][1]
                        globals()['sp%s' % num_sp].append((xpos_new,ypos_new))
                    elif dom == 'down':
                        xpos_new = globals()['sp%s' % num_sp][-1][0]
                        ypos_new = globals()['sp%s' % num_sp][-1][1] - 2
                        globals()['sp%s' % num_sp].append((xpos_new,ypos_new))
                    else: #dom == 'up'
                        xpos_new = globals()['sp%s' % num_sp][-1][0]
                        ypos_new = globals()['sp%s' % num_sp][-1][1] + 2
                        globals()['sp%s' % num_sp].append((xpos_new,ypos_new))
                    
                    '''2.1.3 Renewal Some Vars'''
                    if not dom == 'stay':
                        globals()['move%s' % num_sp] = dom
                    if not tip_1 == 'stay':
                        globals()['move%s' % nom] = tip_1
                    globals()['tip%s' % num_sp] = dom
                    globals()['tip%s' % nom] = tip_1   
                    globals()['tsp%s' % num_sp] = tp
                else: #no branching
                    '''2.2 No Branching'''
                    '''Movement only'''
                    '''2.2.1 Checking no back movement'''
                    globals()['tsp%s' % nom] += tp
                    no_back = globals()['move%s' % nom]
                    while no_back == globals()['move%s' % nom]:
                        trial = random.uniform(0,1)
                        if trial <= dirr[0]: #stay
                            no_back = 'pro' #stay
                        elif trial <= dirr[1]: #left
                            no_back = 'right'
                        elif trial <= dirr[2]: #right
                            no_back = 'left'
                        elif trial <= dirr[3]: #down
                            no_back = 'up'
                        else: #>dirr[3] #up
                            no_back = 'down'
                    if no_back == 'pro':
                        tipp = 'stay'
                        globals()['sp%s' % nom].append(globals()['sp%s' % nom][-1])
                    elif no_back == 'right':
                        tipp = 'left'
                        xpos_new = globals()['sp%s' % nom][-1][0] - 2
                        ypos_new = globals()['sp%s' % nom][-1][1]
                        globals()['sp%s' % nom].append((xpos_new,ypos_new)) 
                    elif no_back == 'left':
                        tipp = 'right'
                        xpos_new = globals()['sp%s' % nom][-1][0] + 2
                        ypos_new = globals()['sp%s' % nom][-1][1]
                        globals()['sp%s' % nom].append((xpos_new,ypos_new)) 
                    elif no_back == 'up':
                        tipp = 'down'
                        xpos_new = globals()['sp%s' % nom][-1][0]
                        ypos_new = globals()['sp%s' % nom][-1][1] - 2
                        globals()['sp%s' % nom].append((xpos_new,ypos_new)) 
                    else:
                        tipp = 'up'
                        xpos_new = globals()['sp%s' % nom][-1][0]
                        ypos_new = globals()['sp%s' % nom][-1][1] + 2
                        globals()['sp%s' % nom].append((xpos_new,ypos_new))
                        
                    '''2.2.2 Renewal Some Vars'''
                    if not tipp == 'stay':
                        globals()['move%s' % nom] = tipp
                    globals()['tip%s' % nom] = tipp  
    print        
    print '*****START HERE FOR TIME STEP', t, '*****'
    print 'Total Tip:',num_sp
    print 'sp_stop list:', sp_stop
    for i in range(1,num_sp+1):
        print 'TIP', i, ':',globals()['sp%s' % i]
        print 'last movement tip', globals()['tip%s' % i]
    print '*****END*****'
    print
    
    '''***BRANCHING/PY END***'''
           
    k += 1 #renewal of iteration
print 'time end : ',t
print 'number of iteration : ',k 

# '''Checking Negative Value'''
# for t in range(k+1):
#    for y in range(Ny+1):
#         for x in range(Nx+1):
#            if n[x,y,t] < 0 or c[x,y,t] <0 or f[x,y,t] < 0:
#                 print x,y,t,'neg'
'''Mesh Division'''
l =10
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

'''Figure Sprouting'''
fig = plt.figure()
plt.xlim(hh,X-hh)
plt.ylim(hh,Y-hh)
ax = fig.add_subplot(111)
# '''tes'''
# i= 1
# globals()['xp%s' % i] =[]
# globals()['yp%s' % i] =[]
# for j in range(0,len(globals()['sp%s' % i])):
#     globals()['xp%s' % i].append(globals()['sp%s' % i][j][0]*hh)
#     globals()['yp%s' % i].append(globals()['sp%s' % i][j][1]*hh)
# globals()['p%s' % i] = ax.plot(globals()['xp%s' % i], globals()['yp%s' % i], 'b') 
# '''tes'''
# '''tes'''
# i= 2
# globals()['xp%s' % i] =[]
# globals()['yp%s' % i] =[]
# for j in range(0,len(globals()['sp%s' % i])):
#     globals()['xp%s' % i].append(globals()['sp%s' % i][j][0]*h)
#     globals()['yp%s' % i].append(globals()['sp%s' % i][j][1]*h)
# globals()['p%s' % i] = ax.plot(globals()['xp%s' % i], globals()['yp%s' % i], 'y') 
# '''tes'''



for i in range(1,num_sp+1):
    globals()['xp%s' % i] =[]
    globals()['yp%s' % i] =[]
    for j in range(0,len(globals()['sp%s' % i])):
        globals()['xp%s' % i].append(globals()['sp%s' % i][j][0]*hh)
        globals()['yp%s' % i].append(globals()['sp%s' % i][j][1]*hh)
    globals()['plo%s' % i] = ax.plot(globals()['xp%s' % i], globals()['yp%s' % i], 'b')
plt.show()   


