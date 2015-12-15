from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
from numpy.linalg import solve, norm
from numpy.random import rand
A = lil_matrix((1000, 1000))
A[0, :100] = rand(100)
A[1, 100:200] = A[0, :100]
A.setdiag(rand(1000))
b = rand(1000)
x = spsolve(A.tocsr(), b)
x_ = solve(A.toarray(), b)
err = norm(x-x_)
print err
if err < 10