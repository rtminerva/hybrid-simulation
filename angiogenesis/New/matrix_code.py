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

def P1_code(h = 0.005,d = 0.00035, ki = 0.38, al = 0.6, ro = 0, cc = 0, x_p = 0, y_p = 0):
    r = d + h*ki/(1+al*cc[x_p-1,y_p+1])*max(-vx_code(x_p = x, y_p = y, cc = c), 0) + h*ro*max(-wx_code(x_p = x, y_p = y, cc = c), 0)
    return r

def P2_code(h = 0.005,d = 0.00035, ki = 0.38, al = 0.6, ro = 0, cc = 0, x_p = 0, y_p = 0):
    r = d + h*ki/(1+al*cc[x_p+1,y_p+1])*max(vx_code(x_p = x, y_p = y, cc = c), 0) + h*ro*max(wx_code(x_p = x, y_p = y, cc = c), 0)
    return r

def P3_code(h = 0.005,d = 0.00035, ki = 0.38, al = 0.6, ro = 0, cc = 0, x_p = 0, y_p = 0):
    r = d + h*ki/(1+al*cc[x_p+1,y_p-1])*max(-vy_code(x_p = x, y_p = y, cc = c), 0) + h*ro*max(-wy_code(x_p = x, y_p = y, cc = c), 0)
    return r

def P4_code(h = 0.005,d = 0.00035, ki = 0.38, al = 0.6, ro = 0, cc = 0, x_p = 0, y_p = 0): #at main lattice
    r = d + h*ki/(1+al*cc[x_p+1,y_p+1])*max(vy_code(x_p = x, y_p = y, cc = c), 0) + h*ro*max(wy_code(x_p = x, y_p = y, cc = c), 0)
    return r

def Matrix_A(h = 0.005, y_p = 1, X = 1):
    hh = h/2
    Nx = int(X/hh)
    import numpy
    A = numpy.zeros(shape=(Nx/2,Nx/2))
    A[0,0] = P1_code(x_p = 1, y_p) + P3_code(x_p = 1, y_p) 
    A[0,1] = -P1_code(x_p = 3, y_p)
    j = Nx/2-1
    A[j,j-1] = -P2_code(x_p = j-2, y_p)
    A[j,j] = P2_code(x_p = j, y_p) + P3_code(x_p = j, y_p)
    for i, x in enumerate(range(1,Nx-1,2)):
        if i == 0:
            pass
        else:
            A[i,i] = P1_code(x_p = x, y_p)+P2_code(x_p = x, y_p)+P3_code(x_p = x, y_p)
            A[i,i-1] = -P2_code(x_p = x-2, y_p)
            A[i,i+1] = -P1_code(x_p = x+2, y_p)
    return A

def Matrix_C(h = 0.005, y_p = int(2/0.005)-1, X = 1):
    hh = h/2
    Nx = int(X/hh)
    import numpy
    C = numpy.zeros(shape=(Nx/2,Nx/2))
    C[0,0] = P1_code(x_p = 1, y_p) + P4_code(x_p = 1, y_p) 
    C[0,1] = -P1_code(x_p = 3, y_p)
    j = Nx/2-1
    C[j,j-1] = -P2_code(x_p = j-2, y_p)
    C[j,j] = P2_code(x_p = j, y_p) + P4_code(x_p = j, y_p)
    for i, x in enumerate(range(1,Nx-1,2)):
        if i == 0:
            pass
        else:
            C[i,i] = P1_code(x_p = x, y_p)+P2_code(x_p = x, y_p)+P4_code(x_p = x, y_p)
            C[i,i-1] = -P2_code(x_p = x-2, y_p)
            C[i,i+1] = -P1_code(x_p = x+2, y_p)
    return C

def Matrix_B(h = 0.005, y_p = 3, X = 1):
    hh = h/2
    Nx = int(X/hh)
    import numpy
    B = numpy.zeros(shape=(Nx/2,Nx/2))
    B[0,0] = P1_code(x_p = 1, y_p) + P3_code(x_p = 1, y_p) + P4_code(x_p = 1, y_p) 
    B[0,1] = -P1_code(x_p = 3, y_p)
    j = Nx/2-1
    B[j,j-1] = -P2_code(x_p = j-2, y_p)
    B[j,j] = P2_code(x_p = j, y_p) + P3_code(x_p = j, y_p) + P4_code(x_p = j, y_p)
    for i, x in enumerate(range(1,Nx-1,2)):
        if i == 0:
            pass
        else:
            B[i,i] = P1_code(x_p = x, y_p) + P2_code(x_p = x, y_p) + P3_code(x_p = x, y_p) + P4_code(x_p = x, y_p)
            B[i,i-1] = -P2_code(x_p = x-2, y_p)
            B[i,i+1] = -P1_code(x_p = x+2, y_p)
    return B

def Matrix D(h = 0.005, y_p = 3, X = 1):


'''Main Function'''

def continuous_matrix_1_iter(X = 1,Y = 1):
    
    import numpy
    if iter == 1:
        import math as m
        
        hh = h/2
        Nx = int(X/hh)
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
    I = numpy.eye((Nx/2)**2) #identity matrix
    
    B = numpy.zeros(shape=(Nx/2,Nx/2))

    D = numpy.zeros(shape=(Nx/2,Nx/2))
    E = numpy.zeros(shape=(Nx/2,Nx/2))
    
    '''Matrix D and E'''
    
    
    
    