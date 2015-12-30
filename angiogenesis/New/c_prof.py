import numpy
hh = h3/2
Nx = int(X/hh)
Ny = int(Y/hh)
if iter == 1:
    import math as m
    
    n = numpy.zeros((Nx+1,Ny+1))
    c = numpy.zeros((Nx+1,Ny+1))
    f = numpy.zeros((Nx+1,Ny+1))
    viu = (m.sqrt(5)-0.1)/(m.sqrt(5)-1)
    for y in range(0,Ny+1,2):
        for x in range(0,Nx+1,2):
            r_c = m.sqrt((x*hh-1)**2+(y*hh-0.5)**2)
            if r_c > 0.1:
                c[x,y] = 1
            else:
                c[x,y] = (viu-r_c)**2/(viu-0.1)**2