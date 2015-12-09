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

def Matrix_A(h = 0.1, yp = 1, X = 1, ccc = 0, fff = 0):
    hh = h/2
    Nx = int(X/hh)
    import numpy
    A = numpy.zeros(shape=(Nx/2,Nx/2))
    A[0,0] = P1_code(x = 1, y = yp, c1 = ccc, f1 = fff) + P3_code(x = 1, y = yp, c1 = ccc, f1 = fff) 
    A[0,1] = -P1_code(x = 3, y = yp, c1 = ccc, f1 = fff)
    j = Nx/2-1
    A[j,j-1] = -P2_code(x = j-2, y = yp, c1 = ccc, f1 = fff)
    A[j,j] = P2_code(x = j, y = yp, c1 = ccc, f1 = fff) + P3_code(x = j, y = yp, c1 = ccc, f1 = fff)
    for i, x1 in enumerate(range(1,Nx-1,2)):
        if i == 0:
            pass
        else:
            A[i,i] = P1_code(x = x1, y = yp, c1 = ccc, f1 = fff)+P2_code(x = x1, y = yp, c1 = ccc, f1 = fff)+P3_code(x = x1, y = yp, c1 = ccc, f1 = fff)
            A[i,i-1] = -P2_code(x = x1-2, y = yp, c1 = ccc, f1 = fff)
            A[i,i+1] = -P1_code(x = x1+2, y = yp, c1 = ccc, f1 = fff)
    return A

def Matrix_C(h = 0.1, yp = int(2/0.1)-1, X = 1, ccc = 0, fff = 0):
    hh = h/2
    Nx = int(X/hh)
    import numpy
    C = numpy.zeros(shape=(Nx/2,Nx/2))
    C[0,0] = P1_code(x = 1, y = yp, c1 = ccc, f1 = fff) + P4_code(x = 1, y = yp, c1 = ccc, f1 = fff) 
    C[0,1] = -P1_code(x = 3, y = yp, c1 = ccc, f1 = fff)
    j = Nx/2-1
    C[j,j-1] = -P2_code(x = j-2, y = yp, c1 = ccc, f1 = fff)
    C[j,j] = P2_code(x = j, y = yp, c1 = ccc, f1 = fff) + P4_code(x = j, y = yp, c1 = ccc, f1 = fff)
    for i, x1 in enumerate(range(1,Nx-1,2)):
        if i == 0:
            pass
        else:
            C[i,i] = P1_code(x = x1, y = yp, c1 = ccc, f1 = fff)+P2_code(x = x1, y = yp, c1 = ccc, f1 = fff)+P4_code(x = x1, y = yp, c1 = ccc, f1 = fff)
            C[i,i-1] = -P2_code(x = x1-2, y = yp, c1 = ccc, f1 = fff)
            C[i,i+1] = -P1_code(x = x1+2, y = yp, c1 = ccc, f1 = fff)
    return C

def Matrix_B(h = 0.1, X = 1, yp = 3, ccc = 0, fff = 0):
    hh = h/2
    Nx = int(X/hh)
    import numpy
    B = numpy.zeros(shape=(Nx/2,Nx/2))
    B[0,0] = P1_code(x = 1, y = yp, c1 = ccc, f1 = fff) + P3_code(x = 1, y = yp, c1 = ccc, f1 = fff) + P4_code(x = 1, y = yp, c1 = ccc, f1 = fff) 
    B[0,1] = -P1_code(x = 3, y = yp, c1 = ccc, f1 = fff)
    j = Nx/2-1
    B[j,j-1] = -P2_code(x = j-2, y = yp, c1 = ccc, f1 = fff)
    B[j,j] = P2_code(x = j, y = yp, c1 = ccc, f1 = fff) + P3_code(x = j, y = yp, c1 = ccc, f1 = fff) + P4_code(x = j, y = yp, c1 = ccc, f1 = fff)
    for i, x1 in enumerate(range(1,Nx-1,2)):
        if i == 0:
            pass
        else:
            B[i,i] = P1_code(x = x1, y = yp, c1 = ccc, f1 = fff) + P2_code(x = x1, y = yp, c1 = ccc, f1 = fff) + P3_code(x = x1, y = yp, c1 = ccc, f1 = fff) + P4_code(x = x1, y = yp, c1 = ccc, f1 = fff)
            B[i,i-1] = -P2_code(x = x1-2, y = yp, c1 = ccc, f1 = fff)
            B[i,i+1] = -P1_code(x = x1+2, y = yp, c1 = ccc, f1 = fff)
    return B

def Matrix_D(h = 0.1, X = 1, yp = 1, ccc = 0, fff = 0):
    hh = h/2
    Nx = int(X/hh)
    import numpy
    D = numpy.zeros(shape=(Nx/2,Nx/2))
    for i, x1 in enumerate(range(1,Nx,2)):
        D[i,i] = -P4_code(x = x1, y = yp, c1 = ccc, f1 = fff)
    return D

def Matrix_E(h = 0.1, X = 1, yp = 3, ccc = 0, fff = 0):
    hh = h/2
    Nx = int(X/hh)
    import numpy
    E = numpy.zeros(shape=(Nx/2,Nx/2))
    for i, x1 in enumerate(range(1,Nx,2)):
        E[i,i] = -P4_code(x = x1, y = yp, c1 = ccc, f1 = fff)
    return E



'''Main Function'''

def continuous_matrix_1_iter(theta = 0,d = 0.00035,ki = 0.38,al = 0.6,ro = 0,
                             nu = 0.1,be = 0.05,ga = 0.1,e = 0.45, number_of_tip = 3,
                             iter = 1, h = 0.1, X = 1,Y = 1):
    
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
#     A, B, D, E
    x = 1
    y = 1
    I = numpy.eye((Nx/2)**2) #identity matrix
    A = Matrix_A(ccc = c, fff = f)
    C = Matrix_C(ccc = c, fff = f)
    B = Matrix_B(yp = 3,ccc = c, fff = f)
    D = Matrix_D(yp = 1,ccc = c, fff = f)
    E = Matrix_E(yp = 3,ccc = c, fff = f)
    
    B = Matrix_B(yp = Nx-1,ccc = c, fff = f)
    D = Matrix_D(yp = Nx-3,ccc = c, fff = f)
    E = Matrix_E(yp = Nx-1,ccc = c, fff = f)
    rr = [A,B,C,D,E,I]
    return rr
r = continuous_matrix_1_iter()

    
    
    
    