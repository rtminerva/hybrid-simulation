

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

def F1x_code(d = 0.00035, ki = 0.38, al = 0.6, ro = 0.3, one = 0, two = 0, three = 0, four = 0, nn = 0, cc = 0, x_p = 0, y_p = 0): #at main lattice n
    r = -d*(nn[x_p+2,y_p]-nn[x_p,y_p])+ki/(1+al*cc[x_p+1,y_p+1])*(nn[x_p,y_p]*one-nn[x_p+2,y_p]*two) + ro*(nn[x_p,y_p]*three-nn[x_p+2,y_p]*four)
    return r
    
def F2x_code(d = 0.00035, ki = 0.38, al = 0.6, ro = 0.3, one = 0, two = 0, three = 0, four = 0, nn = 0, cc = 0, x_p = 0, y_p = 0): #at main lattice n
    r = -d*(nn[x_p,y_p]-nn[x_p-2,y_p])+ki/(1+al*cc[x_p-1,y_p+1])*(nn[x_p-2,y_p]*one-nn[x_p,y_p]*two) + ro*(nn[x_p-2,y_p]*three-nn[x_p,y_p]*four)
    return r
 
def F3y_code(d = 0.00035, ki = 0.38, al = 0.6, ro = 0.3, one = 0, two = 0, three = 0, four = 0, nn = 0, cc = 0, x_p = 0, y_p = 0): #at main lattice n
    r = -d*(nn[x_p,y_p+2]-nn[x_p,y_p])+ki/(1+al*cc[x_p+1,y_p+1])*(nn[x_p,y_p+2]*one-nn[x_p,y_p]*two) + ro*(nn[x_p,y_p+2]*three-nn[x_p,y_p]*four)
    return r 

def F4y_code(d = 0.00035, ki = 0.38, al = 0.6, ro = 0.3, one = 0, two = 0, three = 0, four = 0, nn = 0, cc = 0, x_p = 0, y_p = 0): #at main lattice n
    r = -d*(nn[x_p,y_p]-nn[x_p,y_p-2])+ki/(1+al*cc[x_p+1,y_p-1])*(nn[x_p,y_p]*one-nn[x_p,y_p-2]*two) + ro*(nn[x_p,y_p]*three-nn[x_p,y_p-2]*four)
    return r

'''Main Function'''

def contiuous_1_iter(theta = 0,d = 0.00035,ki = 0.38,al = 0.6,ro = 0.3,
                     nu = 0.1,be = 0.05,ga = 0.1,e = 0.45,X = 1,Y = 1,
                     h = 0.01,tp = 0.001,iter = 0, number_of_tip = 3,
                     n_o = 0, c_o = 0, f_o = 0, n = 0, c = 0, f = 0, time = 0):
    import math as m
    import numpy
    hh = h/2
    Nx = int(X/hh)
    Ny = int(Y/hh)
    
    '''For the beginning'''
    if iter == 1:
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
    '''Solve n at main lattice'''
    for y in range(1,Ny,2):
        for x in range(1,Nx,2):
            if y == 1: #batas bawah
#                 a1 = max(vy_code(x_p = x, y_p = y+2, cc = c), 0)
#                 a2 = max(-vy_code(x_p = x, y_p = y, cc = c), 0)
#                 a3 = max(wy_code(x_p = x, y_p = y+2, ff = f), 0)
#                 a4 = max(-wy_code(x_p = x, y_p = y, ff = f), 0)
                F3y = F3y_code(one = max(vy_code(x_p = x, y_p = y+2, cc = c), 0), 
                               two = max(-vy_code(x_p = x, y_p = y, cc = c), 0), 
                               three = max(wy_code(x_p = x, y_p = y+2, ff = f), 0), 
                               four = max(-wy_code(x_p = x, y_p = y, ff = f), 0), 
                               nn = n_o, cc = c_o, x_p = x, y_p = y)
#                 F3y = -d*(n[x,y+2]-n[x,y])+ki/(1+al*c[x+1,y+1])*(n[x,y+2]*max(vy_code(x_p = x, y_p = y+2, cc = c), 0)-n[x,y]*max(-vy_code(x_p = x, y_p = y, cc = c), 0)) + ro*(n[x,y+2]*max(wy_code(x_p = x, y_p = y+2, ff = f), 0)-n[x,y]*max(-wy_code(x_p = x, y_p = y, ff = f), 0))
                if x == 1: #pojok kiri bawah
#                     a1 = max(vx_code(x_p = x, y_p = y, cc = c), 0)
#                     a2 = max(-vx_code(x_p = x+2, y_p = y, cc = c), 0)
#                     a3 = max(wx_code(x_p = x, y_p = y, ff = f), 0)
#                     a4 = max(-wx_code(x_p = x+2, y_p = y, ff = f), 0)
                    F1x = F1x_code(one = max(vx_code(x_p = x, y_p = y, cc = c), 0), 
                                   two = max(-vx_code(x_p = x+2, y_p = y, cc = c), 0), 
                                   three = max(wx_code(x_p = x, y_p = y, ff = f), 0), 
                                   four = max(-wx_code(x_p = x+2, y_p = y, ff = f), 0), 
                                   nn = n_o, cc = c_o, x_p = x, y_p = y)
#                     F1x = -d*(n[x+2,y]-n[x,y])+ki/(1+al*c[x+1,y+1])*(n[x,y]*max(vx_code(x_p = x, y_p = y, cc = c), 0)-n[x+2,y]*max(-vx_code(x_p = x+2, y_p = y, cc = c), 0)) + ro*(n[x,y]*max(wx_code(x_p = x, y_p = y, ff = f), 0)-n[x+2,y]*max(-wx_code(x_p = x+2, y_p = y, ff = f), 0))
                    n[x,y] = n_o[x,y]-tp/h*(F1x+F3y)
                elif x == Nx-1: #pojok kanan bawah
#                     a1 = max(vx_code(x_p = x-2, y_p = y, cc = c), 0)
#                     a2 = max(-vx_code(x_p = x, y_p = y, cc = c), 0)
#                     a3 = max(wx_code(x_p = x-2, y_p = y, ff = f), 0)
#                     a4 = max(-wx_code(x_p = x, y_p = y, ff = f), 0)
                    F2x = F2x_code(one = max(vx_code(x_p = x-2, y_p = y, cc = c), 0), 
                                   two = max(-vx_code(x_p = x, y_p = y, cc = c), 0), 
                                   three = max(wx_code(x_p = x-2, y_p = y, ff = f), 0), 
                                   four = max(-wx_code(x_p = x, y_p = y, ff = f), 0), 
                                   nn = n_o, cc = c_o, x_p = x, y_p = y)
#                     F2x = -d*(n[x,y]-n[x-2,y])+ki/(1+al*c[x-1,y+1])*(n[x-2,y]*max(vx_code(x_p = x-2, y_p = y, cc = c), 0)-n[x,y]*max(-vx_code(x_p = x, y_p = y, cc = c), 0)) + ro*(n[x-2,y]*max(wx_code(x_p = x-2, y_p = y, ff = f), 0)-n[x,y]*max(-wx_code(x_p = x, y_p = y, ff = f), 0))
                    n[x,y] = n_o[x,y]-tp/h*(-F2x+F3y)
                else:
#                     a1 = max(vx_code(x_p = x, y_p = y, cc = c), 0)
#                     a2 = max(-vx_code(x_p = x+2, y_p = y, cc = c), 0)
#                     a3 = max(wx_code(x_p = x, y_p = y, ff = f), 0)
#                     a4 = max(-wx_code(x_p = x+2, y_p = y, ff = f), 0)
                    F1x = F1x_code(one = max(vx_code(x_p = x, y_p = y, cc = c), 0), 
                                   two = max(-vx_code(x_p = x+2, y_p = y, cc = c), 0), 
                                   three = max(wx_code(x_p = x, y_p = y, ff = f), 0), 
                                   four = max(-wx_code(x_p = x+2, y_p = y, ff = f), 0), 
                                   nn = n_o, cc = c_o, x_p = x, y_p = y)
#                     F1x = -d*(n[x+2,y]-n[x,y])+ki/(1+al*c[x+1,y+1])*(n[x,y]*max(vx_code(x_p = x, y_p = y, cc = c), 0)-n[x+2,y]*max(-vx_code(x_p = x+2, y_p = y, cc = c), 0)) + ro*(n[x,y]*max(wx_code(x_p = x, y_p = y, ff = f), 0)-n[x+2,y]*max(-wx_code(x_p = x+2, y_p = y, ff = f), 0))
#                     a1 = max(vx_code(x_p = x-2, y_p = y, cc = c), 0)
#                     a2 = max(-vx_code(x_p = x, y_p = y, cc = c), 0)
#                     a3 = max(wx_code(x_p = x-2, y_p = y, ff = f), 0)
#                     a4 = max(-wx_code(x_p = x, y_p = y, ff = f), 0)
                    F2x = F2x_code(one = max(vx_code(x_p = x-2, y_p = y, cc = c), 0), 
                                   two = max(-vx_code(x_p = x, y_p = y, cc = c), 0), 
                                   three = max(wx_code(x_p = x-2, y_p = y, ff = f), 0), 
                                   four = max(-wx_code(x_p = x, y_p = y, ff = f), 0), 
                                   nn = n_o, cc = c_o, x_p = x, y_p = y)
#                     F2x = -d*(n[x,y]-n[x-2,y])+ki/(1+al*c[x-1,y+1])*(n[x-2,y]*max(vx_code(x_p = x-2, y_p = y, cc = c), 0)-n[x,y]*max(-vx_code(x_p = x, y_p = y, cc = c), 0)) + ro*(n[x-2,y]*max(wx_code(x_p = x-2, y_p = y, ff = f), 0)-n[x,y]*max(-wx_code(x_p = x, y_p = y, ff = f), 0))
                    n[x,y] = n_o[x,y]-tp/h*(F1x+-F2x+F3y)
            
            elif y == Ny-1: #batas atas
#                 a1 = max(vy_code(x_p = x, y_p = y, cc = c), 0)
#                 a2 = max(-vy_code(x_p = x, y_p = y-2, cc = c), 0)
#                 a3 = max(wy_code(x_p = x, y_p = y, ff = f), 0)
#                 a4 = max(-wy_code(x_p = x, y_p = y-2, ff = f), 0)
                F4y = F4y_code(one = max(vy_code(x_p = x, y_p = y, cc = c), 0), 
                               two = max(-vy_code(x_p = x, y_p = y-2, cc = c), 0), 
                               three = max(wy_code(x_p = x, y_p = y, ff = f), 0), 
                               four = max(-wy_code(x_p = x, y_p = y-2, ff = f), 0), 
                               nn = n_o, cc = c_o, x_p = x, y_p = y)
#                 F4y = -d*(n[x,y]-n[x,y-2])+ki/(1+al*c[x+1,y-1])*(n[x,y]*max(vy_code(x_p = x, y_p = y, cc = c), 0)-n[x,y-2]*max(-vy_code(x_p = x, y_p = y-2, cc = c), 0)) + ro*(n[x,y]*max(wy_code(x_p = x, y_p = y, ff = f), 0)-n[x,y-2]*max(-wy_code(x_p = x, y_p = y-2, ff = f), 0))
                if x == 1: #pojok kiri atas
#                     a1 = max(vx_code(x_p = x, y_p = y, cc = c), 0)
#                     a2 = max(-vx_code(x_p = x+2, y_p = y, cc = c), 0)
#                     a3 = max(wx_code(x_p = x, y_p = y, ff = f), 0)
#                     a4 = max(-wx_code(x_p = x+2, y_p = y, ff = f), 0)
                    F1x = F1x_code(one = max(vx_code(x_p = x, y_p = y, cc = c), 0), 
                                   two = max(-vx_code(x_p = x+2, y_p = y, cc = c), 0), 
                                   three = max(wx_code(x_p = x, y_p = y, ff = f), 0), 
                                   four = max(-wx_code(x_p = x+2, y_p = y, ff = f), 0), 
                                   nn = n_o, cc = c_o, x_p = x, y_p = y)
                    n[x,y] = n_o[x,y]-tp/h*(F1x-F4y)
                elif x == Nx-1: #pojok kanan atas
#                     a1 = max(vx_code(x_p = x-2, y_p = y, cc = c), 0)
#                     a2 = max(-vx_code(x_p = x, y_p = y, cc = c), 0)
#                     a3 = max(wx_code(x_p = x-2, y_p = y, ff = f), 0)
#                     a4 = max(-wx_code(x_p = x, y_p = y, ff = f), 0)
                    F2x = F2x_code(one = max(vx_code(x_p = x-2, y_p = y, cc = c), 0), 
                                   two = max(-vx_code(x_p = x, y_p = y, cc = c), 0), 
                                   three = max(wx_code(x_p = x-2, y_p = y, ff = f), 0), 
                                   four = max(-wx_code(x_p = x, y_p = y, ff = f), 0), 
                                   nn = n_o, cc = c_o, x_p = x, y_p = y)
                    n[x,y] = n_o[x,y]-tp/h*(-F2x-F4y)
                
                else:
#                     a1 = max(vx_code(x_p = x, y_p = y, cc = c), 0)
#                     a2 = max(-vx_code(x_p = x+2, y_p = y, cc = c), 0)
#                     a3 = max(wx_code(x_p = x, y_p = y, ff = f), 0)
#                     a4 = max(-wx_code(x_p = x+2, y_p = y, ff = f), 0)
                    F1x = F1x_code(one = max(vx_code(x_p = x, y_p = y, cc = c), 0), 
                                   two = max(-vx_code(x_p = x+2, y_p = y, cc = c), 0), 
                                   three = max(wx_code(x_p = x, y_p = y, ff = f), 0), 
                                   four = max(-wx_code(x_p = x+2, y_p = y, ff = f), 0), 
                                   nn = n_o, cc = c_o, x_p = x, y_p = y)
#                     a1 = max(vx_code(x_p = x-2, y_p = y, cc = c), 0)
#                     a2 = max(-vx_code(x_p = x, y_p = y, cc = c), 0)
#                     a3 = max(wx_code(x_p = x-2, y_p = y, ff = f), 0)
#                     a4 = max(-wx_code(x_p = x, y_p = y, ff = f), 0)
                    F2x = F2x_code(one = max(vx_code(x_p = x-2, y_p = y, cc = c), 0), 
                                   two = max(-vx_code(x_p = x, y_p = y, cc = c), 0), 
                                   three = max(wx_code(x_p = x-2, y_p = y, ff = f), 0), 
                                   four = max(-wx_code(x_p = x, y_p = y, ff = f), 0), 
                                   nn = n_o, cc = c_o, x_p = x, y_p = y)
                    n[x,y] = n_o[x,y]-tp/h*(F1x-F2x-F4y)
            else:
#                 a1 = max(vy_code(x_p = x, y_p = y+2, cc = c), 0)
#                 a2 = max(-vy_code(x_p = x, y_p = y, cc = c), 0)
#                 a3 = max(wy_code(x_p = x, y_p = y+2, ff = f), 0)
#                 a4 = max(-wy_code(x_p = x, y_p = y, ff = f), 0)
                F3y = F3y_code(one = max(vy_code(x_p = x, y_p = y+2, cc = c), 0), 
                               two = max(-vy_code(x_p = x, y_p = y, cc = c), 0), 
                               three = max(wy_code(x_p = x, y_p = y+2, ff = f), 0), 
                               four = max(-wy_code(x_p = x, y_p = y, ff = f), 0), 
                               nn = n_o, cc = c_o, x_p = x, y_p = y)
#                 a1 = max(vy_code(x_p = x, y_p = y, cc = c), 0)
#                 a2 = max(-vy_code(x_p = x, y_p = y-2, cc = c), 0)
#                 a3 = max(wy_code(x_p = x, y_p = y, ff = f), 0)
#                 a4 = max(-wy_code(x_p = x, y_p = y-2, ff = f), 0)
                F4y = F4y_code(one = max(vy_code(x_p = x, y_p = y, cc = c), 0), 
                               two = max(-vy_code(x_p = x, y_p = y-2, cc = c), 0), 
                               three = max(wy_code(x_p = x, y_p = y, ff = f), 0), 
                               four = max(-wy_code(x_p = x, y_p = y-2, ff = f), 0), 
                               nn = n_o, cc = c_o, x_p = x, y_p = y)
                if x == 1: #batas kiri selain pojokan
#                     a1 = max(vx_code(x_p = x, y_p = y, cc = c), 0)
#                     a2 = max(-vx_code(x_p = x+2, y_p = y, cc = c), 0)
#                     a3 = max(wx_code(x_p = x, y_p = y, ff = f), 0)
#                     a4 = max(-wx_code(x_p = x+2, y_p = y, ff = f), 0)
                    F1x = F1x_code(one = max(vx_code(x_p = x, y_p = y, cc = c), 0), 
                                   two = max(-vx_code(x_p = x+2, y_p = y, cc = c), 0), 
                                   three = max(wx_code(x_p = x, y_p = y, ff = f), 0), 
                                   four = max(-wx_code(x_p = x+2, y_p = y, ff = f), 0), 
                                   nn = n_o, cc = c_o, x_p = x, y_p = y)
                    n[x,y] = n_o[x,y]-tp/h*(F1x+F3y-F4y)
                elif x == Nx-1: #batas kanan selain pojokan
#                     a1 = max(vx_code(x_p = x-2, y_p = y, cc = c), 0)
#                     a2 = max(-vx_code(x_p = x, y_p = y, cc = c), 0)
#                     a3 = max(wx_code(x_p = x-2, y_p = y, ff = f), 0)
#                     a4 = max(-wx_code(x_p = x, y_p = y, ff = f), 0)
                    F2x = F2x_code(one = max(vx_code(x_p = x-2, y_p = y, cc = c), 0), 
                                   two = max(-vx_code(x_p = x, y_p = y, cc = c), 0), 
                                   three = max(wx_code(x_p = x-2, y_p = y, ff = f), 0), 
                                   four = max(-wx_code(x_p = x, y_p = y, ff = f), 0), 
                                   nn = n_o, cc = c_o, x_p = x, y_p = y)
                    n[x,y] = n_o[x,y]-tp/h*(-F2x+F3y-F4y)
                else: #tengah2
#                     a1 = max(vx_code(x_p = x, y_p = y, cc = c), 0)
#                     a2 = max(-vx_code(x_p = x+2, y_p = y, cc = c), 0)
#                     a3 = max(wx_code(x_p = x, y_p = y, ff = f), 0)
#                     a4 = max(-wx_code(x_p = x+2, y_p = y, ff = f), 0)
                    F1x = F1x_code(one = max(vx_code(x_p = x, y_p = y, cc = c), 0), 
                                   two = max(-vx_code(x_p = x+2, y_p = y, cc = c), 0), 
                                   three = max(wx_code(x_p = x, y_p = y, ff = f), 0), 
                                   four = max(-wx_code(x_p = x+2, y_p = y, ff = f), 0), 
                                   nn = n_o, cc = c_o, x_p = x, y_p = y)
#                     a1 = max(vx_code(x_p = x-2, y_p = y, cc = c), 0)
#                     a2 = max(-vx_code(x_p = x, y_p = y, cc = c), 0)
#                     a3 = max(wx_code(x_p = x-2, y_p = y, ff = f), 0)
#                     a4 = max(-wx_code(x_p = x, y_p = y, ff = f), 0)
                    F2x = F2x_code(one = max(vx_code(x_p = x-2, y_p = y, cc = c), 0), 
                                   two = max(-vx_code(x_p = x, y_p = y, cc = c), 0), 
                                   three = max(wx_code(x_p = x-2, y_p = y, ff = f), 0), 
                                   four = max(-wx_code(x_p = x, y_p = y, ff = f), 0), 
                                   nn = n_o, cc = c_o, x_p = x, y_p = y)
                    n[x,y] = n_o[x,y]-tp/h*(F1x-F2x+F3y-F4y)
                    
    '''Solve c, f at sub lattice'''
    for y in range(0,Ny+1,2):
        for x in range(0,Nx+1,2):
            if y == 0:
                if x == 0:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_o[1,1])
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*n_o[1,1]
                elif x == Nx:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_o[Nx-1,1])
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*n_o[Nx-1,1]
                else:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*0.5*(n_o[x+1,1]+n_o[x-1,1]))
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*0.5*(n_o[x+1,1]+n_o[x-1,1])
            elif y == Ny:
                if x == 0:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_o[1,Ny-1])
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*n_o[1,Ny-1]
                elif x == Nx:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*n_o[Nx-1,Ny-1])
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*n_o[Nx-1,Ny-1]
                else:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*0.5*(n_o[x+1,Ny-1]+n_o[x-1,Ny-1]))
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*0.5*(n_o[x+1,Ny-1]+n_o[x-1,Ny-1])
            else:
                if x == 0:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*0.5*(n_o[x+1,y+1]+n_o[x+1,y-1]))
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*0.5*(n_o[x+1,y+1]+n_o[x+1,y-1])
                elif x == Nx:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*0.5*(n_o[x-1,y+1]+n_o[x-1,y-1]))
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*0.5*(n_o[x-1,y+1]+n_o[x-1,y-1])
                else:
                    c[x,y] = c_o[x,y]*(1 - tp*nu*0.25*(n_o[x+1,y+1]+n_o[x-1,y+1]+n_o[x+1,y-1]+n_o[x-1,y-1]))
                    f[x,y] = f_o[x,y]+ tp*(be-ga*f_o[x,y])*0.25*(n_o[x+1,y+1]+n_o[x-1,y+1]+n_o[x+1,y-1]+n_o[x-1,y-1])
    rr = [n_o,c_o,f_o,n,c,f,tp]
    n_o = n
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
    for value in n:
        if value.all < 0:
            print 'Ada N yang negative'
            quit()
#     '''Plot Continuous '''
#     print time
#     if iter % 2 == 0:#time >= 2.8: #iter % 200 == 0 or 
#         print 'plot at time:', time
#         
#         x_main_axis = numpy.arange(hh, X, h)
#         y_main_axis = numpy.arange(hh, Y, h)
#         x_main_axis, y_main_axis = numpy.meshgrid(x_main_axis, y_main_axis)
#         
#         x_sub_axis = numpy.arange(0, X+hh, h)
#         y_sub_axis = numpy.arange(0, Y+hh, h)
#         x_sub_axis, y_sub_axis = numpy.meshgrid(x_sub_axis, y_sub_axis)
#         
# #         c_sol = numpy.zeros((Nx/2+1, Ny/2+1))
# #         f_sol = numpy.zeros((Nx/2+1, Ny/2+1))
#         n_sol = numpy.zeros((Nx/2, Ny/2))
#         
#         for j, y in enumerate(range(1,Ny,2)):
#             for i, x in enumerate(range(1,Nx,2)):
#                 n_sol[i,j] = n[x,y]
#         
#         from matplotlib import cm
#         from matplotlib.ticker import LinearLocator, FormatStrFormatter
#         from mpl_toolkits.mplot3d import Axes3D
#         import matplotlib.pyplot as plt
#         plt.ion()
#         
#         fig = plt.figure()
#         ax = fig.gca(projection='3d')
#         surf = ax.plot_surface(x_main_axis, y_main_axis, n_sol, rstride=1, cstride=1, cmap=cm.coolwarm,
#                 linewidth=0, antialiased=False)
#         # surf = ax.plot_surface(x_sub_axis, y_sub_axis, c_sol, rstride=1, cstride=1, cmap=cm.coolwarm,
#         #         linewidth=0, antialiased=False)
#         ax.set_zlim(-0.1, 1.01)
#         ax.zaxis.set_major_locator(LinearLocator(10))
#         ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
#         fig.colorbar(surf, shrink=0.5, aspect=5)
#         plt.draw()
#     '''Plot'''
    return rr
        