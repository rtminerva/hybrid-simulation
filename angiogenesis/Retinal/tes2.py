import numpy
import time
from matplotlib import pyplot as plt
x = [1, 2, 3]
plt.ion()
for loop in xrange(1, 4):
    y = numpy.dot(loop, x)
    #plt.close()
    plt.figure()
    plt.plot(x,y)
    plt.draw()
    time.sleep(2)