from scipy.sparse import dia_matrix
from scipy.sparse.linalg import spsolve
import numpy

def vx_code(x_p = 0, y_p = 0, set, sol): #at main lattice
    r = 0.5/set['h']*(sol['c'][x_p+1,y_p+1]-sol['c'][x_p-1,y_p+1]+sol['c'][x_p+1,y_p-1]-sol['c'][x_p-1,y_p-1])
    return r
    
def vy_code(x_p = 0, y_p = 0, set, sol): #at main lattice
    r = 0.5/set['h']*(sol['c'][x_p+1,y_p+1]+sol['c'][x_p-1,y_p+1]-sol['c'][x_p+1,y_p-1]-sol['c'][x_p-1,y_p-1])
    return r
    
def wx_code(x_p = 0, y_p = 0, set, sol): #at main lattice
    r = 0.5/set['h']*(sol['f'][x_p+1,y_p+1]-sol['f'][x_p-1,y_p+1]+sol['f'][x_p+1,y_p-1]-sol['f'][x_p-1,y_p-1])
    return r

def wy_code(x_p = 0, y_p = 0, set, sol): #at main lattice
    r = 0.5/set['h']*(sol['f'][x_p+1,y_p+1]+sol['f'][x_p-1,y_p+1]-sol['f'][x_p+1,y_p-1]-sol['f'][x_p-1,y_p-1])
    return r

def P1_code(x = 0, y = 0, coef, set, sol):
    r = coef['D_n'] + set['h']*coef['Ki_n']/(1+coef['Al_n']*1/4*(sol['c'][x-1,y+1]+sol['c'][x+1,y+1]+sol['c'][x-1,y-1]+sol['c'][x+1,y-1]))*max(-vx_code(x_p = x, y_p = y, set, sol), 0) + set['h']*coef['Ro']*max(-wx_code(x_p = x, y_p = y, set, sol), 0)
    return r

def P2_code(x = 0, y = 0, coef, set, sol):
    r = coef['D_n'] + set['h']*coef['Ki_n']/(1+coef['Al_n']*1/4*(sol['c'][x-1,y+1]+sol['c'][x+1,y+1]+sol['c'][x-1,y-1]+sol['c'][x+1,y-1]))*max(vx_code(x_p = x, y_p = y, set, sol), 0) + set['h']*coef['Ro']*max(wx_code(x_p = x, y_p = y, set, sol), 0)
    return r

def P3_code(x = 0, y = 0, coef, set, sol):
    r = coef['D_n'] + set['h']*coef['Ki_n']/(1+coef['Al_n']*1/4*(sol['c'][x-1,y+1]+sol['c'][x+1,y+1]+sol['c'][x-1,y-1]+sol['c'][x+1,y-1]))*max(-vy_code(x_p = x, y_p = y, set, sol), 0) + set['h']*coef['Ro']*max(-wy_code(x_p = x, y_p = y, set, sol), 0)
    return r

def P4_code(x = 0, y = 0, coef, set, sol): #at main lattice
    r = coef['D_n'] + set['h']*coef['Ki_n']/(1+coef['Al_n']*1/4*(sol['c'][x-1,y+1]+sol['c'][x+1,y+1]+sol['c'][x-1,y-1]+sol['c'][x+1,y-1]))*max(vy_code(x_p = x, y_p = y, set, sol), 0) + set['h']*coef['Ro']*max(wy_code(x_p = x, y_p = y, set, sol), 0)
    return r


def vector_A(coef, set, sol, left = False):
    lam = set['dt']/set['h']**2
    
    import numpy
  
    A = numpy.zeros((set['Nx']/2)**2-1)
    
    if left == True: # I + matrix
        ij = 0
        for y1 in range(1,set['Ny'],2):
            for x1 in range(1,set['Nx'],2):
                if ij > 0 and (ij+1) % (set['Nx']/2) == 0:
                    pass
                else:
                    A[ij] = (-P2_code(x = x1, y = y1, coef, set, sol))*set['theta']*lam
                ij += 1
            
#        '''Bottom side'''
#        y1 = 1
#        for i, x1 in enumerate(range(1,set['Nx']-1,2)):
#            A[i] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = set['h'], ro2 = ro1))*set['theta']*lam
#        '''Inside'''
#        for j, y1 in enumerate(range(3,set['Ny']-1,2)):
#            for i, x1 in enumerate(range(1,set['Nx']-1,2)):
#                A[(i+set['Nx']/2)+j*set['Nx']/2] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = set['h'], ro2 = ro1))*set['theta']*lam
#        '''Up side'''
#        y1 = set['Ny']-1
#        for i, x1 in enumerate(range(1,set['Nx']-1,2)):
#            A[i+(set['Nx']/2)**2-Nx/2] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = set['h'], ro2 = ro1))*set['theta']*lam
    else: # I - matrix
        ij = 0
        for y1 in range(1,set['Ny'],2):
            for x1 in range(1,set['Nx'],2):
                if ij > 0 and (ij+1) % (set['Nx']/2) == 0:
                    pass
                else:
                    A[ij] = (-P2_code(x = x1, y = y1, coef, set, sol))*(1-set['theta'])*lam*(-1)
                ij += 1
        
#        '''Bottom side'''
#        y1 = 1
#        for i, x1 in enumerate(range(1,set['Nx']-1,2)):
#            A[i] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = set['h'], ro2 = ro1))*(set['theta']-1)*lam*(-1)
#        '''Inside'''
#        for j, y1 in enumerate(range(3,set['Ny']-1,2)):
#            for i, x1 in enumerate(range(1,set['Nx']-1,2)):
#                A[(i+set['Nx']/2)+j*set['Nx']/2] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = set['h'], ro2 = ro1))*(set['theta']-1)*lam*(-1)
#        '''Up side'''
#        y1 = set['Ny']-1
#        for i, x1 in enumerate(range(1,set['Nx']-1,2)):
#            A[i+(Nx/2)**2-set['Nx']/2] = (-P2_code(x = x1, y = y1, c1 = ccc, f1 = fff, h1 = set['h'], ro2 = ro1))*(set['theta']-1)*lam*(-1)
    A = numpy.append(A, 0)
    return A


def vector_B(coef, set, sol, left = False):
    lam = set['dt']/set['h']**2
    
    import numpy
    B = numpy.zeros((set['Nx']/2)**2)
    if left == True: # I + matrix
        '''Bottom side'''
        y1 = 1
        x1 = 1
        i = 0
        B[i] = 1 + (P2_code(x = x1, y = y1, coef, set, sol)+P4_code(x = x1, y = y1, coef, set, sol))*set['theta']*lam
        for x1 in range(3,set['Nx']-1,2):
            i += 1
            B[i] = 1 + (P1_code(x = x1, y = y1, coef, set, sol)+P2_code(x = x1, y = y1, coef, set, sol)+P4_code(x = x1, y = y1, coef, set, sol))*set['theta']*lam
        
        x1 = set['Nx']-1
        B[i+1] = 1 + (P1_code(x = x1, y = y1, coef, set, sol)+P4_code(x = x1, y = y1, coef, set, sol))*set['theta']*lam
        
        '''Inside'''
        for j, y1 in enumerate(range(3,set['Ny']-1,2)):
            x1 = 1
            i = 0
            B[(i+set['Nx']/2)+j*set['Nx']/2] = 1 + (P2_code(x = x1, y = y1, coef, set, sol) + P3_code(x = x1, y = y1, coef, set, sol) + P4_code(x = x1, y = y1, coef, set, sol))*set['theta']*lam
            for x1 in range(3,set['Nx']-1,2):
                i += 1
                B[(i+set['Nx']/2)+j*set['Nx']/2] = 1 + (P1_code(x = x1, y = y1, coef, set, sol) + P2_code(x = x1, y = y1, coef, set, sol) + P3_code(x = x1, y = y1, coef, set, sol) + P4_code(x = x1, y = y1, coef, set, sol))*set['theta']*lam
            x1 = set['Nx']-1
            B[(i+1+set['Nx']/2)+j*set['Nx']/2] = 1 + (P1_code(x = x1, y = y1, coef, set, sol) + P3_code(x = x1, y = y1, coef, set, sol) + P4_code(x = x1, y = y1, coef, set, sol))*set['theta']*lam
        '''Up side'''
        y1 = set['Ny']-1
        x1 = 1
        i = 0
        B[i+(set['Nx']/2)**2-set['Nx']/2] = 1 + (P2_code(x = x1, y = y1, coef, set, sol)+P3_code(x = x1, y = y1, coef, set, sol))*set['theta']*lam
        for x1 in range(3,set['Nx']-1,2):
            i += 1
            B[i+(set['Nx']/2)**2-set['Nx']/2] = 1 + (P1_code(x = x1, y = y1, coef, set, sol)+P2_code(x = x1, y = y1, coef, set, sol)+P3_code(x = x1, y = y1, coef, set, sol))*set['theta']*lam
        x1 = set['Nx']-1
        B[i+1+(set['Nx']/2)**2-set['Nx']/2] = 1 + (P1_code(x = x1, y = y1, coef, set, sol)+P3_code(x = x1, y = y1, coef, set, sol))*set['theta']*lam
        
    else: # I - matrix
        '''Bottom side'''
        y1 = 1
        x1 = 1
        i = 0
        B[i] = 1 - (P2_code(x = x1, y = y1, coef, set, sol)+P4_code(x = x1, y = y1, coef, set, sol))*(1-set['theta'])*lam
        for x1 in range(3,set['Nx']-1,2):
            i += 1
            B[i] = 1 - (P1_code(x = x1, y = y1, coef, set, sol)+P2_code(x = x1, y = y1, coef, set, sol)+P4_code(x = x1, y = y1, coef, set, sol))*(1-set['theta'])*lam
        
        x1 = set['Nx']-1
        B[i+1] = 1 - (P1_code(x = x1, y = y1, coef, set, sol)+P4_code(x = x1, y = y1, coef, set, sol))*(1-set['theta'])*lam
        
        '''Inside'''
        for j, y1 in enumerate(range(3,set['Ny']-1,2)):
            x1 = 1
            i = 0
            B[(i+set['Nx']/2)+j*set['Nx']/2] = 1 - (P2_code(x = x1, y = y1, coef, set, sol) + P3_code(x = x1, y = y1, coef, set, sol) + P4_code(x = x1, y = y1, coef, set, sol))*(1-set['theta'])*lam
            for x1 in range(3,set['Nx']-1,2):
                i += 1
                B[(i+set['Nx']/2)+j*set['Nx']/2] = 1 - (P1_code(x = x1, y = y1, coef, set, sol) + P2_code(x = x1, y = y1, coef, set, sol) + P3_code(x = x1, y = y1, coef, set, sol) + P4_code(x = x1, y = y1, coef, set, sol))*(1-set['theta'])*lam
            x1 = set['Nx']-1
            B[(i+1+set['Nx']/2)+j*set['Nx']/2] = 1 - (P1_code(x = x1, y = y1, coef, set, sol) + P3_code(x = x1, y = y1, coef, set, sol) + P4_code(x = x1, y = y1, coef, set, sol))*(1-set['theta'])*lam
        '''Up side'''
        y1 = set['Ny']-1
        x1 = 1
        i = 0
        B[i+(set['Nx']/2)**2-set['Nx']/2] = 1 - (P2_code(x = x1, y = y1, coef, set, sol)+P3_code(x = x1, y = y1, coef, set, sol))*(1-set['theta'])*lam
        for x1 in range(3,set['Nx']-1,2):
            i += 1
            B[i+(set['Nx']/2)**2-set['Nx']/2] = 1 - (P1_code(x = x1, y = y1, coef, set, sol)+P2_code(x = x1, y = y1, coef, set, sol)+P3_code(x = x1, y = y1, coef, set, sol))*(1-set['theta'])*lam
        x1 = set['Nx']-1
        B[i+1+(set['Nx']/2)**2-set['Nx']/2] = 1 - (P1_code(x = x1, y = y1, coef, set, sol)+P3_code(x = x1, y = y1, coef, set, sol))*(1-set['theta'])*lam
        
    return B

    
def vector_C(coef, set, sol, left = False):
    lam = set['dt']/set['h']**2
    
    import numpy
    C = numpy.zeros((set['Nx']/2)**2-1)
    if left == True: # I + matrix
        ij = 0
        for y1 in range(1,set['Ny'],2):
            for x1 in range(3,set['Nx']+2,2):
                if ij > 0 and (ij+1) % (set['Nx']/2) == 0:
                    pass
                else:
                    C[ij] = (-P1_code(x = x1, y = y1, coef, set, sol))*set['theta']*lam
                ij += 1
          
                
#        '''Bottom side'''
#        y1 = 1
#        for i, x1 in enumerate(range(3,set['Nx'],2)):
#            C[i] = (-P1_code(x = x1, y = y1, coef, set, sol))*set['theta']*lam
#        '''Inside'''
#        for j, y1 in enumerate(range(3,set['Ny']-1,2)):
#            for i, x1 in enumerate(range(3,set['Nx'],2)):
#                C[(i+set['Nx']/2)+j*set['Nx']/2] = (-P1_code(x = x1, y = y1, coef, set, sol))*set['theta']*lam
#        '''Up side'''
#        y1 = set['Ny']-1
#        for i, x1 in enumerate(range(3,set['Nx'],2)):
#            C[i+(Nx/2)**2-set['Nx']/2] = (-P1_code(x = x1, y = y1, coef, set, sol))*set['theta']*lam
    else: # I - matrix
        ij = 0
        for y1 in range(1,set['Ny'],2):
            for x1 in range(3,set['Nx']+2,2):
                if ij > 0 and (ij+1) % (set['Nx']/2) == 0:
                    pass
                else:
                    C[ij] = (-P1_code(x = x1, y = y1, coef, set, sol))*(1-set['theta'])*lam*(-1)
                ij += 1
               
        
#        '''Bottom side'''
#        y1 = 1
#        for i, x1 in enumerate(range(3,set['Nx'],2)):
#            C[i] = (-P1_code(x = x1, y = y1, coef, set, sol))*set['theta']*lam*(-1)
#        '''Inside'''
#        for j, y1 in enumerate(range(3,set['Ny']-1,2)):
#            for i, x1 in enumerate(range(3,set['Nx'],2)):
#                C[(i+set['Nx']/2)+j*Nx/2] = (-P1_code(x = x1, y = y1, coef, set, sol))*set['theta']*lam*(-1)
#        '''Up side'''
#        y1 = set['Ny']-1
#        for i, x1 in enumerate(range(3,set['Nx'],2)):
#            C[i+(set['Nx']/2)**2-set['Nx']/2] = (-P1_code(x = x1, y = y1, coef, set, sol))*set['theta']*lam*(-1)
    C = numpy.insert(C,0,0)
    return C


def vector_D(coef, set, sol, left = False):
    lam = set['dt']/set['h']**2
    
    import numpy
    D = numpy.zeros(set['Nx']/2*(set['Nx']/2-1)) #set['Nx']/2*(set['Nx']/2-1)
    if left == True: # I + matrix
        i = 0
        for y1 in range(1,set['Ny']-1,2):
            for x1 in range(1,set['Nx'],2):
                D[i] = (-P4_code(x = x1, y = y1, coef, set, sol))*set['theta']*lam
                i += 1
    else: # I - matrix
        i = 0
        for y1 in range(1,set['Ny']-1,2):
            for x1 in range(1,set['Nx'],2):
                D[i] = (-P4_code(x = x1, y = y1, coef, set, sol))*(1-set['theta'])*lam*(-1)
                i += 1
    kk = set['Nx']/2
    D = numpy.append(D, [0]*kk)
    return D

def vector_E(coef, set, sol, left = False):
    lam = set['dt']/set['h']**2
    
    import numpy
    E = numpy.zeros(set['Nx']/2*(set['Nx']/2-1)) #set['Nx']/2*(set['Nx']/2-1)
    if left == True: # I + matrix
        i = 0
        for y1 in range(3,set['Ny'],2):
            for x1 in range(1,set['Nx'],2):
                E[i] = (-P3_code(x = x1, y = y1, coef, set, sol))*set['theta']*lam
                i += 1
    else: # I - matrix
        i = 0
        for y1 in range(3,set['Ny'],2):
            for x1 in range(1,set['Nx'],2):
                E[i] = (-P3_code(x = x1, y = y1, coef, set, sol))*(1-set['theta'])*lam*(-1)
                i += 1
    kk = set['Nx']/2
    E = numpy.insert(E, [0]*kk,0)
    return E

def continuous_n_(coef, set, sol):
   
    '''Creating RHS Sparse Matrix'''
    A_right = vector_A(coef, set, sol)
    B_right = vector_B(coef, set, sol)
    C_right = vector_C(coef, set, sol)
    D_right = vector_D(coef, set, sol)
    E_right = vector_E(coef, set, sol)
    
    data = numpy.array([D_right, A_right, B_right, C_right, E_right])
    ii = (Nx/2)**2
    diags = numpy.array([-set['Nx']/2,-1, 0, 1, set['Nx']/2])
      
    '''RHS Multiply n and store as Q'''
    Q = numpy.zeros((set['Nx']/2)**2)
    for i,j in enumerate(range(1,set['Nx'],2)): #untuk paling awal
        if j == 1: 
            Q[i] = B_right[i]*sol['n'][1,1] + C_right[i+1]*sol['n'][3,1] + E_right[i+set['Nx']/2]*sol['n'][1,3] #B & C , E
        elif j == set['Nx']-1: 
            Q[i] = A_right[i-1]*sol['n'][j-2,1] + B_right[i]*sol['n'][j,1] + E_right[i+set['Nx']/2]*sol['n'][j,3]#A & B, E
        else:
            Q[i] = A_right[i-1]*sol['n'][j-2,1] + B_right[i]*sol['n'][j,1] + C_right[i+1]*sol['n'][j+2,1] + E_right[i+set['Nx']/2]*sol['n'][j,3]#A & B & C, E
            
    i = set['Nx']/2       
    for k,l in enumerate(range(3,set['Nx']-2,2)): 
        for j in range(1,set['Nx'],2): #untuk tengah #set['Nx']/2 , (set['Nx']/2)**2-set['Nx']/2
            if j == 1:
                Q[i] = D_right[i-(set['Nx']/2)]*sol['n'][j,l-2] + B_right[i]*sol['n'][j,l] + C_right[i+1]*sol['n'][j+2,l] + E_right[i+set['Nx']/2]*sol['n'][j,l+2] #D, B & C, E
            elif j == set['Nx']-1:
                Q[i] = D_right[i-(set['Nx']/2)]*sol['n'][j,l-2] + A_right[i-1]*sol['n'][j-2,l] + B_right[i]*sol['n'][j,l] + E_right[i+set['Nx']/2]*sol['n'][j,l+2] #D, A & B, E
            else:
                Q[i] = D_right[i-(set['Nx']/2)]*sol['n'][j,l-2] + A_right[i-1]*sol['n'][j-2,l] + B_right[i]*sol['n'][j,l] + C_right[i+1]*sol['n'][j+2,l] + E_right[i+set['Nx']/2]*sol['n'][j,l+2] #D, A & B & C, E
            i +=1
     
    for i,j in enumerate(range(1,set['Nx'],2)): #untuk terakhir #(set['Nx']/2)**2-set['Nx']/2 , (set['Nx']/2)**2
        i += (set['Nx']/2)**2-set['Nx']/2
        if j == 1:
            Q[i] = D_right[i-(set['Nx']/2)]*sol['n'][1,set['Nx']-3] + B_right[i]*sol['n'][1,set['Nx']-1] + C_right[i+1]*sol['n'][3,set['Nx']-1] #D, B & C
        elif j == set['Nx']-1:
            Q[i] = D_right[i-(set['Nx']/2)]*sol['n'][j,set['Nx']-3] + A_right[i-1]*sol['n'][j-2,set['Nx']-1] + B_right[i]*sol['n'][j,set['Nx']-1] #D, A & B
        else:
            Q[i] = D_right[i-(set['Nx']/2)]*sol['n'][j,set['Nx']-3] + A_right[i-1]*sol['n'][j-2,set['Nx']-1] + B_right[i]*sol['n'][j,set['Nx']-1] + C_right[i+1]*sol['n'][j+2,set['Nx']-1] #D, A & B & C
    del A_right
    del B_right
    del C_right
    del D_right
    del E_right
   
    '''Creating LHS Sparse Matrix'''
    A_left = vector_A(coef, set, sol, left = True)
    B_left = vector_B(coef, set, sol, left = True)
    C_left = vector_C(coef, set, sol, left = True)
    D_left = vector_D(coef, set, sol, left = True)
    E_left = vector_E(coef, set, sol, left = True)
    
    data = numpy.array([D_left, A_left, B_left, C_left, E_left])
    LHS = dia_matrix((data, diags), shape=((set['Nx']/2)**2, (set['Nx']/2)**2))
 
    '''Solve LHS n = V'''
#    from numpy.linalg import solve
    m_sol = spsolve(LHS.tocsr(), Q)
    del LHS
    del Q
    del data
    del diags
    
    '''Storing new n solution into n[x,y]'''  
    i = 0
    for y in range(1,Ny,2):
        for x in range(1,set['Nx'],2):
            sol['n'][x,y] = m_sol[i]
            i +=1
    
    '''Time Step
    v1=[]
    v2=[]
    for y in range(2,Ny+1,2):
        for x in range(0,set['Nx'],2):
            v1.append(max(1/(2*h3)*(p[x+2,y]-p[x,y]+p[x+2,y-2]-p[x,y-2]),1/(2*h3)*(p[x+2,y]-p[x+2,y-2]+p[x,y]-p[x,y-2])))
            v2.append(max(1/(2*h3)*(p_o[x+2,y]-p_o[x,y]+p_o[x+2,y-2]-p_o[x,y-2]),1/(2*h3)*(p_o[x+2,y]-p_o[x+2,y-2]+p_o[x,y]-p_o[x,y-2])))
    tau1 = min(h3/(4*teta*(ki_m*max(v1)/(1+al_m*p.max()))),h3**2/(4*(1-teta)*(d_m+h3*ki_m*max(v2)/(1+al_m*p_o.max()))),1/(d_c*2/h3**2+nu*n.max()),1/(ga*n.max()))
    #print 'TPC', 1/(d_c*2/h3**2+nu*n.max())
    #print 'TPF', 1/(ga*n.max())
    #print 'TP1', h3/(4*teta*(ki_m*max(v1)/(1+al_m*p.max())))
    #print 'TP2', h3**2/(4*(1-teta)*(d_m+h3*ki_m*max(v2)/(1+al_m*p_o.max())))
    tp = tau1
    del v1
    del v2
    del tau1
    '''


    return sol
# continuous_sparse_matrix_1_iter(iter=1)
