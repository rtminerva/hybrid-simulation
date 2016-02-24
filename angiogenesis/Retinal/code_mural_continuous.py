def vx_code(h2 = 0, cc = 0, x_p = 0, y_p = 0): #at main lattice
    r = 0.5/h2*(cc[x_p+1,y_p+1]-cc[x_p-1,y_p+1]+cc[x_p+1,y_p-1]-cc[x_p-1,y_p-1])
    return r
    
def vy_code(h2 = 0, cc = 0, x_p = 0, y_p = 0): #at main lattice
    r = 0.5/h2*(cc[x_p+1,y_p+1]+cc[x_p-1,y_p+1]-cc[x_p+1,y_p-1]-cc[x_p-1,y_p-1])
    return r
    
def wx_code(h2 = 0, ff = 0, x_p = 0, y_p = 0): #at main lattice
    r = 0.5/h2*(ff[x_p+1,y_p+1]-ff[x_p-1,y_p+1]+ff[x_p+1,y_p-1]-ff[x_p-1,y_p-1])
    return r

def wy_code(h2 = 0, ff = 0, x_p = 0, y_p = 0): #at main lattice
    r = 0.5/h2*(ff[x_p+1,y_p+1]+ff[x_p-1,y_p+1]-ff[x_p+1,y_p-1]-ff[x_p-1,y_p-1])
    return r

def P1_code(h1 = 0,d = 0, ki = 0, al = 0, ro2 = 0, c1 = 0, x = 0, y = 0, f1 = 0):
    r = d + h1*ki/(1+al*c1[x-1,y+1])*max(-vx_code(x_p = x, y_p = y, cc = c1, h2 = h1), 0) + h1*ro2*max(-wx_code(x_p = x, y_p = y, ff = f1, h2 = h1), 0)
    return r

def P2_code(h1 = 0,d = 0, ki = 0, al = 0, ro2 = 0, c1 = 0, x = 0, y = 0, f1 = 0):
    r = d + h1*ki/(1+al*c1[x+1,y+1])*max(vx_code(x_p = x, y_p = y, cc = c1, h2 = h1), 0) + h1*ro2*max(wx_code(x_p = x, y_p = y, ff = f1, h2 = h1), 0)
    return r

def P3_code(h1 = 0,d = 0, ki = 0, al = 0, ro2 = 0, c1 = 0, x = 0, y = 0, f1 = 0):
    r = d + h1*ki/(1+al*c1[x+1,y-1])*max(-vy_code(x_p = x, y_p = y, cc = c1, h2 = h1), 0) + h1*ro2*max(-wy_code(x_p = x, y_p = y, ff = f1, h2 = h1), 0)
    return r

def P4_code(h1 = 0,d = 0, ki = 0, al = 0, ro2 = 0, c1 = 0, x = 0, y = 0, f1 = 0): #at main lattice
    r = d + h1*ki/(1+al*c1[x+1,y+1])*max(vy_code(x_p = x, y_p = y, cc = c1, h2 = h1), 0) + h1*ro2*max(wy_code(x_p = x, y_p = y, ff = f1, h2 = h1), 0)
    return r


def vector_A(theta = 0, time_step = 0, h2 = 0, ro1 = 0, Nx1 = 0, Ny1 = 0, ccc = 0, fff = 0, left = False, d1 =0, ki1=1, al1=0):
    lam = time_step/h2**2
    
    import numpy
  
    A = numpy.zeros((Nx1/2)**2-1)
    
    if left == True: # I + matrix
        ij = 0
        for y1 in range(1,Ny1,2):
            for x1 in range(1,Nx1,2):
                if ij > 0 and (ij+1) % (Nx1/2) == 0:
                    pass
                else:
                    A[ij] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*theta*lam
                ij += 1
            
#        '''Bottom side'''
#        y1 = 1
#        for i, x1 in enumerate(range(1,Nx1-1,2)):
#            A[i] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*theta*lam
#        '''Inside'''
#        for j, y1 in enumerate(range(3,Ny1-1,2)):
#            for i, x1 in enumerate(range(1,Nx1-1,2)):
#                A[(i+Nx1/2)+j*Nx1/2] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*theta*lam
#        '''Up side'''
#        y1 = Ny1-1
#        for i, x1 in enumerate(range(1,Nx1-1,2)):
#            A[i+(Nx1/2)**2-Nx/2] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*theta*lam
    else: # I - matrix
        ij = 0
        for y1 in range(1,Ny1,2):
            for x1 in range(1,Nx1,2):
                if ij > 0 and (ij+1) % (Nx1/2) == 0:
                    pass
                else:
                    A[ij] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*(1-theta)*lam*(-1)
                ij += 1
        
#        '''Bottom side'''
#        y1 = 1
#        for i, x1 in enumerate(range(1,Nx1-1,2)):
#            A[i] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*(theta-1)*lam*(-1)
#        '''Inside'''
#        for j, y1 in enumerate(range(3,Ny1-1,2)):
#            for i, x1 in enumerate(range(1,Nx1-1,2)):
#                A[(i+Nx1/2)+j*Nx1/2] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*(theta-1)*lam*(-1)
#        '''Up side'''
#        y1 = Ny1-1
#        for i, x1 in enumerate(range(1,Nx1-1,2)):
#            A[i+(Nx/2)**2-Nx1/2] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*(theta-1)*lam*(-1)
    A = numpy.append(A, 0)
    return A


def vector_B(theta = 0, time_step = 0, h2 = 0, ro1 = 0, Nx1 = 1, Ny1 = 1, ccc = 0, fff = 0, left = False, d1 =0, ki1=1, al1=0):
    lam = time_step/h2**2
    
    import numpy
    B = numpy.zeros((Nx1/2)**2)
    if left == True: # I + matrix
        '''Bottom side'''
        y1 = 1
        x1 = 1
        i = 0
        B[i] = 1 + (P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1)+P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*theta*lam
        for x1 in range(3,Nx1-1,2):
            i += 1
            B[i] = 1 + (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1)+P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1)+P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*theta*lam
        
        x1 = Nx1-1
        B[i+1] = 1 + (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1)+P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*theta*lam
        
        '''Inside'''
        for j, y1 in enumerate(range(3,Ny1-1,2)):
            x1 = 1
            i = 0
            B[(i+Nx1/2)+j*Nx1/2] = 1 + (P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1) + P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1) + P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*theta*lam
            for x1 in range(3,Nx1-1,2):
                i += 1
                B[(i+Nx1/2)+j*Nx1/2] = 1 + (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1) + P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1) + P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1) + P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*theta*lam
            x1 = Nx1-1
            B[(i+1+Nx1/2)+j*Nx1/2] = 1 + (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1) + P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1) + P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*theta*lam
        '''Up side'''
        y1 = Ny1-1
        x1 = 1
        i = 0
        B[i+(Nx1/2)**2-Nx1/2] = 1 + (P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1)+P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*theta*lam
        for x1 in range(3,Nx1-1,2):
            i += 1
            B[i+(Nx1/2)**2-Nx1/2] = 1 + (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1)+P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1)+P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*theta*lam
        x1 = Nx1-1
        B[i+1+(Nx1/2)**2-Nx1/2] = 1 + (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1)+P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*theta*lam
        
    else: # I - matrix
        '''Bottom side'''
        y1 = 1
        x1 = 1
        i = 0
        B[i] = 1 - (P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1)+P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*(1-theta)*lam
        for x1 in range(3,Nx1-1,2):
            i += 1
            B[i] = 1 - (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1)+P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1)+P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*(1-theta)*lam
        
        x1 = Nx1-1
        B[i+1] = 1 - (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1)+P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*(1-theta)*lam
        
        '''Inside'''
        for j, y1 in enumerate(range(3,Ny1-1,2)):
            x1 = 1
            i = 0
            B[(i+Nx1/2)+j*Nx1/2] = 1 - (P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1) + P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1) + P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*(1-theta)*lam
            for x1 in range(3,Nx1-1,2):
                i += 1
                B[(i+Nx1/2)+j*Nx1/2] = 1 - (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1) + P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1) + P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1) + P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*(1-theta)*lam
            x1 = Nx1-1
            B[(i+1+Nx1/2)+j*Nx1/2] = 1 - (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1) + P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1) + P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*(1-theta)*lam
        '''Up side'''
        y1 = Ny1-1
        x1 = 1
        i = 0
        B[i+(Nx1/2)**2-Nx1/2] = 1 - (P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1)+P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*(1-theta)*lam
        for x1 in range(3,Nx1-1,2):
            i += 1
            B[i+(Nx1/2)**2-Nx1/2] = 1 - (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1)+P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1)+P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*(1-theta)*lam
        x1 = Nx1-1
        B[i+1+(Nx1/2)**2-Nx1/2] = 1 - (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1)+P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*(1-theta)*lam
        
    return B

    
def vector_C(theta = 0, time_step = 0, h2 = 0, ro1 = 0, Nx1 = 0, Ny1 = 0, ccc = 0, fff = 0, left = False, d1 =0, ki1=1, al1=0):
    lam = time_step/h2**2
    
    import numpy
    C = numpy.zeros((Nx1/2)**2-1)
    if left == True: # I + matrix
        ij = 0
        for y1 in range(1,Ny1,2):
            for x1 in range(3,Nx1+2,2):
                if ij > 0 and (ij+1) % (Nx1/2) == 0:
                    pass
                else:
                    C[ij] = (-P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*theta*lam
                ij += 1
          
                
#        '''Bottom side'''
#        y1 = 1
#        for i, x1 in enumerate(range(3,Nx1,2)):
#            C[i] = (-P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
#        '''Inside'''
#        for j, y1 in enumerate(range(3,Ny1-1,2)):
#            for i, x1 in enumerate(range(3,Nx1,2)):
#                C[(i+Nx1/2)+j*Nx1/2] = (-P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
#        '''Up side'''
#        y1 = Ny1-1
#        for i, x1 in enumerate(range(3,Nx1,2)):
#            C[i+(Nx/2)**2-Nx1/2] = (-P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2))*theta*lam
    else: # I - matrix
        ij = 0
        for y1 in range(1,Ny1,2):
            for x1 in range(3,Nx1+2,2):
                if ij > 0 and (ij+1) % (Nx1/2) == 0:
                    pass
                else:
                    C[ij] = (-P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*(1-theta)*lam*(-1)
                ij += 1
               
        
#        '''Bottom side'''
#        y1 = 1
#        for i, x1 in enumerate(range(3,Nx1,2)):
#            C[i] = (-P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2))*theta*lam*(-1)
#        '''Inside'''
#        for j, y1 in enumerate(range(3,Ny1-1,2)):
#            for i, x1 in enumerate(range(3,Nx1,2)):
#                C[(i+Nx1/2)+j*Nx/2] = (-P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2))*theta*lam*(-1)
#        '''Up side'''
#        y1 = Ny1-1
#        for i, x1 in enumerate(range(3,Nx1,2)):
#            C[i+(Nx1/2)**2-Nx1/2] = (-P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2))*theta*lam*(-1)
    C = numpy.insert(C,0,0)
    return C


def vector_D(theta = 0, time_step = 0, h2 = 0, ro1 = 0, Nx1 = 0, Ny1 = 0, ccc = 0, fff = 0, left = False, d1 =0, ki1=1, al1=0):
    lam = time_step/h2**2
    
    import numpy
    D = numpy.zeros(Nx1/2*(Nx1/2-1)) #Nx1/2*(Nx1/2-1)
    if left == True: # I + matrix
        i = 0
        for y1 in range(1,Ny1-1,2):
            for x1 in range(1,Nx1,2):
                D[i] = (-P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*theta*lam
                i += 1
    else: # I - matrix
        i = 0
        for y1 in range(1,Ny1-1,2):
            for x1 in range(1,Nx1,2):
                D[i] = (-P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*(1-theta)*lam*(-1)
                i += 1
    kk = Nx1/2
    D = numpy.append(D, [0]*kk)
    return D

def vector_E(theta = 0, time_step = 0, h2 = 0, ro1 = 0, Nx1 = 0, Ny1 = 0, ccc = 0, fff = 0, left = False, d1 =0, ki1=1, al1=0):
    lam = time_step/h2**2
    
    import numpy
    E = numpy.zeros(Nx1/2*(Nx1/2-1)) #Nx1/2*(Nx1/2-1)
    if left == True: # I + matrix
        i = 0
        for y1 in range(3,Ny1,2):
            for x1 in range(1,Nx1,2):
                E[i] = (-P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*theta*lam
                i += 1
    else: # I - matrix
        i = 0
        for y1 in range(3,Ny1,2):
            for x1 in range(1,Nx1,2):
                E[i] = (-P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1, d = d1, ki = ki1, al = al1))*(1-theta)*lam*(-1)
                i += 1
    kk = Nx1/2
    E = numpy.insert(E, [0]*kk,0)
    return E

## MUST FIX THIS
def continuous_sparse_matrix_1_iter(teta = 0,
                                    n = 0, c = 0, f = 0, m=0, p=0, tp = 0, 
                                    iter = 0, hh = 0, Nx = 0, Ny = 0, 
                                    r_min = 0, r_max = 0,
                                    d_c = 0, nu = 0,
                                    be = 0, ga = 0,
                                    d_m = 0, ki_m = 0, al_m = 0, ro = 0,
                                    a_p = 0, b_p = 0, dl = 0,
                                    Error = 0, init_tip = 0):
    
    
    import numpy
    h3 = 2*hh # asli
    O_x = Nx/2*hh
    O_y = Ny/2*hh
    
    '''Define Initial Profile'''
    if iter == 1:
        c = numpy.zeros((Nx+1,Ny+1))
        f = numpy.zeros((Nx+1,Ny+1))
        m = numpy.zeros((Nx+1,Ny+1))
        p = numpy.zeros((Nx+1,Ny+1))
        
        for y in range(0,Ny+1,2):
            for x in range(0,Nx+1,2):
                r_f = numpy.sqrt((x*hh-O_x)**2 + (y*hh-O_y)**2)
                if r_f >= r_min:
                    #c[x,y] = 0.5-0.45*numpy.exp(-(r_f**2)/0.45)
                    f[x,y] = 0.5
                    #f[x,y] = 0.5-0.45*numpy.exp(-(r_max-r_f)**2/0.45)    
        
        for y in range(1,Ny,2):
            for x in range(1,Nx,2):  
                r_f = numpy.sqrt((x*hh-O_x)**2 + (y*hh-O_y)**2)
                if r_f >= r_min:
                    m[x,y] = 0.1

    c_o = c
    f_o = f
    p_o = p
    m_o = m
    
    fake = numpy.zeros((Nx+1,Ny+1))
       
    from scipy.sparse import dia_matrix
    from scipy.sparse.linalg import spsolve
    '''Creating RHS Sparse Matrix'''
    A_right = vector_A(ccc = p_o, fff = fake, theta = teta, time_step = tp, h2 = h3, ro1 = ro, d1 = d_m, ki1 = ki_m, al1 = al_m, Nx1 = Nx, Ny1 = Ny)
    B_right = vector_B(ccc = p_o, fff = fake, theta = teta, time_step = tp, h2 = h3, ro1 = ro, d1 = d_m, ki1 = ki_m, al1 = al_m, Nx1 = Nx, Ny1 = Ny)
    C_right = vector_C(ccc = p_o, fff = fake, theta = teta, time_step = tp, h2 = h3, ro1 = ro, d1 = d_m, ki1 = ki_m, al1 = al_m, Nx1 = Nx, Ny1 = Ny)
    D_right = vector_D(ccc = p_o, fff = fake, theta = teta, time_step = tp, h2 = h3, ro1 = ro, d1 = d_m, ki1 = ki_m, al1 = al_m, Nx1 = Nx, Ny1 = Ny)
    E_right = vector_E(ccc = p_o, fff = fake, theta = teta, time_step = tp, h2 = h3, ro1 = ro, d1 = d_m, ki1 = ki_m, al1 = al_m, Nx1 = Nx, Ny1 = Ny)
    data = numpy.array([D_right, A_right, B_right, C_right, E_right])
    i = Nx/2
    ii = (Nx/2)**2
    diags = numpy.array([-i,-1, 0, 1, i])
      
    '''RHS Multiply n and store as Q'''
    Q = numpy.zeros((Nx/2)**2)
    for i,j in enumerate(range(1,Nx,2)): #untuk paling awal
        if j == 1: 
            Q[i] = B_right[i]*m[1,1] + C_right[i+1]*m[3,1] + E_right[i+Nx/2]*m[1,3] #B & C , E
        elif j == Nx-1: 
            Q[i] = A_right[i-1]*m[j-2,1] + B_right[i]*m[j,1] + E_right[i+Nx/2]*m[j,3]#A & B, E
        else:
            Q[i] = A_right[i-1]*m[j-2,1] + B_right[i]*m[j,1] + C_right[i+1]*m[j+2,1] + E_right[i+Nx/2]*m[j,3]#A & B & C, E
            
    i = Nx/2       
    for k,l in enumerate(range(3,Nx-2,2)): 
        for j in range(1,Nx,2): #untuk tengah #Nx/2 , (Nx/2)**2-Nx/2
            if j == 1:
                Q[i] = D_right[i-(Nx/2)]*m[j,l-2] + B_right[i]*m[j,l] + C_right[i+1]*m[j+2,l] + E_right[i+Nx/2]*m[j,l+2] #D, B & C, E
            elif j == Nx-1:
                Q[i] = D_right[i-(Nx/2)]*m[j,l-2] + A_right[i-1]*m[j-2,l] + B_right[i]*m[j,l] + E_right[i+Nx/2]*m[j,l+2] #D, A & B, E
            else:
                Q[i] = D_right[i-(Nx/2)]*m[j,l-2] + A_right[i-1]*m[j-2,l] + B_right[i]*m[j,l] + C_right[i+1]*m[j+2,l] + E_right[i+Nx/2]*m[j,l+2] #D, A & B & C, E
            i +=1
     
    for i,j in enumerate(range(1,Nx,2)): #untuk terakhir #(Nx/2)**2-Nx/2 , (Nx/2)**2
        i += (Nx/2)**2-Nx/2
        if j == 1:
            Q[i] = D_right[i-(Nx/2)]*m[1,Nx-3] + B_right[i]*m[1,Nx-1] + C_right[i+1]*m[3,Nx-1] #D, B & C
        elif j == Nx-1:
            Q[i] = D_right[i-(Nx/2)]*m[j,Nx-3] + A_right[i-1]*m[j-2,Nx-1] + B_right[i]*m[j,Nx-1] #D, A & B
        else:
            Q[i] = D_right[i-(Nx/2)]*m[j,Nx-3] + A_right[i-1]*m[j-2,Nx-1] + B_right[i]*m[j,Nx-1] + C_right[i+1]*m[j+2,Nx-1] #D, A & B & C
    del A_right
    del B_right
    del C_right
    del D_right
    del E_right
   
    '''Creating LHS Sparse Matrix'''
    data = numpy.array([vector_D(ccc = p_o, fff = fake, theta = teta, left = True, time_step = tp, h2 = h3, ro1 = ro, d1 = d_m, ki1 = ki_m, al1 = al_m, Nx1 = Nx, Ny1 = Ny), vector_A(ccc = p_o, fff = fake, theta = teta, left = True, time_step = tp, h2 = h3, ro1 = ro, d1 = d_m, ki1 = ki_m, al1 = al_m, Nx1 = Nx, Ny1 = Ny), vector_B(ccc = p_o, fff = fake, theta = teta, left = True, time_step = tp, h2 = h3, ro1 = ro, d1 = d_m, ki1 = ki_m, al1 = al_m, Nx1 = Nx, Ny1 = Ny), vector_C(ccc = p_o, fff = fake, theta = teta, left = True, time_step = tp, h2 = h3, ro1 = ro, d1 = d_m, ki1 = ki_m, al1 = al_m, Nx1 = Nx, Ny1 = Ny), vector_E(ccc = p_o, fff = fake, theta = teta, left = True, time_step = tp, h2 = h3, ro1 = ro, d1 = d_m, ki1 = ki_m, al1 = al_m, Nx1 = Nx, Ny1 = Ny)])
    LHS = dia_matrix((data, diags), shape=(ii, ii))
 
    '''Solve LHS n = V'''
#    from numpy.linalg import solve
    m_sol = spsolve(LHS.tocsr(), Q)
    del LHS
    del Q
    del data
    del diags
    
    '''Solve c, f, p at sub lattice'''
    
    for y in range(0,Ny+1,2):
        for x in range(0,Nx+1,2):
            r_f = (x*hh-O_x)**2 + (y*hh-O_y)**2
            if r_f <= (r_min**2 + Error + hh):
                if x >= init_tip[2][0] and y >= init_tip[0][1]: #area 1
                    if n[x+1,y+1] == 1 or n[x-1,y+1] == 1 or n[x+1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool) + d_c*tp/h3**2*(c_o[x+2,y]+c_o[x,y+2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
                    p[x,y] = (a_p*1/3*(m_o[x-1,y+1]+m_o[x+1,y+1]+m_o[x+1,y-1])+b_p)*n_bool - p_o[x,y]*(1-dl) #Ang1
                    #p[x,y] = 1/(a_p*1/3*(m_o[x-1,y+1]+m_o[x+1,y+1]+m_o[x+1,y-1])+b_p) #Ang2

                elif x < init_tip[2][0] and y > init_tip[0][1]: #area 2
                    if n[x-1,y+1] == 1 or n[x+1,y+1] == 1 or n[x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x-2,y]+c_o[x,y+2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
                    p[x,y] = (a_p*1/3*(m_o[x-1,y+1]+m_o[x+1,y+1]+m_o[x+1,y-1])+b_p)*n_bool - p_o[x,y]*(1-dl) #Ang1
                    #p[x,y] = 1/(a_p*1/3*(m_o[x-1,y+1]+m_o[x+1,y+1]+m_o[x+1,y-1])+b_p) #Ang2
                    
                elif x <= init_tip[2][0] and y <= init_tip[0][1]: #area 3
                    if n[x+1,y-1] == 1 or n[x-1,y+1] == 1 or n[x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x-2,y]+c_o[x,y-2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
                    p[x,y] = (a_p*1/3*(m_o[x-1,y+1]+m_o[x+1,y+1]+m_o[x+1,y-1])+b_p)*n_bool - p_o[x,y]*(1-dl) #Ang1
                    #p[x,y] = 1/(a_p*1/3*(m_o[x-1,y+1]+m_o[x+1,y+1]+m_o[x+1,y-1])+b_p) #Ang2
                        
                elif x > init_tip[2][0] and y < init_tip[0][1]: #area 4
                    if n[x+1,y+1] == 1 or n[x-1,y-1] == 1 or n[x+1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x+2,y]+c_o[x,y-2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
                    p[x,y] = (a_p*1/3*(m_o[x-1,y+1]+m_o[x+1,y+1]+m_o[x+1,y-1])+b_p)*n_bool - p_o[x,y]*(1-dl) #Ang1
                    #p[x,y] = 1/(a_p*1/3*(m_o[x-1,y+1]+m_o[x+1,y+1]+m_o[x+1,y-1])+b_p) #Ang2
            
            elif y == 0:
                if x == 0:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n[1,1])+ d_c*tp/h3**2*(c_o[x+2,y]+c_o[x,y+2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n[1,1] - tp*ga*f_o[x,y]*n[1,1]
                    p[x,y] = (a_p*m_o[1,1]+b_p)*n[1,1] - p_o[x,y]*(1-dl) #Ang1
                    #p[x,y] = 1/(a_p*1/3*(m_o[x-1,y+1]+m_o[x+1,y+1]+m_o[x+1,y-1])+b_p) #Ang2
                    
                elif x == Nx:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n[Nx-1,1])+ d_c*tp/h3**2*(c_o[x-2,y]+c_o[x,y+2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n[Nx-1,1] - tp*ga*f_o[x,y]*n[Nx-1,1]
                    p[x,y] = (a_p*m_o[Nx-1,1]+b_p)*n[Nx-1,1] - p_o[x,y]*(1-dl) #Ang1
                    #p[x,y] = 1/(a_p*1/3*(m_o[x-1,y+1]+m_o[x+1,y+1]+m_o[x+1,y-1])+b_p) #Ang2
                else:
                    if n[x+1,1] == 1 or n[x-1,1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]-3*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
                    p[x,y] = (a_p*1/2*(m_o[x+1,1]+m_o[x-1,1])+b_p)*n_bool - p_o[x,y]*(1-dl) #Ang1
                    #p[x,y] = 1/(a_p*1/3*(m_o[x-1,y+1]+m_o[x+1,y+1]+m_o[x+1,y-1])+b_p) #Ang2
            elif y == Ny:
                if x == 0:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n[1,Ny-1])+ d_c*tp/h3**2*(c_o[x+2,y]+c_o[x,y-2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n[1,Ny-1]
                    p[x,y] = (a_p*m_o[1,Ny-1]+b_p)*n_bool - p_o[x,y]*(1-dl) #Ang1
                    #p[x,y] = 1/(a_p*1/3*(m_o[x-1,y+1]+m_o[x+1,y+1]+m_o[x+1,y-1])+b_p) #Ang2
                elif x == Nx:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n[Nx-1,Ny-1])+ d_c*tp/h3**2*(c_o[x-2,y]+c_o[x,y-2]-2*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n[Nx-1,Ny-1]
                    p[x,y] = (a_p*m_o[Nx-1,Ny-1]+b_p)*n_bool - p_o[x,y]*(1-dl) #Ang1
                    #p[x,y] = 1/(a_p*1/3*(m_o[x-1,y+1]+m_o[x+1,y+1]+m_o[x+1,y-1])+b_p) #Ang2
                else:
                    if n[x+1,Ny-1] == 1 or n[x-1,Ny-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y-2]-3*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
                    p[x,y] = (a_p*1/2*(m_o[x+1,Ny-1]+m_o[x-1,Ny-1])+b_p)*n_bool - p_o[x,y]*(1-dl) #Ang1
                    #p[x,y] = 1/(a_p*1/3*(m_o[x-1,y+1]+m_o[x+1,y+1]+m_o[x+1,y-1])+b_p) #Ang2
            else:
                if x == 0:
                    if n[x+1,y+1] == 1 or n[x+1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x+2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
                    p[x,y] = (a_p*1/2*(m_o[x+1,y+1]+m_o[x+1,y-1])+b_p)*n_bool - p_o[x,y]*(1-dl) #Ang1
                    #p[x,y] = 1/(a_p*1/3*(m_o[x-1,y+1]+m_o[x+1,y+1]+m_o[x+1,y-1])+b_p) #Ang2
                elif x == Nx:
                    if n[x-1,y+1] == 1 or n[x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-3*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
                    p[x,y] = (a_p*1/2*(m_o[x-1,y+1]+m_o[x-1,y-1])+b_p)*n_bool - p_o[x,y]*(1-dl) #Ang1
                    #p[x,y] = 1/(a_p*1/3*(m_o[x-1,y+1]+m_o[x+1,y+1]+m_o[x+1,y-1])+b_p) #Ang2
                else:
                    if n[x+1,y+1] == 1 or n[x-1,y+1] == 1 or n[x+1,y-1] == 1 or n[x-1,y-1] == 1:
                        n_bool = 1
                    else:
                        n_bool = 0
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_bool)+ d_c*tp/h3**2*(c_o[x+2,y]+c_o[x-2,y]+c_o[x,y+2]+c_o[x,y-2]-4*c_o[x,y])
                    f[x,y] = f_o[x,y] + tp*be*n_bool - tp*ga*f_o[x,y]*n_bool
                    p[x,y] = (a_p*1/4*(m_o[x-1,y+1]+m_o[x+1,y+1]+m_o[x+1,y-1]+m_o[x-1,y-1])+b_p)*n_bool - p_o[x,y]*(1-dl) #Ang1
                    #p[x,y] = 1/(a_p*1/3*(m_o[x-1,y+1]+m_o[x+1,y+1]+m_o[x+1,y-1])+b_p) #Ang2
            
    
    '''Storing new n solution into n[x,y]'''  
    i = 0
    for y in range(1,Ny,2):
        for x in range(1,Nx,2):
            r_f = numpy.sqrt((x*hh-O_x)**2 + (y*hh-O_y)**2)
            if r_f >= r_min:
                m[x,y] = m_sol[i]
            else:
                m[x,y] = 0
            i +=1 
         
    rr = [c, f, m, p, tp]
    for value in c:
        if value.all < 0:
            print 'Ada VEGF yang negative'
            quit()
    for value in f:
        if value.all < 0:
            print 'Ada Fibronectin yang negative'
            quit()
    for value in m_sol:
        if value.all < 0:
            print 'Ada Mural yang negative'
            quit()
    for value in p:
        if value.all < 0:
            print 'Ada Tie yang negative'
            quit()
    return rr
# continuous_sparse_matrix_1_iter(iter=1)
