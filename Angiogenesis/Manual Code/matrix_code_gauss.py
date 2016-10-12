def vx_code(h = 0.01, cc = 0, x_p = 0, y_p = 0): #at main lattice
    r = 0.5/h*(cc[x_p+1,y_p+1]-cc[x_p-1,y_p+1]+cc[x_p+1,y_p-1]-cc[x_p-1,y_p-1])
    return r
    
def vy_code(h = 0.01, cc = 0, x_p = 0, y_p = 0): #at main lattice
    r = 0.5/h*(cc[x_p+1,y_p+1]+cc[x_p-1,y_p+1]-cc[x_p+1,y_p-1]-cc[x_p-1,y_p-1])
    return r
    
def wx_code(h = 0.01, ff = 0, x_p = 0, y_p = 0): #at main lattice
    r = 0.5/h*(ff[x_p+1,y_p+1]-ff[x_p-1,y_p+1]+ff[x_p+1,y_p-1]-ff[x_p-1,y_p-1])
    return r

def wy_code(h = 0.01, ff = 0, x_p = 0, y_p = 0): #at main lattice
    r = 0.5/h*(ff[x_p+1,y_p+1]+ff[x_p-1,y_p+1]-ff[x_p+1,y_p-1]-ff[x_p-1,y_p-1])
    return r

def P1_code(h = 0.01,d = 0.00035, ki = 0.38, al = 0.6, ro = 0, c1 = 0, x = 0, y = 0, f1 = 0):
    r = d + h*ki/(1+al*c1[x-1,y+1])*max(-vx_code(x_p = x, y_p = y, cc = c1), 0) + h*ro*max(-wx_code(x_p = x, y_p = y, ff = f1), 0)
    return r

def P2_code(h = 0.01,d = 0.00035, ki = 0.38, al = 0.6, ro = 0, c1 = 0, x = 0, y = 0, f1 = 0):
    r = d + h*ki/(1+al*c1[x+1,y+1])*max(vx_code(x_p = x, y_p = y, cc = c1), 0) + h*ro*max(wx_code(x_p = x, y_p = y, ff = f1), 0)
    return r

def P3_code(h = 0.01,d = 0.00035, ki = 0.38, al = 0.6, ro = 0, c1 = 0, x = 0, y = 0, f1 = 0):
    r = d + h*ki/(1+al*c1[x+1,y-1])*max(-vy_code(x_p = x, y_p = y, cc = c1), 0) + h*ro*max(-wy_code(x_p = x, y_p = y, ff = f1), 0)
    return r

def P4_code(h = 0.01,d = 0.00035, ki = 0.38, al = 0.6, ro = 0, c1 = 0, x = 0, y = 0, f1 = 0): #at main lattice
    r = d + h*ki/(1+al*c1[x+1,y+1])*max(vy_code(x_p = x, y_p = y, cc = c1), 0) + h*ro*max(wy_code(x_p = x, y_p = y, ff = f1), 0)
    return r


def vector_A(theta = 0.5, time_step = 0.001, h = 0.01, X = 1, Y = 1, ccc = 0, fff = 0, left = False):
    lam = time_step/h**2
    hh = h/2
    Nx = int(X/hh)
    Ny = int(Y/hh)
    import numpy
    A = numpy.zeros((Nx/2)**2-1)
    if left == True: # I + matrix
        '''Bottom side'''
        j = 1
        for i, x1 in enumerate(range(1,Nx-1,2)):
            A[i] = (-P2_code(x = x1, y = j, c1 = ccc, f1 = fff))*theta*lam
        '''Inside'''
        for j, y1 in enumerate(range(3,Ny-1,2)):
            for i, x1 in enumerate(range(1,Nx-1,2)):
                A[(i+Nx/2)+j*Nx/2] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff))*theta*lam
        '''Up side'''
        j = Ny-1
        for i, x1 in enumerate(range(1,Nx-1,2)):
            A[i+(Nx/2)**2-Nx/2] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff))*theta*lam
    else: # I - matrix
        '''Bottom side'''
        j = 1
        for i, x1 in enumerate(range(1,Nx-1,2)):
            A[i] = (-P2_code(x = x1, y = j, c1 = ccc, f1 = fff))*theta*lam*(-1)
        '''Inside'''
        for j, y1 in enumerate(range(3,Ny-1,2)):
            for i, x1 in enumerate(range(1,Nx-1,2)):
                A[(i+Nx/2)+j*Nx/2] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff))*theta*lam*(-1)
        '''Up side'''
        j = Ny-1
        for i, x1 in enumerate(range(1,Nx-1,2)):
            A[i+(Nx/2)**2-Nx/2] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff))*theta*lam*(-1)
    return A


def vector_B(theta = 0.5, time_step = 0.001, h = 0.01, X = 1, Y = 1, ccc = 0, fff = 0, left = False):
    lam = time_step/h**2
    hh = h/2
    Nx = int(X/hh)
    Ny = int(Y/hh)
    import numpy
    B = numpy.zeros((Nx/2)**2)
    if left == True: # I + matrix
        '''Bottom side'''
        j = 1
        for i, x1 in enumerate(range(1,Nx,2)):
            B[i] = 1 + (P1_code(x = x1, y = j, c1 = ccc, f1 = fff)+P2_code(x = x1, y = j, c1 = ccc, f1 = fff)+P3_code(x = x1, y = j, c1 = ccc, f1 = fff))*theta*lam
        '''Inside'''
        for j, y1 in enumerate(range(3,Ny-1,2)):
            for i, x1 in enumerate(range(1,Nx,2)):
                B[(i+Nx/2)+j*Nx/2] = 1 + (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff) + P2_code(x = x1, y = y1, c1 = ccc, f1 = fff) + P3_code(x = x1, y = y1, c1 = ccc, f1 = fff) + P4_code(x = x1, y = y1, c1 = ccc, f1 = fff))*theta*lam
        '''Up side'''
        j = Ny-1
        for i, x1 in enumerate(range(1,Nx,2)):
            B[i+(Nx/2)**2-Nx/2] = 1 + (P1_code(x = x1, y = j, c1 = ccc, f1 = fff)+P2_code(x = x1, y = j, c1 = ccc, f1 = fff)+P4_code(x = x1, y = j, c1 = ccc, f1 = fff))*theta*lam
    else: # I - matrix
        '''Bottom side'''
        j = 1
        for i, x1 in enumerate(range(1,Nx,2)):
            B[i] = 1 - (P1_code(x = x1, y = j, c1 = ccc, f1 = fff)+P2_code(x = x1, y = j, c1 = ccc, f1 = fff)+P3_code(x = x1, y = j, c1 = ccc, f1 = fff))*theta*lam
        '''Inside'''
        for j, y1 in enumerate(range(3,Ny-1,2)):
            for i, x1 in enumerate(range(1,Nx,2)):
                B[(i+Nx/2)+j*Nx/2] = 1 - (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff) + P2_code(x = x1, y = y1, c1 = ccc, f1 = fff) + P3_code(x = x1, y = y1, c1 = ccc, f1 = fff) + P4_code(x = x1, y = y1, c1 = ccc, f1 = fff))*theta*lam
        '''Up side'''
        j = Ny-1
        for i, x1 in enumerate(range(1,Nx,2)):
            B[i+(Nx/2)**2-Nx/2] = 1 - (P1_code(x = x1, y = j, c1 = ccc, f1 = fff)+P2_code(x = x1, y = j, c1 = ccc, f1 = fff)+P4_code(x = x1, y = j, c1 = ccc, f1 = fff))*theta*lam
    return B

    
def vector_C(theta = 0.5, time_step = 0.001, h = 0.01, X = 1, Y = 1, ccc = 0, fff = 0, left = False):
    lam = time_step/h**2
    hh = h/2
    Nx = int(X/hh)
    Ny = int(Y/hh)
    import numpy
    C = numpy.zeros((Nx/2)**2-1)
    if left == True: # I + matrix
        '''Bottom side'''
        j = 1
        for i, x1 in enumerate(range(3,Nx,2)):
            C[i] = (-P1_code(x = x1, y = j, c1 = ccc, f1 = fff))*theta*lam
        '''Inside'''
        for j, y1 in enumerate(range(3,Ny-1,2)):
            for i, x1 in enumerate(range(3,Nx,2)):
                C[(i+Nx/2)+j*Nx/2] = (-P1_code(x = x1, y = y1, c1 = ccc, f1 = fff))*theta*lam
        '''Up side'''
        j = Ny-1
        for i, x1 in enumerate(range(3,Nx,2)):
            C[i+(Nx/2)**2-Nx/2] = (-P1_code(x = x1, y = y1, c1 = ccc, f1 = fff))*theta*lam
    else: # I - matrix
        '''Bottom side'''
        j = 1
        for i, x1 in enumerate(range(3,Nx,2)):
            C[i] = (-P1_code(x = x1, y = j, c1 = ccc, f1 = fff))*theta*lam*(-1)
        '''Inside'''
        for j, y1 in enumerate(range(3,Ny-1,2)):
            for i, x1 in enumerate(range(3,Nx,2)):
                C[(i+Nx/2)+j*Nx/2] = (-P1_code(x = x1, y = y1, c1 = ccc, f1 = fff))*theta*lam*(-1)
        '''Up side'''
        j = Ny-1
        for i, x1 in enumerate(range(3,Nx,2)):
            C[i+(Nx/2)**2-Nx/2] = (-P1_code(x = x1, y = y1, c1 = ccc, f1 = fff))*theta*lam*(-1)
    return C


def vector_D(theta = 0.5, time_step = 0.001, h = 0.01, X = 1, Y = 1, ccc = 0, fff = 0, left = False):
    lam = time_step/h**2
    hh = h/2
    Nx = int(X/hh)
    Ny = int(Y/hh)
    import numpy
    D = numpy.zeros(Nx/2*(Nx/2-1))
    if left == True: # I + matrix
        for j in range(1,Ny-1,2):
            for i, x1 in enumerate(range(1,Nx,2)):
                D[i] = (-P4_code(x = x1, y = i, c1 = ccc, f1 = fff))*theta*lam
    else: # I - matrix
        for j in range(1,Ny-1,2):
            for i, x1 in enumerate(range(1,Nx,2)):
                D[i] = (-P4_code(x = x1, y = i, c1 = ccc, f1 = fff))*theta*lam*(-1)  
    return D

def vector_E(theta = 0.5, time_step = 0.001, h = 0.01, X = 1, Y = 1, ccc = 0, fff = 0, left = False):
    lam = time_step/h**2
    hh = h/2
    Nx = int(X/hh)
    Ny = int(Y/hh)
    import numpy
    E = numpy.zeros(Nx/2*(Nx/2-1))
    if left == True: # I + matrix
        for j in range(3,Ny,2):
            for i, x1 in enumerate(range(1,Nx,2)):
                E[i] = (-P3_code(x = x1, y = j, c1 = ccc, f1 = fff))*theta*lam
    else: # I - matrix
        for j in range(3,Ny,2):
            for i, x1 in enumerate(range(1,Nx,2)):
                E[i] = (-P3_code(x = x1, y = j, c1 = ccc, f1 = fff))*theta*lam*(-1)
    return E




'''MAIN FUNCTION'''

def continuous_matrix_1_iter(theta = 0.5,d = 0.00035,ki = 0.38,al = 0.6,ro = 0,
                             nu = 0.1,be = 0.05,ga = 0.1,e = 0.45, number_of_tip = 3,
                             iter = 0, h = 0.01, X = 1,Y = 1, tp = 0.001,
                             n_o = 0, c_o = 0, f_o = 0, n = 0, c = 0, f = 0):
    from timeit import default_timer as timer 
    import numpy
    hh = h/2
    Nx = int(X/hh)
    Ny = int(Y/hh)
    if iter == 1:
        import math as m
        
        n = numpy.zeros((Nx+1,Ny+1))
        c = numpy.zeros((Nx+1,Ny+1))
        f = numpy.zeros((Nx+1,Ny+1))
        
        for y in range(0,Ny+1,2):
            for x in range(0,Nx+1,2):
                f[x,y] = 0.75*m.exp(-(x*hh)**2/e)
                c[x,y] = m.exp(-(1-x*hh)**2/e)
        for y in range(1,Ny,2):
            for x in range(1,Nx,2):
#                 n[x,y] = m.exp(-(x*hh)**2/0.001)*(m.sin(number_of_tip*m.pi*y*hh))**2
                n[x,y] = m.exp(-(x*hh)**2/0.01)*(m.sin(number_of_tip*m.pi*y*hh))**2
        n_o = n
        c_o = c
        f_o = f
#         n_o_vector =n_o.flatten()
    
    '''Time Step'''
    v1=[]
    w1=[]
    for y in range(2,Ny+1,2):
        for x in range(0,Nx,2):
#             v1x = 1/(2*h)*(c[x+2,y]-c[x,y]+c[x+2,y-2]-c[x,y-2])
#             v1y = 1/(2*h)*(c[x+2,y]-c[x+2,y-2]+c[x,y]-c[x,y-2])
#             v1.append(max(v1x,v1y))
            v1.append(max(1/(2*h)*(c[x+2,y]-c[x,y]+c[x+2,y-2]-c[x,y-2]),1/(2*h)*(c[x+2,y]-c[x+2,y-2]+c[x,y]-c[x,y-2])))
            
#             w1x = 1/(2*h)*(f[x+2,y]-f[x,y]+f[x+2,y-2]-f[x,y-2])
#             w1y = 1/(2*h)*(f[x+2,y]-f[x+2,y-2]+f[x,y]-f[x,y-2])
#             w1.append(max(w1x,w1y))
            w1.append(max(1/(2*h)*(f[x+2,y]-f[x,y]+f[x+2,y-2]-f[x,y-2]),1/(2*h)*(f[x+2,y]-f[x+2,y-2]+f[x,y]-f[x,y-2])))
#     vv1 = max(v1)
#     ww1 = max(w1)
#     tau1 = h**2/(4*(d+h*ki*vv1/(1+al*c.max())+h*ro*ww1))
#     tau2 = 1/(nu*n.max())
#     tau1 = min(tau1,tau2)
    tau1 = min(h**2/(4*(d+h*ki*max(v1)/(1+al*c.max())+h*ro*max(w1))),1/(nu*n.max()))
    if tau1 < tp:
        tp = tau1
    
    '''Build SPL Matrix of RHS'''
    start_c_1 = timer()
    teta = 0.75

    A_right = vector_A(ccc = c_o, fff = f_o, theta = 1-teta)
    B_right = vector_B(ccc = c_o, fff = f_o, theta = 1-teta)
    C_right = vector_C(ccc = c_o, fff = f_o, theta = 1-teta)
    D_right = vector_D(ccc = c_o, fff = f_o, theta = 1-teta)
    E_right = vector_E(ccc = c_o, fff = f_o, theta = 1-teta)
    
    '''ABCDE n = Q'''
    '''ABCDE mau dibuat matrix segitiga atas lalu diselesaikan menggunakan metode eliminasi gauss'''
    start_c_2 = timer()
    print 'time for SPL right matrix', start_c_2-start_c_1
    '''Creating LHS Matrix using vector to store and create
    (Nx/2-2)*2 zeros vector to make the matix is to be (Nx/2-2)*2+5 diagonal matrix'''
    
    a = []
    a.append(vector_E(ccc = c, fff = f, theta = teta, left = True))
    for i in range(Nx/2-2):
        a.append(numpy.zeros(i-(Nx/2-2)+(Nx/2)**2-1))
    a.append(vector_C(ccc = c, fff = f, theta = teta, left = True))
    a.append(vector_B(ccc = c, fff = f, theta = teta, left = True))
    a.append(vector_A(ccc = c, fff = f, theta = teta, left = True))
    for i in range(Nx/2-2):
        a.append(numpy.zeros((Nx/2)**2-2-i))
    a.append(vector_D(ccc = c, fff = f, theta = teta, left = True))

    '''Computing Vector of Right Side ( as Q)'''
    start_c_3 = timer()
    print 'time LHS Matrix', start_c_3-start_c_2
    Q = numpy.zeros((Nx/2)**2)
    for i,j in enumerate(range(1,Nx,2)): #untuk paling awal
        if j == 1: 
            Q[i] = B_right[i]*n_o[1,1] + C_right[i]*n_o[3,1] + E_right[i]*n_o[1,3] #B & C , E
        elif j == Nx-1: 
            Q[i] = A_right[i-1]*n_o[j-2,1] + B_right[i]*n_o[j,1] + E_right[i]*n_o[j,3]#A & B, E
        else:
            Q[i] = A_right[i-1]*n_o[j-2,1] + B_right[i]*n_o[j,1] + C_right[i]*n_o[j+2,1] + E_right[i]*n_o[j,3]#A & B & C, E
            
    i = Nx/2       
    for k,l in enumerate(range(3,Nx-2,2)): 
        for j in range(1,Nx,2): #untuk tengah #Nx/2 , (Nx/2)**2-Nx/2
            if j == 1:
                Q[i] = D_right[i-(Nx/2)]*n_o[j,l-2] + B_right[i]*n_o[j,l] + C_right[i]*n_o[j+2,l] + E_right[i]*n_o[j,l+2] #D, B & C, E
            elif j == Nx-1:
                Q[i] = D_right[i-(Nx/2)]*n_o[j,l-2] + A_right[i-1]*n_o[j-2,l] + B_right[i]*n_o[j,l] + E_right[i]*n_o[j,l+2] #D, A & B, E
            else:
                Q[i] = D_right[i-(Nx/2)]*n_o[j,l-2] + A_right[i-1]*n_o[j-2,l] + B_right[i]*n_o[j,l] + C_right[i]*n_o[j+2,l] + E_right[i]*n_o[j,l+2] #D, A & B & C, E
            i +=1
     
    for i,j in enumerate(range(1,Nx,2)): #untuk terakhir #(Nx/2)**2-Nx/2 , (Nx/2)**2
        i += (Nx/2)**2-Nx/2
        if j == 1:
            Q[i] = D_right[i-(Nx/2)]*n_o[1,Nx-3] + B_right[i]*n_o[1,Nx-1] + C_right[i]*n_o[3,Nx-1] #D, B & C
        elif j == Nx-1:
            Q[i] = D_right[i-(Nx/2)]*n_o[j,Nx-3] + A_right[i-1]*n_o[j-2,Nx-1] + B_right[i]*n_o[j,Nx-1] #D, A & B
        else:
            Q[i] = D_right[i-(Nx/2)]*n_o[j,Nx-3] + A_right[i-1]*n_o[j-2,Nx-1] + B_right[i]*n_o[j,Nx-1] + C_right[i]*n_o[j+2,Nx-1] #D, A & B & C
    del A_right
    del B_right
    del C_right
    del D_right
    del E_right
    
    '''Algoritma Eliminasi Gauss'''
    '''vz n = Q'''
    '''First, to Make the left Matrix to be upper triangle'''
    start_c_4 = timer()
    print 'time RHS vector', start_c_4-start_c_3
    s = (len(a)-1)/2 #s=5 #index vector diagonal 
                     #number of pivot for each process
                     #number of elimination
    s1 = len(a[s])-1 #s1=3 number of process
    j = 0
    ii = 0
    jk = False
    
    for i in range(0,s1): #range sampai (Nx/2)**2-Nx/2
        if jk == True: #kalau pivot sudah masuk vector akhir
#             print 'proses ke', i
            ii += 1
            for j in range(0,s-ii):
#                 print
#                 print 'pivot ke', j, 'diambil dari element', s+j+1, i, 'dibagi', s,i
                p = a[s+j+1][i]/a[s][i]
                a[s+j+1][i] = 0
#                 print 'Q eliminasi untuk element', i+j+1, 'dikurang p*elemen',i
                Q[i+j+1] = Q[i+j+1]-p*Q[i]
                for u in range(1,s+1-ii):
                    if j+1-u < 0: #untuk lebih dari diagonal 
#                         print 'elmininasI ke', u, 'untuk element', s+j+1-u, jj, 'dikurang p*elemen', s-u, i
                        a[s+j+1-u][jj] = a[s+j+1-u][jj]-p*a[s-u][i]
                    else:
                        jj = i+u
#                         print 'elmininasi ke', u, 'untuk element', s+j+1-u, i+u, 'dikurang p*elemen', s-u, i
                        a[s+j+1-u][i+u] = a[s+j+1-u][i+u]-p*a[s-u][i]
#             print
        else: #normal process
#             print 'proses ke', i
            for j in range(0,s):
#                 print
#                 print 'pivot ke', j, 'diambil dari element', s+j+1, i, 'dibagi', s,i
                p = a[s+j+1][i]/a[s][i]
                a[s+j+1][i] = 0
#                 print 'Q eliminasi untuk element', i+j+1, 'dikurang p*elemen',i
                Q[i+j+1] = Q[i+j+1]-p*Q[i]
                for u in range(1,s+1):
                    if j+1-u < 0: #untuk lebih dari diagonal 
#                         print 'elmininasI ke', u, 'untuk element', s+j+1-u, jj, 'dikurang p*elemen', s-u, i
                        a[s+j+1-u][jj] = a[s+j+1-u][jj]-p*a[s-u][i]
                    else:
                        jj = i+u
#                         print 'elmininasi ke', u, 'untuk element', s+j+1-u, i+u, 'dikurang p*elemen', s-u, i
                        a[s+j+1-u][i+u] = a[s+j+1-u][i+u]-p*a[s-u][i]
#             print   
            if s+j+1 == len(a)-1 and i == len(a[-1])-1:
                jk = True
    
    '''Second is to Solve n by Penyulihan Mundur'''
    start_c_5 = timer()
    print 'time Upper Triange', start_c_5-start_c_4    
    ii = len(Q)-1
    jj = 0
    kk = 0
    n[Nx-1,Ny-1] = Q[ii]/(a[s][ii])
    for j in reversed(range(1,Ny,2)):
        kkk = 0
        for i in reversed(range(1,Nx,2)):
            sum_j = 0
            if j == Ny-1 and i == Nx-1:
                pass
            else:
                ii -= 1
#                 print 'n pos:',i,j,'diagonal:',s,ii
                if kk < Nx/2-1:
                    kk +=1
                    for i1 in range(0,kk):
#                         print 'element vector sum', s-kk+i1, ii
#                         print 'element n multiple', Nx-1-(i1*2), j
                        sum_j += a[s-kk+i1][ii]*n[Nx-1-(i1*2), j] 
#                     print
                else:
                    for i1 in range(0,kkk): #on the same j
#                         print 'element vector sum', s-i1-1, ii
#                         print 'element n multiple', i+2+(i1*2), j
                        sum_j += a[s-i1-1][ii]*n[i+2+(i1*2),j]
                    for i1 in range(kkk,s): #on the upper j
#                         print 'element vector sum', s-i1-1, ii
#                         print 'element n multiple', 1+(i1-kkk)*2, j+2
                        sum_j += a[s-i1-1][ii]*n[1+(i1-kkk)*2,j+2]
#                     print 
                    kkk +=1  
                n[i,j] = (Q[ii]-sum_j)/a[s][ii]
    start_c_6 = timer()
    print 'Time Penyulihan Mundur', start_c_6-start_c_5
    '''Algoritma Eliminasi Gauss'''
    print 'Time increment', tp        
    rr = [n_o,c_o,f_o,n,c,f,tp]#A,B,C,
    n_o = n
    c_o = c
    f_o = f
#     n_o_vector =n_o.flatten() 
    return rr
    
    