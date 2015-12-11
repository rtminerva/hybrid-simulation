def vx_code(h = 0.005, cc = 0, x_p = 0, y_p = 0): #at main lattice
    r = 0.5/h*(cc[x_p+1,y_p+1]-cc[x_p-1,y_p+1]+cc[x_p+1,y_p-1]-cc[x_p-1,y_p-1])
    return r
    
def vy_code(h = 0.005, cc = 0, x_p = 0, y_p = 0): #at main lattice
    r = 0.5/h*(cc[x_p+1,y_p+1]+cc[x_p-1,y_p+1]-cc[x_p+1,y_p-1]-cc[x_p-1,y_p-1])
    return r
    
def wx_code(h = 0.005, ff = 0, x_p = 0, y_p = 0): #at main lattice
    r = 0.5/h*(ff[x_p+1,y_p+1]-ff[x_p-1,y_p+1]+ff[x_p+1,y_p-1]-ff[x_p-1,y_p-1])
    return r

def wy_code(h = 0.005, ff = 0, x_p = 0, y_p = 0): #at main lattice
    r = 0.5/h*(ff[x_p+1,y_p+1]+ff[x_p-1,y_p+1]-ff[x_p+1,y_p-1]-ff[x_p-1,y_p-1])
    return r

def P1_code(h = 0.005,d = 0.00035, ki = 0.38, al = 0.6, ro = 0, c1 = 0, x = 0, y = 0, f1 = 0):
    r = d + h*ki/(1+al*c1[x-1,y+1])*max(-vx_code(x_p = x, y_p = y, cc = c1), 0) + h*ro*max(-wx_code(x_p = x, y_p = y, ff = f1), 0)
    return r

def P2_code(h = 0.005,d = 0.00035, ki = 0.38, al = 0.6, ro = 0, c1 = 0, x = 0, y = 0, f1 = 0):
    r = d + h*ki/(1+al*c1[x+1,y+1])*max(vx_code(x_p = x, y_p = y, cc = c1), 0) + h*ro*max(wx_code(x_p = x, y_p = y, ff = f1), 0)
    return r

def P3_code(h = 0.005,d = 0.00035, ki = 0.38, al = 0.6, ro = 0, c1 = 0, x = 0, y = 0, f1 = 0):
    r = d + h*ki/(1+al*c1[x+1,y-1])*max(-vy_code(x_p = x, y_p = y, cc = c1), 0) + h*ro*max(-wy_code(x_p = x, y_p = y, ff = f1), 0)
    return r

def P4_code(h = 0.005,d = 0.00035, ki = 0.38, al = 0.6, ro = 0, c1 = 0, x = 0, y = 0, f1 = 0): #at main lattice
    r = d + h*ki/(1+al*c1[x+1,y+1])*max(vy_code(x_p = x, y_p = y, cc = c1), 0) + h*ro*max(wy_code(x_p = x, y_p = y, ff = f1), 0)
    return r

def vector_A(theta = 0.5, time_step = 0.001, h = 0.2, X = 1, Y = 1, ccc = 0, fff = 0, left = False):
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


def vector_B(theta = 0.5, time_step = 0.001, h = 0.2, X = 1, Y = 1, ccc = 0, fff = 0, left = False):
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

    
def vector_C(theta = 0.5, time_step = 0.001, h = 0.2, X = 1, Y = 1, ccc = 0, fff = 0, left = False):
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


def vector_D(theta = 0.5, time_step = 0.001, h = 0.2, X = 1, Y = 1, ccc = 0, fff = 0, left = False):
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

def vector_E(theta = 0.5, time_step = 0.001, h = 0.2, X = 1, Y = 1, ccc = 0, fff = 0, left = False):
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



'''Main Function'''

def continuous_matrix_1_iter(theta = 0.5,d = 0.00035,ki = 0.38,al = 0.6,ro = 0,
                             nu = 0.1,be = 0.05,ga = 0.1,e = 0.45, number_of_tip = 3,
                             iter = 1, h = 0.2, X = 1,Y = 1, tp = 0.001):
    
    import numpy
    hh = h/2
    Nx = int(X/hh)
    if iter == 1:
        import math as m
        
        
        Ny = int(Y/hh)
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
    
    '''Build SPL Matrix'''
    teta = 0.75
    
    A_left = vector_A(ccc = c, fff = f, theta = teta, left = True)
    B_left = vector_B(ccc = c, fff = f, theta = teta, left = True)
    C_left = vector_C(ccc = c, fff = f, theta = teta, left = True)
    D_left = vector_D(ccc = c, fff = f, theta = teta, left = True)
    E_left = vector_E(ccc = c, fff = f, theta = teta, left = True)
    
    A_right = vector_A(ccc = c_o, fff = f_o, theta = 1-teta)
    B_right = vector_B(ccc = c_o, fff = f_o, theta = 1-teta)
    C_right = vector_C(ccc = c_o, fff = f_o, theta = 1-teta)
    D_right = vector_D(ccc = c_o, fff = f_o, theta = 1-teta)
    E_right = vector_E(ccc = c_o, fff = f_o, theta = 1-teta)
    rr = [A_left,B_left,C_left,D_left,E_left,A_right,B_right,C_right,D_right,E_right,tp]#A,B,C,
    return rr
r = continuous_matrix_1_iter()
print 'Vector A_left', r[0]
print 'Vector B_left', r[1]
print 'Vector C_left', r[2]
print 'Vector D_left', r[3]
print 'Vector E_left', r[4]    
print
print 'Vector A_right', r[5]
print 'Vector B_right', r[6]
print 'Vector C_right', r[7]
print 'Vector D_right', r[8]
print 'Vector E_right', r[9] 
    
    
    