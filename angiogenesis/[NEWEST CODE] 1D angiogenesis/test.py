import numpy
import matplotlib.pyplot as plt
# t = np.arange(0.0, 2.0, 0.01)
# s = np.sin(2*np.pi*t)
# 
# plt.plot(t,s)
# plt.title(r'$\alpha_i > \beta_i$', fontsize=20)
# plt.text(1, -0.6, r'$\sum_{i=0}^\infty x_i$', fontsize=20)
# plt.text(0.6, 0.6, r'$\mathcal{A}\mathrm{sin}(2 \omega t)$',
#          fontsize=20)
# plt.xlabel('time (s)')
# plt.ylabel('volts (mV)')
# plt.show()

M = numpy.array([[1,2,3,4,15,27,27], [5,6,7,8,55,78,90], [9,10,11,12,32,45,67], [13,14,15,16,32,46,89],[3,6,9,2,7,9,3]])

# a = numpy.array([1,1,1])
# 
# b = numpy.dot(M,a)
# 
# print M
# print a
# print 'b', b

print numpy.delete(M, numpy.s_[1::2], 0)
print numpy.delete(M, numpy.s_[1::2], 1)