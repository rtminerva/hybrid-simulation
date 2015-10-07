v1x = 1/(2*h)*c[2,2,k]-c[0,2,k]+c[2,0,k]-c[0,0,k]
    v1y = 1/(2*h)*c[2,2,k]-c[2,0,k]+c[0,2,k]-c[0,0,k]
    v1 = max(v1x,v1y)
    w1x = 1/(2*h)*f[2,2,k]-f[0,2,k]+f[2,0,k]-f[0,0,k]
    w1y = 1/(2*h)*f[2,2,k]-f[2,0,k]+f[0,2,k]-f[0,0,k]
    w1 = max(w1x,w1y)



a=2
b=3
c = max(a,b)
print c

print range(2,5,2)


quit()
import numpy

a = numpy.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print type(a)
print a[0,:,:]
print a[0,:,:].max()