from pylab import *
x = [1, 2, 3, 4, 5]
y = [1.6, 1.6,1 , 1, 1.5]
width = [5, 2.5, 1.5, .75, .75]

for i in range(len(x)-1):
    #plot(x[i:i+2], y[i:i+2], linewidth=width[i])
    print x[i:i+3]
    plot(x[i:i+5], y[i:i+5], linewidth=width[i])
show()