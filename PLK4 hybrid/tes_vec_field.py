import matplotlib.pyplot as plt
import numpy as np

x, y, u, v = np.random.random((4,10))
print x,y,u,v
plt.quiver(x, y, u, v)
plt.show()