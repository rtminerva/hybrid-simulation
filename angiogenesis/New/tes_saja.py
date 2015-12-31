import numpy as np
from scipy import sparse
import timeit

f = 1
n = 5


Y = np.random.rand(n, f)
print 'Y',Y
Cdiag = np.random.rand(n) # diagonal of C
Cdiag[np.random.rand(n) < 0.5] = 0
print 'Cdiag',Cdiag

# Compute Y.T * C * Y, skipping zero elements
mask = np.flatnonzero(Cdiag)
print 'mask', mask
Cskip = Cdiag[mask]
print 'Cskip',Cskip

def ytcy_fast(Y):
    Yskip = Y[mask,:]
    print 'Yskip', Yskip
    CY = Cskip[:,None] * Yskip  # broadcasting
    print 'CY', CY
    return Yskip.T.dot(CY)

print 'satu:'
ytcy_fast(Y)

# For comparison: all-sparse matrices
#C_sparse = sparse.spdiags([Cdiag], [0], n, n)
#Y_sparse = sparse.csr_matrix(Y)
#Y_sparse.T.dot(C_sparse * Y_sparse)