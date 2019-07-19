import math as m
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

a =1 #1 0.6 
b = 0.39#0.38 #0.39 #0.8
et_1 = 0.23#0.12 #0.23#0.26 #oscilation velocity of vegf
alpha = 0.15
t = 0
ep = 3-0.1

Hh = 0.1/2
Nx = int(1/Hh)
Ny = int(1/Hh)

xline = np.linspace(0, 1, 1000)
yline = np.linspace(0, 1, 1000)
xline, yline = np.meshgrid(xline, yline)

#c = np.zeros((Nx+1,Ny+1))

#r_c = numpy.sqrt((x*Hh)**2+(y*Hh-0.5)**2)

# for y in yline:
#     for x in xline:

c = []#np.zeros(len(xline)*len(yline))
r_c = np.sqrt((xline)**2+(yline-0.5)**2)
print r_c
for rrc in r_c:
    if rrc >= 0.1:
        c.append(a*(b + m.sin(m.pi*et_1*t) * m.exp(-alpha*t)) * (1-(3-rrc)**2/(ep)**2))
    elif rrc>= 0 and rrc < 0.1:
        c.append(0)

c_ = np.asarray(c)

fig = plt.figure()
ax = plt.axes(projection='3d')
#ax.plot3D(xline, yline, c_, 'gray')
ax.plot_surface(xline, yline, c_, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
plt.show()