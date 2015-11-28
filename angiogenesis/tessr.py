from pylab import *
x = [1, 2, 3]
y = [1, 2, 2]
x1 = [2, 2, 3]
y1 = [2, 2.5, 2.5]
width = [8, 4, 2]
width1 = [4, 4, 2]

xlim(1,5)
ylim(-1,3)
for i in range(len(x)-1):
    plot(x[i:i+2], y[i:i+2], linewidth=width[i], color ='b')
    plot(x1[i:i+2], y1[i:i+2], linewidth=width1[i] , color ='b')
show()