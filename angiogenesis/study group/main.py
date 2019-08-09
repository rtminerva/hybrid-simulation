import math as m
import numpy
import os
import matplotlib.pyplot as plt 


plt.ion()

q_0 = 0
r_o = 0.1
mu = 0.3
a = 5

sv = 0

X = 1
Y = 1
dh = 0.005
Nx = int(X/dh)
Ny = int(Y/dh)

dt = 0.01


'''Initial Condition'''
r = [[0.005,100*dh],[0,100*dh]]
q = [[0,1],[1,0]]
f = numpy.zeros((Nx+1,Ny+1))
co = numpy.zeros((Nx+1,Ny+1))
for y in range(0,Ny+1,1):
    for x in range(0,Nx+1,1): 
        f[x,y] = 0.5
        co[x,y] = numpy.exp(-(1-x*dh)**2/0.45)


cell = [0,1]

t = 0
T = 5
while t <= T:
    ro = r[:]
    qo = q[:]
    fo = f[:]
    
    '''For solving fibronectin'''
    for y in range(0,Ny+1,1):
        for x in range(0,Nx+1,1):  
            summ_f = 0
            for in_i, i in enumerate(cell):
                pos_x = ro[i][0]
                pos_y = ro[i][1]
                dis = m.sqrt((x*dh-pos_x)**2+(y*dh-pos_y)**2)
                summ_f += m.exp(-dis**2/a)
                
            f[x,y] = fo[x,y] - dt * mu * fo[x,y] * summ_f
    
    '''For updating cell i position'''
    for in_i, i in enumerate(cell):
        pos_x = ro[i][0]
        pos_y = ro[i][1]
        qi_bar = m.sqrt(qo[i][0]**2+qo[i][1]**2)
        
        pos_x_in = int(pos_x / dh)
        pos_y_in = int(pos_y / dh)
        if f[pos_x_in,pos_y_in] >= 0.1:
            M = 0
        else:
            M = 10
        summ_x = 0
        summ_y = 0
        for nn_i, nn in enumerate(cell):
            if nn_i != in_i:
                pos_x_j = ro[nn][0]
                pos_y_j = ro[nn][1]
                dis_ij = m.sqrt((pos_x_j-pos_x)**2+(pos_y_j-pos_y)**2)
                g_dis = (dis_ij/r_o)**12-(dis_ij/r_o)**6
                summ_x += g_dis*(pos_x_j-pos_x)/dis_ij
                summ_y += g_dis*(pos_y_j-pos_y)/dis_ij
            
        r[i][0] = ro[i][0] + dt * M * q[i][0] / qi_bar + summ_x
        r[i][1] = ro[i][1] + dt * M * q[i][1] / qi_bar + summ_y
        
        q[i][0] = qo[i][0] + dt* ( q_0**2-qi_bar**2 ) * qo[i][0] + (co[pos_x_in+1,pos_y_in] - co[pos_x_in,pos_y_in])/2
        q[i][1] = qo[i][1] + dt* ( q_0**2-qi_bar**2 ) * qo[i][1] + (co[pos_x_in,pos_y_in+1] - co[pos_x_in,pos_y_in])/2
    
    print 'r', r
    print 'q', q
#     print 'f', f
    
    t += dt

    '''Plot'''
    script_dir = os.path.dirname(__file__)
    results_dir0 = os.path.join(script_dir, 'trial_1/')
    if not os.path.isdir(results_dir0):
        os.makedirs(results_dir0)
    
    fig11 = plt.figure(1)
    plt.title('%s%f' % ('cell movement at t=',t))
#     ax = fig11.add_subplot(111)
    x_p = []
    y_p = []
    for pos in r:
        x_p.append(pos[0])
        y_p.append(pos[1])
    plt.scatter(x_p, y_p, marker = 'o', s = 5, color ='r')
    plt.xlim((0,1))
    plt.ylim((0,1))
    sv +=1
    flag = 'sv=%s' % str(sv) 
    plt.savefig(results_dir0 + "%s.png" % flag)
    plt.close()    