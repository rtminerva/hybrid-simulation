import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
import math
tips = 6

def fun(x, y):
    return math.exp(-x**2/0.001)*(math.sin(tips*math.pi*y))**2

fig = plt.figure()
plt.xlim(0,1)
plt.ylim(0,1)
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(0,1,0.001)
X, Y = np.meshgrid(x, y)
zs = np.array([fun(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

g = 5.6
print int(g)