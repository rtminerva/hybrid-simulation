from scipy.sparse import dia_matrix
from scipy.sparse.linalg import spsolve
from numpy.linalg import solve, norm
import scipy as sp
import numpy as np

N = 5
data = np.array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])

# data = np.array([np.ones(N), np.ones(N), np.ones(N), np.ones(N), np.ones(N)])
diags = np.array([-3,-1, 0, 1, 3])
a = dia_matrix((data, diags), shape=(N, N))
print 'a', a.toarray()
b = np.array(np.ones(N))

'''a c/c_ = v(ab)'''
v = np.dot(a.toarray(), b)
# print 'v:',v
# c1 = spsolve(a.tocsr(), b)
c = spsolve(a.tocsr(), v)



# c1_ = solve(a.toarray(), b)
c_ = solve(a.toarray(), v)

err = norm(c-c_)
err1 = norm(c1-c1_)
print 'error', err, err1
print 'by spsolve b',c1
print 'by numpy solve b',c1_
print 'a', a.toarray()
# print 'by spsolve v',c
# print 'by numpy solve v',c_

# '''Checking error solution'''
# D1 = np.dot(a.toarray(),c1)-b
# D = np.dot(a.toarray(),c)-v
# D1_ = np.dot(a.toarray(),c1_)-b
# D_ = np.dot(a.toarray(),c_)-v
# print
# print 'checking solution'
# print D1, D, D1_, D_
