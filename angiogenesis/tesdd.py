from pylab import *
x = [1, 2, 2, 3, 4]
y = [1, 1, 2, 2, 2]
x1 = [2, 3, 3, 4, 4]
y1 = [1, 1, 0, 0, 1]
width = [8, 4, 4, 4]
width1 = [4, 2, 1, 1]
x2 = [3, 4, 4, 4, 4]
y2 = [1, 1, 1, 1, 1]
width2 = [2, 1, 1, 1]
xlim(1,5)
ylim(-1,3)
for i in range(len(x)-1):
    plot(x[i:i+2], y[i:i+2], linewidth=width[i], color ='b')
    plot(x1[i:i+2], y1[i:i+2], linewidth=width1[i] , color ='b')
    plot(x2[i:i+2], y2[i:i+2], linewidth=width2[i] , color ='b')
show()