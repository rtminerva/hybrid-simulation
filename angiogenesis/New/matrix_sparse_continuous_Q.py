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

def P1_code(h1 = 0.005,d = 0.00035, ki = 0.38, al = 0.6, ro2 = 0, c1 = 0, x = 0, y = 0, f1 = 0):
    r = d + h1*ki/(1+al*c1[x-1,y+1])*max(-vx_code(x_p = x, y_p = y, cc = c1), 0) + h1*ro2*max(-wx_code(x_p = x, y_p = y, ff = f1), 0)
    return r

def P2_code(h1 = 0.005,d = 0.00035, ki = 0.38, al = 0.6, ro2 = 0, c1 = 0, x = 0, y = 0, f1 = 0):
    r = d + h1*ki/(1+al*c1[x+1,y+1])*max(vx_code(x_p = x, y_p = y, cc = c1), 0) + h1*ro2*max(wx_code(x_p = x, y_p = y, ff = f1), 0)
    return r

def P3_code(h1 = 0.005,d = 0.00035, ki = 0.38, al = 0.6, ro2 = 0, c1 = 0, x = 0, y = 0, f1 = 0):
    r = d + h1*ki/(1+al*c1[x+1,y-1])*max(-vy_code(x_p = x, y_p = y, cc = c1), 0) + h1*ro2*max(-wy_code(x_p = x, y_p = y, ff = f1), 0)
    return r

def P4_code(h1 = 0.005,d = 0.00035, ki = 0.38, al = 0.6, ro2 = 0, c1 = 0, x = 0, y = 0, f1 = 0): #at main lattice
    r = d + h1*ki/(1+al*c1[x+1,y+1])*max(vy_code(x_p = x, y_p = y, cc = c1), 0) + h1*ro2*max(wy_code(x_p = x, y_p = y, ff = f1), 0)
    return r


def vector_A(theta = 0.5, time_step = 0.1, h2 = 0.005, ro1 = 0, X = 1, Y = 1, ccc = 0, fff = 0, left = False):
    lam = time_step/h2**2
    hh = h2/2
    Nx = int(X/hh)
    Ny = int(Y/hh)
    import numpy
    A = numpy.zeros((Nx/2)**2-1)
    if left: # I + matrix
        '''Bottom side'''
        y1 = 1
        for i, x1 in enumerate(range(1,Nx-1,2)):
            A[i] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*theta*lam
        '''Inside'''
        for j, y1 in enumerate(range(3,Ny-1,2)):
            for i, x1 in enumerate(range(1,Nx-1,2)):
                A[(i+Nx/2)+j*Nx/2] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*theta*lam
        '''Up side'''
        y1 = Ny-1
        for i, x1 in enumerate(range(1,Nx-1,2)):
            A[i+(Nx/2)**2-Nx/2] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*theta*lam
    else: # I - matrix
        '''Bottom side'''
        y1 = 1
        for i, x1 in enumerate(range(1,Nx-1,2)):
            A[i] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*theta*lam*(-1)
        '''Inside'''
        for j, y1 in enumerate(range(3,Ny-1,2)):
            for i, x1 in enumerate(range(1,Nx-1,2)):
                A[(i+Nx/2)+j*Nx/2] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*theta*lam*(-1)
        '''Up side'''
        y1 = Ny-1
        for i, x1 in enumerate(range(1,Nx-1,2)):
            A[i+(Nx/2)**2-Nx/2] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*theta*lam*(-1)
    A = numpy.append(A, 0)
    return A


def vector_B(theta = 0.5, time_step = 0.1, h2 = 0.005, ro1 = 0, X = 1, Y = 1, ccc = 0, fff = 0, left = False):
    lam = time_step/h2**2
    hh = h2/2
    Nx = int(X/hh)
    Ny = int(Y/hh)
    import numpy
    B = numpy.zeros((Nx/2)**2)
    if left: # I + matrix
        '''Bottom side'''
        y1 = 1
        x1 = 1
        i = 0
        B[i] = 1 + (P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1)+P4_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*theta*lam
        for x1 in range(3,Nx-1,2):
            i += 1
            B[i] = 1 + (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1)+P2_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1)+P4_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*theta*lam
        
        x1 = Nx-1
        B[i+1] = 1 + (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1)+P4_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*theta*lam
        
        '''Inside'''
        for j, y1 in enumerate(range(3,Ny-1,2)):
            x1 = 1
            i = 0
            B[(i+Nx/2)+j*Nx/2] = 1 + (P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1) + P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1) + P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*theta*lam
            for x1 in range(3,Nx-1,2):
                i += 1
                B[(i+Nx/2)+j*Nx/2] = 1 + (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1) + P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1) + P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1) + P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*theta*lam
            x1 = Nx-1
            B[(i+1+Nx/2)+j*Nx/2] = 1 + (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1) + P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1) + P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*theta*lam
        '''Up side'''
        y1 = Ny-1
        x1 = 1
        i = 0
        B[i+(Nx/2)**2-Nx/2] = 1 + (P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1)+P3_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*theta*lam
        for x1 in range(3,Nx-1,2):
            i += 1
            B[i+(Nx/2)**2-Nx/2] = 1 + (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1)+P2_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1)+P3_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*theta*lam
        x1 = Nx-1
        B[i+1+(Nx/2)**2-Nx/2] = 1 + (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1)+P3_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*theta*lam
        
    else: # I - matrix
        '''Bottom side'''
        y1 = 1
        x1 = 1
        i = 0
        B[i] = 1 - (P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1)+P4_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*(1-theta)*lam
        for x1 in range(3,Nx-1,2):
            i += 1
            B[i] = 1 - (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1)+P2_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1)+P4_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*(1-theta)*lam
        
        x1 = Nx-1
        B[i+1] = 1 - (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1)+P4_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*(1-theta)*lam
        
        '''Inside'''
        for j, y1 in enumerate(range(3,Ny-1,2)):
            x1 = 1
            i = 0
            B[(i+Nx/2)+j*Nx/2] = 1 - (P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1) + P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1) + P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*(1-theta)*lam
            for x1 in range(3,Nx-1,2):
                i += 1
                B[(i+Nx/2)+j*Nx/2] = 1 - (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1) + P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1) + P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1) + P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*(1-theta)*lam
            x1 = Nx-1
            B[(i+1+Nx/2)+j*Nx/2] = 1 - (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1) + P3_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1) + P4_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*(1-theta)*lam
        '''Up side'''
        y1 = Ny-1
        x1 = 1
        i = 0
        B[i+(Nx/2)**2-Nx/2] = 1 - (P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1)+P3_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*(1-theta)*lam
        for x1 in range(3,Nx-1,2):
            i += 1
            B[i+(Nx/2)**2-Nx/2] = 1 - (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1)+P2_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1)+P3_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*(1-theta)*lam
        x1 = Nx-1
        B[i+1+(Nx/2)**2-Nx/2] = 1 - (P1_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1)+P3_code(x = x1, y = j, c1 = ccc, f1 = fff, h1 = h2, ro2 = ro1))*(1-theta)*lam
        
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
                                    n = 0, c = 0, f = 0):
    
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
#         viu = (m.sqrt(5)-0.1)/(m.sqrt(5)-1)
        for y in range(0,Ny+1,2):
            for x in range(0,Nx+1,2):
                c[x,y] = m.exp(-(1-x*hh)**2/e)
#                 r_c = m.sqrt((x*hh-1)**2+(y*hh-0.5)**2)
#                 if r_c > 0.1:
#                     c[x,y] = (viu-r_c)**2/(viu-0.1)
#                 else:
#                     c[x,y] = 1
                f[x,y] = 0.75*m.exp(-(x*hh)**2/e)
        for y in range(1,Ny,2):
            for x in range(1,Nx,2):
#                 n[x,y] = m.exp(-(x*hh)**2/0.001)*(m.sin(number_of_tip*m.pi*y*hh))**2
                n[x,y] = m.exp(-(x*hh)**2/0.01)*(m.sin(number_of_tip*m.pi*y*hh))**2      
        
#         '''Plot C & N profile'''
#         import matplotlib.pyplot as plt 
#         from matplotlib import cm
#         from matplotlib.ticker import LinearLocator, FormatStrFormatter
#         from mpl_toolkits.mplot3d import Axes3D
#         fig0 = plt.figure(0)
#         ax = fig0.gca(projection='3d')
#         ax.set_zlim(-0.1, 1)
#         ax.zaxis.set_major_locator(LinearLocator(10))
#         ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# #         x_main_axis = numpy.arange(hh, X, h3)
# #         y_main_axis = numpy.arange(hh, Y, h3)
# #         x_main_axis, y_main_axis = numpy.meshgrid(x_main_axis, y_main_axis)
#         x_sub_axis = numpy.arange(0, X+hh, h3)
#         y_sub_axis = numpy.arange(0, Y+hh, h3)
#         x_sub_axis, y_sub_axis = numpy.meshgrid(x_sub_axis, y_sub_axis)
#         c_sol = numpy.zeros((Nx/2+1, Ny/2+1))
# #         n_sol = numpy.zeros((Nx/2, Ny/2))
#         for j, y in enumerate(range(0,Ny+1,2)):
#             for i, x in enumerate(range(0,Nx+1,2)):
#                 c_sol[i,j] = c[x,y]
# #                 n_sol[i,j] = n[x,y]
#         surf = ax.plot_surface(x_sub_axis, y_sub_axis, c_sol, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
# #         surf = ax.plot_surface(x_main_axis, y_main_axis, n_sol, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
#         fig0.show()
#         '''Plot C & N profile'''
        
    c_o = c
    f_o = f   
    from scipy.sparse import dia_matrix
    from scipy.sparse.linalg import spsolve
    '''Creating RHS Sparse Matrix'''
    data = numpy.array([vector_D(ccc = c_o, fff = f_o, theta = 1-teta, time_step = tp, h2 = h3), vector_A(ccc = c_o, fff = f_o, theta = 1-teta, time_step = tp, h2 = h3), vector_B(ccc = c_o, fff = f_o, theta = 1-teta, time_step = tp, h2 = h3), vector_C(ccc = c_o, fff = f_o, theta = 1-teta, time_step = tp, h2 = h3), vector_E(ccc = c_o, fff = f_o, theta = 1-teta, time_step = tp, h2 = h3)])
#     print len(data[0]), len(data[1]), len(data[2]), len(data[3]), len(data[4])
    i = Nx/2
    ii = (Nx/2)**2
    diags = numpy.array([-i,-1, 0, 1, i])
    RHS = dia_matrix((data, diags), shape=(ii, ii))
      
    '''RHS Multiply n and store as Q'''
    A_right = vector_A(ccc = c_o, fff = f_o, theta = 1-teta, time_step = tp, h2 = h3)
    B_right = vector_B(ccc = c_o, fff = f_o, theta = 1-teta, time_step = tp, h2 = h3)
    C_right = vector_C(ccc = c_o, fff = f_o, theta = 1-teta, time_step = tp, h2 = h3)
    D_right = vector_D(ccc = c_o, fff = f_o, theta = 1-teta, time_step = tp, h2 = h3)
    E_right = vector_E(ccc = c_o, fff = f_o, theta = 1-teta, time_step = tp, h2 = h3)
    
    Q = numpy.zeros((Nx/2)**2)
    for i,j in enumerate(range(1,Nx,2)): #untuk paling awal
        if j == 1: 
            Q[i] = B_right[i]*n[1,1] + C_right[i]*n[3,1] + E_right[i]*n[1,3] #B & C , E
        elif j == Nx-1: 
            Q[i] = A_right[i-1]*n[j-2,1] + B_right[i]*n[j,1] + E_right[i]*n[j,3]#A & B, E
        else:
            Q[i] = A_right[i-1]*n[j-2,1] + B_right[i]*n[j,1] + C_right[i]*n[j+2,1] + E_right[i]*n[j,3]#A & B & C, E
            
    i = Nx/2       
    for k,l in enumerate(range(3,Nx-2,2)): 
        for j in range(1,Nx,2): #untuk tengah #Nx/2 , (Nx/2)**2-Nx/2
            if j == 1:
                Q[i] = D_right[i-(Nx/2)]*n[j,l-2] + B_right[i]*n[j,l] + C_right[i]*n[j+2,l] + E_right[i]*n[j,l+2] #D, B & C, E
            elif j == Nx-1:
                Q[i] = D_right[i-(Nx/2)]*n[j,l-2] + A_right[i-1]*n[j-2,l] + B_right[i]*n[j,l] + E_right[i]*n[j,l+2] #D, A & B, E
            else:
                Q[i] = D_right[i-(Nx/2)]*n[j,l-2] + A_right[i-1]*n[j-2,l] + B_right[i]*n[j,l] + C_right[i]*n[j+2,l] + E_right[i]*n[j,l+2] #D, A & B & C, E
            i +=1
     
    for i,j in enumerate(range(1,Nx,2)): #untuk terakhir #(Nx/2)**2-Nx/2 , (Nx/2)**2
        i += (Nx/2)**2-Nx/2
        if j == 1:
            Q[i] = D_right[i-(Nx/2)]*n[1,Nx-3] + B_right[i]*n[1,Nx-1] + C_right[i]*n[3,Nx-1] #D, B & C
        elif j == Nx-1:
            Q[i] = D_right[i-(Nx/2)]*n[j,Nx-3] + A_right[i-1]*n[j-2,Nx-1] + B_right[i]*n[j,Nx-1] #D, A & B
        else:
            Q[i] = D_right[i-(Nx/2)]*n[j,Nx-3] + A_right[i-1]*n[j-2,Nx-1] + B_right[i]*n[j,Nx-1] + C_right[i]*n[j+2,Nx-1] #D, A & B & C
    del A_right
    del B_right
    del C_right
    del D_right
    del E_right
    
    
    
    '''Creating LHS Sparse Matrix'''
    data = numpy.array([vector_D(ccc = c_o, fff = f_o, theta = teta, left = True, time_step = tp, h2 = h3), vector_A(ccc = c_o, fff = f_o, theta = teta, left = True, time_step = tp, h2 = h3), vector_B(ccc = c_o, fff = f_o, theta = teta, left = True, time_step = tp, h2 = h3), vector_C(ccc = c_o, fff = f_o, theta = teta, left = True, time_step = tp, h2 = h3), vector_E(ccc = c_o, fff = f_o, theta = teta, left = True, time_step = tp, h2 = h3)])
    LHS = dia_matrix((data, diags), shape=(ii, ii))
    
    '''Solve LHS n = V'''
    n_sol = spsolve(LHS.tocsr(), Q)
    del RHS
    del LHS
    del Q
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
    
    i = 0
    for y in range(1,Ny,2):
        for x in range(1,Nx,2):
            n[x,y] = n_sol[i] 
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
    tau1 = min(h3/(4*teta*(ki*max(v1)/(1+al*c.max())+ro*max(w1))),h3**2/(4*(1-teta)*(d+h3*ki*max(v2)/(1+al*c_o.max())+h3*ro*max(w2))),1/(nu*n.max()),1/(ga*n.max()))
    tp = tau1
    del v1
    del v2
    del w1
    del w2
    del tau1
         
    rr = [n,c,f,tp]#A,B,C,
    for value in c:
        if value.all < 0:
            print 'Ada C yang negative'
            quit()
    for value in f:
        if value.all < 0:
            print 'Ada F yang negative'
            quit()
    for value in n_sol:
        if value.all < 0:
            print 'Ada N yang negative'
            quit()
    return rr
# continuous_sparse_matrix_1_iter(iter=1)
