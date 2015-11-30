import numpy as np
import math as m

def vx_code(h = 0.01, cc = 0, x_p = 0, y_p = 0):
    r = 0.5/h*(cc[x+1,y+1]-cc[x-1,y+1]+cc[x+1,y-1]-cc[x-1,y-1])
    return r
    
def vy_code(h = 0.01, cc = 0, x_p = 0, y_p = 0):
    r = 0.5/h*(cc[x+1,y+1]+cc[x-1,y+1]-cc[x+1,y-1]-cc[x-1,y-1])
    return r
    
def wx_code(h = 0.01, ff = 0, x_p = 0, y_p = 0):
    r = 0.5/h*(ff[x+1,y+1]-ff[x-1,y+1]+ff[x+1,y-1]-ff[x-1,y-1])
    return r

def wy_code(h = 0.01, ff = 0, x_p = 0, y_p = 0):
    r = 0.5/h*(ff[x+1,y+1]+ff[x-1,y+1]-ff[x+1,y-1]-ff[x-1,y-1])
    return r

def contiuous_1_iter(theta = 0,d = 0.00035,ki = 0.38,al = 0.6,ro = 0,
                     nu = 0.1,be = 0.05,ga = 0.1,e = 0.45,X = 1,Y = 1,
                     h = 0.01,tp = 0.001,iter = 0,number_of_tip = 2):
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
                n[x,y] = m.exp(-(x*hh)**2/0.001)*(m.sin(number_of_tip*m.pi*y*hh))**2
        n_b = n
        c_b = c
        f_b = f
        
        
    '''Time step
    for y in range(2,Ny+1,2):
        for x in range(0,Nx,2):
            v1x = 1/(2*h)*(c[x+2,y,k]-c[x,y,k]+c[x+2,y-2,k]-c[x,y-2,k])
            v1y = 1/(2*h)*(c[x+2,y,k]-c[x+2,y-2,k]+c[x,y,k]-c[x,y-2,k])
            v1.append(max(v1x,v1y))
            w1x = 1/(2*h)*(f[x+2,y,k]-f[x,y,k]+f[x+2,y-2,k]-f[x,y-2,k])
            w1y = 1/(2*h)*(f[x+2,y,k]-f[x+2,y-2,k]+f[x,y,k]-f[x,y-2,k])
            w1.append(max(w1x,w1y))
    vv1 = max(v1)
    ww1 = max(w1)
    tau1 = h**2/(4*(d+h*ki*vv1/(1+al*c.max())+h*ro*ww1))
    tau2 = 1/(nu*n.max())
    tau1 = min(tau1,tau2)
    if tau1 < tau:
        tp = tau1
    else:
        tp = tau
    '''
    '''Solve n at main lattice'''
    for y in range(1,Ny,2):
        for x in range(1,Nx,2):
            if y == 1: #batas bawah
                if x == 1: #pojok kiri bawah
#                     vxl = max(vx_code(x_p = x, y_p = y, cc = c, ff = f), 0)
#                     vxr = max(-vx_code(x_p = x+2, y_p = y, cc = c, ff = f), 0)
#                     vyd = max(vy_code(x_p = x, y_p = y, cc = c, ff = f), 0)
#                     vyu = max(-vy_code(x_p = x, y_p = y+2, cc = c, ff = f), 0)
                    F1 = -d*(n[x+2,y+2]-n[x,y+2])+ki/(1+al*c[x+1,y+1])*(n[x,y]*max(vx_code(x_p = x, y_p = y, cc = c), 0)-n[x+2,y]*max(-vx_code(x_p = x+2, y_p = y, cc = c), 0))+ro*(n[x,y]*max(wx_code(x_p = x, y_p = y, ff = f), 0)-n[x+2,y]*max(-vx_code(x_p = x+2, y_p = y, ff = f), 0))
                    F3 = -d*(n[x+2,y+2]-n[x,y+2])+ki/(1+al*c[x+1,y+1])*(n[x,y]*max(vy_code(x_p = x, y_p = y, cc = c), 0)-n[x,y+2]*max(-vy_code(x_p = x, y_p = y+2, cc = c), 0))+ro*(n[x,y]*max(wy_code(x_p = x, y_p = y, ff = f), 0)-n[x,y+2]*max(-wy_code(x_p = x, y_p = y+2, ff = f), 0))
                    n[x,y] = n[x,y]-tp/h*(F1+F3)
                elif x == Nx-1 #pojok kanan bawah
                else: 
            elif y == Ny-1: #batas atas
                if x == 1: #pojok kiri atas
                elif x == Nx-1 #pojok kanan atas
                else:
            else:
                if x == 1: #batas kiri selain pojokan
                elif x == Nx-1 #batas kanan selain pojokan
                else: #tengah2

        
        
        