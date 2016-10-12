import numpy

def cart2pol(x, y):
    rho = numpy.sqrt(x**2 + y**2)
    phi = numpy.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * numpy.cos(phi)
    y = rho * nump.sin(phi)
    return(x, y)


r = numpy.linspace(0.5, 1, 11)

theta = numpy.linspace(0, 2*numpy.pi, 11)

radius_matrix, theta_matrix = numpy.meshgrid(r,theta)


X = radius_matrix * numpy.cos(theta_matrix)
Y = radius_matrix * numpy.sin(theta_matrix)

import matplotlib.pyplot as plt
ax = plt.subplot(111, polar=True)
ax.plot(theta_matrix, radius_matrix, color='g', ls='none', marker='.')

#U = numpy.sqrt(X**2 + Y**2)
#plt.plot(X,Y,U, 'r')
plt.show()



'''Plot Hybrid
X = 1
Y = 1
hh = h/2 
fig2 = plt.figure(2)
plt.xlim(hh,X-hh)#X-hh
plt.ylim(hh,Y-hh)#
ax = fig2.add_subplot(111)
plot_all = []
for i in range(0,len(g[0])):
    x_p = []
    y_p = []
    for j in range(0,len(g[0][i])):
        x_p.append(g[0][i][j][0]*hh)
        y_p.append(g[0][i][j][1]*hh)
    globals()['plo%s' % i] = ax.plot(x_p, y_p, 'b')
fig2.show()   
del g
raw_input()
# plt.show(block=True)
Plot Hybrid'''
