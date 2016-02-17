from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt
#step = 0.04
#maxval = 1.0
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# create supporting points in polar coordinates
r_max = 1
r = np.linspace(0.1, r_max, 50)
p = np.linspace(0, 2*np.pi, 50)
R, P = np.meshgrid(r, p)
# transform them to cartesian system
X, Y = R*np.cos(P), R*np.sin(P)

#Z = 1-0.45*np.exp(-R**2/0.45) #initial for c
Z = 1-0.45*np.exp(-(r_max-R)**2/0.45) #initial for f
#Z = ((R**2 - 1)**2) #test plot only
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.YlGnBu_r)
ax.set_zlim3d(0, 1)
ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')
plt.show()