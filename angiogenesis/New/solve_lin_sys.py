import numpy
from numpy import matrix
from numpy import linalg
# A = numpy.zeros(shape=(3,3))
# A = numpy.eye(3, k = 1)
# print A
# A = numpy.zeros(shape=(3,3))
A = matrix( [[1,2,3],[11,12,13],[21,22,23]] ) # Creates a matrix.
B = matrix( [[1,2,3],[11,12,13],[21,22,23]] ) # Creates a matrix.
x = matrix( [[1],[2],[3]] )                  # Creates a matrix (like a column vector).
y = matrix( [[1,2,3]] )
# A[0,1] = 100  
# print A                   # Creates a matrix (like a row vector).
# print A.T                                    # Transpose of A.
# print A*x                                    # Matrix multiplication of A and x.
# print A.I                                    # Inverse of A.
print linalg.solve(A, x)     # Solve the linear equation system.

C = numpy.eye(9)
print numpy.insert(C,A,axis = 1)