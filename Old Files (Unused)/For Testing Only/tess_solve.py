from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
from numpy.linalg import solve, norm
from numpy.random import rand
N = 30000
A = lil_matrix((N, N))
A[0, :100] = rand(100)
A[1, 100:200] = A[0, :100]
A.setdiag(rand(N))
#Now convert it to CSR format and solve A x = b for x:

b = rand(N)
x = spsolve(A.tocsr(), b)
print x
del x
#Convert it to a dense matrix and solve, and check that the result is the same:
x_ = solve(A.toarray(), b)
print x_
#Now we can compute norm of the error with:
err = norm(x-x_)
print err
if err < 1e-10:
    print 'True'