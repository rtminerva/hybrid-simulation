def vx_code(h1 = 0.005, cc = 0, x_p = 0, y_p = 0): #at main lattice
    r = 0.5/h1*(cc[x_p+1,y_p+1]-cc[x_p-1,y_p+1]+cc[x_p+1,y_p-1]-cc[x_p-1,y_p-1])
    return r
    
def vy_code(h1 = 0.005, cc = 0, x_p = 0, y_p = 0): #at main lattice
    r = 0.5/h1*(cc[x_p+1,y_p+1]+cc[x_p-1,y_p+1]-cc[x_p+1,y_p-1]-cc[x_p-1,y_p-1])
    return r
    
def wx_code(h1 = 0.005, ff = 0, x_p = 0, y_p = 0): #at main lattice
    r = 0.5/h1*(ff[x_p+1,y_p+1]-ff[x_p-1,y_p+1]+ff[x_p+1,y_p-1]-ff[x_p-1,y_p-1])
    return r

def wy_code(h1 = 0.005, ff = 0, x_p = 0, y_p = 0): #at main lattice
    r = 0.5/h1*(ff[x_p+1,y_p+1]+ff[x_p-1,y_p+1]-ff[x_p+1,y_p-1]-ff[x_p-1,y_p-1])
    return r

def P1_code(h1 = 0.005,d = 0.00035, ki = 0.38, al = 0.6, ro = 0, c1 = 0, x = 0, y = 0, f1 = 0):
    r = d + h1*ki/(1+al*c1[x-1,y+1])*max(-vx_code(x_p = x, y_p = y, cc = c1), 0) + h1*ro*max(-wx_code(x_p = x, y_p = y, ff = f1), 0)
    return r

def P2_code(h1 = 0.005,d = 0.00035, ki = 0.38, al = 0.6, ro = 0, c1 = 0, x = 0, y = 0, f1 = 0):
    r = d + h1*ki/(1+al*c1[x+1,y+1])*max(vx_code(x_p = x, y_p = y, cc = c1), 0) + h1*ro*max(wx_code(x_p = x, y_p = y, ff = f1), 0)
    return r

def P3_code(h1 = 0.005,d = 0.00035, ki = 0.38, al = 0.6, ro = 0, c1 = 0, x = 0, y = 0, f1 = 0):
    r = d + h1*ki/(1+al*c1[x+1,y-1])*max(-vy_code(x_p = x, y_p = y, cc = c1), 0) + h1*ro*max(-wy_code(x_p = x, y_p = y, ff = f1), 0)
    return r

def P4_code(h1 = 0.005,d = 0.00035, ki = 0.38, al = 0.6, ro = 0, c1 = 0, x = 0, y = 0, f1 = 0): #at main lattice
    r = d + h1*ki/(1+al*c1[x+1,y+1])*max(vy_code(x_p = x, y_p = y, cc = c1), 0) + h1*ro*max(wy_code(x_p = x, y_p = y, ff = f1), 0)
    return r


def vector_A(theta = 0.5, time_step = 0.1, h2 = 0.005, X = 1, Y = 1, ccc = 0, fff = 0, left = False):
    lam = time_step/h2**2
    hh = h2/2
    Nx = int(X/hh)
    Ny = int(Y/hh)
    import numpy
    A = numpy.zeros((Nx/2)**2-1)
    if left == True: # I + matrix
        '''Bottom side'''
        j = 1
        for i, x1 in enumerate(range(1,Nx-1,2)):
            A[i] = (-P2_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
        '''Inside'''
        for j, y1 in enumerate(range(3,Ny-1,2)):
            for i, x1 in enumerate(range(1,Nx-1,2)):
                A[(i+Nx/2)+j*Nx/2] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
        '''Up side'''
        j = Ny-1
        for i, x1 in enumerate(range(1,Nx-1,2)):
            A[i+(Nx/2)**2-Nx/2] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
    else: # I - matrix
        '''Bottom side'''
        j = 1
        for i, x1 in enumerate(range(1,Nx-1,2)):
            A[i] = (-P2_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2))*theta*lam*(-1)
        '''Inside'''
        for j, y1 in enumerate(range(3,Ny-1,2)):
            for i, x1 in enumerate(range(1,Nx-1,2)):
                A[(i+Nx/2)+j*Nx/2] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2))*theta*lam*(-1)
        '''Up side'''
        j = Ny-1
        for i, x1 in enumerate(range(1,Nx-1,2)):
            A[i+(Nx/2)**2-Nx/2] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2))*theta*lam*(-1)
    A = numpy.append(A, 0)
    return A


def vector_B(theta = 0.5, time_step = 0.1, h2 = 0.005, X = 1, Y = 1, ccc = 0, fff = 0, left = False):
    lam = time_step/h2**2
    hh = h2/2
    Nx = int(X/hh)
    Ny = int(Y/hh)
    import numpy
    B = numpy.zeros((Nx/2)**2)
    if left == True: # I + matrix
        '''Bottom side'''
        j = 1
        x1 = 1
        i = 0
        B[i] = 1 + (P2_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2)+P4_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
        for x1 in range(3,Nx-1,2):
            i += 1
            B[i] = 1 + (P1_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2)+P2_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2)+P4_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
        
        x1 = Nx-1
        B[i+1] = 1 + (P1_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2)+P4_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
        
        '''Inside'''
        for j, y1 in enumerate(range(3,Ny-1,2)):
            x1 = 1
            i = 0
            B[(i+Nx/2)+j*Nx/2] = 1 + (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2) + P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2) + P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
            for x1 in range(3,Nx-1,2):
                i += 1
                B[(i+Nx/2)+j*Nx/2] = 1 + (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2) + P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2) + P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2) + P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
            x1 = Nx-1
            B[(i+1+Nx/2)+j*Nx/2] = 1 + (P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2) + P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2) + P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
        '''Up side'''
        j = Ny-1
        x1 = 1
        i = 0
        B[i+(Nx/2)**2-Nx/2] = 1 + (P2_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2)+P3_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
        for x1 in range(3,Nx-1,2):
            i += 1
            B[i+(Nx/2)**2-Nx/2] = 1 + (P1_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2)+P2_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2)+P3_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
        x1 = Nx-1
        B[i+1+(Nx/2)**2-Nx/2] = 1 + (P1_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2)+P3_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
        
    else: # I - matrix
        '''Bottom side'''
        j = 1
        x1 = 1
        i = 0
        B[i] = 1 + (P2_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2)+P4_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
        for x1 in range(3,Nx-1,2):
            i += 1
            B[i] = 1 + (P1_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2)+P2_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2)+P4_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
        
        x1 = Nx-1
        B[i+1] = 1 + (P1_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2)+P4_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
        
        '''Inside'''
        for j, y1 in enumerate(range(3,Ny-1,2)):
            x1 = 1
            i = 0
            B[(i+Nx/2)+j*Nx/2] = 1 - (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2) + P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2) + P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
            for x1 in range(3,Nx-1,2):
                i += 1
                B[(i+Nx/2)+j*Nx/2] = 1 - (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2) + P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2) + P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2) + P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
            x1 = Nx-1
            B[(i+1+Nx/2)+j*Nx/2] = 1 - (P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2) + P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2) + P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
        '''Up side'''
        j = Ny-1
        x1 = 1
        i = 0
        B[i+(Nx/2)**2-Nx/2] = 1 - (P2_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2)+P3_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
        for x1 in range(3,Nx-1,2):
            i += 1
            B[i+(Nx/2)**2-Nx/2] = 1 - (P1_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2)+P2_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2)+P3_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
        x1 = Nx-1
        B[i+1+(Nx/2)**2-Nx/2] = 1 - (P1_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2)+P3_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
    return B

    
def vector_C(theta = 0.5, time_step = 0.1, h2 = 0.005, X = 1, Y = 1, ccc = 0, fff = 0, left = False):
    lam = time_step/h2**2
    hh = h2/2
    Nx = int(X/hh)
    Ny = int(Y/hh)
    import numpy
    C = numpy.zeros((Nx/2)**2-1)
    if left == True: # I + matrix
        '''Bottom side'''
        j = 1
        for i, x1 in enumerate(range(3,Nx,2)):
            C[i] = (-P1_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
        '''Inside'''
        for j, y1 in enumerate(range(3,Ny-1,2)):
            for i, x1 in enumerate(range(3,Nx,2)):
                C[(i+Nx/2)+j*Nx/2] = (-P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
        '''Up side'''
        j = Ny-1
        for i, x1 in enumerate(range(3,Nx,2)):
            C[i+(Nx/2)**2-Nx/2] = (-P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
    else: # I - matrix
        '''Bottom side'''
        j = 1
        for i, x1 in enumerate(range(3,Nx,2)):
            C[i] = (-P1_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2))*theta*lam*(-1)
        '''Inside'''
        for j, y1 in enumerate(range(3,Ny-1,2)):
            for i, x1 in enumerate(range(3,Nx,2)):
                C[(i+Nx/2)+j*Nx/2] = (-P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2))*theta*lam*(-1)
        '''Up side'''
        j = Ny-1
        for i, x1 in enumerate(range(3,Nx,2)):
            C[i+(Nx/2)**2-Nx/2] = (-P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2))*theta*lam*(-1)
    C = numpy.insert(C,0,0)
    return C


def vector_D(theta = 0.5, time_step = 0.1, h2 = 0.005, X = 1, Y = 1, ccc = 0, fff = 0, left = False):
    lam = time_step/h2**2
    hh = h2/2
    Nx = int(X/hh)
    Ny = int(Y/hh)
    import numpy
    D = numpy.zeros(Nx/2*(Nx/2-1)) #Nx/2*(Nx/2-1)
    if left == True: # I + matrix
        for j in range(1,Ny-1,2):
            for i, x1 in enumerate(range(1,Nx,2)):
                D[i] = (-P4_code(x = x1, y = i, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
    else: # I - matrix
        for j in range(1,Ny-1,2):
            for i, x1 in enumerate(range(1,Nx,2)):
                D[i] = (-P4_code(x = x1, y = i, c1 = ccc, f1 = fff, h1 = h2))*theta*lam*(-1)  
    kk = Nx/2
    D = numpy.append(D, [0]*kk)
    return D

def vector_E(theta = 0.5, time_step = 0.1, h2 = 0.005, X = 1, Y = 1, ccc = 0, fff = 0, left = False):
    lam = time_step/h2**2
    hh = h2/2
    Nx = int(X/hh)
    Ny = int(Y/hh)
    import numpy
    E = numpy.zeros(Nx/2*(Nx/2-1)) #Nx/2*(Nx/2-1)
    if left == True: # I + matrix
        for j in range(3,Ny,2):
            for i, x1 in enumerate(range(1,Nx,2)):
                E[i] = (-P3_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
    else: # I - matrix
        for j in range(3,Ny,2):
            for i, x1 in enumerate(range(1,Nx,2)):
                E[i] = (-P3_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2))*theta*lam*(-1)
    kk = Nx/2
    E = numpy.insert(E, [0]*kk,0)
    return E




def continuous_sparse_matrix_1_iter(teta = 0.75,d = 0.00035,ki = 0.38,al = 0.6,ro = 0,
                                    nu = 0.1,be = 0.05,ga = 0.1,e = 0.45, number_of_tip = 6,
                                    iter = 0, h3 = 0.005, X = 1,Y = 1, tp = 0.1,
                                    c_o = 0, f_o = 0, n = 0, c = 0, f = 0, n_v = 0):
    from timeit import default_timer as timer 
    import numpy
    hh = h3/2
    Nx = int(X/hh)
    Ny = int(Y/hh)
    if iter == 1:
        import math as m
        
        n = numpy.zeros((Nx+1,Ny+1))
        c = numpy.zeros((Nx+1,Ny+1))
        f = numpy.zeros((Nx+1,Ny+1))
        n_v = numpy.zeros((Nx/2)*(Ny/2))
        
        for y in range(0,Ny+1,2):
            for x in range(0,Nx+1,2):
                f[x,y] = 0.75*m.exp(-(x*hh)**2/e)
                c[x,y] = m.exp(-(1-x*hh)**2/e)
        for y in range(1,Ny,2):
            for x in range(1,Nx,2):
#                 n[x,y] = m.exp(-(x*hh)**2/0.001)*(m.sin(number_of_tip*m.pi*y*hh))**2
                n[x,y] = m.exp(-(x*hh)**2/0.01)*(m.sin(number_of_tip*m.pi*y*hh))**2
                 
        c_o = c
        f_o = f
        i = 0
        for y in range(1,Ny,2):
            for x in range(1,Nx,2):
                n_v[i] = n[x,y]
                i +=1
    
    '''Time Step'''
    v1=[]
    v2=[]
    w1=[]
    w2=[]
    for y in range(2,Ny+1,2):
        for x in range(0,Nx,2):
            v1.append(max(1/(2*h3)*(c[x+2,y]-c[x,y]+c[x+2,y-2]-c[x,y-2]),1/(2*h3)*(c[x+2,y]-c[x+2,y-2]+c[x,y]-c[x,y-2])))
            v2.append(max(1/(2*h3)*(c_o[x+2,y]-c_o[x,y]+c_o[x+2,y-2]-c_o[x,y-2]),1/(2*h3)*(c_o[x+2,y]-c_o[x+2,y-2]+c_o[x,y]-c_o[x,y-2])))
            w2.append(max(1/(2*h3)*(f_o[x+2,y]-f_o[x,y]+f_o[x+2,y-2]-f_o[x,y-2]),1/(2*h3)*(f_o[x+2,y]-f_o[x+2,y-2]+f_o[x,y]-f_o[x,y-2])))
            w1.append(max(1/(2*h3)*(f[x+2,y]-f[x,y]+f[x+2,y-2]-f[x,y-2]),1/(2*h3)*(f[x+2,y]-f[x+2,y-2]+f[x,y]-f[x,y-2])))
    tau1 = min(h3**2/(4*teta*(d+h3*ki*max(v1)/(1+al*c.max())+h3*ro*max(w1))),h3**2/(4*(1-teta)*(d+h3*ki*max(v2)/(1+al*c_o.max())+h3*ro*max(w2))),1/(nu*n.max()))
    if tau1 < tp:
        tp = tau1
    del v1
    del v2
    del w1
    del w2
    del tau1
        
    from scipy.sparse import dia_matrix
    from scipy.sparse.linalg import spsolve
    '''Creating RHS Sparse Matrix'''
    data = numpy.array([vector_D(ccc = c_o, fff = f_o, theta = 1-teta, time_step = tp, h2 = h3), vector_A(ccc = c_o, fff = f_o, theta = 1-teta, time_step = tp, h2 = h3), vector_B(ccc = c_o, fff = f_o, theta = 1-teta, time_step = tp, h2 = h3), vector_C(ccc = c_o, fff = f_o, theta = 1-teta, time_step = tp, h2 = h3), vector_E(ccc = c_o, fff = f_o, theta = 1-teta, time_step = tp, h2 = h3)])
#     print len(data[0]), len(data[1]), len(data[2]), len(data[3]), len(data[4])
    i = Nx/2
    ii = (Nx/2)**2
    diags = numpy.array([-i,-1, 0, 1, i])
    RHS = dia_matrix((data, diags), shape=(ii, ii))
      
    '''RHS Multiply n_v and store as '''
#     print len(n_v)
    V = numpy.dot(RHS.toarray(), n_v)
        
    '''Creating LHS Sparse Matrix'''
    data = numpy.array([vector_D(ccc = c_o, fff = f_o, theta = teta, left = True, time_step = tp, h2 = h3), vector_A(ccc = c_o, fff = f_o, theta = teta, left = True, time_step = tp, h2 = h3), vector_B(ccc = c_o, fff = f_o, theta = teta, left = True, time_step = tp, h2 = h3), vector_C(ccc = c_o, fff = f_o, theta = teta, left = True, time_step = tp, h2 = h3), vector_E(ccc = c_o, fff = f_o, theta = teta, left = True, time_step = tp, h2 = h3)])
    LHS = dia_matrix((data, diags), shape=(ii, ii))
    
    '''Solve LHS n = V'''
    n_sol = spsolve(LHS.tocsr(), V)
    del RHS
    del LHS
    del V
    del data
    del diags
    
    '''Solve c, f at sub lattice'''
    for y in range(0,Ny+1,2):
        for x in range(0,Nx+1,2):
            if y == 0:
                if x == 0:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n[1,1])
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*n[1,1]
                elif x == Nx:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n[Nx-1,1])
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*n[Nx-1,1]
                else:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*0.5*(n[x+1,1]+n[x-1,1]))
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*0.5*(n[x+1,1]+n[x-1,1])
            elif y == Ny:
                if x == 0:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n[1,Ny-1])
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*n[1,Ny-1]
                elif x == Nx:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n[Nx-1,Ny-1])
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*n[Nx-1,Ny-1]
                else:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*0.5*(n[x+1,Ny-1]+n[x-1,Ny-1]))
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*0.5*(n[x+1,Ny-1]+n[x-1,Ny-1])
            else:
                if x == 0:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*0.5*(n[x+1,y+1]+n[x+1,y-1]))
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*0.5*(n[x+1,y+1]+n[x+1,y-1])
                elif x == Nx:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*0.5*(n[x-1,y+1]+n[x-1,y-1]))
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*0.5*(n[x-1,y+1]+n[x-1,y-1])
                else:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*0.25*(n[x+1,y+1]+n[x-1,y+1]+n[x+1,y-1]+n[x-1,y-1]))
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*0.25*(n[x+1,y+1]+n[x-1,y+1]+n[x+1,y-1]+n[x-1,y-1])
    
    
    
    '''Storing new n solution into n[x,y]'''
    n_v = n_sol
    i = 0
    for y in range(1,Ny,2):
        for x in range(1,Nx,2):
            n[x,y] = n_v[i] 
            i +=1      
    rr = [n_v,c_o,f_o,n,c,f,tp]#A,B,C,
    c_o = c
    f_o = f
    for value in c:
        if value.all < 0:
            print 'Ada C yang negative'
            quit()
    for value in f:
        if value.all < 0:
            print 'Ada F yang negative'
            quit()
    for value in n_v:
        if value.all < 0:
            print 'Ada N yang negative'
            quit()
    return rr
# continuous_sparse_matrix_1_iter(iter=1)
