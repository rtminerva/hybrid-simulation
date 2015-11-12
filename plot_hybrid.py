

'''Mesh Division'''
l =10
print 'at time', time[l]
time_plot = time[l]
x_main_axis = numpy.arange(hh, X, h)
y_main_axis = numpy.arange(hh, Y, h)
x_main_axis, y_main_axis = numpy.meshgrid(x_main_axis, y_main_axis)

x_sub_axis = numpy.arange(0, X+hh, h)
y_sub_axis = numpy.arange(0, Y+hh, h)
x_sub_axis, y_sub_axis = numpy.meshgrid(x_sub_axis, y_sub_axis)

c_sol = numpy.zeros((Nx/2+1, Ny/2+1))
f_sol = numpy.zeros((Nx/2+1, Ny/2+1))
n_sol = numpy.zeros((Nx/2, Ny/2))

for j, y in enumerate(range(0,Ny+1,2)):
    for i, x in enumerate(range(0,Nx+1,2)):
        c_sol[i,j] = c[x,y,l]
        f_sol[i,j] = f[x,y,l]       
        
for j, y in enumerate(range(1,Ny,2)):
    for i, x in enumerate(range(1,Nx,2)):
        n_sol[i,j] = n[x,y,l]
        
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt

'''Figure Sprouting'''
fig = plt.figure()
plt.xlim(hh,X-hh)
plt.ylim(hh,Y-hh)
ax = fig.add_subplot(111)
'''tes'''
i= 1
globals()['xp%s' % i] =[]
globals()['yp%s' % i] =[]
for j in range(0,len(globals()['sp%s' % i])):
    globals()['xp%s' % i].append(globals()['sp%s' % i][j][0]*hh)
    globals()['yp%s' % i].append(globals()['sp%s' % i][j][1]*hh)
globals()['p%s' % i] = ax.plot(globals()['xp%s' % i], globals()['yp%s' % i], 'b') 
'''tes'''
'''tes'''
i= 2
globals()['xp%s' % i] =[]
globals()['yp%s' % i] =[]
for j in range(0,len(globals()['sp%s' % i])):
    globals()['xp%s' % i].append(globals()['sp%s' % i][j][0]*hh)
    globals()['yp%s' % i].append(globals()['sp%s' % i][j][1]*hh)
globals()['p%s' % i] = ax.plot(globals()['xp%s' % i], globals()['yp%s' % i], 'y') 
'''tes'''



#for i in range(1,num_sp+1):
#    globals()['xp%s' % i] =[]
#    globals()['yp%s' % i] =[]
#    for j in range(0,len(globals()['sp%s' % i])):
#        globals()['xp%s' % i].append(globals()['sp%s' % i][j][0]*hh)
#        globals()['yp%s' % i].append(globals()['sp%s' % i][j][1]*hh)
#    globals()['plo%s' % i] = ax.plot(globals()['xp%s' % i], globals()['yp%s' % i], 'b')
plt.show()   

