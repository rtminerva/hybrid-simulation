import numpy
import scipy
x = numpy.zeros((2,3))
x_o = numpy.copy(x)
x_o[1,2] = 5
print x[1,2]