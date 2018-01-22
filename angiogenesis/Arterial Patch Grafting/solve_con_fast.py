from random import randint, sample, uniform
import numpy

def system_3d(coef, set, sol):
    c_o = sol['c'][:]
    cn_o = sol['cn'][:]
    c_1 = numpy.reshape(c_o, (set['Nx']+1)**3) 
    cn_1 = numpy.reshape(cn_o, (set['Nx']+1)**3)
#     n_o = sol['tip_pos'][:]
#     n_1 = numpy.reshape(n_o, (set['Nx']+1)**3)
#     n_2 = numpy.diag(n_1)
    
    #c*n
#     cn_o = numpy.dot(c_1,n_2)
    #-Nu*c*n
    coef = -set['dt']*coef['Nu']
    term = cn_1 * coef
    #c_o - Nu*c*n
    result = c_1 + term
    print result
    #convert to matrix
    sol['c'] = numpy.reshape(result,(set['Nx']+1,set['Nx']+1,set['Nx']+1))
    return sol