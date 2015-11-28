from matplotlib import pyplot as plt
import numpy as np

x = np.array([0.01, 0.02, 0.02, 0.02, 0.03])
y = np.array([1.6, 1.6,1.59 , 1.58, 1.58])
lwidths = np.array([10,10,5,4,2])#(1+x)**2 # scatter 'o' marker size is specified by area not radius 
print lwidths
plt.scatter(x,y, s=lwidths, color='blue')
plt.xlim(0,1)
plt.ylim(1,2)
plt.show()
